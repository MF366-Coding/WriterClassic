# WriterClassic.py

# [i] Just disabling some annoying Pylint stuff, don't mind me :D
# pylint: disable=W0122
# pylint: disable=E1101
# pylint: disable=W0621
# pylint: disable=W0212
# pylint: disable=W0718
# pylint: disable=W0603
# pylint: disable=W0404
# pylint: disable=W0201
# pylint: disable=W0105

'''
WriterClassic

Powered by: Python 3.10.11 (in my Windows computer)

The colored menu seems to only work on Linux.
But the app works on Windows and Mac, without the colored menu thought.

Official Repo:
    https://github.com/MF366-Coding/WriterClassic

Find me in this spots:
    https://github.com/MF366-Coding
    https://www.youtube.com/@mf_366
    https://www.buymeacoffee.com/mf366 (Support me please!)

Original idea by: MF366
Fully developed by: MF366

Small but lovely contributions by:
    Norb (norbcodes at GitHub)
    Zeca70 (Zeca70 at GitHub)
'''

# [i] NOW_FILE is the currently opened file
# [i] if none is open, then it's False
NOW_FILE = False
lines = 0
cur_data: str = ""
SAVE_STATUS: bool = True
keys_to_go: int = 0

import os, sys, json, random, datetime, platform, importlib

# [*] Get the absolute path of the script
script_path = os.path.abspath(__file__)

# [*] Get the directory containing the script
script_dir = os.path.dirname(script_path)

config = os.path.join(script_dir, 'config')
user_data = os.path.join(script_dir, 'user_data')
nix_assets = os.path.join(script_dir, 'nix_assets')
plugin_dir = os.path.join(script_dir, 'plugins')
data_dir = os.path.join(script_dir, 'data')
locale = os.path.join(script_dir, 'locale')
temp_dir = os.path.join(script_dir, 'temp')
scripts_dir = os.path.join(script_dir, "scripts")

def now() -> str:
    """
    now returns the current time and date in the form of a string
    
    This is simply an easier way to call `datetime.datetime.now()`

    Returns:
        str: the current date and time
    """
    return datetime.datetime.now()

def check_paths(var) -> str:
    """
    check_paths checks if the directories exist

    This function checks if the directories related to WriterClassic exist or should be created.

    Args:
        var (str, absolute filepath): the path that must be checked

    Returns:
        str: either 'Created' or 'Was there', depending on if it existed before or not
    """
    
    if not os.path.exists(var):
        os.mkdir(var)
        return "Created."

    return "Was there."

debug_a = []
debug_a.append(config)
debug_a.append(user_data)
debug_a.append(nix_assets)
debug_a.append(plugin_dir)
debug_a.append(data_dir)
debug_a.append(locale)
debug_a.append(temp_dir)
debug_a.append(scripts_dir)

for i in debug_a:
    check_paths(i)

_LOG = open(os.path.join(user_data, "log.wclassic"), mode="a", encoding="utf-8")

_LOG.write("\n")
_LOG.write(f"{str(now())} - WriterClassic was executed: OK\n")

WCLASSIC_VARS: dict[str, str] = {
    "$APPDATA": os.environ.get('APPDATA') if sys.platform == 'win32' else "$APPDATA",
    "$LOCALAPPDATA": os.environ.get('LOCALAPPDATA') if sys.platform == 'win32' else "$LOCALAPPDATA",
    "$USER": os.path.expanduser('~'),
    "$COMMONROOT": "C:\\" if sys.platform == 'win32' else "/",
    "$BITNESS": platform.architecture()[0],
    "$PYTHON": sys.executable,
    "$WRITERCLASSIC": script_path,
    "$LOGGER": os.path.join(user_data, "log.wclassic"),
    "$REPO": "https://github.com/MF366-Coding/WriterClassic",
    "$WEBSITE": "https://mf366-coding.github.io/writerclassic.html",
    "$OSVERSION": platform.version(),
    "$PLATFORM": sys.platform,
    "$OS": os.name
}

try:
    # [*] Imports down here
    # [*] Time to organize this tho

    from typing import Literal # [i] Making things nicer, I guess

    from getpass import getuser # [i] Used in order to obtain the username of the current user, which is used for the Auto Signature

    from icecream import ic # [i] Used for debugging

    from PIL import Image, ImageTk # [i] Used for placing the WriterClassic logo on the screen

    import zipfile # [i] Used to extract the zip files used by plugins

    import asyncio # /-/ [i] Used for an attempt at making an autosave feature
    import tracemalloc # /-/ [i] Also used for an attempt at making an autosave feature

    from setting_loader import get_settings, dump_settings # [i] Used to load and dump WriterClassic's settings

    from tkinter import Tk, Toplevel, TclError, Label, Button, StringVar, Entry, END, Menu, Checkbutton, IntVar, INSERT # [i] Used for the UI
    from tkinter.scrolledtext import ScrolledText # [i] Used instead of the regular Text widget, since this one has a scroll bar
    from tkinter.ttk import Button, Checkbutton, Label, Entry # [i] Used because of the auto syling in tkinter.ttk
    import tkinter.messagebox as mb # [i] Used for the message boxes
    import tkinter.filedialog as dlg # [i] Used for the "save", "open" dialogues
    from tkinter import simpledialog as sdg # [i] Used for dialogues that ask you for an input
    from tkinter.font import Font # [i] Used for controlling the fonts in the Text widget

    import keyboard # [i] Used to send the Copy, Paste and Cut commands to the OS

    import smtplib # [i] Used for the Send E-mail option - server management

    # [i] The next 4 are all used for the Send E-mail option - encodings and e-mail parts
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email import encoders

    import markdown2 # [i] Used to make HTML files from Markdown

    from plugin_system import initializer, run_a_plugin # [i] WriterClassic's Plugin "API"

    import simple_webbrowser # [i] My own Python module (used for the Search with... options)
    from requests import get, exceptions # [i] Used for regular interactions with the Internet

except (ModuleNotFoundError, ImportError) as e:
    _LOG.write(f"{str(now())} - A required module has not been found in the device: ERROR\n")
    _LOG.write(f"{str(now())} - Proceeding with the installation of the dependencies: AWAITING\n")

    _command: str = f"pip install --upgrade -r \"{os.path.join(script_dir, 'requirements.txt')}\""

    if sys.platform == "win32":
        _command: str = f"python -m pip install --upgrade -r \"{os.path.join(script_dir, 'requirements.txt')}\""

    try:
        os.system(_command)

    except Exception as e:
        _LOG.write(f"{str(now())} - Something went wrong: ABORTING - {e}\n")
        sys.exit()

    else:
        _LOG.write(f"{str(now())} - Installation completed: LOADING GUI\n")


    # [*] reapeating the imports, Goddamn it!
    
    from typing import Literal # [i] Making things nicer, I guess

    from getpass import getuser # [i] Used in order to obtain the username of the current user, which is used for the Auto Signature

    from icecream import ic # [i] Used for debugging

    from PIL import Image, ImageTk # [i] Used for placing the WriterClassic logo on the screen

    import zipfile # [i] Used to extract the zip files used by plugins

    import asyncio # /-/ [i] Used for an attempt at making an autosave feature
    import tracemalloc # /-/ [i] Also used for an attempt at making an autosave feature

    from setting_loader import get_settings, dump_settings # [i] Used to load and dump WriterClassic's settings

    from tkinter import Tk, Toplevel, TclError, Label, Button, StringVar, Entry, END, Menu, Checkbutton, IntVar, INSERT # [i] Used for the UI
    from tkinter.scrolledtext import ScrolledText # [i] Used instead of the regular Text widget, since this one has a scroll bar
    from tkinter.ttk import Button, Checkbutton, Label, Entry # [i] Used because of the auto syling in tkinter.ttk
    import tkinter.messagebox as mb # [i] Used for the message boxes
    import tkinter.filedialog as dlg # [i] Used for the "save", "open" dialogues
    from tkinter import simpledialog as sdg # [i] Used for dialogues that ask you for an input
    from tkinter.font import Font # [i] Used for controlling the fonts in the Text widget
    
    import keyboard # [i] Used to send the Copy, Paste and Cut commands to the OS

    import smtplib # [i] Used for the Send E-mail option - server management

    # [i] The next 4 are all used for the Send E-mail option - encodings and e-mail parts
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email import encoders

    import markdown2 # [i] Used to make HTML files from Markdown

    from plugin_system import initializer, run_a_plugin # [i] WriterClassic's Plugin "API"

    from requests import get, exceptions # [i] Used for regular interactions with the Internet
    
    import simple_webbrowser # [i] My own Python module (used for the Search with... options)
    
    tracemalloc.start()

ic.configureOutput(prefix="ic debug statement | -> ")

def clamp(val, _min, _max):
    """
    clamp clamps and returns a value

    Clamping a value is setting it between the max value and min value in case it exceeds those

    Args:
        val (Any): the value to clamp
        _min (Any): the min value allowed
        _max (Any): the max value allowed

    Returns:
        type(val): the clamped value of val
    """
    
    if val < _min:
        return _min

    if val > _max:
        return _max

    return val

'''
if os.path.exists(os.path.join(scripts_dir, "quick_acess.wscript")):
    quick_acess_content = open(os.path.join(scripts_dir, "quick_acess.wscript"), "r", encoding="utf-8").read().split("\n")

    for i in range(len(quick_acess_content)):
        if i != 10:
            QUICK_ACESS_DATA.append(quick_acess_content[i])

        else:
            break

    quick_acess_content = None
'''

desktop_win = Tk()
TextWidget = ScrolledText(desktop_win, font=("Calibri", 13), borderwidth=5, undo=True)
TextWidget.pack()
cur_data = TextWidget.get(0.0, END)
# /-/ TextWidget.insert(END, "WriterClassic is a free and open-source project made by MF366.\n\nYour support is appreciated: https://www.buymeacoffee.com/mf366\n\nThank you <3")

UNIX_OSES = [
            "darwin",
            "linux",
            "linux2"
        ]

NOT_ALLOWED = [
    "",
    " ",
    "  ",
    "\n",
    "   ",
    "    ",
    "     "
]

settings = get_settings(f"{config}/settings.json")

if not settings["debugging"]:
    ic.disable()

ic(settings)
for debug_b in debug_a:
    ic(debug_a)

startApp = settings["startup"]
if not startApp:
    startApp = "0"
    _LOG.write(f"{str(now())} - Check for updates on startup: DISABLED\n")

else:
    startApp = "1"
    _LOG.write(f"{str(now())} - Check for updates on startup: ENABLED\n")

ic(startApp)
autosave_cooldown = None
update_check_button = IntVar(desktop_win, 1)
update_check_button.set(int(startApp))

ic(script_dir)
ic(script_path)
ic(f"{data_dir}/logo.png")

# [!] py_compile is not needed anymore
'''
from py_compile import compile as _compile
_LOG.write(f"{str(now())} - Imported compile from py_compile: OK\n")
'''


_LOG.write(f"{str(now())} - Imported getuser from getpass: OK\n")


_LOG.write(f"{str(now())} - Imported simpledialog from tkinter: OK\n")


_LOG.write(f"{str(now())} - Imported filedialog from tkinter: OK\n")


_LOG.write(f"{str(now())} - Imported messagebox from tkinter: OK\n")


_LOG.write(f"{str(now())} - Imported Font from tkinter.font: OK\n")

ic(now())

setLang = settings["language"]
autosave_cooldown = 60.0
can_autosave = IntVar(desktop_win, 0)

ic(setLang)

with open(f'{locale}/'+str(setLang[0:2])+'.wclassic', 'r', encoding='utf-8') as usedLangFile:
    usedLang = usedLangFile.read()
    lang = usedLang.split('\n')
    _LOG.write(f"{str(now())} - Language has been configured correctly: OK\n")

# [*] Windowing
_LOG.write(f"{str(now())} - WriterClassic launched: OK\n")

if sys.platform == "win32":
    desktop_win.iconbitmap(f"{data_dir}/app_icon.ico")
    _LOG.write(f"{str(now())} - Icon has been changed to WriterClassic's icon [WINDOWS ONLY]: OK\n")

latest_version = None

IGNORE_CHECKING = False

if startApp == '1':
    try:
        response = get('https://api.github.com/repos/MF366-Coding/WriterClassic/releases/latest', timeout=3.5)
        _LOG.write(f"{str(now())} - Connected to GitHub: OK\n")
        data = json.loads(response.text)
        _LOG.write(f"{str(now())} - Got WriterClassic Releases data: OK\n")
        latest_version = data['tag_name']
        _LOG.write(f"{str(now())} - Got the latest release's tag: OK\n")

    except (exceptions.ConnectTimeout, exceptions.ConnectionError, TimeoutError, exceptions.ReadTimeout):
        mb.showerror(lang[148], f"{lang[135]}\n{lang[136]}")
        _LOG.write(f"{str(now())} - Connected to GitHub: ERROR\n")
        _LOG.write(f"{str(now())} - Connection has timed out, is restricted or is simply unavailable: INFO\n")
        IGNORE_CHECKING = True
        _LOG.write(f"{str(now())} - WriterClassic is launching without checking for updates: OK\n")

ic(IGNORE_CHECKING)
ic(latest_version)

# [!] Very Important: Keeping track of versions and commits
appV = "v10.2.0"
advV ="v10.2.0.269"
# [i] the fourth number up here, is the commit where this changes have been made

# [i] Config files
ic(appV)
ic(advV)

theme = settings["theme"]

ic(theme)

_LOG.write(f"{str(now())} - Got the current theme: OK\n")

