# pylint: disable=W4901
# pylint: disable=W0105
# pylint: disable=W0603
# pylint: disable=W0718

# [!!] All these "errors" annoy me!

# [!?] this is MF366's mediocre plugin system

import os
import datetime
import imp
from tkinter import messagebox as mb

"""
The imp module is obsolete but still works.

Until I find a better option (for what I want, importlib ain't an option),
I'll use imp module. What a weird name, imp!
"""

wclassic_vars = {}
_LOG = None
plugin_dir = ""
lang = []

def now() -> str:
    return datetime.datetime.now()

def initializer(wclassic_globals):
    global wclassic_vars, _LOG, plugin_dir, lang
    
    wclassic_vars = wclassic_globals
    _LOG = wclassic_vars["_LOG"]
    plugin_dir = wclassic_vars["plugin_dir"]
    lang = wclassic_vars["lang"]
    
    _LOG.write(f"{str(now())} - Initializing Plugin System: OK\n")

def run_a_plugin(number: int):
    try:
        new_folder = os.path.join(plugin_dir, f"plugin_{number}")

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
        
        module.start(wclassic_vars)

        # Now you can use functions/classes/etc. defined in the module

    except Exception as e:
        mb.showerror(lang[133], lang[134])
        
        _LOG.write(f"{str(now())} - Running the plugin number {str(number)}: ERROR - {e}\n")