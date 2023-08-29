# Hello world, Norb here.

from glob import glob
# Look ma, no imports from WriterClassic!
import datetime # Really, bro?
now = datetime.datetime.now()
# yes bro

class Script:
    # The base script class.
    _GLOBALS = {}  # What ever variables the script can legally modify
    _BYTECODE = None
    _NAME = None
    _LOGGER = None

    def __init__(self, path: str, name: str, logger, **_globals):
        """
        Load and compile a plugin.

        Args:
            path: Where is the plugin
            name: Name of the plugin
            _globals: The name of the variable : the variable value before running the plugin
        """

        self._BYTECODE = compile(path, name, 'exec')
        self._GLOBALS = _globals
        self._NAME = name
        self._LOGGER = logger  # is this necessary? yeah, gotta log everything right? ;)
        self._LOGGER.write(f"{str(now)} - Lock and loaded plugin {self._NAME}!\n")

    def SyncGlobalVars(self):
        """
        Updated the program variables that were affected by the plugin.
        This is why the _globals param exists in the constructor
        """
        for global_var in self._GLOBALS:
            exec(f"global {global_var}\n{global_var} = {self._GLOBALS[global_var]}", globals())

    def RunScript(self):
        """
        Run the actual thingy.
        """
        _LOGGER.write(f"{str(now)} - Running script {self._NAME}!\n")
        exec(self._BYTECODE, self._GLOBALS)
        # now obviously one should run verified plugins only, unless you potentially want your pc
        # to spontaneously combust.

class ScriptManager:
    # It manages scripts!
    _SCRIPTS = None

    def __init__(self):
        self._SCRIPTS = {}

    def LoadPlugins(self, _globals: dict):
        # call globals() in WriterClassic so we can access them here.
        # I ain't importing shit!
        _files = glob(f"*.py", root_dir="./plugins/")  # sorry c++ plugins, though import DLLs might be a possibility...
        for file in _files:
            _name = file.replace(".py", "")
            self._SCRIPTS["file"] = Script (
                file, _name, _globals['_LOG'],
                desktop_win     = _globals['desktop_win'],
                TextWidget      = _globals['TextWidget'],
                config          = _globals['config'],
                data_dir        = _globals['data_dir'],
                user_data       = _globals['user_data'],
                nix_assets      = _globals['nix_assets'],
                plugin_dir      = _globals['plugin_dir'],
                locale          = _globals['locale']
            )