font_use = settings["font"]
_LOG.write(f"{str(now())} - Got the current font family/type: OK\n")
_LOG.write(f"{str(now())} - Got the current font size: OK\n")

def fast_dump():
    """
    fast_dump allows to quickly dump the app's settings
    """
    
    dump_settings(f"{config}/settings.json", settings)

temp_files = os.listdir(temp_dir)

for temp_file in temp_files:
    file_to_delete = os.path.join(temp_dir, temp_file)
    if os.path.isfile(file_to_delete):
        os.remove(file_to_delete)

if os.path.exists(os.path.join(scripts_dir, "auto.wscript")):
    auto_content = open(os.path.join(scripts_dir, "auto.wscript"), "r", encoding="utf-8").read()

    _run_auto = mb.askyesno(lang[1], f"{lang[289]}\n{lang[290]}\n{lang[291]}")

    if _run_auto == True:
        exec(auto_content)

# [i] Windowing... again
if NOW_FILE == False:
    desktop_win.title(lang[1])

_LOG.write(f"{str(now())} - Window's title was set to WriterClassic: OK\n")

try:
    FontSet = Font(family=font_use["type"], size=font_use["size"])
    __font_type = font_use["type"]
    __font_size = font_use["size"]
    _LOG.write(f"{str(now())} - Font size is {str(__font_size)}: OK\n")
    _LOG.write(f"{str(now())} - Font family/type is {str(__font_type)}: OK\n")

except TclError:
    mb.showerror(lang[149], f"{lang[144]}\n{lang[145]}\n{lang[146]}")
    _LOG.write(f"{str(now())} - Font size is set to 14 because of a font error: OK\n")
    FontSet = Font(family="Segoe UI", size=14)
    _LOG.write(f"{str(now())} - Font type is set to Segoe UI because of a font error: OK\n")
    settings["font"] = {
        "type": "Segoe UI",
        "size": 14
    }

    fast_dump()


_LOG.write(f"{str(now())} - The editing interface has been created: OK\n")

geomValue = settings["geometry"]
_LOG.write(f"{str(now())} - Got the window's dimensions settings: OK\n")
GeomValues = geomValue.split('x')

try:
    desktop_win.geometry(geomValue)
    _LOG.write(f"{str(now())} - Applied the window's dimensions: OK\n")

except TclError:
    desktop_win.geometry("700x500")
    GeomValues = [700, 500]
    _LOG.write(f"{str(now())} - Applied the window's dimensions: ERROR\n")
    _LOG.write(f"{str(now())} - Reverted to 700x500: OK\n")
    mb.showerror(lang[166], f"{lang[167]}\n{lang[168]}")

try:
    TextWidget.configure(background=theme["color"], foreground=theme["fg"], width=int(GeomValues[0]), height=int(GeomValues[1]), insertbackground=theme["ct"], font=FontSet)
    _LOG.write(f"{str(now())} - Applied configurations to the editing interface: OK\n")

except TclError:
    _LOG.write(f"{str(now())} - Applied configurations to the editing interface: ERROR\n")
    mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
    TextWidget.configure(background="black", foreground="white", width=int(GeomValues[0]), height=int(GeomValues[1]), insertbackground="white", font=FontSet)
    _LOG.write(f"{str(now())} - Reconfigured the editing interface: OK\n")

_LOG.write(f"{str(now())} - 'Packed' the editing interface: OK\n")

# [i] Defining the menu bar
menu_bar = Menu(desktop_win)
_LOG.write(f"{str(now())} - Created the menu bar: OK\n")

try:
    if sys.platform == "linux":
        menu_bar.configure(background=theme["menu"], foreground=theme["mfg"])
        _LOG.write(f"{str(now())} - Applied the theme to the menu bar: OK\n")

except TclError:
    if sys.platform == "linux":
        _LOG.write(f"{str(now())} - Applied the theme to the menu bar: ERROR\n")
        mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
        menu_bar.configure(background="white", foreground="black")
        _LOG.write(f"{str(now())} - Applied the light theme to the menu bar as last resource: OK\n")

ic(sys.platform)

window_lock_status = IntVar(desktop_win, 1)
advanced_mode_status = IntVar(desktop_win, 0)

desktop_win.resizable(bool(window_lock_status.get()), bool(window_lock_status.get()))

if settings["advanced-mode"]:
    ADVANCED = True

else:
    ADVANCED = False

ic(ADVANCED)

advanced_mode_status.set(int(ADVANCED))

menu_1 = Menu(menu_bar)
menu_2 = Menu(menu_1)
menu_3 = Menu(menu_2)
menu_4 = Menu(menu_1)
menu_5 = Menu(menu_4)
menu_6 = Menu(menu_4)
menu_7 = Menu(menu_1)
menu_8 = Menu(menu_bar)
menu_9 = Menu(menu_8)
menu_10 = Menu(menu_bar)
menu_11 = Menu(menu_bar)
menu_12 = Menu(menu_bar)
menu_13 = Menu(menu_12)

if ADVANCED:
    menu_14 = Menu(menu_bar)

menu_15 = Menu(menu_bar)
menu_16 = Menu(menu_15)
menu_17 = Menu(menu_15)
# /-/ menu_18 = Menu(menu_10)

_LOG.write(f"{str(now())} - Created all the menus: OK\n")

def writeStartup(text: bool):
    """
    writeStartup changes the startup value on the settings and then saves it

    Args:
        text (bool): the new startup value
    """
    
    settings["startup"] = text
    fast_dump()
    _LOG.write(f"{str(now())} - Check for updates on Startup (True - 1/False - 0) has been changed to {text}: OK\n")

# [i] Check for Updates
class UpdateCheck:
    @staticmethod
    def check_other():
        """
        check_other checks for updates on startup only
        """

        if appV != latest_version and IGNORE_CHECKING == False:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            _LOG.write(f"{str(now())} - Versions don't match: WARNING\n")
            if askForUpdate:
                simple_webbrowser.Website('https://github.com/MF366-Coding/WriterClassic/releases/latest')
                _LOG.write(f"{str(now())} - Went to the latest release at GitHub: OK\n")

        elif IGNORE_CHECKING == True:
            _LOG.write(f"{str(now())} - Couldn't check for updates on startup: WARNING\n")
            return

    @staticmethod
    def check():
        """
        check checks for updates whenever the user clicks Check for Updates
        """

        if appV != latest_version and IGNORE_CHECKING == False:
            askForUpdate = mb.askyesno(lang[72], lang[73])
            if askForUpdate:
                _LOG.write(f"{str(now())} - Went to the latest release at GitHub: OK\n")
                simple_webbrowser.Website('https://github.com/MF366-Coding/WriterClassic/releases/latest')

        elif appV == latest_version and IGNORE_CHECKING == False:
            mb.showinfo(title=lang[93], message=lang[92])
            _LOG.write(f"{str(now())} - Versions match | WriterClassic is up to date: OK\n")

        else:
            mb.showerror(lang[148], f"{lang[135]}\n{lang[136]}")
            _LOG.write(f"{str(now())} - Couldn't check for updates (Bad Internet, Connection Timeout, Restricted Internet): WARNING\n")

    @staticmethod
    def change():
        """
        change swaps the current value of the startup setting
        """
        writeStartup(bool(update_check_button.get()))
        mb.showinfo(title=lang[1], message=lang[101])
        _LOG.write(f"{str(now())} - Check for updates on startup setting has been changed: OK\n")

if startApp == '1':
    UpdateCheck.check_other()
    _LOG.write(f"{str(now())} - Checked for updates on startup: AWAITING REPLY\n")

# [i] Windowing... one more time...
def SetWinSize():
    """
    SetWinSize creates a GUI in order to change the dimensions of the window
    """
    
    widthSet = sdg.askinteger(lang[1], lang[57])
    _LOG.write(f"{str(now())} - Got a width value: AWAITING FOR ANTI-BUG CHECK\n")
    if widthSet in NOT_ALLOWED:
        mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        _LOG.write(f"{str(now())} - Got a width value: ERROR (ILLEGAL VALUE)\n")

    elif widthSet not in NOT_ALLOWED:
        _LOG.write(f"{str(now())} - Got a width value: OK\n")
        heightSet = sdg.askinteger(lang[1], lang[58])
        _LOG.write(f"{str(now())} - Got a height value: AWAITING FOR ANTI-BUG CHECK\n")

        if heightSet in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
            _LOG.write(f"{str(now())} - Got a width value: ERROR (ILLEGAL VALUE)\n")

        elif heightSet not in NOT_ALLOWED:
            _LOG.write(f"{str(now())} - Got a width value: OK\n")
            TextWidget.configure(width=widthSet, height=heightSet)
            _LOG.write(f"{str(now())} - Editing interface has been reconfigured: OK\n")
            desktop_win.geometry(str(widthSet)+'x'+str(heightSet))
            _LOG.write(f"{str(now())} - Window's dimensions were set: OK\n")

            _LOG.write(f"{str(now())} - Configured default window's dimensions: OK\n")
            settings["geometry"] = str(widthSet)+'x'+str(heightSet)
            fast_dump()

# [i] Theme Picker
def ThemeSet(*colors):
    """
    ThemeSet sets a new theme

    Args in the following order:
        - the background color
        - the foreground color (text color)
        - the color of the cursor, usually the same as the foreground color
        - the background of the menus (LINUX ONLY; menu background)
        - the color of the text in the menus (LINUX ONLY; menu foreground)
    """
    
    global theme
    
    theme = {
        "color": str(colors[0]),
        "ct": str(colors[2]),
        "fg": str(colors[1]),
        "mfg": str(colors[4]),
        "menu": str(colors[3])
    }

    settings["theme"] = theme

    fast_dump()

    TextWidget.configure(background=colors[0], foreground=colors[1], insertbackground=colors[2])
    _LOG.write(f"{str(now())} - Editing interface has been reconfigured: OK\n")

    try:
        if sys.platform == "linux":
            # [i] Themed menus only on Linux Python3
            # /-/ Themed menus are also compatible with Windows and Mac, tho
            menu_10.configure(background=colors[3], foreground=colors[4])
            menu_11.configure(background=colors[3], foreground=colors[4])
            menu_1.configure(background=colors[3], foreground=colors[4])
            menu_2.configure(background=colors[3], foreground=colors[4])
            menu_3.configure(background=colors[3], foreground=colors[4])
            menu_5.configure(background=colors[3], foreground=colors[4])
            menu_4.configure(background=colors[3], foreground=colors[4])
            menu_6.configure(background=colors[3], foreground=colors[4])
            menu_7.configure(background=colors[3], foreground=colors[4])
            menu_12.configure(background=colors[3], foreground=colors[4])
            menu_8.configure(background=colors[3], foreground=colors[4])
            menu_9.configure(background=colors[3], foreground=colors[4])
            menu_13.configure(background=colors[3], foreground=colors[4])
            if ADVANCED:
                menu_14.configure(background=colors[3], foreground=colors[4])
            menu_15.configure(background=colors[3], foreground=colors[4])
            menu_16.configure(background=colors[3], foreground=colors[4])
            menu_17.configure(background=colors[3], foreground=colors[4])
            _LOG.write(f"{str(now())} - The Menus have been themed [LINUX ONLY]: OK\n")
    
    except (TypeError, ValueError, TclError):
        if sys.platform == "linux":
            # [i] Themed menus only on Linux Python3
            # /-/ Themed menus are also compatible with Windows and Mac, tho
            mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
            menu_10.configure(background="white", foreground="black")
            menu_11.configure(background="white", foreground="black")
            menu_1.configure(background="white", foreground="black")
            menu_2.configure(background="white", foreground="black")
            menu_3.configure(background="white", foreground="black")
            menu_5.configure(background="white", foreground="black")
            menu_4.configure(background="white", foreground="black")
            menu_6.configure(background="white", foreground="black")
            menu_7.configure(background="white", foreground="black")
            menu_12.configure(background="white", foreground="black")
            menu_8.configure(background="white", foreground="black")
            menu_9.configure(background="white", foreground="black")
            menu_13.configure(background="white", foreground="black")
            if ADVANCED:
                menu_14.configure(background="white", foreground="black")
            menu_15.configure(background="white", foreground="black")
            menu_17.configure(background="white", foreground="black")
            menu_16.configure(background="white", foreground="black")
            _LOG.write(f"{str(now())} - The Menus have been themed [LINUX ONLY]: OK\n")

    # [i] Themes now update in real time
    '''
    waitResponse = mb.askyesno(parent=desktop_win, title=lang[30], message=lang[31])
    _LOG.write(f"{str(now())} - Asked for app restart: AWAITING RESPONSE\n")

    if waitResponse:
        desktop_win.destroy()
        _LOG.write(f"{str(now())} - End of session: QUIT\n")

    else:
        _LOG.write(f"{str(now())} - Cancel/No as response: OK\n")
    '''

# [!] Althrought not deprecated at all, must not be used.
# [i] quickway() quits the app without asking for confirmation
# [!?] Which means it might break stuff that was being saved when the function was called
# [i] Can only be called from the Command Menu
# [i] Ctrl + Shift + P and type 'ragequit'
def quickway():
    """
    quickway instantly quits the app without any confirmation
    
    Not recommended at all!
    """
    _LOG.write(f"{str(now())} - End of session: QUIT\n")
    _LOG.close()
    desktop_win.destroy()
    sys.exit()

