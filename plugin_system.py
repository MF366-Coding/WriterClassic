# pylint: disable=W4901
# pylint: disable=W0105
# pylint: disable=W0603
# pylint: disable=W0718

# [!!] All these "errors" annoy me!

# [!?] this is MF366's mediocre plugin system

import os, datetime
from tkinter import messagebox as mb
import importlib.machinery

wclassic_vars = {}
_LOG = None
plugin_dir = ""
lang = []

# [i] Alternative to using deprecated imp module
def load_module_from_source(module_name, source_path):
    loader = importlib.machinery.SourceFileLoader(module_name, source_path)
    spec = importlib.util.spec_from_loader(module_name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module

# [!?] the 'load_module_from_source' function is used like this:
# [*] loaded_module = load_module_from_source("something", "C:\\Users\\user\\johndoe.py")

now = datetime.datetime.now

def initializer(wclassic_globals):
    global wclassic_vars, _LOG, plugin_dir, lang
    
    wclassic_vars = wclassic_globals
    _LOG = wclassic_vars["_LOG"]
    plugin_dir = wclassic_vars["plugin_dir"]
    lang = wclassic_vars["lang"]
    
    _LOG.write(f"{str(now())} - Initializing Plugin System: OK\n")

def run_a_plugin(number_or_name: int | str) -> bool:
    def end_func() -> False:
        return False
    
    try:
        if type(number_or_name) == int:
            new_folder = os.path.join(plugin_dir, f"plugin_{number_or_name}")

            if not os.path.exists(path=new_folder):                
                mb.showerror(lang[161], lang[162])
                return False
            
            details_file = os.path.join(new_folder, "Details.txt")
            image_file = os.path.join(new_folder, "WriterPlugin.png")
            
            with open(details_file, "r", encoding="utf-8") as f:
                _title = f.readline().strip()
                f.close()
            
            possible_plugin_filepath = os.path.join(new_folder, f"{_title.replace(' ', '_')}.py")
            
            if not os.path.exists(possible_plugin_filepath):                
                mb.showerror(lang[161], lang[162])
                return False
            
            plugin_filepath = possible_plugin_filepath
            
            w = wclassic_vars['Toplevel'](wclassic_vars['desktop_win'])
            
            # [*] Load the PNG image using PIL
            image = wclassic_vars['Image'].open(image_file)

            # [*] Get the dimensions of the image
            image_width, image_height = image.size

            # [*] Define the maximum width and height for the resized image
            max_width = 200
            max_height = 200

            # [*] Calculate the desired dimensions while maintaining the aspect ratio
            if image_width > image_height:
                # [i] Calculate the desired width based on the maximum width
                desired_width = min(image_width, max_width)
                # [i] Calculate the corresponding height
                desired_height = int(desired_width * image_height / image_width)
            else:
                # [i] Calculate the desired height based on the maximum height
                desired_height = min(image_height, max_height)
                # [i] Calculate the corresponding width
                desired_width = int(desired_height * image_width / image_height)

            # [*] Resize the image
            # [?] Should I not use LANCZOS? It seems the best for this but...
            resized_image = image.resize((desired_width, desired_height), wclassic_vars['Image'].LANCZOS)

            # [*] Create a PhotoImage object from the resized image
            photo = wclassic_vars['ImageTk'].PhotoImage(resized_image)
            
            image_label = wclassic_vars['Label'](w, image=photo)
            
            image_label.pack()
                
            _LOG.write(f"{str(now())} - Running the plugin number {str(number_or_name)} stored at {plugin_filepath}: OK\n")

            module_path = plugin_filepath

            module = load_module_from_source(_title.replace(" ", "_"), module_path)
            
            module.start(wclassic_vars)

            # [i] Now you can use functions/classes/etc. defined in the module
            w.mainloop()
            
        else:
            plugin_filepath: str | None = None

            for dir_num in range(1, 1000):
                a = os.path.join(plugin_dir, f"plugin_{dir_num}", "Details.txt")
                image_file = os.path.join(plugin_dir, f"plugin_{dir_num}", "WriterPlugin.png")

                if not os.path.exists(a):
                    continue
                
                if not os.path.exists(image_file):
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
                w = wclassic_vars['Toplevel'](wclassic_vars['desktop_win'])
            
                # [*] Load the PNG image using PIL
                image = wclassic_vars['Image'].open(image_file)

                # [*] Get the dimensions of the image
                image_width, image_height = image.size

                # [*] Define the maximum width and height for the resized image
                max_width = 200
                max_height = 200

                # [*] Calculate the desired dimensions while maintaining the aspect ratio
                if image_width > image_height:
                    # [i] Calculate the desired width based on the maximum width
                    desired_width = min(image_width, max_width)
                    # [i] Calculate the corresponding height
                    desired_height = int(desired_width * image_height / image_width)
                else:
                    # [i] Calculate the desired height based on the maximum height
                    desired_height = min(image_height, max_height)
                    # [i] Calculate the corresponding width
                    desired_width = int(desired_height * image_width / image_height)

                # [*] Resize the image
                # [?] Should I not use LANCZOS? It seems the best for this but...
                resized_image = image.resize((desired_width, desired_height), wclassic_vars['Image'].LANCZOS)

                # [*] Create a PhotoImage object from the resized image
                photo = wclassic_vars['ImageTk'].PhotoImage(resized_image)
                
                image_label = wclassic_vars['Label'](w, image=photo)
                
                image_label.pack()
                
                _LOG.write(f"{str(now())} - Running the plugin '{str(number_or_name)}' stored at {plugin_filepath}: OK\n")
                
                module_path = plugin_filepath

                module = load_module_from_source(_title.replace(" ", "_"), module_path)

                module.start(wclassic_vars)
                
                w.mainloop()
                
        return True

    except Exception as e:        
        mb.showerror(lang[133], lang[134] + f"\n{e}")
        
        if type(number_or_name) == int:
            _LOG.write(f"{str(now())} - Running the plugin number {str(number_or_name)}: ERROR - {e}\n")
        
        else:
            _LOG.write(f"{str(now())} - Running the plugin '{str(number_or_name)}': ERROR - {e}\n")
            
        return False
        