# Hello world, Norb here.

from glob import glob
# Look ma, no imports from WriterClassic!
import datetime # Really, bro?
now = datetime.datetime.now()
# yes bro

_PLUGIN_DATA_FILE = "Details.txt"

def ParsePluginData(pluginpath: str):
    """
    Plugin path is assumed to be the folder where the .py is
    We load the Details.txt file and read it
    """
    with open(pluginpath + _PLUGIN_DATA_FILE, "rt") as Data:
        return {
            "Name": Data.readline().strip(),
            "Author": Data.readline().strip(),
            "Desc": Data.readline().strip()
        }

class Script:
    # The base script class.
    _GLOBALS = {}  # What ever variables the script can legally modify
    _BYTECODE = None
    _NAME = None
    _PATH = None
    _LOGGER = None
    _SUCCESS = None

    def __init__(self, path: str, logger, **_globals):
        """
        Load and compile a plugin.

        Args:
            path: Where is the plugin
            _globals: The name of the variable : the variable value before running the plugin
        """

        # path is the folder with the .py
        PluginData = ParsePluginData(path)

        self._NAME = PluginData["Name"]
        self._PATH = path
        self._GLOBALS = _globals
        self._LOGGER = logger  # is this necessary? yeah, gotta log everything right? ;)

        try:
            self._BYTECODE = compile(
                open( glob(f"{self._PATH}{PluginData['Name']}.py")[0], "rt" ).read(),
                f"{self._PATH}{self._NAME}.py",
                'exec'
            )
        except Exception as Ex:
            self._SUCCESS = False
            self._LOGGER.write(
                f"\n{str(now)} - Error caught while trying to compile plugin {self._NAME}:"
                f"\n{Ex}\nFile located at {self._PATH}{self._NAME}.py\n\n"
            )
            return

        self._SUCCESS = True
        self._LOGGER.write(f"{str(now)} - Lock and loaded plugin {self._NAME}!\n")

    def SyncGlobalVars(self):
        """
        Updated the program variables that were affected by the plugin.
        This is why the _globals param exists in the constructor
        """
        for global_var in self._GLOBALS:
            exec(f"global {global_var}\n{global_var} = {self._GLOBALS[global_var]}", globals())

    def GetName(self):
        return self._NAME

    def RunScript(self):
        """
        Run the actual thingy.
        """
        self._LOGGER.write(f"{str(now)} - Running script {self._NAME}!\n")
        try:
            exec(self._BYTECODE, self._GLOBALS)
        except Exception as Ex:
            self._LOGGER.write(
                f"\n{str(now)} - Error caught while trying to run plugin {self._NAME}:"
                f"\n{Ex}\nFile located at {self._PATH}{self._NAME}.py\n\n"
            )
        # now obviously one should run verified plugins only, unless you potentially want your pc
        # to spontaneously combust.

class ScriptManager:
    # It manages scripts!
    _SCRIPTS: list[Script] = None

    def __init__(self):
        self._SCRIPTS = {}

    def LoadPlugins(self, _globals: dict):
        # call globals() in WriterClassic so we can access them here.
        # I ain't importing shit!
        _folders = glob(".\\plugins\\*\\")  # sorry c++ plugins, though import DLLs might be a possibility...
        for folder in _folders:
            scr = Script (
                folder, _globals['_LOG'],
                desktop_win     = _globals['desktop_win'],
                TextWidget      = _globals['TextWidget'],
                config          = _globals['config'],
                data_dir        = _globals['data_dir'],
                user_data       = _globals['user_data'],
                nix_assets      = _globals['nix_assets'],
                plugin_dir      = _globals['plugin_dir'],
                locale          = _globals['locale']
            )
            self._SCRIPTS[scr.GetName()] = scr

    def RunPlugin(self, name):
        self._SCRIPTS[name].RunScript()