# [i] Setup (Lang files)
def LanguageSet(language_set, root_win):
    """
    LanguageSet sets a new language as the setting

    Args:
        language_set (str): the string that represents the locale file. Examples: `pt`, `sk` and `en`
        root_win (Tk | Toplevel): the window where this change takes place
    """
    settings["language"] = language_set
    _LOG.write(f"{str(now())} - A new language has been set ({str(language_set)}): OK\n")
    fast_dump()

    popup_define = mb.askyesno(parent=root_win, title=lang[30], message=lang[31])
    _LOG.write(f"{str(now())} - Asked for app restart: AWAITING RESPONSE\n")
    if popup_define:
        root_win.destroy()
        _LOG.write(f"{str(now())} - End of session: QUIT\n")
    else:
        _LOG.write(f"{str(now())} - Cancel/No as response: OK\n")

# [i] Notepad
def new_window():
    """
    new_window loads the GUI for the Notepad plugin/tool

    In the early days, this function was supposed to launch a new WriterClassic window.
    """
    
    newWindow = Toplevel(desktop_win)
    _LOG.write(f"{str(now())} - A new window has been called: AWAITING CONFIGURATION\n")

    # [i] Windowing
    newWindow.title(lang[22])
    newWindow.geometry("600x400")

    TextWidget2 = ScrolledText(newWindow, borderwidth=5)

    TextWidget2.configure(background=theme["color"], foreground=theme["fg"], width=GeomValues[0], height=GeomValues[1], insertbackground=theme["ct"], font=FontSet)
    TextWidget2.pack()

    _LOG.write(f"{str(now())} - Notes Plugin's window has been fully configured: OK\n")

    newWindow.mainloop()

def DOC_STATS():
    """
    DOC_STATS presents the stats of the current editor to the user

    Stats:
    - No of lines
    """
    
    global lines

    _data = TextWidget.get(0.0, END)
    _LOG.write(f"{str(now())} - Extracted text from the editing interface: OK\n")

    if _data in NOT_ALLOWED:
        lines = 0
        _LOG.write(f"{str(now())} - There were {str(lines)} lines: INFO (EMPTY FILE)\n")

    else:
        _lines = _data.split("\n")
        y_lines = list(filter(("").__ne__, _lines))
        x_lines = int(len(y_lines))
        lines = x_lines
        _LOG.write(f"{str(now())} - There were {str(lines)} lines: OK\n")

    mb.showinfo(lang[164], f"{lang[165]}: {str(lines)}")

# [i] Repo
def repo():
    """
    repo sends the user to the official repository
    """
    
    simple_webbrowser.Website("https://github.com/MF366-Coding/WriterClassic/")
    _LOG.write(f"{str(now())} - Opened the repository: AWAITING FOR FUNCTION OR ERROR\n")

def bool_swap(value: bool | None, default_for_none: bool = True):
    """
    bool_swap swaps the value of a boolean and returns it

    When a value, either a bool or None, is given, if it's True, the function will return False. If False, return True.
    
    If the `default_for_none` is specified (defaults to True), when the given value is None, the fucntion returns `default_for_none`'s value.
    
    Example:
        `bool_swap(True)` will return False
        `bool_swap(True, False)` will also return False
        `bool_swap(False)` will return True
        `bool_swap(False, True)` will also return True
        `bool_swap(None)` will return True (because that's the default for `default_for_none`)
        `bool_swap(None, False)` will return False (because `default_for_none` was set to False)

    Args:
        value (bool | None): the value to swap
        default_for_none (bool, optional): in case None is given as `value`, this argument will be returned. Defaults to True.

    Returns:
        bool: the swapped value
    """
    
    if value:
        value = False

    elif not value:
        value = True

    elif value == None:
        value = default_for_none

    return value

class BackupSystem:
    def __init__(self, plugin_path: str = plugin_dir, autoscr_path: str = scripts_dir, config_path: str = config, main_dir: str = script_dir) -> None:
        """
        __init__ is the initializer for the BackupSystem

        Args:
            plugin_path (str, optional): the path where plugins are stored. Defaults to plugin_dir.
            autoscr_path (str, optional): the path where auto scripts are stored. Defaults to scripts_dir.
            config_path (str, optional): the path where the settings are saved. Defaults to config.
            main_dir (str, optional): the dir where WriterClassic is stored. Defaults to script_dir.
        """
        
        self._folder_paths = [plugin_path, autoscr_path, config_path]
        self.__orig_folder_paths = (plugin_path, autoscr_path, config_path)
        self._main_dir = main_dir

    def _zip_files(self, root_path: str):
        """
        _zip_files is responsible for creating the Backup file

        Args:
            root_path (str): directory where the zip file will be saved
        """
        
        with zipfile.ZipFile(os.path.join(root_path, f"Backup_WriterClassic_{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}.zip"), 'w') as zip_file:
            for folder_path in self._folder_paths:
                if "plugin_" in folder_path:
                    arcname = folder_path
                else:
                    arcname = os.path.basename(folder_path)
                zip_file.write(folder_path, arcname=arcname)
                for filename in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, filename)
                    if os.path.isfile(file_path):
                        zip_file.write(file_path, arcname=os.path.join(arcname, filename))

                    elif os.path.isdir(file_path) and '__pycache__' not in file_path:
                        zip_file.write(file_path, arcname=os.path.join(arcname, filename))
                        if "plugin_" in file_path:
                            self._folder_paths.append(f"plugins/{filename}")

    def _extract_files(self, file_path: str):
        """
        _extract_files extracts the backup to the location where WriterClassic is stored

        Args:
            file_path (str): the path where the zip backup is
        """
        
        with zipfile.ZipFile(file_path, 'r') as zip_file:
            for path_to_remove in self.__orig_folder_paths:
                try:
                    if sys.platform == "win32":
                        os.system(f'rmdir /s /q {path_to_remove}')

                    else:
                        os.system(f'rm -rf {path_to_remove}')

                except Exception:
                    mb.showerror(lang[1], lang[322])
                    continue

            zip_file.extractall(self._main_dir)

    def run_action(self, _type: Literal["zip", "extract", "make", "load", "create", "restore", "unzip"], root_win: Tk | Toplevel = desktop_win):
        """
        run_action runs an action related to either extracting or creating a backup

        Args:
            _type (Literal, in the form of str): if it's supposed to extract or create the backup
            root_win (Tk | Toplevel, optional): the window wjere the dialogues should appear. Defaults to desktop_win.
        """

        _DIR: str | None = None

        loading_types = ("extract", "load", "restore", "unzip")
        making_types = ("zip", "make", "create")

        if _type in making_types:
            _DIR = dlg.askdirectory(mustexist=True, title=lang[316])

            self._zip_files(_DIR)

        elif _type in loading_types:
            file_path = dlg.asksaveasfilename(parent=root_win, filetypes=[(lang[318], '*.zip')], defaultextension="*.*", initialfile="Load a Backup", confirmoverwrite=False, title=lang[317])

            if not file_path.lower().endswith(".zip") or not os.path.exists(file_path):
                mb.showerror(lang[1], lang[319])
                return

            self._extract_files(file_path)

        else:
            mb.showerror(lang[1], lang[319])

# [i] Clock
# [!] Deprecated feature
async def clockPlugin():
    """
    clockPlugin shows the current time on the screen

    XXX Deprecated feature because of its lack of purpose
    """
    
    clockWindow = Toplevel(desktop_win)
    clockWindow.geometry('275x65')
    clockWindow.resizable(False, False)
    running = True
    clockWindow.protocol("WM_DELETE_WINDOW", lambda: bool_swap(running))
    _LOG.write(f"{str(now())} - A new window has been called: AWAITING CONFIGURATION\n")

    # [i] Windowing
    clockWindow.title(lang[23])

    TextWidget2 = Label(clockWindow)
    TextWidget2.configure(
        font=(100)
        )

    while running:
        await asyncio.sleep(0.01)
        TextWidget2.configure(text=now())
        TextWidget.pack()

    _LOG.write(f"{str(now())} - Clock Plugin's window has been configured: OK\n")


# [i] Text font
def fontEdit(winType: int | bool):
    """
    fontEdit allows the user to easily change their font settings

    If `winType` is 1 or True, the size will be changed.
    
    Otherwise, the font setting itself will be modified.

    Args:
        winType (int | bool): controls whether the size or the font should be changed
    """
    if winType == 1:
        fontSize = sdg.askinteger(lang[59], lang[60], minvalue=1)
        if fontSize in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        elif fontSize not in NOT_ALLOWED:
            font_use["size"] = fontSize
            settings["font"]["size"] = fontSize
            fast_dump()
            _LOG.write(f"{str(now())} - Font size has been changed to {str(fontSize)}: OK\n")
            mb.showinfo(lang[1], lang[63])
    else:
        fontType = sdg.askstring(lang[61], lang[62])
        if fontType in NOT_ALLOWED:
            mb.showerror(lang[147], f"{lang[133]}\n{lang[134]}")
        elif fontType not in NOT_ALLOWED:
            font_use["type"] = fontType
            settings["font"]["type"] = fontType
            fast_dump()
            _LOG.write(f"{str(now())} - Font type has been changed to {str(fontType)}: OK\n")
            mb.showinfo(lang[1], lang[63])

# [i] clears the screen
def NewFile():
    """
    NewFile clears the editor and purges current cached data on the last file to be opened/saved

    It also resets the modified status (check `ModifiedStatus` - function and `SAVE_STATUS` - global variable, bool type)
    """

    global NOW_FILE, cur_data, SAVE_STATUS
    
    SAVE_STATUS = True

    desktop_win.title(lang[1])
    TextWidget.delete(index1=0.0, index2=END)
    cur_data = TextWidget.get(0.0, END)
    
    NOW_FILE = False

    _LOG.write(f"{str(now())} - A new file has been created: OK\n")

    ic(NOW_FILE)


file_types = [(lang[32], '*.txt'),
              (lang[33], '*.config'),
              (lang[34], '*.css'),
              (lang[35], '*.csv'),
              (lang[36], '*.html'),
              (lang[37], '*.inf'),
              (lang[38], '*.info'),
              (lang[39], '*.ini'),
              (lang[40], '*.js'),
              (lang[41], '*.py'),
              (lang[42], '*.log'),
              (lang[43], '*.xml'),
              (lang[44], '*.1st'),
              (lang[45], '*.a'),
              (lang[46], '*.a8s'),
              (lang[47], '*.ans'),
              (lang[48], '*.arena'),
              (lang[49], '*.as'),
              (lang[50], '*.asa'),
              (lang[51], '*.asm'),
              (lang[52], '*.md'),
              (lang[102], '*.json'),
              (lang[185], '*.wclassic'),
              (lang[288], "*.wscript"),
              (lang[110], '*.ath'),
              (lang[111], "*.att"),
              (lang[112], "*.avs"),
              (lang[113], "*.bbz"),
              (lang[114], "*.bcs"),
              (lang[115], "*.bmk"),
              (lang[116], "*.book"),
              (lang[117], "*.bpw"),
              (lang[118], "*.bsd"),
              (lang[119], "*.bsdl"),
              (lang[120], "*.bsh"),
              (lang[121], "*.camp"),
              (lang[122], "*.cel"),
              (lang[123], "*.celx"),
              (lang[124], "*.cgi"),
              (lang[127], "*.*")
              ]

_LOG.write(f"{str(now())} - Filetypes have been configured correctly: OK\n")

# [i] functions to open a file
def OpenFileManually(file_path: str, root_win: Tk = desktop_win):
    """
    OpenFile opens a file selected from the following interface

    Args:
        file_path: The filepath to open with extension
        (optional, defaults to the main window) root_win (Tk): WriterClassic's main window
    """
    
    global NOW_FILE, cur_data, SAVE_STATUS
    
    file_path = os.path.abspath(file_path)

    _basepath = os.path.join(os.path.dirname(file_path), os.path.basename(file_path) + ".wscript")

    if os.path.exists(_basepath) and file_path.lower().endswith(".wclassic"):
        run_auto = mb.askyesno(lang[1], f"{lang[285]}\n{lang[286]}\n{lang[287]}")

        if run_auto == True:
            exec(open(_basepath, "r", encoding="utf-8").read())

    try:
        file_input = open(file_path, "rt", encoding="utf-8")
        file_data = file_input.read()

        root_win.title(f"{lang[1]} - {os.path.basename(file_path)}")
        TextWidget.delete(index1=0.0, index2=END)
        TextWidget.insert(chars=file_data, index=END)
        cur_data = TextWidget.get(0.0, END)
        SAVE_STATUS = True

        _LOG.write(f"{str(now())} - A file at the path {str(file_path)} has been opened: OK\n")

        NOW_FILE = str(file_path)
        file_input.close()

    except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
        mb.showerror(title=lang[187], message=f"{lang[188]} {str(file_path)}.")
        run_default = mb.askyesno(title=lang[187], message=lang[189])
        if run_default:
            os.system(str(file_path))

    finally:
        ic(NOW_FILE)

