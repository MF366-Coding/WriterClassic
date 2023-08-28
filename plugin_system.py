# Hello world, Norb here.

from WriterClassic import now, _LOG, plugin_dir
from glob import glob

from WriterClassic import desktop_win, TextWidget, config, data_dir, user_data, nix_assets, plugin_dir, locale

class Script:
    # The base script class.
    _GLOBALS = {}  # What ever variables the script can legally modify
    _BYTECODE = None
    _NAME = None

    def __init__(self, path: str, name: str, **_globals):
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
        _LOG.write(f"{str(now)} - Lock and loaded plugin {self._NAME}!\n")

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
        _LOG.write(f"{str(now)} - Running script {self._NAME}!\n")
        exec(self._BYTECODE, self._GLOBALS)
        # now obviously one should run verified plugins only, unless you potentially want your pc
        # to spontaneously combust.

class ScriptManager:
    # It manages scripts!
    _SCRIPTS = None

    def __init__(self):
        self._SCRIPTS = {}

    def LoadPlugins(self):
        _files = glob(f"*.py", root_dir="./plugins/")  # sorry c++ plugins, though import DLLs might be a possibility...
        for file in _files:
            _name = file.replace(".py", "")
            self._SCRIPTS["file"] = Script (
                file, _name,
                desktop_win=desktop_win,
                TextWidget=TextWidget,
                config=config,
                data_dir=data_dir,
                user_data=user_data,
                nix_assets=nix_assets,
                plugin_dir=plugin_dir,
                locale=locale
            )