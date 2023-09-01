# this is MF366's mediocre plugin system

import os
import datetime
import imp

"""
The imp module is obsolete but still works.

Until I find a better option (for what I want, importlib ain't an option),
I'll use imp module. What a weird name, imp!

--
Truly yours, MF366
"""

desktop_winx = None
NOW_FILEX = None
textwdigetx = None
settingsx = None

paths = None
_LOG = None
lang = None
mb = None

def now() -> str:
    return datetime.datetime.now()

def initializer(_logger, _paths, _sets, _wins, _texts, _filex, langz: list, _mb):
    global _LOG, paths, settingsx, desktop_winx, NOW_FILEX, textwdigetx, lang, mb
    
    _LOG = _logger
    paths = _paths
    settingsx = _sets
    desktop_winx = _wins
    textwdigetx = _texts
    NOW_FILEX = _filex
    lang = langz
    mb = _mb
    
    _LOG.write(f"{str(now())} - Initializing Plugin System: OK\n")

def run_a_plugin(number: int):
    try:
        new_folder = os.path.join(paths, f"plugin_{number}")

        if not os.path.exists(path=new_folder):
            mb.showerror(lang[161], lang[162])
            return
        
        details_file = os.path.join(new_folder, "Details.txt")
        
        with open(details_file, "r", encoding="utf-8") as f:
            _f = f.read()
            _title = _f.split("\n")
            f.close()
            
        possible_plugin_filepath = os.path.join(new_folder, f"{_title[0].replace(' ', '_')}.py")
        
        if not os.path.exists(possible_plugin_filepath):
            mb.showerror(lang[161], lang[162])
            return
        
        plugin_filepath = possible_plugin_filepath
        
        _LOG.write(f"{str(now())} - Running the plugin number {str(number)} stored at {plugin_filepath}: OK\n")


        #-> ChatGPT help down here :)
        # Absolute path to the module's .py file
        module_path = plugin_filepath

        # Load the module using imp.load_source
        module = imp.load_source(_title[0].replace(" ", "_"), module_path)
        
        module.plugin(desktop_win=desktop_winx,
                    TextWidget=textwdigetx,
                    settings=settingsx,
                    _lang=lang,
                    NOW_FILE=NOW_FILEX,
                    logger=_LOG,
                    plugin_dir=paths)

        # Now you can use functions/classes/etc. defined in the module

    except Exception as e:
        mb.showerror(lang[133], lang[134])
        
        _LOG.write(f"{str(now())} - Running the plugin number {str(number)}: ERROR - {e}\n")