def OpenFile(root_win: Tk = desktop_win):
    """
    OpenFile opens a file selected from the following interface

    Args:
        root_win (Tk): WriterClassic's main window
    """
    global NOW_FILE, cur_data, SAVE_STATUS

    file_path = dlg.asksaveasfilename(parent=root_win, filetypes=file_types, defaultextension="*.*", initialfile="Open a File", confirmoverwrite=False, title=lang[7])

    if sys.platform != 'linux':
        # [*] Get the selected file extension
        selected_extension = None
        for ft in file_types:
            if file_path.lower().endswith(ft[1]):
                selected_extension = ft[1]
                break

        # [*] Append the selected extension if not already included
        if selected_extension and not file_path.lower().endswith(selected_extension):
            file_path += selected_extension

    _basepath = os.path.join(str(os.path.dirname(file_path)), str(os.path.basename(file_path)) + ".wscript")
    ic(_basepath)

    if os.path.exists(_basepath) and file_path.lower().endswith(".wclassic"):
        run_auto = mb.askyesno(lang[1], f"{lang[285]}\n{lang[286]}\n{lang[287]}")

        if run_auto == True:
            exec(open(_basepath, "r", encoding="utf-8").read())

    try:
        file_input = open(file_path, "rt", encoding="utf-8")
        file_data = file_input.read()

        root_win.title(f"{lang[1]} - {os.path.basename(file_path)}")
        TextWidget.delete(index1=0.0, index2=END)
        TextWidget.insert(chars=file_data, index=END)
        cur_data = TextWidget.get(0.0, END)
        SAVE_STATUS = True

        _LOG.write(f"{str(now())} - A file at the path {str(file_path)} has been opened: OK\n")

        NOW_FILE = str(file_path)
        file_input.close()

    except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
        mb.showerror(title=lang[187], message=f"{lang[188]} {str(file_path)}.")
        run_default = mb.askyesno(title=lang[187], message=lang[189])
        if run_default:
            os.system(str(file_path))

    finally:
        ic(NOW_FILE)

# [i] Saving as
def SaveFile(root_win: Tk = desktop_win):
    """
    SaveFile saves the current file as

    Basically, the tipical Save As feature.

    Args:
        root_win (Tk, optional): the window where changes take place. Defaults to desktop_win.
    """
    global NOW_FILE, cur_data, SAVE_STATUS

    data = TextWidget.get(0.0, END)
    SAVE_STATUS = True
    file_path = dlg.asksaveasfilename(parent=root_win, title=lang[9], confirmoverwrite=True, filetypes=file_types, defaultextension="*.*", initialfile="New File To Save")

    if sys.platform != 'linux':
        # [*] Get the selected file extension
        selected_extension = None
        for ft in file_types:
            if file_path.lower().endswith(ft[1]):
                selected_extension = ft[1]
                break

        # [*] Append the selected extension if not already included
        if selected_extension and not file_path.lower().endswith(selected_extension):
            file_path += selected_extension
            
    if file_path.lower().endswith(".wclassic") and "$VARS" in data:
        for __var in WCLASSIC_VARS:
            for _ in range(data.count(__var)):
                data = data.replace(__var, WCLASSIC_VARS[__var])

    file = open(file_path, "wt", encoding='utf-8')
    file.write(str(data))
    cur_data = data
    file.close()
    mb.showinfo(lang[1], lang[101])
    root_win.title(f"{lang[1]} - {os.path.basename(file_path)}")

    _LOG.write(f"{str(now())} - A file has been saved as {str(file_path)}: OK\n")

    NOW_FILE = str(file_path)
    ic(NOW_FILE)
    
    OpenFileManually(NOW_FILE)

def Save(root_win: Tk = desktop_win):
    """
    Save saves the current file

    If the file exists, then it will be saved over without asking questions.
    
    If the file doesn't exist though, the `SaveFile` feature gets called (Save As)

    Args:
        root_win (Tk, optional): the window where changes take place. Defaults to desktop_win.
    """
    
    global NOW_FILE, cur_data, SAVE_STATUS

    if NOW_FILE is False:
        return SaveFile(root_win=root_win)

    data: str = TextWidget.get(0.0, END)
    
    SAVE_STATUS = True

    file_path = NOW_FILE
    
    if file_path.lower().endswith(".wclassic") and "$VARS" in data:
            for __var in WCLASSIC_VARS:
                for _ in range(data.count(__var)):
                    data = data.replace(__var, WCLASSIC_VARS[__var])
    
    file = open(file_path, "wt", encoding='utf-8')
    file.write(str(data))
    cur_data = data
    file.close()
    mb.showinfo(lang[1], lang[101])
    root_win.title(f"{lang[1]} - {os.path.basename(file_path)}")

    OpenFileManually(NOW_FILE)

    _LOG.write(f"{str(now())} - An existing file has been saved over ({str(file_path)}): OK\n")

    NOW_FILE = str(file_path)
    ic(NOW_FILE)

# [*] Whatever... (File Eraser)
def WipeFile(root_win: Tk = desktop_win):
    sureConfirm = mb.askyesno(title=lang[55], message=lang[56])
    if sureConfirm:
        file_path = dlg.asksaveasfilename(parent=root_win, confirmoverwrite=False, filetypes=file_types, defaultextension="*.*", initialfile="File to Wipe")

        if sys.platform != 'linux':
            # [*] Get the selected file extension
            selected_extension = None
            for ft in file_types:
                if file_path.lower().endswith(ft[1]):
                    selected_extension = ft[1]
                    break

            # [*] Append the selected extension if not already included
            if selected_extension and not file_path.lower().endswith(selected_extension):
                file_path += selected_extension

        file_input = open(file_path, "wt", encoding="utf-8")
        file_input.write('')
        mb.showinfo(title=lang[1], message=lang[101])

        _LOG.write(f"{str(now())} - A file has been wiped at {str(file_path)}: OK\n")
        file_input.close()

desktop_entry = None

def select_all(text_widget: ScrolledText = TextWidget):
    text_widget.tag_add("sel", 0.0, END)

def search_for(replace: bool = False, index_a = INSERT, line_limit: int = 100):
    text = sdg.askstring(lang[1], lang[323])

    if replace:
        replaced_text = sdg.askstring(lang[1], lang[324] + "\n" + lang[325])

    search_backwards = mb.askyesno(lang[1], lang[326])
    case_sensitive = mb.askyesno(lang[1], lang[327])

    x = TextWidget.search(text, index_a, END, forwards=True, backwards=search_backwards, nocase=bool_swap(case_sensitive))

    if x != "":
        b: list[str] = x.split(".")
        c: int = b[1] + 1

        for i in range(len(text)):
            if c >= line_limit:
                break

            if text[i] == TextWidget.get(f"{b[0]}.{str(c)}"):
                if replace:
                    TextWidget.delete(f"{b[0]}.{str(c)}")

                    try:
                        TextWidget.insert(f"{b[0]}.{str(c-1)}", replaced_text[i])
                        
                    except IndexError:
                        pass

                c += 1
                continue

            break

        TextWidget.tag_add("search", x, f"{b[0]}.{str(c)}")

    else:
        mb.showwarning(lang[1], lang[328])

def lorem_ipsum():
    TextWidget.insert(TextWidget.index(INSERT), """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque lobortis lacus nibh, ut mattis nisi cursus nec. In aliquam scelerisque eleifend. Suspendisse tempor sem ut ipsum imperdiet, a iaculis dui congue. In in ex massa. Aliquam in dignissim ligula. Mauris pretium mi at molestie feugiat. Cras quam ipsum, congue tempus erat id, rhoncus facilisis mauris. Nam augue nunc, porta ac vestibulum nec, euismod ac est. Duis consectetur risus eu justo pretium volutpat. Vestibulum fringilla purus velit, sed sagittis augue porta a. Vivamus vestibulum turpis ac quam eleifend, ut luctus eros placerat. Praesent pellentesque faucibus ligula, nec varius mi viverra ut. Mauris blandit vitae purus auctor imperdiet. Nullam non sem nisi.

Nullam ullamcorper lacus quis libero luctus ullamcorper. Vestibulum id nisl sit amet ipsum cursus consectetur. Nam et metus leo. Ut a justo scelerisque, imperdiet sapien sed, pharetra ligula. Fusce vel tortor rhoncus nisi elementum commodo at vel massa. Proin suscipit ipsum tristique, ornare quam et, finibus mauris. Curabitur hendrerit, odio eu venenatis aliquam, mi est tincidunt lorem, lacinia placerat lectus nunc rutrum libero.

Maecenas hendrerit diam id mi blandit, vitae dignissim tellus consequat. Vestibulum bibendum convallis nibh eget mattis. Fusce aliquam molestie eros et finibus. Quisque vehicula ex est, vitae convallis lacus dictum at. In id congue velit, sed auctor odio. Aliquam erat volutpat. Ut et molestie lectus, dignissim aliquam libero. Suspendisse potenti.

In pulvinar gravida condimentum. Proin nec sem vitae urna egestas mollis nec vel tortor. Ut sodales eget felis in bibendum. Fusce eu lacus a purus tempus rhoncus non nec magna. Donec sed egestas eros, ut vulputate leo. Sed non libero purus. Suspendisse suscipit nisi vel fringilla suscipit. Integer dapibus tincidunt iaculis. Vivamus risus tortor, cursus vel tincidunt vel, ullamcorper non quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel magna dui.

Nam gravida nibh leo, eget tincidunt neque facilisis sed. Integer malesuada dui sit amet nulla cursus, eget porttitor nulla fringilla. Proin condimentum mattis posuere. Vivamus sit amet sem non felis aliquet vehicula vel a lorem. Nam accumsan tortor a mattis lacinia. Curabitur ultricies eros lacus, tempor pretium nibh laoreet vel. Curabitur a orci sit amet massa iaculis imperdiet. Phasellus porta aliquet nunc vitae vulputate. Ut non elementum nibh. Sed bibendum ultricies sapien eget dapibus. Pellentesque at lacus sed elit gravida dignissim. Phasellus eu tempus nisl. Suspendisse feugiat risus in laoreet fringilla. Nam sit amet purus laoreet, aliquam augue a, fringilla diam. """)

def readme_writer_classic():
    with open(os.path.join(script_dir, "README.md"), "r", encoding='utf-8') as readme_wrcl_f:
        TextWidget.insert(TextWidget.index(INSERT), f"README.md (WriterClassic at GitHub; Markdown)\n{readme_wrcl_f.read()}")
        readme_wrcl_f.close()

def ModifiedStatus(text_widget: ScrolledText = TextWidget, main_win: Tk | Toplevel = desktop_win) -> bool | None:
    global SAVE_STATUS, keys_to_go
    
    if keys_to_go > 0:
        keys_to_go -= 1
        keys_to_go = clamp(keys_to_go, 0, 10)
        return None
    
    if cur_data == text_widget.get(0.0, END):
        if " (*)" in main_win.title():
            main_win.title(main_win.title().removesuffix(" (*)"))
            
        SAVE_STATUS = True
        return SAVE_STATUS
        
    if " (*)" not in main_win.title():
        main_win.title(f"{main_win.title()} (*)")
        
    SAVE_STATUS = False
    return SAVE_STATUS

rmb_menu = Menu(desktop_win, tearoff = 0)
rmb_menu.add_command(label=lang[295], command=lambda:
    keyboard.send("Control+x"), accelerator="Ctrl + X")
rmb_menu.add_command(label=lang[296], command=lambda:
    keyboard.send("Control+c"), accelerator="Ctrl + C")
rmb_menu.add_command(label=lang[297], command=lambda:
    keyboard.send("Control+v"), accelerator="Ctrl + V")
rmb_menu.add_separator()
rmb_menu.add_command(label=lang[293], command=TextWidget.edit_undo, accelerator="Ctrl + Z")
rmb_menu.add_command(label=lang[294], command=TextWidget.edit_redo, accelerator="Ctrl + Y")
rmb_menu.add_separator()
rmb_menu.add_command(label=lang[331], command=select_all, accelerator="Ctrl + A")
rmb_menu.add_separator()
rmb_menu.add_command(label="Lorem ipsum", command=lorem_ipsum)
rmb_menu.add_command(label="README.md", command=readme_writer_classic)

def rmb_popup(event, root: Tk | Toplevel = desktop_win):
    x, y = 0, 0
    if event == None:
        x, y = root.winfo_pointerxy()

        window_x = root.winfo_rootx()
        window_y = root.winfo_rooty()

        x = clamp(x, window_x, root.winfo_width() - 50)
        y = clamp(y, window_y, root.winfo_height() - 5)

    else:
        x, y = event.x_root, event.y_root

    try:
        rmb_menu.tk_popup(x, y)

    finally:
        rmb_menu.grab_release()

TextWidget.bind("<Button-3>", rmb_popup)

# [!] Use this instead of the class DevOption!!!!
def dev_option(prog_lang: str, mode: Literal["run", "build"] = "build") -> None:
    """
    dev_option is the actual responsible for the developer options

    Not to be confused with DevOption, the deprecated module, also in this file!

    Args:
        prog_lang (str): The programming language to use
        mode (str, optional): Sets a different mode. Options: 'build' (default) or 'run'

    Returns:
        None: return is only used to end the function
    """

    mode = mode.replace(" ", "_").lower()
    prog_lang = prog_lang.strip()

    if NOW_FILE is False:
        mb.showerror(lang[1], lang[239])
        return

    match mode:
        case "build":
            match prog_lang.lower():
                case "c#":
                    if not NOW_FILE.strip().endswith(("cs", "csproj")):
                        mb.showerror(lang[1], lang[284])
                        return

                    os.system(f"dotnet build \"{os.path.dirname(NOW_FILE)}\"")
                    return
                
                case _:
                    return

        case "run":
            match prog_lang.lower():
                case "c#":
                    if not NOW_FILE.strip().endswith((".cs", ".csproj")):
                        mb.showerror(lang[1], lang[284])
                        return

                    os.system(f"dotnet run --project \"{os.path.dirname(NOW_FILE)}\"")
                    return

                case "python":
                    if not NOW_FILE.strip().endswith('.py'):
                        mb.showerror(lang[1], lang[284])
                        return

                    if sys.platform == "win32":
                        os.system(f"python \"{NOW_FILE}\"")
                        return

                    os.system(f"python3 \"{NOW_FILE}\"")
                    return
                    
                case _:
                    return
                
        case _:
            return

