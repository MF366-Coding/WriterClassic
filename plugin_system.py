# pylint: disable=W4901
# pylint: disable=W0105
# pylint: disable=W0603
# pylint: disable=W0718

# [!!] All these "errors" annoy me!

# [!?] this is MF366's mediocre plugin system

import os
import datetime
from pygame import mixer # for the exe version, the module should have been already compiled
from tkinter import messagebox as mb
from typing import Any
import importlib.machinery

wclassic_vars: dict[str, Any] = {}
_LOG = None
plugin_dir: str = ""
lang = None


# [i] Alternative to using deprecated imp module
def load_module_from_source(module_name: str, source_path: str):
    """
    load_module_from_source loads a Python module from an absolute location of a *.py file

    Args:
        module_name (str): the name of the module
        source_path (str): the path to the module
        
    Used like:
        loaded_module = load_module_from_source("something", "C:\\Users\\user\\johndoe.py")

    Returns:
        Any: the module
    """
    
    loader = importlib.machinery.SourceFileLoader(module_name, source_path)
    spec = importlib.util.spec_from_loader(module_name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


now = datetime.datetime.now


def initializer(wclassic_globals):
    global wclassic_vars, _LOG, plugin_dir, lang

    wclassic_vars = wclassic_globals
    _LOG = wclassic_vars["LOG"]
    plugin_dir = wclassic_vars["plugin_dir"]
    lang = wclassic_vars["lang"]

    _LOG.write(f"{str(now())} - Initializing Plugin System: OK\n")


def run_a_plugin(number_or_name: int | str) -> bool:    
    try:
        if isinstance(number_or_name, int):
            new_folder = os.path.join(plugin_dir, f"plugin_{number_or_name}")

            if not os.path.exists(path=new_folder):
                mb.showerror(lang('plugerror'), lang('plug_dmg'))
                return False

            details_file = os.path.join(new_folder, "Details.txt")

            with open(details_file, "r", encoding="utf-8") as f:
                _title = f.readline().strip()
                f.close()

            possible_plugin_filepath = os.path.join(new_folder, f"{_title.replace(' ', '_')}.py")

            if not os.path.exists(possible_plugin_filepath):
                mb.showerror(lang('plugerror'), lang('plug_dmg'))
                return False

            plugin_filepath = possible_plugin_filepath

            _LOG.write(f"{str(now())} - Running the plugin number {str(number_or_name)} stored at {plugin_filepath}: OK\n")

            mixer.quit()
            mixer.init()
            mixer.music.load(os.path.join(wclassic_vars['data_dir'], 'sucessful.mp3'))
            mixer.music.set_volume(0.5)
            mixer.music.play()

            module_path = plugin_filepath

            module = load_module_from_source(_title.replace(" ", "_"), module_path)

            module.start(wclassic_vars)

        else:
            plugin_filepath: str | None = None

            for dir_num in range(1, 1000):
                a = os.path.join(plugin_dir, f"plugin_{dir_num}", "Details.txt")

                if not os.path.exists(a):
                    continue

                with open(a, "r", encoding="utf-8") as f:
                    _title = f.readline().strip()

                b: str | None = "?"

                if number_or_name == _title.replace("_", " "):
                    b = os.path.join(plugin_dir, f"plugin_{dir_num}", f"{_title.replace(' ', '_')}.py")

                if os.path.exists(b):
                    plugin_filepath = b
                    break

            if plugin_filepath:
                _LOG.write(f"{str(now())} - Running the plugin '{str(number_or_name)}' stored at {plugin_filepath}: OK\n")

                module_path = plugin_filepath

                mixer.quit()
                mixer.init()
                mixer.music.load(os.path.join(wclassic_vars['data_dir'], 'sucessful.mp3'))
                mixer.music.set_volume(0.5)
                mixer.music.play()

                module = load_module_from_source(_title.replace(" ", "_"), module_path)

                module.start(wclassic_vars)

        return True

    except Exception as e:
        mb.showerror(lang('notallowed'), lang('nope') + f"\n{e}")

        if isinstance(number_or_name, int):
            _LOG.write(f"{str(now())} - Running the plugin number {str(number_or_name)}: ERROR - {e}\n")

        else:
            _LOG.write(f"{str(now())} - Running the plugin '{str(number_or_name)}': ERROR - {e}\n")

        return False