# [!] Over all... a deprecated class lol
class DevOption:
    # [!!] Deprecated function - only here for hmmmm... compatibility reasons?
    def old_init(self, filetypes: str | tuple , programming_language: str, run_cmd: str, build_cmd: str, can_build: bool = False, can_run: bool = True) -> None:
        """
        old_init initializes the DevOption class

        Args:
            filetypes (str | tuple): Filetype(s) that is/are assigned to that programming language
            programming_language (str): The actual programming language
            run_cmd (str): The command you use to run the code
            build_cmd (str): The command you use to build the code without running
            can_build (bool, optional): Can the code be built? Defaults to False.
            can_run (bool, optional): Can the code run without building it? Defaults to True.
        """

        self.filetypes = filetypes
        self.programming_lang = programming_language
        self.build_cmd = build_cmd
        self.run_cmd = run_cmd

        self.CAN_BUILD = can_build
        self.CAN_RUN = can_run

    # [!!] Another deprecated function
    def _build(self) -> None:
        if not self.CAN_BUILD:
            return

        if not NOW_FILE:
            mb.showerror(lang[1], lang[239])

        if type(self.filetypes) == str:
            self.filetypes = (self.filetypes)

        if NOW_FILE.strip().endswith(self.filetypes):
            os.system(f'cd "{os.path.dirname(NOW_FILE)}"')
            os.system(self.build_cmd)

    # [!!] Ugh... one more yay!
    def _run_code(self) -> None:
        if not self.CAN_RUN:
            return

        if not NOW_FILE:
            mb.showerror(lang[1], lang[239])

        if type(self.filetypes) == str:
            self.filetypes = (self.filetypes)

        if NOW_FILE.strip().endswith(self.filetypes):
            os.system(f'cd "{os.path.dirname(NOW_FILE)}"')
            os.system(self.run_cmd)


def desktop_create(pycommand: str):
    """
    desktop_create creates a Desktop File for Linux

    Args:
        pycommand (string): The command/alias for Python (example: pycommand='python3')
    """

    global desktop_entry

    desktop_entry = f"""#!/usr/bin/env xdg-open
[Desktop Entry]
Name=WriterClassic
Categories=Utility;Office;
Comment[pt_PT]=Editor de ficheiros de texto plano
Comment=Plain text editor
Exec={pycommand} {script_path}
GenericName[pt_PT]=Editor de Texto
GenericName=Text Editor
Icon={data_dir}/logo.png
InitialPreference=8
Keywords[pt_PT]=texto;txt;editor;nota;bloco de notas;wclassic;
Keywords=text;txt;editor;note;notepad;wclassic;
MimeType=text/plain;
Path=
StartupNotify=true
StartupWMClass=WriterClassic
Terminal=false
TerminalOptions=
Type=Application
X-DBUS-ServiceName=
X-DBUS-StartupType=Multi
X-DocPath=
X-KDE-SubstituteUID=false
X-KDE-Username=
"""

    with open(f"{script_dir}/WriterClassic.desktop", mode="w", encoding='utf-8') as desktop_file:
        desktop_file.write(desktop_entry)
        mb.showinfo(lang[1], lang[101])
        desktop_file.close()

    ic(desktop_entry)


def desktop_create_win():
    """
    desktop_create_win creates the window that later on calls desktop_create

    No args needed or wanted.
    """
    desktop_created_win = Toplevel(desktop_win)
    desktop_created_win.title(lang[197])
    if sys.platform == "win32":
        desktop_created_win.iconbitmap(f"{data_dir}/app_icon.ico")
    desktop_created_win.geometry("600x150")
    desktop_created_win.resizable(False, False)

    LabA = Label(desktop_created_win, text=lang[193], font=("Segoe UI", 15))
    LabB = Label(desktop_created_win, text=lang[194], font=("Segoe UI", 12))
    ButtA = Button(desktop_created_win, text=lang[196], command=lambda:
        desktop_create(pycommand='python3'))
    ButtB = Button(desktop_created_win, text=lang[195], command=lambda:
        desktop_create(pycommand='python'))

    LabA.pack()
    LabB.pack()
    ButtA.pack()
    ButtB.pack()

# [i] Credits
def appCredits():
    mb.showinfo(title=lang[28], message=lang[65])
    _LOG.write(f"{str(now())} - The Credits have been shown: OK\n")

# /-/ Super Secret Easter Eggs
# [!?] you saw nothin'
def surprise_egg():
    askNow = sdg.askstring(lang[29], lang[66])

    if askNow == "":
        ic()
        return None

    else:
        mb.showerror(lang[29], lang[67])
        ic()

# [i] The Help section
def APP_HELP():
    simple_webbrowser.Website("https://mf366-coding.github.io/writerclassic.html#docs")
    _LOG.write(f"{str(now())} - Requested online help: AWAITING FOR CONNECTION\n")
    ic()

# [i] This is... well the About section
def aboutApp():
    with open(f"{data_dir}/about.wclassic", mode="r", encoding='utf-8') as about_d:
        about_data = about_d.read()

    about_dialogue = Toplevel(desktop_win)
    about_dialogue.geometry("600x275")

    about_dialogue.resizable(False, False)

    about_dialogue.title(lang[64])
    label_1 = Label(about_dialogue, text=str(about_data), font=("Calibri", 13))

    # [!?] ChatGPT instrusion down here (lol)

    # [*] Load the PNG image using PIL
    image = Image.open(f"{data_dir}/logo.png")

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
    resized_image = image.resize((desired_width, desired_height), Image.LANCZOS)

    # [*] Create a PhotoImage object from the resized image
    photo = ImageTk.PhotoImage(resized_image)

    button_1 = Button(about_dialogue, text="Ok", command=about_dialogue.destroy)
    button_2 = Button(about_dialogue, text=lang[278], command=lambda:
        simple_webbrowser.webbrowser.open("https://mf366-coding.github.io/writerclassic.html", new=2))

    # [*] Create a Label widget to display the image
    image_label = Label(about_dialogue, image=photo)

    image_label.grid(column=1, row=1)
    label_1.grid(column=2, row=1)
    button_1.grid(column=1, row=2)
    button_2.grid(column=2, row=2)

    about_dialogue.mainloop()

    _LOG.write(f"{str(now())} - The About dialogue has been shown\n")
    about_d.close()

    ic()


def markdown_preview() -> None:
    if not NOW_FILE:
        mb.showerror(lang[1], lang[221])
        return

    if not NOW_FILE.lower().endswith((".md", ".mdown", ".mkd", ".mkdn")):
        mb.showerror(lang[1], lang[222])
        return

    temp_html_path = os.path.join(temp_dir, f"{random.randint(1, 1000)}_{os.path.basename(NOW_FILE).replace(' ', '_')}.html")
    html_content = markdown2.markdown(TextWidget.get(0.0, END))

    with open(temp_html_path, "w", encoding="utf-8")as temp_html_f:
        temp_html_f.write(html_content)
        temp_html_f.close()

    os.system(temp_html_path)


def Tips_Tricks():
    picked_text = random.choice((
        lang[140],
        lang[142],
        lang[299],
        lang[300],
        lang[301],
        lang[302],
        lang[303],
        lang[305]
    ))

    ic(picked_text)

    mb.showinfo(lang[1], picked_text)
    _LOG.write(f"{str(now())} - Requested Tips & Tricks: OK\n")

    ic()

def resetWriter():
    global settings

    ic(settings)

    askSOS = mb.askyesno(lang[77], lang[78])
    if askSOS:
        settings = {
            "font": {
                "type": "Segoe UI",
                "size": 12
            },
            "theme": {
                "color": "black",
                "ct": "white",
                "fg": "white",
                "mfg": "black",
                "menu": "dark grey"
            },
            "advanced-mode": False,
            "startup": True,
            "geometry": "700x500",
            "language": "en",
            "dencrypt": "",
            "debugging": False,
            "email": ""
        }

        ic(settings)

        fast_dump()

        _LOG.write(f"{str(now())} - Fonts have been reset: OK\n")

        _LOG.write(f"{str(now())} - Language and theme have both been reset: OK\n")

        desktop_win.geometry('700x500')

        _LOG.write(f"{str(now())} - Window's dimensions have been reset: OK\n")

        with open(f"{config}/signature.wclassic", "w", encoding='utf-8') as sigFILE:
            sigFILE.write("--\nBest regards,\nThis is a customizable signature in a file named signature.wclassic in the data folder...")
            _LOG.write(f"{str(now())} - The Custom Signature has been reset: OK\n")

    ic(settings)

def _terminal_get(entry_selection):
    _data = entry_selection.get()

    os.system(_data)

    _LOG.write(f"{str(now())} - Used the following command on the Terminal - {str(_data)}: OK\n")

    ic(_data)

def _trick_terminal(func, window):
    window.destroy()

    func()
    ic()

    _LOG.write(f"{str(now())} - Refreshed the Terminal Inputs: OK\n")

def Terminal():
    terminal = Toplevel(desktop_win)

    terminal.title(lang[183])

    _LOG.write(f"{str(now())} - Opened the Terminal Inputs: OK\n")

    entry_1 = Entry(terminal, font=("Calibri", 13))
    butt_1 = Button(terminal, text=lang[178], command=lambda:
        _terminal_get(entry_1))
    butt_2 = Button(terminal, text=lang[184], command=lambda:
        _trick_terminal(Terminal, terminal))

    entry_1.pack()
    butt_1.pack()
    butt_2.pack()

    terminal.mainloop()

class InternetOnWriter:
    @staticmethod
    def Website():
        askForLink = sdg.askstring(lang[80], lang[91])
        if askForLink != ' ' or askForLink != '':
            simple_webbrowser.Website(askForLink)
            _LOG.write(f"{str(now())} - Went to {str(askForLink)} via WriterClassic: OK\n")
        ic()

    @staticmethod
    def Search(engine):
        if engine == 'google':
            askForTyping = sdg.askstring(lang[83], lang[90])
            if askForTyping != '':
                simple_webbrowser.Google(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on Google: OK\n")

        elif engine == 'bing':
            askForTyping = sdg.askstring(lang[82], lang[90])
            if askForTyping != '':
                simple_webbrowser.Bing(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on Bing: OK\n")

        elif engine == 'ysearch':
            # [i] stands for Yahoo!
            askForTyping = sdg.askstring(lang[85], lang[90])
            if askForTyping != '':
                simple_webbrowser.Yahoo(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on Yahoo!: OK\n")

        elif engine == 'ddgo':
            # [i] stands for DuckDuckGo
            askForTyping = sdg.askstring(lang[84], lang[90])
            if askForTyping != '':
                simple_webbrowser.DuckDuckGo(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on DuckDuckGo: OK\n")

        elif engine == "yt":
            # [i] stands for YouTube
            askForTyping = sdg.askstring(lang[99], lang[90])
            if askForTyping != '':
                simple_webbrowser.YouTube(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on YouTube: OK\n")

        elif engine == "ecosia":
            askForTyping = sdg.askstring(lang[98], lang[90])
            if askForTyping != '':
                simple_webbrowser.Ecosia(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on Ecosia: OK\n")

        elif engine == "stack":
            # [i] stands for Stack Overflow
            askForTyping = sdg.askstring(lang[100], lang[90])
            if askForTyping != '':
                simple_webbrowser.StackOverflow(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on StackOverflow: OK\n")

        elif engine == "soundcloud":
            askForTyping = sdg.askstring(lang[104], lang[90])
            if askForTyping != '':
                simple_webbrowser.SoundCloud(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on SoundCloud: OK\n")

        elif engine == "archive":
            # [i] stands for The Internet Archive
            askForTyping = sdg.askstring(lang[109], lang[90])
            if askForTyping != '':
                simple_webbrowser.Archive(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on The Internet Archive: OK\n")

        elif engine == "qwant":
            # [i] stands for Qwant.com
            askForTyping = sdg.askstring(lang[108], lang[90])
            if askForTyping != '':
                simple_webbrowser.Qwant(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on Qwant: OK\n")

        elif engine == "spotify":
            # [i] stands for Spotify Online
            askForTyping = sdg.askstring(lang[126], lang[90])
            if askForTyping != '':
                simple_webbrowser.SpotifyOnline(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on Spotify Online: OK\n")

        elif engine == 'brave':
            # [i] stands for Brave Search
            askForTyping = sdg.askstring(lang[139], lang[90])
            if askForTyping != '':
                simple_webbrowser.Brave(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on Brave Search: OK\n")

        elif engine == "github":
            askForTyping = sdg.askstring(lang[170], lang[90])
            if askForTyping != '':
                simple_webbrowser.GitHub(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on GitHub: OK\n")

        elif engine == "gitlab":
            askForTyping = sdg.askstring(lang[172], lang[90])
            if askForTyping != '':
                simple_webbrowser.GitLab(askForTyping)
                _LOG.write(f"{str(now())} - Searched for {str(askForTyping)} on GitLab: OK\n")

def lock_a_win(window: Tk = desktop_win):
    window.resizable(bool(window_lock_status.get()), bool(window_lock_status.get()))

def plugin_help():
    simple_webbrowser.Website("https://github.com/MF366-Coding/WriterClassic/wiki/Plugin-Setup")
    _LOG.write(f"{str(now())} - Requested help with the Plugin Central: OK\n")

def article_md():
    simple_webbrowser.Website(url='https://github.com/MF366-Coding/WriterClassic/wiki/Manual-Configuration-Setup')
    _LOG.write(f"{str(now())} - Requested help with the Manual Configuration: OK\n")


class _Plugin:
    def __init__(self, folder_name: str) -> None:
        """
        __init__ intializes the class _Plugin

        Args:
            folder_name (str): the name of the folder, to be honest
        """
        self.FOLDER_URL = folder_name
        # --
        self.DETAILS_FILE = None
        self.DETAILS_CONTENT = None
        self.MAIN_CONTENT = None
        self.MAIN_FILE = None
        self.ICON_FILE = None
        self.ICON = None

    def _get_files(self) -> None:
        try:
            versioning_file = get(f"https://raw.githubusercontent.com/MF366-Coding/WriterClassic-OfficialPlugins/main/Verified_Plugins/{self.FOLDER_URL}/Versions.txt", timeout=3.5)

            versioning_data = versioning_file.text

            # [*] Window Creation
            datax = sdg.askinteger(title=f"{lang[1]} - {lang[203]}", prompt=f'{lang[202]}\n{lang[204]} {int(versioning_data)}.', initialvalue=int(versioning_data), minvalue=1, maxvalue=int(versioning_data))

            # [!?] Some of the following code belongs to ChatGPT and other AIs!

            # [i] URL of the zip file
            zip_url = f"https://raw.githubusercontent.com/MF366-Coding/WriterClassic-OfficialPlugins/main/Verified_Plugins/{self.FOLDER_URL}/Version{int(datax)}.zip"

            # [i] Send a GET request to download the zip file
            zip_response = get(zip_url, timeout=4.5)

        except (exceptions.ConnectTimeout, exceptions.ConnectionError, TimeoutError, exceptions.ReadTimeout):
            mb.showerror(lang[148], {lang[135]})

        except Exception:
            mb.showerror(lang[133], lang[134])

        else:
            parent_directory = plugin_dir
            new_folder_base_name = 'plugin'
            counter = 1

            while True:
                new_folder_name = f'{new_folder_base_name}_{counter}'
                new_folder_path = os.path.join(parent_directory, new_folder_name)

                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)
                    break

                counter += 1

            if zip_response.status_code == 200:
                zip_filepath = os.path.join(new_folder_path, "Plugin.zip")

                # [i] Save the downloaded zip file
                with open(zip_filepath, "wb") as f:
                    f.write(zip_response.content)

                # [i] Extract the contents of the zip file to the same location
                with zipfile.ZipFile(zip_filepath, mode="r") as zip_ref:
                    zip_ref.extractall(new_folder_path)

                # [!?] Delete the downloaded zip file
                os.remove(zip_filepath)


def install_plugin(**options):
    """
    install_plugin installs a plugin using _Plugin
    """
    questiony = None

    try:
        if len(options["folder_name"]) >= 1:
            questiony = options["folder_name"]

    except KeyError:
        questiony = sdg.askstring(lang[1], f'{lang[220]}\n{lang[219]}', initialvalue="Type here.")

    finally:
        plugin = _Plugin(folder_name=str(questiony))
        plugin._get_files()

def remove_action(_id: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | int, _plug: int = 1):
    """
    remove_action removes a directory related to WriterClassic

    It first asks the user's consent.

    Args:
        _id (int): the ID of the dir to remove
        _plug (int, optional): the plugin you want to remove. This will be ignored unless the _id argument is 2 or 3. Defaults to 1.

    The Possible IDs:
        0 - Dir where all plugins are stored (plugins)
        1 - WriterClassic's main dir
        2 or 3 - X plugin (used alongside the _plug arg)
        4 - Dir where settings are stored (config)
        5 - Dir where the Log File is stored (user_data)
        6 - Optional dir where a Linux *.desktop file comes (nix_assets)
        7 - Dir where data like versioning and logos are (data)
        8 - Dir where all language files are stored (locale)
        9 - Dir where all temporary files get stored (temp; this folder is cleared every time you open WriterClassic)
        10 - Dir where auto scripts are stored (scripts)
    """

    ids = (
        plugin_dir,
        script_dir,
        "plugx",
        "plugx",
        config,
        user_data,
        nix_assets,
        data_dir,
        locale,
        temp_dir,
        scripts_dir
    )

    _id = clamp(_id, 0, len(ids) - 1)

    path_to_remove = ids[_id]

    if path_to_remove == "plugx":
        path_to_remove = os.path.join(plugin_dir, f"plugin_{_plug}")

    c = mb.askyesno(lang[308], f"{lang[307]} '{path_to_remove}'.")

    if c:
        try:
            if sys.platform == "win32":
                os.system(f'rmdir /s /q {path_to_remove}')
                return

            os.system(f'rm -rf {path_to_remove}')

        except Exception as e:
            mb.showerror(lang[308], f"{lang[309]} '{path_to_remove}':\n{e}")


def execute(datay: int | str):
    # [i] Initializes the plugin system
    initializer(globals())

    run_a_plugin(datay)

def remove_plugin():
    c = mb.askyesno(lang[311], lang[314])

    if not c:
        return

    datax = sdg.askinteger(lang[311], f"{lang[312]}\n{lang[313]}", initialvalue=1, minvalue=1)

    try:
        if sys.platform == "win32":
            os.system(f'rmdir /s /q {os.path.join(plugin_dir, f"plugin_{datax}")}')
            return

        os.system(f'rm -rf {os.path.join(plugin_dir, f"plugin_{datax}")}')

    except Exception as e:
        mb.showerror(lang[311], f"{lang[309]} '{os.path.join(plugin_dir, f'plugin_{datax}')}':\n{e}")

def run_plugin():
    questionx = mb.askyesnocancel(title=lang[1], message=lang[218])

    if not questionx or questionx == None:
        return

    datax: str = sdg.askstring(lang[1], lang[315], initialvalue=1)

    if datax.isdigit():
        datax = int(datax)

    execute(datay=datax)

def clear_log_file():
    with open(os.path.join(user_data, "log.wclassic"), "w", encoding="utf-8") as f:
        f.write("""--
Log File
--
""")
        f.close()

def clear_log_screen(text_interface):
    text_interface.delete(0.0, END)

    with open(f"{user_data}/log.wclassic", "r", encoding="utf-8") as _TEMP_LOG:
        temp_log = _TEMP_LOG.read()
        text_interface.insert(0.0, str(temp_log))
        _TEMP_LOG.close()

    _LOG.write(f"{str(now())} - Log File has been refreshed: OK\n")

def do_nothing(event):
    event = 'break'
    return event

def show_log():
    _new_window = Toplevel(desktop_win)
    _new_window.resizable(False, False)
    _new_editor = ScrolledText(_new_window, background=theme["color"], foreground=theme["fg"], insertbackground=theme["ct"], font=("Calibri", 14), borderwidth=5)
    _new_editor.bind("<Key>", do_nothing)
    _new_window.title(lang[180])
    _new_editor.pack()
    _new_button = Button(_new_window, text=lang[181], command=lambda:
        clear_log_screen(_new_editor))
    _new_button.pack()

    with open(f"{user_data}/log.wclassic", "r", encoding="utf-8") as _TEMP_LOG:
        temp_log = _TEMP_LOG.read()
        _new_editor.insert(0.0, str(temp_log))
        _TEMP_LOG.close()

    _LOG.write(f"{str(now())} - The Log File has been shown: OK\n")

ic(settings["dencrypt"])

async def autosave():
    return

    if NOW_FILE == False or can_autosave.get() != 1:
        ic('autosave() return None')
        await asyncio.sleep(0.01)
        return

    can_autosave.set(0)
    ic('Cannot autosave.')
    await asyncio.sleep(autosave_cooldown)
    ic('Can autosave.')
    can_autosave.set(1)

def autosave_config():
    return

    global autosave_cooldown

    y = sdg.askfloat(lang[309], f"{lang[310]}\n{lang[311]}", initialvalue=60.0, minvalue=10.0, maxvalue=3600.0)

    ic(y)

    if y != None:
        ic()
        settings['autosave']['cooldown'] = y
        autosave_cooldown = y
        fast_dump()
        return

class SignaturePlugin:
    @staticmethod
    def custom():
        with open(f"{config}/signature.wclassic", "r", encoding="utf-8") as SIGNATURE_FILE:
            signature = SIGNATURE_FILE.read()
            SIGNATURE_FILE.close()

        TextWidget.insert(END, f"\n\n{str(signature)}")

        _LOG.write(f"{str(now())} - The Custom signature has been inserted: OK\n")

    @staticmethod
    def getx() -> str:
        with open(f"{config}/signature.wclassic", "r", encoding="utf-8") as SIGNATURE_FILE:
            signature = SIGNATURE_FILE.read()
            SIGNATURE_FILE.close()

        return signature

    @staticmethod
    def auto():
        username = getuser()
        transformed_username = username.title()

        signature = f"--\n{lang[132]}\n{transformed_username}"

        TextWidget.insert(END, f"\n\n{str(signature)}")

        _LOG.write(f"{str(now())} - The Auto signature has been inserted: OK\n")

def commandPrompt() -> None | bool:
    askNow = sdg.askstring(lang[68], lang[69]).title().replace(" ", "")

    commands: dict[str] = {
        "Editor:Undo": TextWidget.edit_undo,
        "Editor:Redo": TextWidget.edit_redo,
        "Editor:Reset": NewFile,
        "File:Open": OpenFile,
        "File:SaveAs": SaveFile,
        "Status:Save": Save,
        "Status:Refresh": ModifiedStatus,
        "Plugins:Install": install_plugin,
        "Plugins:Run": run_plugin,
        "Plugins:Remove": remove_plugin,
        "History:Reset": TextWidget.edit_reset,
        "Software:Quit": QUIT_WRITER,
        "Software:ForceQuit": quickway,
        "Software:About": aboutApp,
        "Software:Help": APP_HELP,
        "Software:Repo": repo,
        "Software:Credits": appCredits,
        "Log:Clear": clear_log_file,
        "Log:Preview": show_log,
        "Advanced:Send": adv_login,
        "Debug:Swap": show_debug,
        "Tools:ReadmeGen": readme_gen_win,
        "Tools:D3Ncryp7": dencrypt,
        "Advanced:Dencrypt": dencrypt,
        "Software:Version": UpdateCheck.check,
        "Advanced:Version": show_advV,
        "File:OpenWith": open_with_adv,
        "Advanced:Open": open_with_adv,
        "Settings:Dump": fast_dump,
        "Settings:Save": fast_dump,
        "Settings:Size": SetWinSize,
        "Tools:Notepad": new_window,
        "Editor:Stats": DOC_STATS,
        "Tools:WipeFile": WipeFile,
        "Editor:Select": select_all,
        "Editor:SelectAll": select_all,
        "Editor:Lorem": lorem_ipsum,
        "Editor:Readme": readme_writer_classic,
        "Advanced:DesktopFile": desktop_create_win,
        "Tools:Markdown": markdown_preview,
        "Software:Tips": Tips_Tricks,
        "Settings:Reset": resetWriter,
        "Tools:Terminal": Terminal,
        "Internet:Website": InternetOnWriter.Website
    }

    if askNow in commands.keys():
        commands[askNow]()

    elif askNow == None:
        return
    
    mb.showerror(lang[68], lang[70])
    return

backup_system = BackupSystem()

# [i] Key bindings
desktop_win.bind('<Control-o>', lambda a:
    OpenFile(desktop_win))

desktop_win.bind('<Control-n>', lambda a:
    NewFile())

desktop_win.bind('<Control-s>', lambda a:
    Save(desktop_win))

desktop_win.bind('<Control-S>', lambda a:
    SaveFile(desktop_win))

desktop_win.bind('<Control-z>', lambda a:
    TextWidget.edit_undo())

desktop_win.bind('<Control-y>', lambda a:
    TextWidget.edit_redo())

desktop_win.bind('<Control-i>', lambda a:
    aboutApp())

desktop_win.bind('<F1>', lambda a:
    APP_HELP())

desktop_win.bind('<Control-d>', lambda a:
    ThemeSet('#020202', '#fcfcfc', 'white', 'black', '#f4f8f8'))

desktop_win.bind('<Control-l>', lambda a:
    ThemeSet('#fcfcfc', '#020202', 'black', '#f4f8f8', 'black'))

desktop_win.bind('<Control-G>', lambda a:
    SetWinSize())

desktop_win.bind('<Control-P>', lambda a:
    commandPrompt())

'''
desktop_win.bind('<Control-h>', lambda a:
    search_for(True, line_limit=120))

desktop_win.bind('<Control-f>', lambda a:
    search_for(line_limit=120))
'''

desktop_win.bind('<Control-F1>', lambda a:
    execute(1))

desktop_win.bind('<Control-F2>', lambda a:
    execute(2))

desktop_win.bind('<Control-F3>', lambda a:
    execute(3))

desktop_win.bind('<Control-F4>', lambda a:
    execute(4))

desktop_win.bind('<Control-F5>', lambda a:
    execute(5))

desktop_win.bind('<Control-F6>', lambda a:
    execute(6))

desktop_win.bind('<Control-F7>', lambda a:
    execute(7))

desktop_win.bind('<Control-F8>', lambda a:
    execute(8))

desktop_win.bind('<Control-F9>', lambda a:
    execute(9))

desktop_win.bind('<Control-F10>', lambda a:
    execute(10))

desktop_win.bind('<Control-F11>', lambda a:
    execute(11))

desktop_win.bind('<Control-F12>', lambda a:
    execute(12))

desktop_win.bind('<Control-a>', lambda a:
    select_all())

desktop_win.bind('<KeyRelease>', lambda a:
    ModifiedStatus())

keyboard.on_press_key(93, lambda a:
    rmb_popup(None))

def autosave_apply():
    ic()
    return

    settings['autosave']['status'] = bool(can_autosave.get())
    ic(settings['autosave'])
    ic(bool(can_autosave.get()))
    fast_dump()

def close_confirm() -> None:
    ic()
    
    if not ModifiedStatus():
        choice = mb.askyesnocancel(lang[53], f"{lang[199]}\n{lang[200]}")

        if choice == None:
            ic()
            return None

        if choice:
            ic()
            Save(desktop_win)
            ic("Called the save function.")

    ic()
    desktop_win.destroy()
    _LOG.close()
    sys.exit()

# [!] Deprecated way to call the closing of a window
# [!?] Please use to close_confirm instead
def on_closing():
    """
    on_closing asks for the user's confirmation before closing

    XXX This function is deprecated because `close_confirm` offers a better way to handle this situation
    """
    
    ic()

    result = mb.askyesno(lang[53], lang[54])

    if not result:
        ic()
        return

    ic()

    desktop_win.destroy()
    _LOG.close()
    sys.exit()

def QUIT_WRITER():
    """
    QUIT_WRITER quits the software using close_confirm
    
    It serves as a connection bridge.
    """

    ic()

    close_confirm()

# [i] Creating the menu dropdowns and buttons
menu_10.add_command(label=lang[94], command=NewFile, accelerator="Ctrl + N")
menu_10.add_command(label=lang[7], command=lambda:
    OpenFile(desktop_win), accelerator="Ctrl + O")
'''
if QUICK_ACESS_DATA != []:
    menu_10.add_cascade(label=lang[292], menu=menu_18)
'''
menu_10.add_separator()
menu_10.add_command(label = lang[8], command=lambda:
    Save(desktop_win), accelerator="Ctrl + S")
menu_10.add_command(label = lang[9], command=lambda:
    SaveFile(desktop_win), accelerator="Ctrl + Shift + S")
menu_10.add_separator()
menu_10.add_command(label=lang[293], command=TextWidget.edit_undo, accelerator="Ctrl + Z")
menu_10.add_command(label=lang[294], command=TextWidget.edit_redo, accelerator="Ctrl + Y")
'''
menu_10.add_separator()
menu_10.add_command(label=lang[329], command=search_for, accelerator="Ctrl + F")
menu_10.add_command(label=lang[330], command=lambda:
    search_for(True), accelerator="Ctrl + H")
'''
menu_10.add_separator()
menu_10.add_command(label=lang[163], command=DOC_STATS)
menu_10.add_separator()
menu_10.add_command(label=lang[11], command=QUIT_WRITER, accelerator="Alt + F4")

'''
for i in range(len(QUICK_ACESS_DATA)):
    menu_18.add_command(label=str(QUICK_ACESS_DATA[i]), command=lambda:
        OpenFileManually(str(QUICK_ACESS_DATA[i])))
'''

if startApp == "1":
    menu_11.add_command(label=lang[75], command=UpdateCheck.check)
    menu_11.add_separator()
menu_11.add_command(label=lang[25], command=aboutApp, accelerator="Ctrl + I")
menu_11.add_command(label=lang[186], command=lambda:
    simple_webbrowser.Website("https://www.buymeacoffee.com/mf366"))
menu_11.add_command(label=lang[26], command=APP_HELP, accelerator="F1")
menu_11.add_command(label=lang[27], command=repo)
menu_11.add_command(label=lang[179], command=show_log)
menu_11.add_separator()
menu_11.add_command(label=lang[28], command=appCredits)
menu_11.add_separator()
menu_11.add_command(label=lang[137], command=Tips_Tricks)
'''
menu_11.add_separator()
menu_11.add_command(label=lang[29], command=surprise_egg, state='disabled')
'''

menu_1.add_command(label=lang[12], command=SetWinSize, accelerator="Ctrl + Shift + G")


menu_7.add_command(label=lang[20], command=lambda:
                        fontEdit(1))
menu_7.add_command(label=lang[21], command=lambda:
                        fontEdit(2))

menu_8.add_command(label=lang[22], command=new_window)
'''
menu_8.add_command(label=lang[23], command=clockPlugin, state="disabled")
'''
menu_8.add_command(label=lang[182], command=Terminal)
menu_8.add_separator()
menu_8.add_command(label=lang[131], command=SignaturePlugin.custom)
menu_8.add_command(label=lang[130], command=SignaturePlugin.auto)
menu_8.add_separator()
menu_8.add_command(label=lang[10], command=lambda:
    WipeFile(desktop_win))
menu_8.add_separator()

menu_8.add_command(label=lang[217], command=install_plugin)
menu_8.add_command(label=lang[216], command=run_plugin)
menu_8.add_command(label=lang[310], command=remove_plugin)

menu_9.add_command(label=lang[81], command=InternetOnWriter.Website)
menu_9.add_separator()
menu_9.add_command(label=lang[87], command=lambda:
    InternetOnWriter.Search('google'))
menu_9.add_command(label=lang[86], command=lambda:
    InternetOnWriter.Search('bing'))
menu_9.add_command(label=lang[89], command=lambda:
    InternetOnWriter.Search('ysearch'))
menu_9.add_command(label=lang[88], command=lambda:
    InternetOnWriter.Search('ddgo'))
menu_9.add_command(label=lang[138], command=lambda:
    InternetOnWriter.Search("brave"))
menu_9.add_command(label=lang[95], command=lambda:
    InternetOnWriter.Search("ecosia"))
menu_9.add_command(label=lang[106], command=lambda:
    InternetOnWriter.Search("qwant"))
menu_9.add_separator()
menu_9.add_command(label=lang[97], command=lambda:
    InternetOnWriter.Search("stack"))
menu_9.add_separator()
menu_9.add_command(label=lang[96], command=lambda:
    InternetOnWriter.Search("yt"))
menu_9.add_command(label=lang[103], command=lambda:
    InternetOnWriter.Search("soundcloud"))
menu_9.add_command(label=lang[125], command=lambda:
    InternetOnWriter.Search("spotify"))
menu_9.add_separator()
menu_9.add_command(label=lang[107], command=lambda:
    InternetOnWriter.Search("archive"))
menu_9.add_separator()
menu_9.add_command(label=lang[169], command=lambda:
    InternetOnWriter.Search("github"))
menu_9.add_command(label=lang[171], command=lambda:
    InternetOnWriter.Search("gitlab"))

# [!!] Languages need to be fixed
# [!!] Some languages are in a verification state
# [!!] They might stay in such state for ages
# [!] Please be patient
# [!?] Thank you!
# --
# [i] English verified by MF366
# [i] Slovak verified by Norb
# [!?] Portuguese still being verified by MF366 and Zeca70
# --
# [i] Thank you, dear contributors for all the help!
'''
menu_13.add_command(label="Čeština (Čechie)", command=lambda:
    LanguageSet("cs", desktop_win), state='disabled')
menu_13.add_command(label="Dansk (Danmark)", command=lambda:
    LanguageSet("da", desktop_win), state='disabled')
'''
menu_13.add_command(label="Deutsch (Deutschland)", command=lambda:
    LanguageSet("de", desktop_win), state='disabled')
menu_13.add_command(label='English (USA)', command=lambda:
    LanguageSet('en', desktop_win))
menu_13.add_command(label='Español (España)', command=lambda:
    LanguageSet('es', desktop_win), state='disabled')
menu_13.add_command(label='Français (France)', command=lambda:
    LanguageSet('fr', desktop_win), state='disabled')
menu_13.add_command(label='Italiano (Italia)', command=lambda:
    LanguageSet('it', desktop_win), state='disabled')
'''
menu_13.add_command(label='Ελληνικά (Ελλάδα)', command=lambda:
    LanguageSet("el", desktop_win), state='disabled')
menu_13.add_command(label="Norsk (Norge)", command=lambda:
    LanguageSet("nb", desktop_win), state='disabled')
'''
menu_13.add_command(label='Português (Brasil)', command=lambda:
    LanguageSet('br', desktop_win), state='disabled')
menu_13.add_command(label='Português (Portugal)', command=lambda:
    LanguageSet('pt', desktop_win))
menu_13.add_command(label='Slovenčina (Slovensko)', command=lambda:
    LanguageSet('sk', desktop_win))
'''
menu_13.add_command(label="Svenska (Sverige)", command=lambda:
    LanguageSet("sv", desktop_win), state='disabled')
menu_13.add_command(label="Українська (Україна)", command=lambda:
    LanguageSet("uk", desktop_win), state='disabled')
'''

menu_12.add_cascade(label=lang[198], menu=menu_13)
'''
menu_12.add_separator()
menu_12.add_checkbutton(label=lang[307], variable=can_autosave, command=autosave_apply)
menu_12.add_command(label=lang[308], command=autosave_config)
'''
menu_12.add_separator()
menu_12.add_checkbutton(label=lang[298], variable=update_check_button, command=UpdateCheck.change)
menu_12.add_separator()

if sys.platform == "linux":
    menu_12.add_command(label=lang[192], command=desktop_create_win)
    menu_12.add_separator()

menu_12.add_checkbutton(label=lang[191], variable=window_lock_status, command=lock_a_win)
menu_12.add_separator()
menu_12.add_command(label=lang[320], command=lambda:
    backup_system.run_action("zip"))
menu_12.add_command(label=lang[321], command=lambda:
    backup_system.run_action("load"))
menu_12.add_separator()
menu_12.add_command(label=lang[76], command=resetWriter)
'''
menu_12.add_separator()
menu_12.add_command(label=lang[105], command=article_md, state='disabled')
'''


menu_15.add_command(label=lang[279], command=markdown_preview)
menu_15.add_separator()
menu_15.add_cascade(menu=menu_16, label=lang[282])
menu_15.add_cascade(menu=menu_17, label=lang[283])

menu_16.add_command(label="C#", command=lambda:
    dev_option("C#"))

menu_17.add_command(label="C#", command=lambda:
    dev_option("C#", "run"))
menu_17.add_command(label="Python", command=lambda:
    dev_option("Python", "run"))


menu_5.add_command(label=lang[16], command=lambda:
    ThemeSet('#fcfcfc', '#020202', 'black', '#f4f8f8', 'black'), accelerator="Ctrl + L")
menu_5.add_command(label=lang[17], command=lambda:
    ThemeSet('#020202', '#fcfcfc', 'white', 'black', '#f4f8f8'), accelerator="Ctrl + D")
menu_5.add_separator()
menu_5.add_command(label=lang[18], command=lambda:
    ThemeSet('grey', 'black', 'black', 'black', 'white'))


menu_6.add_command(label="WriterClassic v8.1.1 (Norb)", command=lambda:
    ThemeSet("#0055FF", "#B3BFFF", "#fcfff7", "#fcfff7", "#0055FF"))

menu_6.add_separator()

menu_6.add_command(label='WriterClassic Aqua', command=lambda:
    ThemeSet('#12aace', '#040426', '#040426', '#070755', '#bcf6f1'))

menu_6.add_command(label='WriterClassic Earth', command=lambda:
    ThemeSet('#4a0d0d', '#eccccc', '#e8bebe', '#2b0808', '#e8bebe'))

menu_6.add_command(label='Codetime', command=lambda:
    ThemeSet('#0f0e0e', '#3fdc24', '#33e814', 'black', '#2af48e'))

menu_6.add_separator()

menu_6.add_command(label='Darkest Night Ever', command=lambda:
    ThemeSet('#040114', '#e8a78e', '#e8a78e', 'black', '#e8a78e'))

menu_6.add_command(label='Dark Forest', command=lambda:
    ThemeSet('#0e2414', '#c0db7b', '#c0db7b', '#040d07', '#ccf0c5'))

menu_6.add_command(label='Christmas Night', command=lambda:
    ThemeSet('#020421', '#a5a9e8', '#a5a9e8', '#020312', '#cbcef2'))

menu_6.add_command(label='Silent Night', command=lambda:
    ThemeSet('#020421','pink', 'pink', '#020312', '#ebd1ed'))

if sys.platform == "win32":
    menu_6.add_command(label='PowerShell Theme', command=lambda:
        ThemeSet("#012456", "#eeedf0", "#fedba9", "#eeedf0", "#012456"))

ic(settings["advanced-mode"])
ic(settings["debugging"])

def adv_change():
    settings["advanced-mode"] = bool(advanced_mode_status.get())

    ic(settings["advanced-mode"])
    fast_dump()

    mb.showinfo(message=lang[63], title=lang[1])

menu_12.add_separator()
menu_12.add_checkbutton(label=lang[306], variable=advanced_mode_status, command=adv_change)

def show_debug():
    if settings["debugging"]:
        settings["debugging"] = False

    else:
        settings["debugging"] = True

    ic(settings["debugging"])
    fast_dump()

    mb.showinfo(message=lang[63], title=lang[1])

def dencrypt():
    def runx(pathx: str, parameters: str):
        settings["dencrypt"] = pathx
        fast_dump()

        if not NOW_FILE:
            mb.showinfo(lang[1], lang[239])

        else:
            os.system(f'"{pathx}" "{NOW_FILE}" {parameters}')
            mb.showinfo(lang[1], lang[275])

    new = Toplevel(desktop_win)
    if sys.platform == "win32":
        new.iconbitmap(f"{data_dir}/app_icon.ico")
    new.title(f"{lang[1]} - {lang[274]}")
    new.resizable(False, False)

    label_1 = Label(new, text=f"{lang[273]}: ", font=("Segoe UI", 13))
    entry_1 = Entry(new, font=('Segoe UI', 13), width=58)
    label_2 = Label(new, text=f"{lang[272]}: ", font=("Segoe UI", 13))
    entry_2 = Entry(new, font=('Segoe UI', 13), width=58)

    entry_1.insert(0, settings["dencrypt"])
    entry_2.insert(0, "-e")

    butt_1 = Button(new, text=f"{lang[178]}!", command=lambda:
        runx(entry_1.get(), entry_2.get()))
    butt_2 = Button(new, text=lang[271], command=lambda:
        simple_webbrowser.Website("https://github.com/MF366-Coding/d3NCRYP7#d3ncryp7---simple-encryption-and-decryption-system"))

    label_1.grid(column=1, row=1)
    entry_1.grid(column=2, row=1)
    label_2.grid(column=1, row=2)
    entry_2.grid(column=2, row=2)
    butt_1.grid(column=1, row=3)
    butt_2.grid(column=2, row=3)

    new.mainloop()

def readme_gen(*entries):
    _title = entries[0]
    _describe = entries[1]
    _author_email = entries[2]
    _author_website = entries[3]
    _project_website = entries[4]
    _sponsor_site = entries[5]

    TextWidget.delete(0.0, END)

    if _title in NOT_ALLOWED:
        _title = lang[270]

    if _describe in NOT_ALLOWED:
        _describe = f"{lang[269]} {_title}"

    readme_generated = f"""{_title}
**{_describe}**

"""

    if _author_email not in NOT_ALLOWED:
        readme_generated += f"""[{lang[268]}]({_author_email})\n"""

    if _author_website not in NOT_ALLOWED:
        readme_generated += f"""[{lang[267]}: {_author_website}]({_author_website})\n"""

    if _project_website not in NOT_ALLOWED:
        readme_generated += f"""[{lang[266]}: {_project_website}]({_project_website})\n"""

    if _sponsor_site not in NOT_ALLOWED:
        readme_generated += f"""[{lang[265]}]({_sponsor_site})\n"""

    TextWidget.insert(chars=readme_generated, index=0.0)

    ic(readme_generated)

def readme_gen_win():
    # [i] Window Creation
    window = Toplevel(desktop_win)
    window.title(f"{lang[1]} - {lang[226]}")
    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    label_1 = Label(window, text=f'{lang[264]}:', font=('Calibri', 13))
    label_2 = Label(window, text=f'{lang[263]}:', font=('Calibri', 13))
    label_3 = Label(window, text=f'{lang[262]}:', font=('Calibri', 13))
    label_4 = Label(window, text=f'{lang[261]}:', font=('Calibri', 13))
    label_5 = Label(window, text=f'{lang[260]}:', font=('Calibri', 13))
    label_6 = Label(window, text=f'{lang[259]}:', font=('Calibri', 13))
    label_7 = Label(window, text=f"{lang[258]}:".upper(), font=("Calibri", 13))
    label_8 = Label(window, text=lang[257], font=("Calibri", 13))

    _title = Entry(window, font=('Calibri', 12))
    _describe = Entry(window, font=('Calibri', 12))
    _author_email = Entry(window, font=('Calibri', 12))
    _author_website = Entry(window, font=('Calibri', 12))
    _project_website = Entry(window, font=('Calibri', 12))
    _sponsor_site = Entry(window, font=('Calibri', 12))

    butt_1 = Button(window, text=lang[256], command=lambda:
        readme_gen(_title.get(), _describe.get(), _author_email.get(), _author_website.get(), _project_website.get(), _sponsor_site.get()))

    butt_2 = Button(window, text=lang[255], command=window.destroy)

    label_1.grid(column=1, row=2)
    label_2.grid(column=1, row=3)
    label_3.grid(column=1, row=4)
    label_4.grid(column=1, row=5)
    label_5.grid(column=1, row=6)
    label_6.grid(column=1, row=7)
    label_7.grid(column=1, row=1)
    label_8.grid(column=2, row=1)

    _title.grid(column=2, row=2)
    _describe.grid(column=2, row=3)
    _author_email.grid(column=2, row=4)
    _author_website.grid(column=2, row=5)
    _project_website.grid(column=2, row=6)
    _sponsor_site.grid(column=2, row=7)

    butt_1.grid(column=1, row=8)
    butt_2.grid(column=2, row=8)

    window.mainloop()

def open_with_adv():
    window = Toplevel(desktop_win)
    window.title(f"{lang[1]} - {lang[254]}")
    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    def action_1():
        if not NOW_FILE:
            mb.showinfo(lang[1], lang[239])
        else:
            os.system(f'"{str(NOW_FILE)}"')

        window.destroy()

    def action_2(requested_entry):
        if not NOW_FILE:
            mb.showinfo(lang[1], lang[239])
        else:
            if " " in requested_entry:
                os.system(f'"{requested_entry}" "{str(NOW_FILE)}"')
            else:
                os.system(f'{requested_entry} "{str(NOW_FILE)}"')

        window.destroy()

    butt_1 = Button(window, text=lang[253], command=action_1)
    label_1 = Label(window, text=lang[252].upper(), font=("Arial", 15))
    label_2 = Label(window, text=lang[251], font=("Calibri", 13))
    entry_1 = Entry(window, font=("Calibri", 13))
    butt_2 = Button(window, text=lang[250], command=lambda:
        action_2(entry_1.get()))

    butt_1.grid(column=1, row=1)
    label_1.grid(column=1, row=2)
    label_2.grid(column=1, row=3)
    entry_1.grid(column=2, row=3)
    butt_2.grid(column=1, row=4)

    window.mainloop()

def send_email_with_attachment(win, signa: bool, sender_email: str, sender_password: str, recipient_email: str, subject: str, body: str):
    win.destroy()

    if not signa:
        body += f"\n\n{lang[249]} (https://mf366-coding.github.io/writerclassic.html)"

    elif signa:
        body += f"\n\n{SignaturePlugin.getx()}"

    # [!?] Certain parts of this function belongs to:
    # [*] https://medium.com/@hannanmentor/20-python-scripts-with-code-to-automate-your-work-68662a8dcbc1
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    try:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        with open(NOW_FILE, "r", encoding="utf-8") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(NOW_FILE)}")
            message.attach(part)
        server.sendmail(sender_email, recipient_email, message.as_string())

    except Exception:
        mb.showerror(lang[1], f"{lang[247]}\n{lang[248]}")

    server.quit()

def message_write(mail: str, pwd: str, _variable, win):
    win.destroy()

    if _variable == '1':
        try:
            settings["email"] = str(mail)
            fast_dump()
        except Exception:
            pass

    # [*] Window Creation
    window = Toplevel(desktop_win)
    window.title(f"{lang[1]} - {lang[246]}")

    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    label_1 = Label(window, text=f"{lang[245]}: ", font=("Noto Sans", 13))
    label_2 = Label(window, text=lang[244], font=("Noto Sans", 11))
    label_3 = Label(window, text=f"{lang[243]}: ", font=("Noto Sans", 13))
    label_4 = Label(window, text=f"{lang[242]}: ", font=("Noto Sans", 13))

    entry_1 = Entry(window, font=("Noto Sans", 13))
    entry_2 = Entry(window, font=("Noto Sans", 13))

    text_1 = ScrolledText(window, borderwidth=5, font=(font_use["type"], font_use["size"]), insertbackground=theme["ct"], foreground=theme["fg"], background=theme["color"], height=10)

    butt_1 = Button(window, text=lang[241], command=lambda:
        send_email_with_attachment(window, False, mail, pwd, entry_2.get(), entry_1.get(), text_1.get(0.0, END)))

    butt_2 = Button(window, text=lang[240], command=lambda:
        send_email_with_attachment(window, True, mail, pwd, entry_2.get(), entry_1.get(), text_1.get(0.0, END)))

    label_1.pack()
    label_2.pack()
    entry_2.pack()

    label_3.pack()
    entry_1.pack()

    label_4.pack()
    text_1.pack()

    butt_1.pack()
    butt_2.pack()

    window.mainloop()


def adv_login():
    # [*] Window Creation
    if not NOW_FILE:
        mb.showerror(lang[1], lang[239])
        return

    window = Toplevel(desktop_win)
    window.title(f"{lang[1]} - {lang[238]}")

    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    label_1 = Label(window, text=lang[237], font=("Noto Sans", 14))
    label_2 = Label(window, text=lang[236], font=("Noto Sans", 11))
    label_3 = Label(window, text=lang[235], font=("Noto Sans", 12))
    label_4 = Label(window, text=f"{lang[234]}: ", font=("Noto Sans", 13))
    label_5 = Label(window, text=f"{lang[233]}: ", font=("Noto Sans", 13))

    entry_1 = Entry(window, font=("Noto Sans", 12))
    entry_2 = Entry(window, font=("Noto Sans", 10), show="*")

    entry_1.insert(0, settings["email"])

    a = StringVar(window)

    butt_1 = Checkbutton(window, text=lang[231], variable=a)
    butt_2 = Button(window, text=lang[232], command=lambda:
        message_write(entry_1.get(), entry_2.get(), a.get(), window))

    label_1.pack()
    label_2.pack()
    label_3.pack()
    label_4.pack()
    entry_1.pack()
    label_5.pack()
    entry_2.pack()
    butt_1.pack()
    butt_2.pack()

    window.mainloop()

def show_advV():
    mb.showinfo(lang[1], f"{lang[230]} {advV}.")
    ic(advV)

if ADVANCED:
    menu_14.add_command(label=lang[224], command=show_debug)
    if sys.platform == "win32":
        menu_14.add_command(label=lang[225], command=dencrypt)
    menu_14.add_command(label=lang[226], command=readme_gen_win)
    menu_14.add_command(label=lang[227], command=open_with_adv)
    menu_14.add_command(label=lang[228], command=adv_login)
    menu_14.add_command(label=lang[229], command=show_advV)

try:
    if sys.platform == "linux":
        # [i] Themed menus only on Linux Python3
        # /-/ Themed menus are also compatible with Windows and Mac, tho
        menu_10.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_11.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_1.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_2.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_3.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_5.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_4.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_6.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_7.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_12.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_8.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_9.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_13.configure(background=theme["menu"], foreground=theme["mfg"])
        if ADVANCED:
            menu_14.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_15.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_16.configure(background=theme["menu"], foreground=theme["mfg"])
        menu_17.configure(background=theme["menu"], foreground=theme["mfg"])
        _LOG.write(f"{str(now())} - The Menus have been themed [LINUX ONLY]: OK\n")
except TclError:
    if sys.platform == "linux":
        # [i] Themed menus only on Linux Python3
        # /-/ Themed menus are also compatible with Windows and Mac, tho
        mb.showerror(lang[150], f"{lang[151]}\n{lang[152]}")
        menu_10.configure(background="white", foreground="black")
        menu_11.configure(background="white", foreground="black")
        menu_1.configure(background="white", foreground="black")
        menu_2.configure(background="white", foreground="black")
        menu_3.configure(background="white", foreground="black")
        menu_5.configure(background="white", foreground="black")
        menu_4.configure(background="white", foreground="black")
        menu_6.configure(background="white", foreground="black")
        menu_7.configure(background="white", foreground="black")
        menu_12.configure(background="white", foreground="black")
        menu_8.configure(background="white", foreground="black")
        menu_9.configure(background="white", foreground="black")
        menu_13.configure(background="white", foreground="black")
        if ADVANCED:
            menu_14.configure(background="white", foreground="black")
        menu_15.configure(background="white", foreground="black")
        menu_17.configure(background="white", foreground="black")
        menu_16.configure(background="white", foreground="black")
        _LOG.write(f"{str(now())} - The Menus have been themed [LINUX ONLY]: OK\n")

# [*] dropdowns/cascades
menu_bar.add_cascade(label=lang[2],menu=menu_10)
menu_bar.add_cascade(label=lang[3],menu=menu_1)
menu_1.add_cascade(label=lang[13], menu=menu_4)
menu_4.add_cascade(label=lang[15], menu=menu_5)
menu_4.add_cascade(label=lang[19], menu=menu_6)
menu_4.add_separator()
menu_4.add_command(label=lang[153], command=lambda:
    simple_webbrowser.Website(url="https://github.com/MF366-Coding/WriterClassic-ExtraThemes"))
menu_1.add_cascade(label=lang[14], menu=menu_7)
menu_bar.add_cascade(label=lang[4], menu=menu_8)
menu_bar.add_cascade(label=lang[79], menu=menu_9)
menu_bar.add_cascade(label=lang[5], menu=menu_12)
menu_bar.add_cascade(label=lang[6], menu=menu_11)
menu_bar.add_cascade(label=lang[280], menu=menu_15)

if ADVANCED:
    menu_bar.add_cascade(label=lang[277], menu=menu_14)

ic(ADVANCED)

# [i] Yes, menu_bar is desktop_win's menu bar lmfao
desktop_win.configure(menu=menu_bar)
_LOG.write(f"{str(now())} - The Menu bar has been configured correctly: OK\n")

if len(sys.argv) > 1:
    # [i] The first command-line argument is the file path
    file_path = sys.argv[1]
    ic(file_path)

    try:
        OpenFileManually(file_path)

    except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
        mb.showerror(title=lang[187], message=f"{lang[188]} {str(file_path)}.")
        run_default = mb.askyesno(title=lang[187], message=lang[189])
        # [?] What if WriterClassic is the default thought lol?
        if run_default:
            os.system(str(file_path))

    except FileNotFoundError as e:
        desktop_win.destroy()
        ic(e)
        _LOG.write(f"{str(now())} - Found error {e} while trying to open file at {str(file_path)}: INFO\n")
        quit()

    finally:
        ic(NOW_FILE)

desktop_win.protocol("WM_DELETE_WINDOW", close_confirm)

# [*] And done!
# [i] Now, it will continuously mainlooping! Enjoy!
desktop_win.mainloop()
