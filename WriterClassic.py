# WriterClassic.py

'''
WriterClassic

Powered by: Python 3.11.8

Official Website:
    https://mf366-coding.github.io/writerclassic.html

Official Repo:
    https://github.com/MF366-Coding/WriterClassic

Find me in this spots:
    https://github.com/MF366-Coding
    https://www.buymeacoffee.com/mf366 (Support me please!)

Original idea and development by: MF366

Small but lovely contributions by:
    Norb (norbcodes at GitHub)
    Zeca70 (Zeca70 at GitHub)
'''

# [*] Sorting the imports
import os
import shutil
import sys
import json
import subprocess
import random
import datetime
import base64
import gzip
import platform
import math
import cmath
import tracemalloc

from typing import Literal, SupportsFloat, Any, Callable  # [i] Making things nicer, I guess

from getpass import getuser # [i] Used in order to obtain the username of the current user, which is used for the Auto Signature

import zipfile as zipper # [i] Used to extract the zip files used by plugins

# [i] tkinter is used for the UI, duh?!
from tkinter import Listbox, Event, DISABLED, NORMAL, SINGLE, Tk, Toplevel, TclError, StringVar, END, Menu, IntVar, INSERT, Frame, WORD, CHAR, NONE, Variable
from tkinter.ttk import Button, Checkbutton, Label, Entry, OptionMenu, Radiobutton, Style # [i] Used because of the auto styling in tkinter.ttk
from tkinter import SEL_FIRST, SEL_LAST
from tkinter.scrolledtext import ScrolledText # [!?] Only here so pyinstaller compiles it - not needed and gets removed later on
import tkinter.messagebox as mb # [i] Used for the message boxes
import tkinter.filedialog as dlg # [i] Used for the "save", "open" dialogues
from tkinter import simpledialog as sdg # [i] Used for dialogues that ask you for an input
from tkinter.font import Font # [i] Used for controlling the fonts in the Text widget
from tkinter import colorchooser # [!?] Same reason why ScrolledText was imported, see above

import smtplib # [i] Used for the Send E-mail option - server management

# [i] The next 4 are all used for the Send E-mail option - encodings and e-mail parts
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# [i] Custom widgets for WriterClassic specifically (a custom ScrolledText widget and a custom Toplevel for Search & Replace)
from editor import WriterClassicEditor, SearchReplace, CustomThemeMaker, deprecated
from plugin_system import load_module_from_source # [i] For WriterClassic's Plugin "API"
from setting_loader import get_settings, dump_settings # [i] Used to load and dump WriterClassic's settings

from pygame import mixer # [i] Playing the sucessful sound => Only in this file so it gets compiled

from icecream import ic # [i] Used for debugging

from PIL import Image, ImageTk # [i] Used for placing the WriterClassic logo on the screen

import tkfontchooser # [i] used for the new Font picker

import pyperclip as pyclip # [i] used for the clipboard options

import markdown2 # [i] Used to make HTML files from Markdown

import simple_webbrowser # [i] My own Python module (used for the Search with... options)
from requests import get, exceptions # [i] Used for regular interactions with the Internet

# /-/ import chlorophyl # [i] Code view for Snippets

del ScrolledText, colorchooser

current_file = False # [*] current file, otherwise False
cur_data: str = ""
grp: None = None # [i] Redefined later on...
save_status: bool = True
TOOLBAR_LEN: int = 11

CREDITS = """WriterClassic by: MF366
Powered by: Python 3.11+

- Thank you, Norb and Zeca70, best GitHub contributors (and friends) ever! :)

- Thank you, j4321 for your tkFontChooser module, which really helped me a LOT when implementing the improved version of the Font Picker.

- And thank you, dear user, for using WriterClassic! <3"""

# [!?] Disabling annoying Pylint stuff (specially stupid conventions)

# [*] Everything related to general exceptions (catching them and raising them)
# pylint: disable=W0718
# pylint: disable=W0719

# [*] Module 'PIL.Image' has no 'LANCZOS' member (hint: it does)
# pylint: disable=E1101

# [*] Redefining from outer scope
# pylint: disable=W0621

# [*] Global statement, exec and eval
# pylint: disable=W0603
# pylint: disable=W0122
# pylint: disable=W0123

# [*] Bad indentation nonsense
# pylint: disable=W0311

# [*] String statement doesn't have any effect
# pylint: disable=W0105

# [*] Consider explicitly re-raising...
# pylint: disable=W0707

# [*] Get the absolute path of the script
script_path: str = os.path.abspath(__file__)

# [*] Get the directory containing the script
script_dir: str = os.path.dirname(script_path)

config: str = os.path.join(script_dir, 'config')
user_data: str = os.path.join(script_dir, 'user_data')
nix_assets: str = os.path.join(script_dir, 'nix_assets')
plugin_dir: str = os.path.join(script_dir, 'plugins')
data_dir: str = os.path.join(script_dir, 'data')
locale: str = os.path.join(script_dir, 'locale')
temp_dir: str = os.path.join(script_dir, 'temp')
scripts_dir: str = os.path.join(script_dir, "scripts")

now = datetime.datetime.now


def check_paths(var: str) -> str:
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


debug_a: list[str] = [config, user_data, nix_assets, plugin_dir, data_dir, locale, temp_dir, scripts_dir]

for i in debug_a:
    check_paths(i)


class Logger:
    def __init__(self, logger_path: str, encoding: str = 'utf-8') -> None:
        """
        __init__ is the initializer for the Logger class

        Args:
            logger_path (str): the path to the log file
            encoding (str, optional): the encoding to use when opening the file. Defaults to 'utf-8'.

        Raises:
            ValueError: empty string as path or invalid path
        """

        if logger_path.strip() == '':
            raise ValueError('emptry string as a path value')

        if not os.path.exists(logger_path) or not os.path.isfile(logger_path):
            raise ValueError('invalid path - must be existing file')

        self.logger = open(logger_path, 'a', encoding=encoding)
        self.__newline()

    def write(self, text: str) -> None:
        """
        write writes text to the log file

        Args:
            text (str)
        """

        self.logger.write(text)

    def error(self, text: str, error_details: str | None = None) -> None:
        """
        error writes an error information to the log file

        Syntax is:
            Current Time - text argument: error_details argument

        Args:
            text (str)
            error_details (str | None, optional): extra details such as NO INETERNET CONNECTION. Defaults to ERROR.
        """

        if error_details is None:
            error_details = 'ERROR'

        self.logger.write(f"{str(now())} - {text}: {error_details}\n")

    def warning(self, text: str, details: str | None = None) -> None:
        """
        warning writes a warning to the log file

        Syntax used:
            Current Time - text arg - details arg

        Args:
            text (str)
            details (str | None, optional): extra details such as AN INSECURE ACTION HAS BEEN EXECUTED. Defaults to WARNING.
        """

        if details is None:
            details = 'WARNING'

        self.logger.write(f"{str(now())} - {text}: {details}\n")

    def action(self, text: str, extra: str | None = None) -> None:
        """
        action writes a simple action in the syntax:
            Current Time - text arg - extra arg

        Args:
            text (str)
            extra (str | None, optional): extra details on what was done. Defaults to nothing.
        """

        if extra is None:
            extra = ''

        self.logger.write(f"{str(now())} - {text}: OK {extra}".rstrip() + "\n")

    def close(self) -> None:
        """
        close closes the log file
        """

        self.logger.close()

    def __newline(self) -> None:
        """
        Internal function.
        """

        self.logger.write('\n')

    def __repr__(self) -> str:
        """
        String representation of the logger

        Returns:
            str: same as str(filelike object)
        """

        return str(self.logger)


LOG = Logger(os.path.join(user_data, "log.wclassic"))

LOG.action("WriterClassic was executed")

tracemalloc.start()

ic.configureOutput(prefix="ic debug statement | -> ")


def showerror(title: str | None = None, message: str | None = None, **options) -> str:
    """
    showerror works just like tkinter.messagebox.showerror() but saves the information to the WriterClassic log file

    Args:
        title (str | None, optional): the title of the messagebox. Defaults to None.
        message (str | None, optional): the contents of the messagebox. Defaults to None.

    Returns:
        str: value returned by `tkinter.messagebox.showerror(title, message, **options)`
    """

    s: str = mb.showerror(title, message, **options)

    if title is not None and message is not None:
        LOG.error(message.split('\n')[-1], title.strip())

    return s


def showwarning(title: str | None = None, message: str | None = None, **options) -> str:
    """
    showwarning works just like tkinter.messagebox.showwarning() but saves the information to the WriterClassic log file

    Args:
        title (str | None, optional): the title of the messagebox. Defaults to None.
        message (str | None, optional): the contents of the messagebox. Defaults to None.

    Returns:
        str: value returned by `tkinter.messagebox.showwarning(title, message, **options)`
    """

    s = mb.showwarning(title, message, **options)

    if title is not None and message is not None:
        LOG.warning(message.split('\n')[-1], title.strip())

    return s


def showinfo(title: str | None = None, message: str | None = None, **options) -> str:
    """
    showinfo works just like tkinter.messagebox.showinfo() but saves the information to the WriterClassic log file

    Args:
        title (str | None, optional): the title of the messagebox. Defaults to None.
        message (str | None, optional): the contents of the messagebox. Defaults to None.

    Returns:
        str: value returned by `tkinter.messagebox.showinfo(title, message, **options)`
    """

    s = mb.showinfo(title, message, **options)

    if title is not None and message is not None:
        LOG.action(message.split('\n')[-1], f"- MESSAGEBOX => {title.strip()}")

    return s


def asklink(title: str, prompt: str, encoding: str | None = 'utf-8', require_https: bool = False, initialvalue: str | None = None, show: str | None = None, warning_message: str | None = None):
    link: str = sdg.askstring(title, prompt, initialvalue=initialvalue, show=show)

    if not warning_message:
        warning_message = f"{lang[133]}\n{lang[359]}"

    if require_https:
        while not link.lstrip().startswith('https://'):
            showwarning(title, warning_message)
            link: str = sdg.askstring(title, prompt, initialvalue=link, show=show)

    return simple_webbrowser.LinkString(link.rstrip(), encoding)


def clamp(val: float | int, _min: float | int, _max: float | int) -> object:
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


def open_in_file_explorer(path: str):
    if sys.platform == "win32":
        os.startfile(path)

    elif sys.platform == "darwin":
        subprocess.Popen(["open", path])

    else:
        subprocess.Popen(["xdg-open", path])


desktop_win = Tk()
LOG.action("The window has been created")
text_widget = WriterClassicEditor(desktop_win, font=("Calibri", 13), borderwidth=5, undo=True)
LOG.action("The editor has been created sucessfully")


class WrongClipboardAction(Exception): ...
class InvalidSnippet(Exception): ...
class InvalidEngine(Exception): ...
class ScriptError(Exception): ...
class VersionError(Exception): ...
class PluginNotFoundError(Exception): ...
class CircularListenning(Exception): ...


class CallHistory:
    def __init__(self, function_limit: int = 60):
        self._history: list[int] = []
        self._LIMIT = function_limit

    def register_call(self, function_or_func_id: Callable | int):
        if isinstance(function_or_func_id, int):
            what_to_add = function_or_func_id

        else:
            what_to_add = id(function_or_func_id)

        if what_to_add in self._history:
            return

        if len(self._history) == self._LIMIT:
            self._history.pop(0)

        self._history.append(what_to_add)

    def has_been_registered(self, what_to_check: Callable | int):
        if isinstance(what_to_check, int):
            value = what_to_check

        else:
            value = id(what_to_check)

        if value in self._history:
            return True

        return False

    def clear_history(self):
        self._history: list[int] = []

    @property
    def entry_limit(self):
        return self._LIMIT

    @property
    def call_history(self):
        return self._history.copy()


writerclassic_call_history = CallHistory(32)


class Listener:
    def __init__(self, _id: bytes, target: Callable, output: Callable, condition: str = "True") -> None:
        if self.target == self.output:
            raise CircularListenning('cannot target the output function')

        self._id: str = str(base64.b64encode(gzip.compress(_id)), 'utf-8')
        self._target: Callable = target
        self._output: Callable = output
        self._condition: str = condition # [i] is evaluated later on

    def run_output(self) -> Any | str:
        if eval(self._condition, globals().copy()) is True:
            return self._output()

        return f"False condition; aborted listener with ID: {self._id}"

    @property
    def target(self):
        return self._target

    @property
    def output(self):
        return self._output

    @property
    def listener_id(self) -> str:
        return self._id


class FunctionListeners:
    def __init__(self):
        self._stop_group = 'StoppedInactive'
        self._listeners = {
            self._stop_group: set()
        }

    def _create_subgroup(self, subgroup_function: Callable, listener: Listener, *other_listeners: Listener) -> int:
        if subgroup_function in self._listeners.keys():
            return 9 # [!?] Subgroup already exists

        if self.edit_listener(listener.listener_id, 4) == 2:
            self._listeners[subgroup_function] = {listener}

        else:
            return 10 # [!?] ID already exists

        for other_listener in other_listeners:
            if self.edit_listener(other_listener.listener_id, 4) == 2:
                self._listeners[subgroup_function].add(other_listener)

            else:
                return 10 # [i] see above

        return 0 # [*] Success!

    def add_listeners(self, listeners: set[Listener]) -> int:
        for listener in listeners:
            if listener.target in self._listeners:
                if self.edit_listener(listener.listener_id, 4) == 2:
                    self._listeners[listener.target] = listener

                else:
                    return 10 # [!?] ID already exists

            else:
                self._create_subgroup(listener.target, listener)

        return 0 # [*] Success!

    def edit_listener(self, listener_id: str, operation_type: int) -> int:
        correct_group = None
        correct_listener = None

        for listener_group in self._listeners.values():
            for listener in listener_group:
                if listener.listener_id == listener_id:
                    correct_group = listener_group
                    correct_listener = listener
                    break

        if not correct_listener:
            return 2 # [!?] Invalid ID

        match operation_type:
            case 1:
                if correct_group == self._stop_group:
                    return 4 # [!?] Operation 1 failed since the listener was stopped already

                self._listeners[self._stop_group].add(correct_listener)
                self._listeners[correct_group].remove(correct_listener)

            case 2:
                if correct_group != self._stop_group:
                    return 3 # [!?] Operation 2 failed since the listener wasn't stopped

                self._listeners[self._stop_group].remove(correct_listener)
                self.add_listeners({correct_listener})

            case 3:
                self._listeners[correct_group].remove(correct_listener)
                return correct_listener

            case _:
                return 5 # [!?] Invalid operation type (must be 1, 2 or 3)

        return 0 # [*] Success!

    def run_group(self, group: Callable, auto_purge: bool = True) -> int:
        exception_occured = False

        if group == self._stop_group:
            return 6 # [!?] You cannot run the inactive group as a whole

        if group not in self._listeners.keys():
            return 7 # [!?] The group does not exist

        for listener in self._listeners[group]:
            try:
                listener.run_output()

            except Exception as e:
                print(f"Listener {listener.listener_id} failed - {e}")
                exception_occured = True
                self.edit_listener(listener.listener_id, 3)
                continue

        if exception_occured:
            if auto_purge:
                return 8 # [!?] Successful with certain listeners being purged

            return 1 # [!?] Successful with certain listeners giving errors but not being purged

        return 0 # [*] Succesful with no errors or purges

    def remove_group(self, group: Callable):
        if group == self._stop_group:
            return 12 # [!?] the disabled group cannot be removed

        return self._listeners.pop(group, 11) # [!?] 11 if the group does not exist

    def remove_all_groups(self):
        for group in self._listeners:
            if group == self._stop_group:
                continue

            self.remove_group(group)

        return 0 # [*] Sucess!

    @property
    def listeners(self) -> dict[Callable | str, set[Listener]]:
        return self._listeners.copy()


before_listeners = FunctionListeners()
after_listeners = FunctionListeners()


def is_being_listened(target: Callable, *groups: FunctionListeners):
    if len(groups) == 0:
        groups = (before_listeners, after_listeners)

    for group in groups:
        for possible_target in group.listeners:
            if possible_target == target:
                return True

    return False


def has_been_called(function_or_function_id: Callable | int, call_history: CallHistory = writerclassic_call_history) -> bool:
    return call_history.has_been_registered(function_or_function_id)


def clip_actions(__id: Literal['copy', 'paste'], __s: str = '') -> str:
    """
    clip_actions sends an instruction to the clipboard

    It could be either a copy or a paste instruction.

    Args:
        __id ('copy' or 'paste'): the action to run
        __s (str): the text to copy (when using the 'copy' action). Defaults to ''.

    Returns:
        str: the value of __s when copying; the last item to be copied when pasting.

    Raises:
        WrongClipboardAction: if an action different from 'copy' or 'paste' is given.
    """

    match __id:
        case 'copy':
            LOG.action(f"Copied '{__s}' to the clipboard")
            pyclip.copy(__s)
            return __s

        case 'paste':
            LOG.action("Pasted the contents")
            return pyclip.paste()

        case _:
            LOG.error('Wrong clipboard action', 'ONLY COPY & PASTE ALLOWED')
            raise WrongClipboardAction('Can only copy or paste.')


settings: dict[str, dict[str, str | int | bool] | bool | str | list[str] | int] = get_settings(f"{config}/settings.json")

LOG.action("Got the settings")

if not settings["debugging"]:
    ic.disable()
    LOG.action("Debugging is disabled")

ic(settings)

if ic.enabled:
    for debug_b in debug_a:
        ic(debug_a)

ic(script_dir)
ic(script_path)
ic(f"{data_dir}/logo.png")

ic(now())

ic(settings['language'])

with open(os.path.join(locale, f"{settings['language'][:2]}.wclassic"), 'r', encoding='utf-8') as usedLangFile:
    usedLang = usedLangFile.read()
    lang = usedLang.split('\n')
    LOG.write(f"{str(now())} - Language has been configured correctly: OK\n")

# [*] Windowing
LOG.write(f"{str(now())} - WriterClassic launched: OK\n")

if sys.platform == "win32":
    desktop_win.iconbitmap(f"{data_dir}/app_icon.ico")
    LOG.write(f"{str(now())} - Icon has been changed to WriterClassic's icon [WINDOWS ONLY]: OK\n")

LATEST = None
ic(LATEST)

# [!] Very Important: Keeping track of versions and commits
APP_VERSION = "v12.0.0"
ADVANCED_VERSION ="v11.0.0.372"

# [i] the fourth number up here, is the commit where this changes have been made

ABOUT_WRITER = f"""App name: WriterClassic
Developer: MF366 (at GitHub: MF366-Coding)
Version number: {APP_VERSION[1:]}
Powered by: Python 3.11.8 (x64)
Tested on: Windows, Linux

https://mf366-coding.github.io/writerclassic.html
https://github.com/MF366-Coding/WriterClassic

Thank you for using Writer Classic! <3
"""


def advanced_clipping(__action: Literal['copy', 'paste', 'cut'], text_widget: WriterClassicEditor = text_widget) -> str:
    """
    advanced_clipping sends something to the clipboard based on the GUI

    Args:
        __action ('copy', 'paste', 'cut'): the clipboard action to perform
        text_widget (WriterClassicEditor, optional): the WriterClassicEditor widget that gets affected by the 'paste' and 'cut' operations. Defaults to text_widget.

    Returns:
        str: either the value of a copy/paste operation or an empty string
    """

    before_listeners.run_group(advanced_clipping)
    writerclassic_call_history.register_call(id(advanced_clipping))

    selection: str = ''


    try:
        # [*] Get the current selection
        selection = text_widget.get(SEL_FIRST, SEL_LAST)

    except TclError:
        selection = INSERT

        if __action in ('copy', 'cut'):
            return ''

        __action = 'paste'

    if __action in ('copy', 'cut'):
        clip_actions('copy', selection)

        if __action == 'cut':
            text_widget.replace(SEL_FIRST, SEL_LAST, '')

        return selection

    __s: str = clip_actions('paste')

    if selection == INSERT:
        text_widget.insert(INSERT, __s)

    else:
        text_widget.replace(SEL_FIRST, SEL_LAST, __s)

    after_listeners.run_group(advanced_clipping)

    return __s

copy, paste, cut = lambda: advanced_clipping('copy'), lambda: advanced_clipping('paste'), lambda: advanced_clipping('cut')

# [i] Config files
ic(APP_VERSION)
ic(ADVANCED_VERSION)

ic(settings['theme'])

LOG.write(f"{str(now())} - Got the current theme: OK\n")

LOG.write(f"{str(now())} - Got the current font family/type: OK\n")
LOG.write(f"{str(now())} - Got the current font size: OK\n")


temp_files = os.listdir(temp_dir)

for temp_file in temp_files:
    file_to_delete = os.path.join(temp_dir, temp_file)
    if os.path.isfile(file_to_delete):
        os.remove(file_to_delete)


class Stack:
    def __init__(self):
        """
        NOTE: Not a regular Stack data type!!!

        This is a Stack that doesn't allow repeated values.

        When a repeated value appears it instead of repeating gets moved to the last index.

        The stack is initialized with an empty list.
        """

        self.items = []

    def fromlist(self, seq: list):
        """
        Load all elements from a list (`seq`), except for items that can't be added such as booleans.
        """

        if isinstance(seq, list):
            old_items = self.content
            self.items = []

            for i in seq:
                if not i:
                    continue

                if not isinstance(i, str):
                    continue

                if i not in self.items:
                    self.push(i)

                else:
                    self.items.remove(i)
                    self.push(i)

            return old_items

        raise TypeError('cannot use anything other than a list')
        # [i] VSCode marks this code as unreachable but it can actually be reached since type annotations are not strict in Python

    loadlist = fromlist

    def copy(self):
        """
        Return a shallow copy of the whole stack
        """

        s = Stack()
        s.fromlist(self.content)

        return s

    def __len__(self) -> int:
        """
        Lenght of the list
        """

        return len(self.items)

    def push(self, data) -> Any:
        """
        push appends `data` to the stack

        As explained above, if the item already exists, it gets moved to the last position.

        Alias:
            append

        Args:
            data (Any): the value to append

        Returns:
            Any: `data` or an empty string if the data can't be added
        """

        if not data:
            return ''

        if not isinstance(data, str):
            return ''

        if data not in self.items:
            self.items.append(data)
            return data

        self.items.remove(data)
        self.items.append(data)
        return data

    append = push

    def pop(self) -> Any:
        """
        pop removes the last item

        Alias:
            remove

        Returns:
            Any: the last item
        """

        return self.items.pop()

    remove = pop

    def peek(self):
        """
        peek returns the last item

        Alias:
            top

        Returns:
            Any: last item in the stack
        """

        return self.items[-1]

    top = peek

    @property
    def is_empty(self) -> bool:
        """
        Is the lenght 0?
        """

        return len(self) == 0

    @property
    def content(self) -> list:
        """
        Shallow copy of the items only
        """

        return self.items.copy()


last_file: str | None = None
recent_stack = Stack()

for i in settings['recent']:
    if not i:
        settings['recent'].remove(i)
        continue

    if not isinstance(i, str):
        settings['recent'].remove(i)
        continue

    if os.path.exists(i):
        continue

    settings['recent'].remove(i)

recent_files: list[str] = settings['recent'].copy()

if len(recent_files) > 0:
    recent_stack.fromlist(recent_files)

    last_file = recent_stack.top()


def fast_dump(*_):
    """
    fast_dump dumps the settings of WriterClassic

    Why use this instead of dump_settings from the settings_loader?
        - This only dumps the 10 most recent files from recent_stack
        - No arguments needed (hence the use of *_)
    """

    before_listeners.run_group(fast_dump)
    writerclassic_call_history.register_call(id(fast_dump))

    if len(recent_stack) > 10:
        settings['recent'] = recent_stack.content[-10:]

    else:
        settings['recent'] = recent_stack.content

    after_listeners.run_group(advanced_clipping)

    dump_settings(os.path.join(config, 'settings.json'), settings)


fast_dump()

# [i] Windowing... again
if current_file is False:
    desktop_win.title(lang[1])

LOG.write(f"{str(now())} - Window's title was set to WriterClassic: OK\n")

config_font = Font(family="Segoe UI", size=12, slant='roman', weight='normal', underline=False, overstrike=False)

try:
    config_font = Font(family=settings["font"]["family"], size=settings['font']["size"], slant=settings['font']['slant'], weight=settings['font']['weight'], underline=settings['font']['underline'], overstrike=settings['font']['overstrike'])
    LOG.write(f"{str(now())} - Font size is {str(settings['font']['family'])}: OK\n")
    LOG.write(f"{str(now())} - Font family/type is {str(settings['font']['size'])}: OK\n")

except TclError:
    showerror(lang[149], f"{lang[144]}\n{lang[145]}\n{lang[146]}")
    LOG.write(f"{str(now())} - Font size is set to 14 because of a font error: OK\n")

    config_font = Font(family="Segoe UI", size=12, slant='roman', weight='normal', underline=False, overstrike=False)
    LOG.write(f"{str(now())} - Font type is set to Segoe UI because of a font error: OK\n")

    settings["font"] = {
        "family": "Segoe UI",
        "size": 12,
        "weight": "normal",
        "slant": "roman",
        "underline": 0,
        "overstrike": 0
    }

    fast_dump()


LOG.write(f"{str(now())} - The editing interface has been created: OK\n")

# [!?] https://github.com/rdbende/Sun-Valley-ttk-theme (Sun Valley theme)
desktop_win.tk.call("source", os.path.join(data_dir, "sv.tcl"))
style = Style(desktop_win)
style.theme_use(f"sun-valley-{settings.get('theme')['sv']}")

geom_value = settings["geometry"]
LOG.write(f"{str(now())} - Got the window's dimensions settings: OK\n")
geom_values = geom_value.split('x')

try:
    desktop_win.geometry(geom_value)
    LOG.write(f"{str(now())} - Applied the window's dimensions: OK\n")

except TclError:
    desktop_win.geometry("700x500")
    geom_values = [700, 500]
    LOG.write(f"{str(now())} - Applied the window's dimensions: ERROR\n")
    LOG.write(f"{str(now())} - Reverted to 700x500: OK\n")
    showerror(lang[166], f"{lang[167]}\n{lang[168]}")

try:
    text_widget.configure(background=settings['theme']["color"], foreground=settings['theme']["fg"], width=int(geom_values[0]), height=int(geom_values[1]), insertbackground=settings['theme']["ct"], font=config_font)
    LOG.write(f"{str(now())} - Applied configurations to the editing interface: OK\n")

except TclError:
    LOG.write(f"{str(now())} - Applied configurations to the editing interface: ERROR\n")
    showerror(lang[150], f"{lang[151]}\n{lang[152]}")
    text_widget.configure(background="black", foreground="white", width=int(geom_values[0]), height=int(geom_values[1]), insertbackground="white", font=config_font)
    LOG.write(f"{str(now())} - Reconfigured the editing interface: OK\n")

LOG.write(f"{str(now())} - 'Packed' the editing interface: OK\n")

# [i] Defining the menu bar
menu_bar = Menu(desktop_win)
LOG.write(f"{str(now())} - Created the menu bar: OK\n")

try:
    if sys.platform == "linux":
        menu_bar.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        LOG.write(f"{str(now())} - Applied the theme to the menu bar: OK\n")

except TclError:
    if sys.platform == "linux":
        LOG.write(f"{str(now())} - Applied the theme to the menu bar: ERROR\n")
        showerror(lang[150], f"{lang[151]}\n{lang[152]}")
        menu_bar.configure(background="white", foreground="black")
        LOG.write(f"{str(now())} - Applied the light theme to the menu bar as last resource: OK\n")

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
menu_4 = Menu(menu_1)
menu_5 = Menu(menu_4)
menu_6 = Menu(menu_4)
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

LOG.write(f"{str(now())} - Created all the menus: OK\n")

WCLASSIC_VARS: dict[str, str] = {
    "$APPDATA": os.environ.get('APPDATA') if sys.platform == 'win32' else "$APPDATA",
    "$LOCALAPPDATA": os.environ.get('LOCALAPPDATA') if sys.platform == 'win32' else "$LOCALAPPDATA",
    "$USER": os.path.expanduser('~'),
    "$ROOT": "$ROOT" if sys.platform == 'win32' else "/",
    "$BITNESS": platform.architecture()[0],
    "$BITS": platform.architecture()[0],
    "$PYTHON": sys.executable,
    "$WRITERCLASSIC": script_path,
    "$LOGGER": os.path.join(user_data, "log.wclassic"),
    "$REPO": "https://github.com/MF366-Coding/WriterClassic",
    "$WEBSITE": "https://mf366-coding.github.io/writerclassic.html",
    "$OSVERSION": platform.version(),
    "$PLATFORM": sys.platform,
    "$OS": os.name
}


def writeStartup(text: bool) -> None:
    """
    writeStartup changes the startup value on the settings and then saves it

    Args:
        text (bool): the new startup value
    """

    before_listeners.run_group(writeStartup)
    writerclassic_call_history.register_call(id(writeStartup))

    settings["startup"] = text
    fast_dump()
    LOG.write(f"{str(now())} - Check for updates on Startup (True - 1/False - 0) has been changed to {text}: OK\n")

    after_listeners.run_group(advanced_clipping)


class WScript:
    def __init__(self):
        """
        __init__ initializes an instance of WScript
        """

        self.script: str | None = None
        self.__executed: bool = False

    def loadpath(self, location: str, encoding: str = 'utf-8'):
        """
        loadpath loads a WScript from a filepath

        This is the legacy way as a matter of speech

        NOTE: It's recommended you use `frompath` instead

        Must meet the following criteria:
            - the path value must not be a representation of False (such as 0, an empty string, etc)
            - the path must exist
            - the path must be a file
            - the path must be a *.wscript file

        If the name is exactly EightBall.wscript **with this particular casing**, a special behavior will be applied.

        Args:
            location (str): filepath
            encoding (str, optional): file encoding. Defaults to 'utf-8'.

        Raises:
            ValueError: if at least one of the criteria above fails
        """

        location = location.strip()

        if not location:
            raise ValueError('empty string as path value')

        if not os.path.exists(location) or not os.path.isfile(location):
            raise ValueError('invalid path')

        if not location.lower().endswith('.wscript'):
            raise ValueError('must be WSCRIPT file')

        if os.path.basename(location) == "EightBall.wscript":
            self.script = """_prompts = ['Yes!', "Don't think so...", "Doubtly.", "Absolutely.", "Nope.", "Not happening.", "WriterClassic is a good text editor!", "MF366 is cool.", "Of course!"]

showinfo(f"{lang[1]} - Eight Ball", random.choice(_prompts))
"""
            return

        with open(location, 'r', encoding=encoding) as f:
            self.script = f.read()
            f.close()

    def loadstr(self, script: str):
        """
        loadstr loads a WScript from a string

        There's no special behaviors but there's one criteria that must meet:
            - script mustn't be a representation of False (0, empty string, etc)

        Args:
            script (str): the script

        Raises:
            ValueError: the criteria failed
        """

        if not script:
            raise ValueError('representation of False as a script')

        self.script = script

    def run(self, scope: Literal['read', 'write'] = 'read'):
        """
        run runs the current WScript

        Args:
            scope (wither 'read' or 'write', optional): defines if the script can write to globals or not. Either ways, it will be able to read them. Defaults to 'read' (readonly).
        """

        _globs: dict[str, Any] | None = None

        if scope == 'write':
            _globs = globals()

        else:
            _globs = globals().copy()

        exec(self.script, _globs)
        self.__executed = True

    @property
    def has_been_executed(self) -> bool:
        """
        Has this particular instance of WScript been executed at least once?
        """

        return self.__executed

    def __len__(self) -> int:
        return len(self.script) if self.script is not None else 0

    def __repr__(self) -> str:
        return str(self.script)


class GlobalRestorePoint:
    def __init__(self) -> None:
        """
        Restore point for WriterClassic's global variables
        """

        self.__globals: dict[str, Any] = globals().copy()

    def __repr__(self) -> str:
        s: str = "== GlobalRestorePoint ==\n"

        for key, value in self.status.items():
            s += f"{key}: {value}\n"

        return s

    def __eq__(self, __value: dict) -> bool:
        return self.__globals == __value

    def __ne__(self, __value: dict) -> bool:
        return self.__globals != __value

    @property
    def status(self) -> dict[str, Any]:
        """
        Shallow copy of the globals() inside this Restore Point
        """

        return self.__globals.copy()

    def restore(self):
        """
        restore restores the globals() that were being used before the creation of the instance of a restore point that saved them
        """

        globals().update(self.__globals)


# [i] Check for Updates
class UpdateCheck:
    def __init__(self, app_version: str = APP_VERSION, latest_v: Any = LATEST):
        """
        Args:
            app_version (str, optional): current version. Defaults to APP_VERSION.
            latest_v (Any, optional): latest version of WriterClassic. Defaults to LATEST.
        """

        self.app_version = app_version
        self.latest = latest_v

    def manual_check(self):
        """
        manual_check checks for updates when the user clicks 'Check for Updates'
        """

        if self.app_version != self.latest:
            askForUpdate = mb.askyesno(lang[72], lang[73])

            if askForUpdate:
                LOG.write(f"{str(now())} - Went to the latest release at GitHub: OK\n")
                simple_webbrowser.website('https://github.com/MF366-Coding/WriterClassic/releases/latest')

        elif self.app_version == self.latest:
            showinfo(title=lang[93], message=lang[92])
            LOG.write(f"{str(now())} - Versions match | WriterClassic is up to date: OK\n")

        else:
            showerror(lang[148], f"{lang[135]}\n{lang[136]}")
            LOG.write(f"{str(now())} - Couldn't check for updates (Bad Internet, Connection Timeout, Restricted Internet): WARNING\n")


update_check = UpdateCheck()


def set_window_size(root: Tk = desktop_win, **_) -> None:
    """
    set_window_size creates a GUI in order to change the dimensions of the window

    The GUI is created with `root` as master.

    No other arguments needed.
    """

    before_listeners.run_group(set_window_size)
    writerclassic_call_history.register_call(id(set_window_size))

    def _change_window_size(*params) -> bool:
        try:
            e1 = int(params[0].get())
            e2 = int(params[1].get())

        except TypeError as e:
            showerror(lang[147], f"{lang[133]}\n{lang[134]}\n{e}")
            params[2].destroy()
            return False

        else:
            params[3].geometry(f"{e1}x{e2}")
            settings["geometry"] = f"{e1}x{e2}"

        finally:
            after_listeners.run_group(advanced_clipping)
            fast_dump()

        return True

    geometry_set = Toplevel()
    geometry_set.title(string=f"{lang[1]} - {lang[12]}")
    geometry_set.resizable(width=False, height=False)

    if sys.platform == 'win32':
        geometry_set.iconbitmap(bitmap=os.path.join(data_dir, 'app_icon.ico'))

    frame0 = Frame(master=geometry_set)
    frame1 = Frame(frame0)
    frame2 = Frame(frame0)

    width_label = Label(frame1, text=lang[57], font=Font(family=config_font.actual('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    height_label = Label(frame2, text=lang[58], font=Font(family=config_font.actual('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))

    width_set = Entry(frame1, font=Font(family=config_font.actual('family'), size=11, weight='normal', slant='roman', underline=False, overstrike=False))
    height_set = Entry(frame2, font=Font(family=config_font.actual('family'), size=11, weight='normal', slant='roman', underline=False, overstrike=False))

    confirm_butt = Button(geometry_set, text='Ok', command=lambda:
        _change_window_size(width_set, height_set, geometry_set, root))

    width_set.insert(0, settings["geometry"].lower().split('x')[0])
    height_set.insert(0, settings["geometry"].lower().split('x')[1])

    width_label.grid(column=0, row=0)
    width_set.grid(column=0, row=1)

    height_label.grid(column=0, row=0)
    height_set.grid(column=0, row=1)

    frame1.grid(column=0, row=0)
    frame2.grid(column=1, row=0)

    frame0.pack()

    confirm_butt.pack()

    geometry_set.mainloop()


def evaluate_expression(start: str | float | None = None, end: str | float | None = None, **kwargs) -> tuple:
    """
    evaluate_expression evaluates an expression inside a text widget

    Priorities by order:
        1. bool(ean)
        2. complex
        3. int(eger)
        4. float
        5. Any(thing else) converted to str(ing)

    Args:
        start (str | float | None, optional): index1. Defaults to SEL_FIRST.
        end (str | float | None, optional): index2. Defaults to SEL_LAST.
        widget (WriterClassicEditor, optional): the widget where changes take place. Defaults to text_widget.

    Returns:
        tuple: expression, value returnes by eval(), evaluated expression. (If all are None, then SEL_FIRST and SEL_LAST are not marked.)
    """

    before_listeners.run_group(evaluate_expression)
    writerclassic_call_history.register_call(id(evaluate_expression))

    widget: WriterClassicEditor = kwargs.get('widget', text_widget)

    if start is None:
        try:
            start = SEL_FIRST

        except TclError:
            return None, None, None

    if end is None:
        try:
            end = SEL_LAST

        except TclError:
            return None, None, None

    mathematics: dict[str, Any] = {**math.__dict__.copy(), **cmath.__dict__.copy()}

    exp: str = widget.get(start, end)
    eval_exp: bool | complex | int | float
    EVALUATED_EXP = eval(exp, mathematics)

    # [*] 1st Priority
    if isinstance(EVALUATED_EXP, bool):
        eval_exp = EVALUATED_EXP

    # [*] 2nd Priority
    elif isinstance(EVALUATED_EXP, complex):
        eval_exp = EVALUATED_EXP

    # [*] 3rd Priority
    elif isinstance(EVALUATED_EXP, int):
        eval_exp = EVALUATED_EXP

    # [*] 4th Priority
    elif isinstance(EVALUATED_EXP, float):
        if int(EVALUATED_EXP) == EVALUATED_EXP:
            eval_exp = int(EVALUATED_EXP)

        else:
            eval_exp = EVALUATED_EXP

    # [!?] 5th Priority: kinda dangerous???
    else:
        eval_exp = str(EVALUATED_EXP)

    ic(EVALUATED_EXP)
    ic(type(EVALUATED_EXP))

    widget.replace(start, end, str(eval_exp))

    after_listeners.run_group(advanced_clipping)

    return exp, EVALUATED_EXP, eval_exp


# [i] Theme Picker
def set_theme(**kw):
    """
    set_theme sets a new theme

    NOTE: Pretty complex function, requires a lot of attention when using.

    Possible args:
        bg: the background color
        fg: the foreground color (text color)
        ct: the color of the cursor, usually the same as the foreground color
        mbg: the background of the menus (LINUX ONLY; menu background)
        mfg: the color of the text in the menus (LINUX ONLY; menu foreground)
        sv: the sun valley theme to use
        widget: the widget where changes take place
        settings_: mapping that contains the settings
        dump: function that allows to dump/save the changed settings
        menus: list containing existing menus
        logger: logger class
        special_menu: special menu that is only trigerred by `special_cond`
        special_cond: boolean condition that decides whether to trigger `special_menu` or not
    """

    before_listeners.run_group(set_theme)
    writerclassic_call_history.register_call(id(set_theme))

    logger: Logger = kw.get('logger', LOG)
    widget: WriterClassicEditor = kw.get('widget', text_widget)
    menus: list[Menu] = kw.get('menus', [menu_1, menu_4, menu_5, menu_6, menu_8, menu_9, menu_10, menu_11, menu_12, menu_13, menu_15, menu_16, menu_17])
    special_cond: bool = kw.get('special_cond', ADVANCED)

    if special_cond:
        special_menu: Menu = kw.get('special_menu', menu_14)

    _configs: dict = kw.get('settings_', settings)
    dump: Callable = kw.get('dump', fast_dump)
    bg: str = kw.get('bg', _configs['theme']['color'])
    fg: str = kw.get('fg', settings['theme']['fg'])
    ct: str = kw.get('ct', settings['theme']['ct'])
    mbg: str = kw.get('mbg', settings['theme']['menu'])
    mfg: str = kw.get('mfg', settings['theme']['mfg'])
    sv: str = kw.get('sv', settings['theme']['sv'])

    colors = {'color': bg, 'fg': fg, 'ct': ct, 'menu': mbg, 'mfg': mfg, 'sv': sv}

    for i, j in colors.items():
        _configs['theme'][i] = j

    dump()

    widget.configure(background=bg, foreground=fg, insertbackground=ct)
    logger.write(f"{str(now())} - Editing interface has been reconfigured: OK\n")

    if special_cond and sys.platform == 'linux':
        menus.append(special_menu)

    if sys.platform == 'linux':
        # [i] Themed menus only on Linux Python3
        try:
            for menu in menus:
                menu.configure(background=mbg, foreground=mfg)

            logger.write(f"{str(now())} - The Menus have been themed [LINUX ONLY]: OK\n")

        except (TypeError, ValueError, TclError):
            showerror(lang[150], f"{lang[151]}\n{lang[152]}")

            for menu in menus:
                menu.configure(background=mbg, foreground=mfg)

            logger.write(f"{str(now())} - The Menus have been themed [LINUX ONLY]: OK\n")

    style.theme_use(f"sun-valley-{settings.get('theme')['sv']}")
    after_listeners.run_group(set_theme)

# [!] WARNING: QUICKWAY() WILL BE DEPREACTED IN V11.0.1
def quickway():
    """
    quickway instantly quits the app without any confirmation
    """

    before_listeners.run_group(quickway)
    writerclassic_call_history.clear_history()

    LOG.write(f"{str(now())} - End of session: QUIT\n")
    LOG.close()
    desktop_win.destroy()
    sys.exit()


# [i] Setup (Lang files)
def set_language(language_set, root_win):
    """
    set_language sets a new language as the app language

    Args:
        language_set (str): the string that represents the locale file. Examples: `pt`, `sk` and `en`
        root_win (Tk | Toplevel): the window where this change takes place
    """

    before_listeners.run_group(set_language)
    writerclassic_call_history.register_call(id(set_language))

    settings["language"] = language_set
    LOG.write(f"{str(now())} - A new language has been set ({str(language_set)}): OK\n")
    fast_dump()

    popup_define = mb.askyesno(parent=root_win, title=lang[30], message=lang[31])
    LOG.write(f"{str(now())} - Asked for app restart: AWAITING RESPONSE\n")

    if popup_define:
        root_win.destroy()
        LOG.write(f"{str(now())} - End of session: QUIT\n")

    else:
        LOG.write(f"{str(now())} - Cancel/No as response: OK\n")

    after_listeners.run_group(set_language)


# [i] Notepad
def draft_notepad() -> None:
    """
    draf_notepad loads the GUI for the Notepad plugin/tool

    In the early days, this function was supposed to launch a new WriterClassic window.
    """

    before_listeners.run_group(draft_notepad)
    writerclassic_call_history.register_call(id(draft_notepad))

    new_window = Toplevel(desktop_win)
    LOG.write(f"{str(now())} - A new window has been called: AWAITING CONFIGURATION\n")

    # [i] Windowing
    new_window.title(lang[22])
    new_window.geometry("600x400")

    if sys.platform == "win32":
        new_window.iconbitmap(f"{data_dir}/app_icon.ico")

    other_widget = WriterClassicEditor(new_window, borderwidth=5)

    other_widget.configure(background=settings['theme']["color"], foreground=settings['theme']["fg"], width=geom_values[0], height=geom_values[1], insertbackground=settings['theme']["ct"], font=config_font)
    other_widget.pack()

    LOG.write(f"{str(now())} - Notes Plugin's window has been fully configured: OK\n")

    after_listeners.run_group(draft_notepad)

    new_window.mainloop()


def document_status(widget: WriterClassicEditor = text_widget):
    """
    document_status presents the stats of the current editor to the user

    Stats:
    - No of lines
    """

    before_listeners.run_group(document_status)
    writerclassic_call_history.register_call(id(document_status))

    showinfo(lang[164], f"{lang[165]}: {widget.num_lines - 1}")

    after_listeners.run_group(document_status)


# [i] Repo
def repository():
    """
    repo sends the user to the official repository
    """

    before_listeners.run_group(repository)
    writerclassic_call_history.register_call(id(repository))

    simple_webbrowser.website("https://github.com/MF366-Coding/WriterClassic/")
    LOG.write(f"{str(now())} - Opened the repository: AWAITING FOR FUNCTION OR ERROR\n")

    after_listeners.run_group(repository)


class BackupSystem:
    def __init__(self, autoscr_path: str = scripts_dir, config_path: str = config, main_dir: str = script_dir) -> None:
        """
        __init__ is the initializer for the BackupSystem

        Args:
            autoscr_path (str, optional): the path where auto scripts are stored. Defaults to scripts_dir.
            config_path (str, optional): the path where the settings are saved. Defaults to config.
            main_dir (str, optional): the dir where WriterClassic is stored. Defaults to script_dir.
        """

        self._folder_paths = (autoscr_path, config_path)
        self._main_dir = main_dir


    def _zip_files(self, root_path: str):
        """
        Internal function.
        """

        with zipper.ZipFile(os.path.join(root_path, f"Backup_WriterClassic_{datetime.datetime.now().day}-{datetime.datetime.now().month}-{datetime.datetime.now().year}.zip"), 'w') as zip_file:
            for folder_path in self._folder_paths:
                arcname: str = os.path.basename(folder_path)

                zip_file.write(filename=folder_path, arcname=arcname)

                for filename in os.listdir(folder_path):
                    file_path: str = os.path.join(folder_path, filename)

                    if os.path.isfile(path=file_path):
                        zip_file.write(filename=file_path, arcname=os.path.join(arcname, filename))

            zip_file.close()

    def _extract_files(self, file_path: str) -> None:
        """
        _extract_files extracts the backup to the location where WriterClassic is stored

        Args:
            file_path (str): the path where the zip backup is
        """

        with zipper.ZipFile(file_path, 'r') as zip_file:
            for path_to_remove in self._folder_paths:
                try:
                    if sys.platform == "win32":
                        os.system(command=f'rmdir /s /q {path_to_remove}')

                    else:
                        os.system(f'rm -rf {path_to_remove}')

                except FileNotFoundError as e:
                    LOG.error(text="File/directory missing while trying to extract the backup", error_details=str(object=e))
                    raise Exception from e # [i] it will be caught by the statement below

                except Exception:
                    showerror(title=lang[1], message=lang[322])
                    continue

            zip_file.extractall(path=self._main_dir)


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
                showerror(lang[1], lang[319])
                return

            self._extract_files(file_path)

        else:
            showerror(lang[1], lang[319])


def recent_files(**kw):
    """
    recent_files opens a selection window for recently open files

    After this description, follows a list of the possible arguments in 'name = default value' syntax.

    --

    GENERAL WRITERCLASSIC ARGUMENTS

    root (Tk | Toplevel) = desktop_win

    --

    WINDOW ARGUMENTS

    iconbitmap (str | PathLike) = WriterClassic icon

    --

    SPECIFIC ARGUMENTS

    expressions (list[str]) = WriterClassic language list
    recents (Stack) = stack object containing the recent files
    """

    before_listeners.run_group(recent_files)
    writerclassic_call_history.register_call(id(recent_files))

    def _open(lb: Listbox, root: Tk | Toplevel, aux: list[str], exps: list[str], win: Toplevel):
        """
        Internal function.
        """

        try:
            open_file_manually(aux[lb.index(lb.curselection())], root)

        except TclError:
            showwarning(exps[1], exps[357])

        else:
            win.destroy()


    root: Tk | Toplevel = kw.get('root', desktop_win)
    icopath: str = kw.get('iconbitmap', os.path.join(data_dir, 'app_icon.ico'))
    exps: list[str] = kw.get('expressions', lang.copy())
    recents: Stack = kw.get('recents', recent_stack).copy()

    if recents.is_empty:
        showinfo(exps[1], exps[356])
        return

    w = Toplevel(root)
    w.title(exps[355])
    w.resizable(False, False)

    if sys.platform == 'win32':
        w.iconbitmap(icopath)

    lb = Listbox(w, selectmode=SINGLE, font=Font(family=settings['font']['family'], size=12, weight='normal', slant='roman', underline=False, overstrike=False), bg=settings['theme']['color'], fg=settings['theme']['fg'], borderwidth=3, width=75)
    aux = []

    for _ in range(len(recents)) if len(recents) <= 10 else range(10):
        lb.insert(END, os.path.basename(recents.top()))
        aux.append(recents.top())
        recents.pop()

    b = Button(w, text=exps[7], command=lambda:
        _open(lb, root, aux, exps, w))

    lb.pack()
    b.pack()

    after_listeners.run_group(recent_files)

    w.mainloop()


class Snippets:
    """
    Work with snippets for WriterClassic.

    Useful methods to make this feature extremely moddable.
    """

    def __init__(self, name: str) -> None:
        """
        __init__ is the initializer for the Snippets

        Args:
            name (str): general tag for the snippets, such as 'Extra Snippets', 'C++ Snippts'
        """

        self.name: str = name
        self._snippets: dict[str, (str, str, str)] = {}
        self.__taken_names = []

    def register(self, name: str, value: str, _lang: str, desc: str | None = None):
        """
        register adds a new snippet to the snippet table

        Args:
            name (str): the name of the snippet
            value (str): its value in the form of a string
            _lang (str): the markup/programming language the snippet refers to (e.g: Python, Markdown)
            desc (str | None, optional): a valid description. Defaults to None.

        Raises:
            InvalidSnippet: in case the name is already taken
        """

        if name in self.__taken_names:
            raise InvalidSnippet(f'{name} is already taken')

        if desc is None:
            desc = lang[337]

        self.__taken_names.append(name)

        self._new_snippet(name, (value, _lang, desc))

    def _new_snippet(self, _name: str, _snippet_data: tuple[str, str, str | None]):
        """
        Internal function.
        """

        self._snippets[_name] = _snippet_data

    def _return_snippet(self, _name: str) -> tuple[str, str, str]:
        """
        Internal function.
        """

        return self._snippets[_name]

    def get_index(self, name: str) -> int:
        """
        get_index returns the index of the snippet

        Actually, it's no index. It is instead the order of adding snippet names.

        If you get 3, it isn't an index since snippets are stored as dictionaries.

        It instead means that the snippet you asked for was the third to be added.

        Please note that this also doesn't reflect a Python index, as it starts on 1.

        Args:
            name (str): the name of the snippet

        Raises:
            InvalidSnippet: snippet doesn't exist

        Returns:
            int: the snippet's "index"
        """

        if name not in self._snippets:
            raise InvalidSnippet(f"snippet {name} doesn't exist")

        return self.__taken_names.index(name) + 1

    def get_snippet(self, name: str) -> tuple[str, str, str, str]:
        """
        get_snippet returns the wanted snippet's data

        Args:
            name (str): the name of the snippet to return

        Raises:
            InvalidSnippet: in case the snippet with name `name` doesn't exist

        Returns:
            tuple[str, str, str, str]: name, value, language, description
        """

        if name not in self._snippets:
            raise InvalidSnippet(f"snippet {name} doesn't exist")

        __snippet_data = self._return_snippet(name)

        return (name, __snippet_data[0], __snippet_data[1], __snippet_data[2])

    def remove_snippet(self, name: str):
        """
        remove_snippet is pretty straight-forward:

        If the given snippet name exists, remove the snippet associated with it.

        Args:
            name (str): snippet to remove

        Raises:
            InvalidSnippet: the snippet you wish to remove doesn't exists

        Returns:
            tuple[str, str, str]: the removed snippet's data
        """

        if name not in self._snippets:
            raise InvalidSnippet(f"snippet {name} doesn't exist")

        return self._snippets.pop(name)

    def __str__(self) -> str:
        return self.name

    def get_taken_names(self) -> list[str]:
        """
        get_taken_names returns the list of the names that are taken

        Returns:
            list[str]
        """

        return self.__taken_names[:]

    def __len__(self) -> int:
        return len(self.__taken_names)


def snippet_picker(snippets: Snippets, pos = INSERT, root: Tk | Toplevel = desktop_win, widget: WriterClassicEditor = text_widget):
    """
    snippet_picker launchs a window to pick a snippet from `snippets` to insert at position `pos`

    The snippet is sent to the `widget` and the picker window has `root` as its master.

    Args:
        snippets (Snippets): snippets to pick from
        pos (_type_, optional): position to insert the snippet in. Defaults to INSERT.
        root (Tk | Toplevel, optional): root window for the picker Toplevel. Defaults to desktop_win.
        widget (WriterClassicEditor, optional): text editor where the snippet is inserted onto. Defaults to text_widget.
    """

    before_listeners.run_group(snippet_picker)
    writerclassic_call_history.register_call(id(snippet_picker))

    def update_info_view(*labels):
        n: str = labels[1].get()
        s: tuple = labels[0].get_snippet(n)
        m: int = labels[0].get_index(n)

        labels[2].configure(text=f"{s[0]} ({s[2]} - #{m})")

        labels[3].configure(state=NORMAL)

        labels[3].delete(0.0, END)
        labels[3].insert(0.0, f"{lang[334]}:\n---\n{s[1]}\n---\n{s[3]}")

        labels[3].configure(state=DISABLED)

    def insert_val(*args):
        n: str = args[1].get()
        s: tuple = args[0].get_snippet(n)

        args[3].insert(args[2], s[1])

        args[4].destroy()

    w = Toplevel(root)
    w.title(f"{lang[1]} - {lang[341]}")
    w.resizable(False, False)

    if sys.platform == "win32":
        desktop_win.iconbitmap(f"{data_dir}/app_icon.ico")

    f = config_font.actual()

    h1 = Font(w, family=f['family'], size=18, weight='bold', slant='roman', overstrike=False, underline=False)
    h2 = Font(w, family=f['family'], size=16, weight='bold', slant='roman', overstrike=False, underline=True)
    body1 = Font(w, family=f['family'], size=13, weight='normal', slant='roman', overstrike=False, underline=False)
    body2 = Font(w, family=f['family'], size=11, weight='normal', slant='roman', overstrike=False, underline=False)

    title_label = Label(w, font=h1, text=snippets.name)
    adjust_frame = Frame(w)

    snippet_label = Label(adjust_frame, font=body1, text=f'{lang[338]}: ')

    snippet_name = StringVar(w)

    g = ()

    for i in snippets.get_taken_names():
        g = (*g, i)

    name_label = Label(w, font=h2, text=lang[339])
    desc_label = WriterClassicEditor(w, font=body2)
    desc_label.configure(borderwidth=0, insertbackground='white')

    desc_label.insert(0.0, lang[340])

    desc_label.configure(state=DISABLED)

    z = (snippets, snippet_name, name_label, desc_label)

    name_picker = OptionMenu(adjust_frame, snippet_name, None, *g, direction='below')

    ok_butt = Button(adjust_frame, text=lang[335], command=lambda:
        update_info_view(*z))

    insert_butt = Button(w, text=lang[336], command=lambda:
        insert_val(snippets, snippet_name, pos, widget, w))

    title_label.pack()

    snippet_label.grid(column=0, row=0)
    name_picker.grid(column=1, row=0)
    ok_butt.grid(column=2, row=0)

    adjust_frame.pack()
    name_label.pack()
    desc_label.pack()
    insert_butt.pack()

    after_listeners.run_group(snippet_picker)

    w.mainloop()

default_snippets = Snippets(lang[333])

default_snippets.register('if-elif-else', 'if !!!:\n\t!!!\nelif !!!:\n\t!!!\nelse:\n\t!!!', 'Python 3', "Python's if-elif-else statement, where the '!!!' marks the things you might want to change.")
default_snippets.register('try-except-else-finally', 'try:\n\t!!!\nexcept !!!:\n\t!!!\nelse:\n\t!!!\nfinally:\n\t!!!', 'Python 3', "Python's try-except clause but with additional else and finally for a better error handling.")
default_snippets.register('ifmain', 'if __name__ == "__main__":\n\tmain()', 'Python 3', "Execution clause made easy. Just click 'Insert' and boom!")
default_snippets.register('general-except', 'try:\n\t!!!\nexcept Exception:\n\t!!!', 'Python 3', "Catch a general exception in Python with this clause. 'Exception' inherits from the 'BaseException' class and behaves like a general exception.")
default_snippets.register('class', 'class !!!:\n\tdef __init__(self) -> None:\n\t\tpass\n\n\tdef __str__(self) -> str:\n\t\treturn !!!\n\n\tdef __len__(self) -> int:\n\t\treturn !!!', 'Python 3', "Need a class and need it quick? With this snippet, you can have a class with a constructor, a __str__ method (gets called when converting the class to a str object) and a __len__ method (gets called when using the len function with the class instance as its argument).")
default_snippets.register('function', 'def !!!(!!!):\n\treturn', 'Python 3', "Just a small function, defined with the def keyword in Python.")
default_snippets.register('bold', '**!!!**', 'Markdown', 'Need to be **bold**? You can be **bold** in Markdown!')
# [!?] If you want more snippets, they are extendable by plugins :D


# [i] Font Picker :)
def set_font(root: Tk | Toplevel = desktop_win, editor: WriterClassicEditor = text_widget, dump_func = fast_dump, sample: str = 'Lorem ipsum dolor sit amet, ...', **kw) -> Font | dict[bytes, bytes]:
    """
    set_font launches a font picker that affects `editor` and has `root` as master

    NOTE: the font picker itself was created by **j4321** (tkfontchooser)!!

    Args:
        root (Tk | Toplevel, optional): explained above. Defaults to desktop_win.
        editor (WriterClassicEditor, optional): explained above. Defaults to text_widget.
        dump_func (_type_, optional): function that dumps the settings. Defaults to fast_dump.
        sample (str, optional): text sample used inside the font picker. Defaults to 'Lorem ipsum dolor sit amet, ...'.

    Returns:
        Font | dict[bytes, bytes]: font configurations
    """

    before_listeners.run_group(set_font)
    writerclassic_call_history.register_call(id(set_font))

    __dump_func = kw.get('__dump_func', dump_func)
    __sample = kw.get('__sample', sample)

    font_details = dict(tkfontchooser.askfont(root, __sample, f"{lang[1]} - {lang[332]}", family=settings['font']['family'], size=settings['font']['size'], weight=settings['font']['weight'], slant=settings['font']['slant'], underline=settings['font']['underline'], overstrike=settings['font']['overstrike']))
    config_font.configure(family=font_details['family'], size=font_details['size'], weight=font_details['weight'], slant=font_details['slant'], underline=font_details['underline'], overstrike=font_details['overstrike'])

    settings['font'] = font_details
    __dump_func()

    editor.configure(font=config_font)

    after_listeners.run_group(set_font)

    return config_font or font_details


# [i] New File but with confirmation
def new_file(skip_confirmation: bool = False):
    """
    new_file clears the editor and purges current cached data on the last file to be opened/saved

    It also resets the modified status (check `ModifiedStatus` - function and `save_status` - global variable, bool type)

    However, it first checks if the contents of the editor have been modified (unless confirmation ahs been skipped via the only argument).
    """

    global current_file, cur_data, save_status

    before_listeners.run_group(new_file)
    writerclassic_call_history.register_call(id(new_file))

    if not skip_confirmation:
        ic()

        a = has_been_modified()

        if not a:
            b = mb.askyesnocancel(lang[1], f"{lang[352]}\n{lang[353]}")

            if b is None:
                ic()
                return

            if b:
                ic()
                save_file()

            else:
                ic()

    save_status = True

    desktop_win.title(lang[1])
    text_widget.delete(index1=0.0, index2=END)
    cur_data = text_widget.content

    current_file = False

    LOG.write(f"{str(now())} - A new file has been created: OK\n")

    ic(current_file)

    after_listeners.run_group(new_file)


FILETYPES = [(lang[32], '*.txt'),
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

LOG.write(f"{str(now())} - Filetypes have been configured correctly: OK\n")


# [i] functions to open a file
def stem_only(__s: str) -> str:
    """
    stem_only returns the stem part of a filename

    Args:
        __s (str): filename

    Returns:
        str: the stem part of the filename
    """

    before_listeners.run_group(stem_only)
    writerclassic_call_history.register_call(id(stem_only))

    generated_list: list[str] = __s.split('.')

    modified_list: list[str] = [generated_list[i] for i in range(len(generated_list) - 2)]

    stem_part: str = '.'.join(modified_list)

    after_listeners.run_group(stem_only)

    return stem_part


def open_file_manually(file_path: str, root_win: Tk = desktop_win) -> None:
    global current_file, cur_data, save_status

    before_listeners.run_group(open_file_manually)
    writerclassic_call_history.register_call(id(open_file_manually))

    file_path = os.path.abspath(file_path)

    try:
        with open(file_path, 'rt', encoding='utf-8'):
            file_input = open(file_path, "rt", encoding="utf-8")
            file_data = file_input.read()

            root_win.title(f"{lang[1]} - {os.path.basename(file_path)}")
            text_widget.delete(index1=0.0, index2=END)
            text_widget.insert(chars=file_data, index=END)

            current_file = file_path
            cur_data = text_widget.content
            save_status = True

            LOG.write(f"{str(now())} - A file at the path {str(file_path)} has been opened: OK\n")

    except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
        showerror(title=lang[187], message=f"{lang[188]} {str(file_path)}.")
        run_default = mb.askyesno(title=lang[187], message=lang[189])

        if run_default:
            os.system(str(file_path))

    else:
        recent_stack.append(current_file)

    finally:
        fast_dump()
        ic(current_file)

    after_listeners.run_group(open_file_manually)


def open_file(root_win: Tk = desktop_win, initialfile: str = 'Open a File', **kw):
    """
    open_file opens a file selected from the following interface

    Args:
        root_win (Tk): WriterClassic's main window
    """

    before_listeners.run_group(open_file)
    writerclassic_call_history.register_call(id(open_file))

    filetypes: list[tuple[str, str]] = kw.get('filetypes', FILETYPES.copy())

    file_path: str = dlg.asksaveasfilename(parent=root_win, filetypes=filetypes, defaultextension="*.*", initialfile=initialfile, confirmoverwrite=False, title=lang[7])

    if not file_path:
        return

    open_file_manually(file_path)


# [i] Saving as
def save_as_file(root_win: Tk = desktop_win):
    """
    save_as_file saves the current file as

    Basically, the tipical Save As feature.

    Args:
        root_win (Tk, optional): the window where changes take place. Defaults to desktop_win.
    """

    global current_file, cur_data, save_status

    before_listeners.run_group(save_as_file)
    writerclassic_call_history.register_call(id(save_as_file))

    data = text_widget.content
    save_status = True
    file_path = dlg.asksaveasfilename(parent=root_win, title=lang[9], confirmoverwrite=True, filetypes=FILETYPES, defaultextension="*.*", initialfile="New File To Save")

    # [*] Get the selected file extension
    selected_extension = None
    for ft in FILETYPES:
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
    file.write(str(data.rstrip('\n')) + '\n')
    cur_data = data
    file.close()
    showinfo(lang[1], lang[101])
    root_win.title(f"{lang[1]} - {os.path.basename(file_path)}")

    LOG.write(f"{str(now())} - A file has been saved as {str(file_path)}: OK\n")

    current_file = str(file_path)
    ic(current_file)

    after_listeners.run_group(save_as_file)

    open_file_manually(current_file)


def save_file(root_win: Tk = desktop_win):
    """
    save_file saves the current file

    If the file exists, then it will be saved over without asking questions.

    If the file doesn't exist though, the `SaveFile` feature gets called (Save As)

    Args:
        root_win (Tk, optional): the window where changes take place. Defaults to desktop_win.
    """

    global current_file, cur_data, save_status

    before_listeners.run_group(save_file)
    writerclassic_call_history.register_call(id(save_file))

    if current_file is False:
        return save_as_file(root_win=root_win)

    data: str = text_widget.content

    save_status = True

    file_path = current_file

    if file_path.lower().endswith(".wclassic") and "$VARS" in data:
        for __var in WCLASSIC_VARS:
                for _ in range(data.count(__var)):
                    data = data.replace(__var, WCLASSIC_VARS[__var])

    file = open(file_path, "wt", encoding='utf-8')
    file.write(str(data.rstrip('\n')) + '\n') # [i] save the document with 1 newline in the end
    cur_data = data
    file.close()
    showinfo(lang[1], lang[101])
    root_win.title(f"{lang[1]} - {os.path.basename(file_path)}")

    current_file = str(file_path)
    ic(current_file)

    open_file_manually(current_file)

    LOG.write(f"{str(now())} - An existing file has been saved over ({str(file_path)}): OK\n")


# [!] WARNING: THIS FUNCTION WILL BE DEPRECATED IN V11.0.1
def wipe_file(root_win: Tk = desktop_win):
    before_listeners.run_group(wipe_file)
    writerclassic_call_history.register_call(id(wipe_file))

    sureConfirm = mb.askyesno(title=lang[55], message=lang[56])
    if sureConfirm:
        file_path = dlg.asksaveasfilename(parent=root_win, confirmoverwrite=False, filetypes=FILETYPES, defaultextension="*.*", initialfile="File to Wipe")

        if sys.platform != 'linux':
            # [*] Get the selected file extension
            selected_extension = None
            for ft in FILETYPES:
                if file_path.lower().endswith(ft[1]):
                    selected_extension = ft[1]
                    break

            # [*] Append the selected extension if not already included
            if selected_extension and not file_path.lower().endswith(selected_extension):
                file_path += selected_extension

        file_input = open(file_path, "wt", encoding="utf-8")
        file_input.write('')
        showinfo(title=lang[1], message=lang[101])

        LOG.write(f"{str(now())} - A file has been wiped at {str(file_path)}: OK\n")
        file_input.close()

    after_listeners.run_group(wipe_file)


desktop_entry = None


def select_all(**kw):
    before_listeners.run_group(select_all)
    writerclassic_call_history.register_call(id(select_all))

    widget: WriterClassicEditor = kw.get('widget', text_widget)
    mark: bool = kw.get('mark', True)
    see: float | str = kw.get('see', END)

    widget.select_text(start=0.0, end=END, see=see, mark=mark)

    after_listeners.run_group(select_all)


def lorem_ipsum():
    before_listeners.run_group(lorem_ipsum)
    writerclassic_call_history.register_call(id(lorem_ipsum))

    text_widget.insert(text_widget.index(INSERT), """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque lobortis lacus nibh, ut mattis nisi cursus nec. In aliquam scelerisque eleifend. Suspendisse tempor sem ut ipsum imperdiet, a iaculis dui congue. In in ex massa. Aliquam in dignissim ligula. Mauris pretium mi at molestie feugiat. Cras quam ipsum, congue tempus erat id, rhoncus facilisis mauris. Nam augue nunc, porta ac vestibulum nec, euismod ac est. Duis consectetur risus eu justo pretium volutpat. Vestibulum fringilla purus velit, sed sagittis augue porta a. Vivamus vestibulum turpis ac quam eleifend, ut luctus eros placerat. Praesent pellentesque faucibus ligula, nec varius mi viverra ut. Mauris blandit vitae purus auctor imperdiet. Nullam non sem nisi.

Nullam ullamcorper lacus quis libero luctus ullamcorper. Vestibulum id nisl sit amet ipsum cursus consectetur. Nam et metus leo. Ut a justo scelerisque, imperdiet sapien sed, pharetra ligula. Fusce vel tortor rhoncus nisi elementum commodo at vel massa. Proin suscipit ipsum tristique, ornare quam et, finibus mauris. Curabitur hendrerit, odio eu venenatis aliquam, mi est tincidunt lorem, lacinia placerat lectus nunc rutrum libero.

Maecenas hendrerit diam id mi blandit, vitae dignissim tellus consequat. Vestibulum bibendum convallis nibh eget mattis. Fusce aliquam molestie eros et finibus. Quisque vehicula ex est, vitae convallis lacus dictum at. In id congue velit, sed auctor odio. Aliquam erat volutpat. Ut et molestie lectus, dignissim aliquam libero. Suspendisse potenti.

In pulvinar gravida condimentum. Proin nec sem vitae urna egestas mollis nec vel tortor. Ut sodales eget felis in bibendum. Fusce eu lacus a purus tempus rhoncus non nec magna. Donec sed egestas eros, ut vulputate leo. Sed non libero purus. Suspendisse suscipit nisi vel fringilla suscipit. Integer dapibus tincidunt iaculis. Vivamus risus tortor, cursus vel tincidunt vel, ullamcorper non quam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel magna dui.

Nam gravida nibh leo, eget tincidunt neque facilisis sed. Integer malesuada dui sit amet nulla cursus, eget porttitor nulla fringilla. Proin condimentum mattis posuere. Vivamus sit amet sem non felis aliquet vehicula vel a lorem. Nam accumsan tortor a mattis lacinia. Curabitur ultricies eros lacus, tempor pretium nibh laoreet vel. Curabitur a orci sit amet massa iaculis imperdiet. Phasellus porta aliquet nunc vitae vulputate. Ut non elementum nibh. Sed bibendum ultricies sapien eget dapibus. Pellentesque at lacus sed elit gravida dignissim. Phasellus eu tempus nisl. Suspendisse feugiat risus in laoreet fringilla. Nam sit amet purus laoreet, aliquam augue a, fringilla diam. """)

    after_listeners.run_group(lorem_ipsum)


def readme_writer_classic():
    before_listeners.run_group(readme_writer_classic)
    writerclassic_call_history.register_call(id(readme_writer_classic))

    with open(os.path.join(script_dir, "README.md"), "r", encoding='utf-8') as readme_wrcl_f:
        text_widget.insert(text_widget.index(INSERT), f"README.md (WriterClassic at GitHub; Markdown)\n{readme_wrcl_f.read()}")
        readme_wrcl_f.close()


def has_been_modified(text_widget: WriterClassicEditor = text_widget, main_win: Tk | Toplevel = desktop_win) -> bool | None:
    global save_status

    before_listeners.run_group(has_been_modified)
    writerclassic_call_history.register_call(id(has_been_modified))

    if cur_data == text_widget.content:
        if " (*)" in main_win.title():
            main_win.title(main_win.title().removesuffix(" (*)"))

        save_status = True
        after_listeners.run_group(save_status)
        return save_status

    if " (*)" not in main_win.title():
        main_win.title(f"{main_win.title()} (*)")

    save_status = False

    after_listeners.run_group(save_status)

    return save_status


def change_casing() -> None:
    before_listeners.run_group(change_casing)
    writerclassic_call_history.register_call(id(change_casing))

    def _swap_casing(casing: str):
        if not text_widget.selection:
            showerror(lang[1], lang[372])

        else:
            text_widget.change_selection_casing(casing)

    w = Toplevel()
    w.title(lang[371])
    w.resizable(False, False)

    if sys.platform == 'win32':
        w.iconbitmap(os.path.join(data_dir, 'app_icon.ico'))

    f1 = Frame(w)
    f2 = Frame(w)

    lower_butt = Button(f1, text="lower case", command=lambda:
        _swap_casing('lower'))
    upper_butt = Button(f1, text="UPPER CASE", command=lambda:
        _swap_casing('upper'))
    title_butt = Button(f1, text="Title Case", command=lambda:
        _swap_casing('title'))
    pascal_butt = Button(f1, text="PascalCase", command=lambda:
        _swap_casing('pascal'))
    constant_butt = Button(f1, text="CONSTANT_CASE", command=lambda:
        _swap_casing('constant'))
    snake_butt = Button(f1, text="snake_case", command=lambda:
        _swap_casing('snake'))
    camel_butt = Button(f2, text="camelCase", command=lambda:
        _swap_casing('camel'))
    train_butt = Button(f2, text="Train-Case", command=lambda:
        _swap_casing('train'))
    cobol_butt = Button(f2, text="COBOL-CASE", command=lambda:
        _swap_casing('cobol'))
    kebab_butt = Button(f2, text="kebab-case", command=lambda:
        _swap_casing('kebab'))
    inverted_butt = Button(f2, text="InVeRtEd cAsE", command=lambda:
        _swap_casing('inverted'))
    alternating_butt = Button(f2, text="aLtErNaTiNg cAsE", command=lambda:
        _swap_casing('alternating'))

    lower_butt.grid(column=0, row=0, padx=5, pady=5)
    upper_butt.grid(column=1, row=0, padx=5, pady=5)
    title_butt.grid(column=2, row=0, padx=5, pady=5)
    pascal_butt.grid(column=3, row=0, padx=5, pady=5)
    constant_butt.grid(column=4, row=0, padx=5, pady=5)
    snake_butt.grid(column=5, row=0, padx=5, pady=5)

    camel_butt.grid(column=0, row=0, padx=5, pady=5)
    train_butt.grid(column=1, row=0, padx=5, pady=5)
    cobol_butt.grid(column=2, row=0, padx=5, pady=5)
    kebab_butt.grid(column=3, row=0, padx=5, pady=5)
    inverted_butt.grid(column=4, row=0, padx=5, pady=5)
    alternating_butt.grid(column=5, row=0, padx=5, pady=5)

    f1.pack()
    f2.pack()

    w.mainloop()


rmb_menu = Menu(desktop_win, tearoff = 0)
rmb_menu.add_command(label=lang[293], command=text_widget.edit_undo, accelerator="Ctrl + Z")
rmb_menu.add_command(label=lang[294], command=text_widget.edit_redo, accelerator="Ctrl + Y")
rmb_menu.add_separator()
rmb_menu.add_command(label=lang[341], command=lambda:
    snippet_picker(default_snippets))
rmb_menu.add_command(label=lang[371], command=change_casing)
rmb_menu.add_separator()
rmb_menu.add_command(label=lang[331], command=select_all, accelerator="Ctrl + A")
rmb_menu.add_separator()
rmb_menu.add_command(label=lang[354], command=evaluate_expression, accelerator="Ctrl + R")
rmb_menu.add_separator()
rmb_menu.add_command(label="Lorem ipsum", command=lorem_ipsum)
rmb_menu.add_command(label="README.md", command=readme_writer_classic)


class _XYEvent:
    def __init__(self, x: SupportsFloat, y: SupportsFloat):
        self.x_root = x
        self.y_root = y

    def update(self, params: tuple[int]):
        self.x_root, self.y_root = params


def rmb_popup(event: _XYEvent | Event):
    before_listeners.run_group(rmb_popup)
    writerclassic_call_history.register_call(id(rmb_popup))

    x, y = event.x_root, event.y_root

    try:
        rmb_menu.tk_popup(x, y)

    finally:
        rmb_menu.grab_release()


def dev_option(prog_lang: str, mode: Literal["run", "build"] = "build") -> None:
    """
    dev_option is the actual responsible for the developer options

    Args:
        prog_lang (str): The programming language to use
        mode (str, optional): Sets a different mode. Options: 'build' (default) or 'run'

    Returns:
        None: return is only used to end the function
    """

    before_listeners.run_group(dev_option)
    writerclassic_call_history.register_call(id(dev_option))

    mode = mode.replace(" ", "_").lower()
    prog_lang = prog_lang.strip()

    if current_file is False:
        showerror(lang[1], lang[239])
        return

    match mode:
        case "build":
            match prog_lang.lower():
                case "c++": # [!] THIS ASSUMES YOUR COMPILATION HAS NO EXTRA LIBRARIES
                    if not current_file.strip().endswith("cpp"):
                        showerror(lang[1], lang[284])
                        return

                    os.system(f"g++ \"{os.path.dirname(current_file)}\"")
                    return

                case "c#":
                    if not current_file.strip().endswith(("cs", "csproj")):
                        showerror(lang[1], lang[284])
                        return

                    os.system(f"dotnet build \"{os.path.dirname(current_file)}\"")
                    return

                case _:
                    return

        case "run":
            match prog_lang.lower():
                case "c#":
                    if not current_file.strip().endswith((".cs", ".csproj")):
                        showerror(lang[1], lang[284])
                        return

                    os.system(f"dotnet run --project \"{os.path.dirname(current_file)}\"")
                    return

                case "python":
                    if not current_file.strip().endswith('.py'):
                        showerror(lang[1], lang[284])
                        return

                    if sys.platform == "win32":
                        os.system(f"{sys.executable} \"{current_file}\"")
                        return

                    os.system(f"{sys.executable} \"{current_file}\"")
                    return

                case _:
                    return

        case _:
            return

# [!] DevOption has been removed since it was deprecated

def create_desktop_file_linux(pycommand: str = sys.executable):
    """
    desktop_create creates a Desktop File for Linux

    Args:
        pycommand (string): The command/alias for Python (example: pycommand='python3')
    """

    global desktop_entry

    before_listeners.run_group(create_desktop_file_linux)
    writerclassic_call_history.register_call(id(create_desktop_file_linux))

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
        showinfo(lang[1], lang[101])
        desktop_file.close()

    after_listeners.run_group(create_desktop_file_linux)
    ic(desktop_entry)


def create_window_desktop_file_linux():
    """
    desktop_create_win creates the window that later on calls desktop_create

    No args needed or wanted.
    """

    before_listeners.run_group(create_window_desktop_file_linux)
    writerclassic_call_history.register_call(id(create_window_desktop_file_linux))

    desktop_created_win = Toplevel(desktop_win)
    desktop_created_win.title(lang[197])
    if sys.platform == "win32":
        desktop_created_win.iconbitmap(f"{data_dir}/app_icon.ico")
    desktop_created_win.resizable(False, False)

    LabA = Label(desktop_created_win, text=lang[193], font=Font(family=config_font.actual('family'), size=15, weight='bold'))
    LabB = Label(desktop_created_win, text=lang[194], font=Font(family=config_font.actual('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    Butt = Button(desktop_created_win, text='Ok', command=create_desktop_file_linux)

    LabA.pack()
    LabB.pack()
    Butt.pack()


# [!] WARNING: The deprecation of this function is planned but not confirmed
def app_credits():
    showinfo(title=lang[28], message=CREDITS)
    LOG.write(f"{str(now())} - The Credits have been shown: OK\n")


def surprise_egg():
    before_listeners.run_group(surprise_egg)
    writerclassic_call_history.register_call(id(surprise_egg))

    askNow = sdg.askstring(lang[29], lang[66])

    if not askNow:
        ic()
        return

    elif askNow == 'Entities lurk in the dark.':
        if sys.platform != 'win32':
            if mb.askyesno('ENTITIES!', "This compiled binary is for Windows\nYou can compile it yourself for Linux though.\nCHECK ENTITIES2 OUT BY NORB!!!"):
                simple_webbrowser.website("https://github.com/norbcodes/entities")

            else:
                mb.showinfo('ENTITIES! is now sad :(', ":(")

        try:
            response = get("https://raw.githubusercontent.com/MF366-Coding/WriterClassic/main/.github/entities2_by_norb.exe", timeout=2)

            with open(os.path.join(script_dir, "entities2_by_norb.exe"), 'wb') as f:
                f.write(response.content)

            if mb.askyesno('ENTITIES!!', "Yay, your entities2 is ready on the WriterClassic directory!\nCheck the creator's profile? (entities2 by Norb)"):
                simple_webbrowser.website("https://github.com/norbcodes/entities")

            else:
                mb.showinfo('ENTITIES! is now sad :(', ":(")

        except Exception:
            mb.showerror('ENTITIES!!', "Bad internet :(")

        ic()
        return

    elif askNow == 'Psst, I see dead people':
        simple_webbrowser.SpotifyOnline("Not Like Us Kendrick Lamar")

    elif askNow == str(base64.b64encode(bytes('MaybeHawk', 'utf-8')), 'utf-8'):
        simple_webbrowser.website("https://github.com/maybehawk1")

    elif askNow == "Are you ready?":
        simple_webbrowser.SpotifyOnline('Blind Korn')

    elif askNow == "Em's fastest rap :O":
        simple_webbrowser.SpotifyOnline('Godzilla Eminem')

    else:
        showerror(lang[29], lang[67])
        ic()

    after_listeners.run_group(surprise_egg)

# [i] The Help section

def _help():
    before_listeners.run_group(_help)
    writerclassic_call_history.register_call(id(_help))

    simple_webbrowser.website("https://mf366-coding.github.io/writerclassic.html#docs")
    LOG.write(f"{str(now())} - Requested online help: AWAITING FOR CONNECTION\n")
    ic()

    after_listeners.run_group(_help)

APP_HELP = _help


# [i] This is... well the About section
def about_writerclassic():
    before_listeners.run_group(about_writerclassic)
    writerclassic_call_history.register_call(id(about_writerclassic))

    about_data = ABOUT_WRITER

    about_dialogue = Toplevel(desktop_win)
    about_dialogue.geometry("600x275")
    about_dialogue.resizable(False, False)

    if sys.platform == "win32":
        about_dialogue.iconbitmap(f"{data_dir}/app_icon.ico")

    about_dialogue.title(lang[64])
    label_1 = Label(about_dialogue, text=str(about_data), font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))

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
        simple_webbrowser.website("https://mf366-coding.github.io/writerclassic.html", new=2))

    # [*] Create a Label widget to display the image
    image_label = Label(about_dialogue, image=photo)

    image_label.grid(column=1, row=1)
    label_1.grid(column=2, row=1)
    button_1.grid(column=1, row=2)
    button_2.grid(column=2, row=2)

    after_listeners.run_group(about_writerclassic)

    about_dialogue.mainloop()

    LOG.action('The About dialogue has been shown')

    ic()


def search_replace():
    before_listeners.run_group(search_replace)
    writerclassic_call_history.register_call(id(search_replace))

    search_window = SearchReplace(desktop_win, text_widget, True, lang_exps=lang.copy(), ico=os.path.join(data_dir, 'app_icon.ico'))
    search_window.initiate_setup(search_window)
    search_window.resizable(False, False)
    search_window.mainloop()

    after_listeners.run_group(search_replace)


def markdown_preview() -> None:
    before_listeners.run_group(markdown_preview)
    writerclassic_call_history.register_call(id(markdown_preview))

    if not current_file:
        showerror(lang[1], lang[221])
        return

    if not current_file.lower().endswith((".md", ".mdown", ".mkd", ".mkdn")):
        showerror(lang[1], lang[222])
        return

    temp_html_path = os.path.join(temp_dir, f"{random.randint(1, 1000)}_{os.path.basename(current_file).replace(' ', '_')}.html")
    html_content = markdown2.markdown(text_widget.content)

    with open(temp_html_path, "w", encoding="utf-8") as temp_html_f:
        temp_html_f.write(html_content)
        temp_html_f.close()

    tmp = temp_html_path.replace('\\', '/')

    simple_webbrowser.website(f"file:///{tmp}")
    after_listeners.run_group(markdown_preview)

    del tmp


def tips_tricks():
    before_listeners.run_group(tips_tricks)
    writerclassic_call_history.register_call(id(tips_tricks))

    picked_text = random.choice((
        lang[140],
        lang[141],
        lang[142],
        lang[299],
        lang[301],
        lang[302],
        lang[303],
        lang[305]
    ))

    ic(picked_text)

    showinfo(lang[1], picked_text)
    LOG.write(f"{str(now())} - Requested Tips & Tricks: OK\n")

    after_listeners.run_group(tips_tricks)

    ic()


def reset_writerclassic():
    global settings

    before_listeners.run_group(reset_writerclassic)
    writerclassic_call_history.register_call(id(reset_writerclassic))

    ic(settings)

    confirmation = mb.askyesno(lang[77], lang[78])

    if confirmation:
        settings = {
            "font": {
                "family":"Segoe UI",
                "size": 12,
                "weight": "normal",
                "slant": "roman",
                "underline": 0,
                "overstrike": 0
            },
            "theme": {
                "color": "#020202",
                "ct": "white",
                "fg": "#fcfcfc",
                "mfg": "#f4f8f8",
                "menu": "black"
            },
            "advanced-mode": False,
            "startup": True,
            "geometry": "700x500",
            "language": "en",
            "dencrypt": "",
            "debugging": False,
            "email": "",
            "recent": []
        }

        ic(settings)

        fast_dump()

        LOG.write(f"{str(now())} - Fonts have been reset: OK\n")

        LOG.write(f"{str(now())} - Language and theme have both been reset: OK\n")

        desktop_win.geometry('700x500')

        LOG.write(f"{str(now())} - Window's dimensions have been reset: OK\n")

        with open(f"{config}/signature.wclassic", "w", encoding='utf-8') as sigFILE:
            sigFILE.write("--\nBest regards,\nThis is a customizable signature in a file named signature.wclassic in the data folder...")
            LOG.write(f"{str(now())} - The Custom Signature has been reset: OK\n")

    after_listeners.run_group(reset_writerclassic)

    ic(settings)


# TODO: Terminal will go thru a renaissence (planned for next version - not 11.0.0)
def terminal_inputs():
    before_listeners.run_group(terminal_inputs)
    writerclassic_call_history.register_call(id(terminal_inputs))

    def _trick_terminal(entry: Entry):
        entry.delete(0, END)

        ic()

        LOG.write(f"{str(now())} - Refreshed the Terminal Inputs: OK\n")

    def _terminal_get(entry_selection: Entry):
        _data = entry_selection.get()

        subprocess.run(_data, shell=True)
        # /-/ os.system(_data)

        after_listeners.run_group(terminal_inputs)

        LOG.write(f"{str(now())} - Used the following command on the Terminal - {str(_data)}: OK\n")

        ic(_data)

    terminal = Toplevel(desktop_win)
    terminal.title(lang[183])

    if sys.platform == "win32":
        terminal.iconbitmap(f"{data_dir}/app_icon.ico")

    LOG.write(f"{str(now())} - Opened the Terminal Inputs: OK\n")

    entry_1 = Entry(terminal)
    butt_1 = Button(terminal, text=lang[178], command=lambda:
        _terminal_get(entry_1))
    butt_2 = Button(terminal, text=lang[184], command=lambda:
        _trick_terminal(entry_1))

    entry_1.pack()
    butt_1.pack()
    butt_2.pack()

    terminal.mainloop()


class InternetOnWriter:
    def __init__(self, autoraise: bool = True):
        self.AUTORAISE = autoraise

    def goto_website(self, new: Literal[0, 1, 2] = 0):
        website_url = asklink(lang[80], lang[91], require_https=True).link

        if website_url:
            simple_webbrowser.website(website_url, new, self.AUTORAISE)
            LOG.write(f"{str(now())} - Went to {str(website_url)} via WriterClassic: OK\n")

        ic()

    def search_with_engine(self, engine: Literal['google', 'bing', 'ysearch', 'ddgo', 'yt', 'ecosia', 'stack', 'soundcloud', 'archive', 'qwant', 'spotify', 'brave', 'github', 'gitlab']):
        match engine:
            case 'google':
                search_query = sdg.askstring(lang[83], lang[90])

                if search_query:
                    simple_webbrowser.Google(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on Google: OK\n")

            case 'bing':
                search_query = sdg.askstring(lang[82], lang[90])

                if search_query:
                    simple_webbrowser.Bing(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on Bing: OK\n")

            case 'ysearch':
                # [i] stands for Yahoo!
                search_query = sdg.askstring(lang[85], lang[90])

                if search_query:
                    simple_webbrowser.Yahoo(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on Yahoo!: OK\n")

            case 'ddgo':
                # [i] stands for DuckDuckGo
                search_query = sdg.askstring(lang[84], lang[90])

                if search_query:
                    simple_webbrowser.DuckDuckGo(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on DuckDuckGo: OK\n")

            case "yt":
                # [i] stands for YouTube
                search_query = sdg.askstring(lang[99], lang[90])

                if search_query:
                    simple_webbrowser.YouTube(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on YouTube: OK\n")

            case "ecosia":
                search_query = sdg.askstring(lang[98], lang[90])

                if search_query:
                    simple_webbrowser.Ecosia(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on Ecosia: OK\n")

            case "stack":
                # [i] stands for Stack Overflow
                search_query = sdg.askstring(lang[100], lang[90])

                if search_query:
                    simple_webbrowser.StackOverflow(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on StackOverflow: OK\n")

            case "soundcloud":
                search_query = sdg.askstring(lang[104], lang[90])

                if search_query:
                    simple_webbrowser.SoundCloud(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on SoundCloud: OK\n")

            case "archive":
                # [i] stands for The Internet Archive
                search_query = sdg.askstring(lang[109], lang[90])

                if search_query:
                    simple_webbrowser.Archive(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on The Internet Archive: OK\n")

            case "qwant":
                # [i] stands for Qwant.com
                search_query = sdg.askstring(lang[108], lang[90])

                if search_query:
                    simple_webbrowser.Qwant(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on Qwant: OK\n")

            case "spotify":
                # [i] stands for Spotify Online
                search_query = sdg.askstring(lang[126], lang[90])

                if search_query:
                    simple_webbrowser.SpotifyOnline(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on Spotify Online: OK\n")

            case 'brave':
                # [i] stands for Brave Search
                search_query = sdg.askstring(lang[139], lang[90])

                if search_query:
                    simple_webbrowser.Brave(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on Brave Search: OK\n")

            case "github":
                search_query = sdg.askstring(lang[170], lang[90])

                if search_query:
                    simple_webbrowser.GitHub(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on GitHub: OK\n")

            case "gitlab":
                search_query = sdg.askstring(lang[172], lang[90])

                if search_query:
                    simple_webbrowser.GitLab(search_query)
                    LOG.write(f"{str(now())} - Searched for {str(search_query)} on GitLab: OK\n")

            case _:
                raise InvalidEngine('Invalid search engine for InternetOnWriter.')

internet_plugin = InternetOnWriter()


def lock_a_win(window: Tk = desktop_win):
    before_listeners.run_group(lock_a_win)
    writerclassic_call_history.register_call(id(lock_a_win))
    window.resizable(bool(window_lock_status.get()), bool(window_lock_status.get()))
    after_listeners.run_group(lock_a_win)


class Plugin:
    def __init__(self, folder_name: str, **kw) -> None:
        """
        __init__ intializes the class Plugin

        Args:
            folder_name (str): the name of the folder
            root_name (str, keyword arg): defaults to Verified_Plugins
        """

        self.ROOT_DIR = kw.get('root_name', 'Verified_Plugins')
        self.FOLDER_URL = folder_name

    def obtain_files(self, mode: Literal['manifest', 'versioning'] = 'manifest') -> None:
        """
        obtain_files gets the files of the plugin

        Args:
            mode ('manifest' or 'versioning', optional): mode to use. Defaults to 'manifest' (new in v10.6.0+ and recommended!).
        """

        if mode == 'versioning':
            self._get_files_by_version()
            return

        self._get_files_by_manifest()


    def _get_files_by_manifest(self) -> None:
        """
        Internal function.

        Uses manifests instead of version files.
        """

        try:
            manifest: dict = json.loads(get(f"https://raw.githubusercontent.com/MF366-Coding/WriterClassic-OfficialPlugins/main/{self.ROOT_DIR}/{self.FOLDER_URL}/manifest.json", timeout=1).text)

            __versions: list = [int(i[1:]) for i in manifest]

            # [*] Window Creation
            datax = sdg.askinteger(title=f'{lang[1]} - {lang[203]}', prompt=f'{lang[202]}\n{lang[204]} {max(__versions)}.', initialvalue=max(__versions), minvalue=1, maxvalue=max(__versions))

            datax = f"v{datax}"

            if datax not in manifest:
                raise ValueError('no such version')

            params: dict = manifest[datax]

            zipfile: str | None = params.get('zipfile', None)

            author: str = params.get('author', 'Author')
            name: str | None = params.get('name', self.FOLDER_URL)
            exclude: list[str] = params.get('uncompatible', [])
            description: str | None = params.get('description', 'Description')
            imagefile: str | None = params.get('imagefile', 'https://raw.githubusercontent.com/MF366-Coding/WriterClassic-OfficialPlugins/main/WriterPlugin.png')
            pyfile: str | None = params.get('pyfile', None)

            if APP_VERSION in exclude:
                raise VersionError('uncompatible version')

            if ADVANCED_VERSION in exclude:
                raise VersionError('uncompatible version')

            if zipfile:
                # [i] Send a GET request to download the zip file
                zip_response = get(zipfile, timeout=3)

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
                    with zipper.ZipFile(zip_filepath, mode="r") as zip_ref:
                        zip_ref.extractall(new_folder_path)

                    with open(os.path.join(new_folder_path, 'Details.txt'), 'a', encoding='utf-8') as f:
                        f.write(f'\n{datax.strip()}')

                    # [!?] Delete the downloaded zip file
                    os.remove(zip_filepath)

            else:
                if not pyfile:
                    raise ValueError('no Python file was given')

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

                with open(os.path.join(new_folder_path, 'Details.txt'), 'w', encoding='utf-8') as f:
                    f.write(f"{name.strip()}\n{author.strip()}\n{description.strip()}\n{datax.strip()}")

                response = get(pyfile, timeout=1)
                response.raise_for_status()

                with open(os.path.join(new_folder_path, f"{name.strip()}.py"), 'w', encoding='utf-8') as f:
                    f.write(response.text)

                response = get(imagefile, stream=True, timeout=2)
                response.raise_for_status()

                with open(os.path.join(new_folder_path, 'WriterPlugin.png'), 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

        except (exceptions.ConnectTimeout, exceptions.ConnectionError, TimeoutError, exceptions.ReadTimeout):
            showerror(lang[148], lang[135])

        except VersionError:
            showerror(lang[1], lang[358])

        except ValueError as e:
            LOG.error("Invalid version or missing Python file while attempting to download a plugin using a MANIFEST", str(e))
            raise Exception from e

        except Exception as e:
            showerror(lang[133], f"{lang[134]}\n{e}")

    _get_files = _get_files_by_manifest

    @deprecated('since the addition of manifests, using version files isn\'t recommended and is planned for removal in v10.9.0')
    def _get_files_by_version(self) -> None:
        """
        Deprecated internal function.
        """

        try:
            versioning_file = get(f"https://raw.githubusercontent.com/MF366-Coding/WriterClassic-OfficialPlugins/main/{self.ROOT_DIR}/{self.FOLDER_URL}/Versions.txt", timeout=2)

            versioning_data = versioning_file.text

            # [*] Window Creation
            datax = sdg.askinteger(title=f"{lang[1]} - {lang[203]}", prompt=f'{lang[202]}\n{lang[204]} {int(versioning_data)}.', initialvalue=int(versioning_data), minvalue=1, maxvalue=int(versioning_data))

            # [!?] Some of the following code belongs to ChatGPT and other AIs!

            # [i] URL of the zip file
            zip_url = f"https://raw.githubusercontent.com/MF366-Coding/WriterClassic-OfficialPlugins/main/Verified_Plugins/{self.FOLDER_URL}/Version{int(datax)}.zip"

            # [i] Send a GET request to download the zip file
            zip_response = get(zip_url, timeout=3)

        except (exceptions.ConnectTimeout, exceptions.ConnectionError, TimeoutError, exceptions.ReadTimeout) as e:
            showerror(lang[148], f"{lang[135]}\n{e}")

        except Exception:
            showerror(lang[133], lang[134])

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
                with zipper.ZipFile(zip_filepath, mode="r") as zip_ref:
                    zip_ref.extractall(new_folder_path)

                # [!?] Delete the downloaded zip file
                os.remove(zip_filepath)


class PluginCentral:
    """
    PluginCentral

    A feature rich plugin central
    """

    def __init__(self, plugin_folder: str = plugin_dir) -> None:
        self.PLUGIN_FOLDER: str = plugin_folder
        self._plugins: dict[str, tuple[str, str, str, str, str]] = {}

        self.CENTRAL, self.TITLE, self.FRAME, self.TITLE = None, None, None, None
        self.SELECTION_BOX, self.RUN_BUTT, self.INSTALL_BUTT, self.REMOVE_BUTT = None, None, None, None
        self.INFO_BUTT, self.SHOW_BUTT, self.EXIT_BUTT, self.REFRESH_BUTT = None, None, None, None
        self._plugins_var = None

        self._list_plugins()

    def destroy_ui(self):
        if self.CENTRAL is None:
            return

        self.CENTRAL.destroy()

        self.CENTRAL, self.TITLE, self.FRAME, self.TITLE = None, None, None, None
        self.SELECTION_BOX, self.RUN_BUTT, self.INSTALL_BUTT, self.REMOVE_BUTT = None, None, None, None
        self.INFO_BUTT, self.SHOW_BUTT, self.EXIT_BUTT, self.REFRESH_BUTT = None, None, None, None
        self._plugins_var = None

    def display_ui(self, root: Tk | Toplevel = desktop_win, limit_windows: bool = True):
        self._list_plugins()

        if isinstance(self.CENTRAL, Toplevel) and limit_windows:
            self.CENTRAL.focus_set()
            return

        self.CENTRAL = Toplevel(root)
        self.CENTRAL.title(f"{lang[1]} - Plugin Central")
        self.CENTRAL.resizable(False, False)

        if sys.platform == "win32":
            self.CENTRAL.iconbitmap(f"{data_dir}/app_icon.ico")

        self._plugins_var = Variable(self.CENTRAL, tuple(self._plugins.keys()))

        self.FRAME = Frame(self.CENTRAL)

        self.TITLE = Label(self.CENTRAL, text="Plugin Central", font=Font(family=config_font.actual()['family'], size=16, weight='bold', slant='roman', overstrike=False))
        self.SELECTION_BOX = Listbox(self.CENTRAL, listvariable=self._plugins_var, background='black', foreground='white', selectmode=SINGLE)

        self.RUN_BUTT = Button(self.FRAME, text='Run', command=self.run_plugin)
        self.INSTALL_BUTT = Button(self.FRAME, text='Install', command=self.install_plugin)
        self.REMOVE_BUTT = Button(self.FRAME, text='Remove', command=self.remove_plugin)
        self.REFRESH_BUTT = Button(self.FRAME, text='Refresh', command=self.refresh_selection_listbox)

        self.INFO_BUTT = Button(self.FRAME, text='Info', command=self.display_plugin_info_on_window)
        self.SHOW_BUTT = Button(self.FRAME, text='Show in File Manager', command=self.show_plugin_in_explorer)
        self.EXIT_BUTT = Button(self.FRAME, text='Quit the Central', command=self.destroy_ui)

        self.RUN_BUTT.grid(column=0, row=0, padx=5, pady=5)
        self.INSTALL_BUTT.grid(column=1, row=0, padx=5, pady=5)
        self.REMOVE_BUTT.grid(column=2, row=0, padx=5, pady=5)

        self.REFRESH_BUTT.grid(column=0, row=1, padx=5, pady=5)
        self.INFO_BUTT.grid(column=1, row=1, padx=5, pady=5)
        self.SHOW_BUTT.grid(column=2, row=1, padx=5, pady=5)

        self.EXIT_BUTT.grid(column=1, row=2, padx=5, pady=5)

        self.TITLE.pack()
        self.SELECTION_BOX.pack()
        self.FRAME.pack()

        self.CENTRAL.protocol(name="WM_DELETE_WINDOW", func=self.destroy_ui)

        self.CENTRAL.mainloop()

    def refresh_selection_listbox(self):
        self._list_plugins()

        if isinstance(self._plugins_var, Variable):
            self._plugins_var.set(tuple(self._plugins.keys()))

    def _show_in_file_explorer(self, name: str | None = None):
        if not name:
            try:
                name: str = self.SELECTION_BOX.get(self.SELECTION_BOX.curselection()[0])

            except TclError:
                showerror(lang[1], "You must select a plugin to open in Explorer!")
                return

        ic(name)
        ic(self._plugins)
        ic(self._plugins[name])

        try:
            module_path: str = self._plugins[name][4]

        except (KeyError, IndexError) as e:
            raise PluginNotFoundError(f"no plugin results for '{name}' or no version details: {e}")

        try:
            open_in_file_explorer(os.path.abspath(os.path.dirname(module_path)))

        except Exception as e:
            showerror(lang[1], f"Seems like something went wrong...\n{e}")

    def show_plugin_in_explorer(self, name: str | None = None):
        try:
            self._show_in_file_explorer(name)

        except PluginNotFoundError as e:
            showerror(lang[1], f"The selected plugin doesn't exist.\n{e}")

        except Exception as e:
            showerror(lang[133], f"{lang[134]}\n{e}")

    def _display_plugin_info(self, name: str | None = None):
        if not name:
            try:
                name: str = self.SELECTION_BOX.get(self.SELECTION_BOX.curselection()[0])

            except TclError:
                showerror(lang[1], "You must select a plugin!")
                return

        ic(name)
        ic(self._plugins)
        ic(self._plugins[name])

        try:
            module_info: tuple[str, str, str, str, str] = self._plugins[name]

        except (KeyError, IndexError) as e:
            raise PluginNotFoundError(f"no plugin results for '{name}' or no version details: {e}")

        subwindow = Toplevel(desktop_win if self.CENTRAL is None else self.CENTRAL)
        subwindow.title(f"{lang[1]} - Plugin Info")
        subwindow.resizable(False, False)

        if sys.platform == "win32":
            subwindow.iconbitmap(f"{data_dir}/app_icon.ico")

        image = Image.open(os.path.join(os.path.abspath(os.path.dirname(module_info[4])), "WriterPlugin.png"))
        image_width, image_height = image.size

        max_width = 200
        max_height = 200

        if image_width > image_height:
            desired_width = min(image_width, max_width)
            desired_height = int(desired_width * image_height / image_width)

        else:
            desired_height = min(image_height, max_height)
            desired_width = int(desired_height * image_width / image_height)

        resized_image: Image.Image = image.resize((desired_width, desired_height), Image.LANCZOS)

        short_description: str = module_info[2].strip()

        if len(short_description) > 60:
            short_description = f"{short_description[:60]}..."

        photo = ImageTk.PhotoImage(resized_image)

        image_label = Label(subwindow, image=photo)
        plugin_name_label = Label(subwindow, text=module_info[0].strip(), font=Font(family=config_font.actual()['family'], size=16, weight='bold', slant='roman', overstrike=False))
        plugin_version_label = Label(subwindow, text=f"Version: {module_info[3].strip()}")
        plugin_author_label = Label(subwindow, text=f"Author: {module_info[1].strip()}")
        plugin_description_label = Label(subwindow, text=f"Description:\n{short_description}")

        plugin_name_label.pack()
        image_label.pack()
        plugin_version_label.pack()
        plugin_author_label.pack()
        plugin_description_label.pack()

        subwindow.mainloop()

    def display_plugin_info_on_window(self, name: str | None = None):
        try:
            self._display_plugin_info(name)

        except PluginNotFoundError as e:
            showerror(lang[1], f"The selected plugin doesn't exist.\n{e}")

        except Exception as e:
            showerror(lang[133], f"{lang[134]}\n{e}")

    def _remove_plugin(self, name: str | None = None):
        if not name:
            try:
                name: str = self.SELECTION_BOX.get(self.SELECTION_BOX.curselection()[0])

            except TclError:
                showerror(lang[1], "You must select a plugin to remove!")
                return

        ic(name)
        ic(self._plugins)
        ic(self._plugins[name])

        try:
            module_path: str = self._plugins[name][4]

        except (KeyError, IndexError) as e:
            raise PluginNotFoundError(f"no plugin results for '{name}' or no version details: {e}")

        confirmation = mb.askyesno(lang[1], f"Are you sure you want to remove plugin {name}?\nThis action is permanent and cannot be undone!")

        if not confirmation:
            return

        module_folder = os.path.dirname(module_path)

        try:
            shutil.rmtree(os.path.abspath(module_folder))

        except (PermissionError, OSError) as e:
            showerror(lang[1], f"WriterClassic lacks the permissions to remove the plugin.\nA manual removal might be necessary.\n{e}")

    def remove_plugin(self, name: str | None = None):
        try:
            self._remove_plugin(name)

        except PluginNotFoundError as e:
            showerror(lang[1], f"The selected plugin doesn't exist.\n{e}")

        except Exception as e:
            showerror(lang[133], f"{lang[134]}\n{e}")

        self.refresh_selection_listbox()

    def _run_plugin(self, name: str | None = None):
        if not name:
            try:
                name: str = self.SELECTION_BOX.get(self.SELECTION_BOX.curselection()[0])

            except TclError:
                showerror(lang[1], "You must select a plugin to run!")
                return

        ic(name)
        ic(self._plugins)
        ic(self._plugins[name])

        try:
            module_path = self._plugins[name][4]

        except (KeyError, IndexError) as e:
            raise PluginNotFoundError(f"no plugin results for '{name}' or no version details: {e}")

        wclassic_vars = globals().copy()

        mixer.quit()
        mixer.init()
        mixer.music.load(os.path.join(wclassic_vars['data_dir'], 'sucessful.mp3'))
        mixer.music.set_volume(0.5)
        mixer.music.play()

        module = load_module_from_source(self._plugins[name][0].replace(" ", "_"), module_path)

        module.start(wclassic_vars)

    def run_plugin(self, name: str | None = None):
        try:
            self._run_plugin(name)

        except PluginNotFoundError as e:
            showerror(lang[1], f"The selected plugin doesn't exist.\n{e}")

        except Exception as e:
            showerror(lang[133], f"{lang[134]}\n{e}")

    def install_plugin(self, plugin_name: str | None = None, **_):
        """
        install_plugin installs a plugin using Plugin

        If `plugin_name` is None or an empty string, launch the GUI.

        Else, no GUI is launched whatsoever.
        """

        if not plugin_name:
            plugin_name = sdg.askstring(lang[1], f'{lang[220]}\n{lang[219]}', initialvalue="Type here.")

        plugin = Plugin(folder_name=plugin_name)
        plugin.obtain_files()

        self.refresh_selection_listbox()

    def _list_plugins(self) -> None:
        plugin_folder = self.PLUGIN_FOLDER
        installed_plugins: dict[str, tuple[str, str, str, str, str]] = {}

        for root, _, filenames in os.walk(plugin_folder, False):
            root = os.path.abspath(root)
            directory = os.path.basename(root)

            if directory == 'plugins':
                continue

            if not directory.startswith('plugin_'):
                continue

            if not directory[7:].isdigit():
                continue

            if 'Details.txt' not in filenames:
                continue

            if 'WriterPlugin.png' not in filenames:
                continue

            details: list | None = None

            with open(os.path.join(root, 'Details.txt'), 'r', encoding='utf-8') as f:
                details = f.read().split('\n', maxsplit=4)

            if len(details) < 4:
                continue

            if f"{details[0].replace(' ', '_')}.py" not in filenames:
                continue

            details: list[str] = details[:4]
            details.append(os.path.join(root, f"{details[0].replace(' ', '_')}.py"))

            installed_plugins[f"{details[0].strip()} ({details[3].strip()})"] = tuple(details.copy())

        self._plugins = installed_plugins.copy()
        ic(self._plugins)


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
        10 - Dir where WSCRIPTs are stored (scripts)
    """

    before_listeners.run_group(remove_action)
    writerclassic_call_history.register_call(id(remove_action))

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

    confirmation = mb.askyesno(lang[308], f"{lang[307]} '{path_to_remove}'.")

    if confirmation:
        try:
            if sys.platform == "win32":
                os.system(f'rmdir /s /q {path_to_remove}')
                after_listeners.run_group(remove_action)
                return

            os.system(f'rm -rf {path_to_remove}')
            after_listeners.run_group(remove_action)
            return

        except FileNotFoundError as e:
            LOG.error(text="File/directory missing while trying to extract the backup", error_details=str(object=e))
            raise Exception from e # [i] it will be caught by the statement below

        except Exception as e:
            showerror(lang[308], f"{lang[309]} '{path_to_remove}':\n{e}")

    after_listeners.run_group(remove_action)


def clear_log_file():
    before_listeners.run_group(clear_log_file)
    writerclassic_call_history.register_call(id(clear_log_file))

    with open(os.path.join(user_data, "log.wclassic"), "w", encoding="utf-8") as f:
        f.write("""--
Log File
--
""")
        f.close()

    after_listeners.run_group(clear_log_file)


def show_log():
    before_listeners.run_group(show_log)
    writerclassic_call_history.register_call(id(show_log))

    _new_window = Toplevel(desktop_win)
    _new_window.resizable(False, False)

    if sys.platform == "win32":
        _new_window.iconbitmap(f"{data_dir}/app_icon.ico")

    _new_editor = WriterClassicEditor(_new_window, background=settings['theme']["color"], foreground=settings['theme']["fg"], insertbackground=settings['theme']["ct"], font=config_font, borderwidth=5)
    _new_window.title(lang[180])
    _new_editor.pack()

    with open(f"{user_data}/log.wclassic", "r", encoding="utf-8") as _TEMP_LOG:
        temp_log = _TEMP_LOG.read()
        _new_editor.insert(0.0, str(temp_log))
        _TEMP_LOG.close()

    _new_editor.configure(state=DISABLED)

    LOG.write(f"{str(now())} - The Log File has been shown: OK\n")

    after_listeners.run_group(show_log)

ic(settings["dencrypt"])


class SignaturePlugin:
    def __init__(self, path_to_sig: str = os.path.join(config, 'signature.wclassic')):
        """
        __init__ initializes an instance of the signature plugin

        Args:
            path_to_sig (str, optional): the path to the signature file. Defaults to os.path.join(config, 'signature.wclassic').
        """

        self.SIGNATURE: str = ''
        self.USERNAME: str = ''
        self._gather_data(path_to_sig)

    def _gather_data(self, path) -> tuple[str, str]:
        """
        Internal function.

        Returns:
            tuple[str, str]: custom signature, current username
        """

        with open(path, "r", encoding="utf-8") as sig_file:
            self.SIGNATURE = sig_file.read()
            sig_file.close()

        self.USERNAME = getuser().title()

        return self.SIGNATURE, self.USERNAME

    def _insert_custom(self, pos = END, widget: WriterClassicEditor = text_widget):
        """
        Internal function.
        """

        widget.insert(pos, f"\n\n{self.SIGNATURE}")

    def custom(self, **params):
        """
        custom inserts a custom signature

        Optional key args:
            - pos: the position to insert the signature, defaults to `tkinter.END` a.k.a. `Literal['end']` or `'end'`
            - widget: the Text-like widget where the signature should be inserted, defaults to `text_widget`
        """

        if 'pos' not in params:
            params['pos'] = END

        if 'widget' not in params:
            params['widget'] = text_widget

        self._insert_custom(pos=params['pos'], widget=params['widget'])

        LOG.write(f"{str(now())} - The Custom signature has been inserted: OK\n")

    def _get_details(self) -> tuple[str, str]:
        """
        Internal function.
        """

        return self.SIGNATURE, self.USERNAME

    def get_custom_sig(self) -> str:
        """
        get_custom_sig returns the custom signature

        Returns:
            str: custom signature via `SignaturePlugin._get_details()` (internal function)
        """

        return self._get_details()[0]

    def _insert_auto(self, pos = END, widget: WriterClassicEditor = text_widget):
        """
        Internal function.
        """

        _signature = f"--\n{lang[132]}\n{self.USERNAME}"

        widget.insert(pos, f"\n\n{_signature}")

    def auto(self, **params: str | WriterClassicEditor):
        """
        auto inserts an auto signature

        Optional key args:
            - pos: the position to insert the signature, defaults to `tkinter.END` a.k.a. `Literal['end']` or `'end'`
            - widget: the Text-like widget where the signature should be inserted, defaults to `text_widget`
        """

        if 'pos' not in params:
            params['pos'] = END

        if 'widget' not in params:
            params['widget'] = text_widget

        self._insert_auto(pos=params['pos'], widget=params['widget'])

        LOG.write(f"{str(now())} - The Custom signature has been inserted: OK\n")


backup_system = BackupSystem()
signature_plugin = SignaturePlugin()
plugin_central = PluginCentral()


def change_wrap(**kw) -> None:
    before_listeners.run_group(change_wrap)
    writerclassic_call_history.register_call(id(change_wrap))

    def inner(win, val: StringVar, editor: WriterClassicEditor):
        editor.change_wrapping(val.get())
        after_listeners.run_group(change_wrap)
        win.destroy()

    widget: WriterClassicEditor = kw.get('widget', text_widget)
    root: Tk = kw.get('root', desktop_win)

    w = Toplevel(root)
    w.title(lang[351])
    w.resizable(False, False)

    if sys.platform == 'win32':
        w.iconbitmap(os.path.join(data_dir, 'app_icon.ico'))

    s = StringVar(w, value=widget.wrapping)

    r1 = Radiobutton(w, variable=s, value=NONE, text=lang[342])
    r2 = Radiobutton(w, variable=s, value=CHAR, text=lang[344])
    r3 = Radiobutton(w, variable=s, value=WORD, text=lang[343])

    b = Button(w, text='Ok', command=lambda:
        inner(w, s, widget))

    r1.pack()
    r2.pack()
    r3.pack()
    b.pack()

    w.mainloop()


def theme_maker() -> None:
    before_listeners.run_group(theme_maker)
    writerclassic_call_history.register_call(id(theme_maker))

    w = Toplevel()
    w.title(lang[365])

    if sys.platform == 'win32':
        w.iconbitmap(os.path.join(data_dir, 'app_icon.ico'))

    c = CustomThemeMaker(lang, settings, set_theme, w)
    c.pack()

    after_listeners.run_group(theme_maker)

    w.mainloop()


def close_confirm() -> None:
    before_listeners.run_group(close_confirm)
    writerclassic_call_history.register_call(id(close_confirm))

    ic()

    if not has_been_modified():
        choice: bool | None = mb.askyesnocancel(lang[53], f"{lang[199]}\n{lang[200]}")

        if choice is None:
            ic()
            after_listeners.run_group(close_confirm)
            return None

        if choice:
            ic()
            save_file(desktop_win)
            ic("Called the save function.")

    ic()
    after_listeners.run_group(close_confirm)
    desktop_win.destroy()
    LOG.close()
    sys.exit()


COMMANDS: dict[str, Any] = {
    "Editor:Undo": text_widget.edit_undo,
    "Editor:Redo": text_widget.edit_redo,
    "Editor:Reset": new_file,
    "Editor:Stats": document_status,
    "Editor:SelectAll": select_all,
    "Editor:Lorem": lorem_ipsum,
    "Editor:Readme": readme_writer_classic,
    "Editor:Select": select_all,
    "Editor:Camel": lambda: text_widget.change_selection_casing('camel'),
    "Editor:Pascal": lambda: text_widget.change_selection_casing('pascal'),
    "Editor:Lower": lambda: text_widget.change_selection_casing('lower'),
    "Editor:Title": lambda: text_widget.change_selection_casing('title'),
    "Editor:Upper": lambda: text_widget.change_selection_casing('upper'),
    "Editor:Snake": lambda: text_widget.change_selection_casing('snake'),
    "Editor:Constant": lambda: text_widget.change_selection_casing('constant'),
    "Editor:Inverted": lambda: text_widget.change_selection_casing('inverted'),
    "Editor:Inverted1": lambda: text_widget.change_selection_casing('inverted1'),
    "Editor:Inverted2": lambda: text_widget.change_selection_casing('inverted2'),

    "File:Open": open_file,
    "File:SaveAs": save_as_file,

    "Status:Save": save_file,
    "Status:Refresh": has_been_modified,

    "Plugins:Central": plugin_central.display_ui,
    "Plugins:NewCentral": lambda: plugin_central.display_ui(limit_windows=False),

    "History:Reset": text_widget.edit_reset,

    "Software:Quit": close_confirm,
    "Software:ForceQuit": quickway,
    "Software:About": about_writerclassic,
    "Software:Help": APP_HELP,
    "Software:Repo": repository,
    "Software:Reload": None,
    "Software:Credits": app_credits,
    "Software:Tips": tips_tricks,
    "Software:Version": update_check.manual_check,

    "Log:Clear": clear_log_file,
    "Log:Preview": show_log,

    "Settings:Dump": fast_dump,
    "Settings:Save": fast_dump,
    "Settings:Size": set_window_size,
    "Settings:Reset": reset_writerclassic,
    "Settings:Backup": lambda: backup_system.run_action("zip"),
    "Settings:Load": lambda: backup_system.run_action('unzip'),

    "Tools:Notepad": draft_notepad,
    "Tools:WipeFile": wipe_file,
    "Tools:Markdown": markdown_preview,
    "Tools:Terminal": terminal_inputs,

    "Advanced:DesktopFile": create_window_desktop_file_linux,

    "Internet:Website": internet_plugin.goto_website,

    "Listeners:ClearBefore": before_listeners.remove_all_groups,
    "Listeners:ClearAfter": after_listeners.remove_all_groups,

    "CallHistory:Clear": writerclassic_call_history.clear_history,
}


def command_menu() -> None | bool:
    before_listeners.run_group(command_menu)
    writerclassic_call_history.register_call(id(command_menu))

    new = Toplevel(desktop_win)

    def reload_file():
        if current_file is not False:
            open_file_manually(current_file)

        else:
            return

    def action_logic(_scope: str, _action: str):
        commands: dict[str, Any] = COMMANDS.copy()
        commands["File:Reload"] = reload_file

        a: str = f"{_scope}:{_action}"

        if a in commands.keys():
            commands[a]()
            after_listeners.run_group(command_menu)
            return

        if a.strip() in (None, ''):
            after_listeners.run_group(command_menu)
            return

        showerror(lang[68], lang[70])
        after_listeners.run_group(group=command_menu)
        return

    if sys.platform == "win32":
        new.iconbitmap(f"{data_dir}/app_icon.ico")

    new.title(lang[68])
    new.resizable(False, False)

    action_picker = Entry(new, justify='left', width=65)

    scope = StringVar(new)
    scope_picker = OptionMenu(new, scope, None, "Editor", "File", "Status", "Plugins", "History", "Software", "Log", "Debug", "Advanced", "Tools", "Internet", "Settings", direction='below')

    go_butt = Button(new, text="Ok", command=lambda:
        action_logic(scope.get(), action_picker.get()))

    scope_picker.grid(column=0, row=0)
    action_picker.grid(column=1, row=0)
    go_butt.grid(column=2, row=0)

    action_picker.insert(0, 'Action name goes here!')

    new.mainloop()


event_main = _XYEvent(text_widget.winfo_rootx(), text_widget.winfo_rooty())

# [i] Key bindings below

# [*] RMB Menu
text_widget.bind("<Button-3>", rmb_popup)

# [*] Updating the x, y coordinates
desktop_win.bind('<Key>', lambda _:
    event_main.update((text_widget.winfo_rootx(), text_widget.winfo_rooty())))

# [*] Same as RMB Menu but via keyboard
text_widget.bind('<App>', lambda _:
    rmb_popup(event_main))

# [*] Evaluate expression via keyboard
text_widget.bind('<Control-r>', lambda _:
    evaluate_expression())

# [*] Opening a file
text_widget.bind('<Control-o>', lambda _:
    open_file(desktop_win))

# [*] Recent Files
text_widget.bind('<Control-O>', lambda _:
    recent_files())

# [*] Creating a new file
text_widget.bind('<Control-n>', lambda _:
    new_file())

# [*] Saving the current file
text_widget.bind('<Control-s>', lambda _:
    save_file(desktop_win))

# [*] Saving current file as
text_widget.bind('<Control-S>', lambda _:
    save_as_file(desktop_win))

# [*] Undo
text_widget.bind('<Control-z>', lambda _:
    text_widget.edit_undo())

# [*] Redo
text_widget.bind('<Control-y>', lambda _:
    text_widget.edit_redo())

# [*] About WriterClassic
desktop_win.bind('<Control-i>', lambda _:
    about_writerclassic())

# [*] Search and replace on the editor
text_widget.bind('<Control-f>', lambda _:
    search_replace())

text_widget.bind('<Control-h>', lambda _:
    search_replace())

# [*] Help Online
text_widget.bind('<F1>', lambda _:
    APP_HELP())

# [*] Open the Terminal inputs plugin
text_widget.bind('<F4>', lambda _:
    terminal_inputs())

# [*] Reload current file
text_widget.bind('<F5>', lambda _:
    open_file_manually('' if current_file is False else current_file))

# [*] Change line wrapping
text_widget.bind('<F7>', lambda _:
    change_wrap())

# [*] Dark theme
text_widget.bind('<Control-d>', lambda _:
    set_theme(bg='#020202', fg='#fcfcfc', ct='white', mbg='black', mfg='#f4f8f8', sv='dark'))

# [*] Light theme
text_widget.bind('<Control-l>', lambda _:
    set_theme(bg='#fcfcfc', fg='#020202', ct='black', mbg='#f4f8f8', mfg='black', sv='light'))

# [*] Change window size
text_widget.bind('<Control-G>', lambda _:
    set_window_size())

# [*] Command Menu
text_widget.bind('<Control-P>', lambda _:
    command_menu())

# [*] Command Menu (alias)
text_widget.bind('<Control-greater>', lambda _:
    command_menu())

# [*] Execute plugins 1 - 10
desktop_win.bind('<Control-Key-0>', lambda _:
    plugin_central.display_ui()) # [i] creates new window if non existant, else uses existing

desktop_win.bind('<Control-Shift-Key-0>', lambda _:
    plugin_central.display_ui(limit_windows=False)) # [i] creates new window no mather what

# [*] Select all text in the editor
text_widget.bind('<Control-a>', lambda _:
    select_all())

# [*] Update the modified status
text_widget.bind('<KeyRelease>', lambda _:
    has_been_modified())


# [i] Creating the menu dropdowns and buttons
menu_10.add_command(label=lang[94], command=new_file, accelerator="Ctrl + N")
menu_10.add_command(label=lang[7], command=lambda:
    open_file(desktop_win), accelerator="Ctrl + O")
menu_10.add_command(label=lang[355], command=recent_files, accelerator="Ctrl + Shift + O")
menu_10.add_separator()
menu_10.add_command(label=lang[8], command=lambda:
    save_file(desktop_win), accelerator="Ctrl + S")
menu_10.add_command(label=lang[9], command=lambda:
    save_as_file(desktop_win), accelerator="Ctrl + Shift + S")
menu_10.add_separator()
menu_10.add_command(label=lang[293], command=text_widget.edit_undo, accelerator="Ctrl + Z")
menu_10.add_command(label=lang[294], command=text_widget.edit_redo, accelerator="Ctrl + Y")
menu_10.add_separator()
menu_10.add_command(label=lang[329], command=search_replace, accelerator="Ctrl + F")
menu_10.add_separator()
menu_10.add_command(label=lang[163], command=document_status)
menu_10.add_separator()
menu_10.add_command(label=lang[11], command=close_confirm, accelerator="Alt + F4")

menu_11.add_command(label=lang[75], command=update_check.manual_check)
menu_11.add_separator()

menu_11.add_command(label=lang[25], command=about_writerclassic, accelerator="Ctrl + I")
menu_11.add_command(label=lang[186], command=lambda:
    simple_webbrowser.website("https://www.buymeacoffee.com/mf366"))
menu_11.add_command(label=lang[26], command=APP_HELP, accelerator="F1")
menu_11.add_command(label=lang[27], command=repository)
menu_11.add_command(label=lang[179], command=show_log)
menu_11.add_separator()
menu_11.add_command(label=lang[28], command=app_credits)
menu_11.add_separator()
menu_11.add_command(label=lang[137], command=tips_tricks)
menu_11.add_command(label='Return of the Easter Eggs (ENGLISH ONLY)', command=surprise_egg)

menu_1.add_command(label=lang[12], command=set_window_size, accelerator="Ctrl + Shift + G")
menu_1.add_command(label=lang[332], command=set_font)
menu_1.add_command(label=lang[351], command=change_wrap)
menu_1.add_command(label=lang[365], command=theme_maker)

menu_8.add_command(label=lang[22], command=draft_notepad)
menu_8.add_command(label=lang[182], command=terminal_inputs)
menu_8.add_separator()
menu_8.add_command(label=lang[131], command=signature_plugin.custom)
menu_8.add_command(label=lang[130], command=signature_plugin.auto)
menu_8.add_separator()
menu_8.add_command(label=lang[10], command=lambda:
    wipe_file(desktop_win))
menu_8.add_separator()
menu_8.add_command(label="Plugin Central", command=plugin_central.display_ui)

menu_9.add_command(label=lang[81], command=internet_plugin.goto_website)
menu_9.add_separator()
menu_9.add_command(label=lang[87], command=lambda:
    internet_plugin.search_with_engine('google'))
menu_9.add_command(label=lang[86], command=lambda:
    internet_plugin.search_with_engine('bing'))
menu_9.add_command(label=lang[89], command=lambda:
    internet_plugin.search_with_engine('ysearch'))
menu_9.add_command(label=lang[88], command=lambda:
    internet_plugin.search_with_engine('ddgo'))
menu_9.add_command(label=lang[138], command=lambda:
    internet_plugin.search_with_engine("brave"))
menu_9.add_command(label=lang[95], command=lambda:
    internet_plugin.search_with_engine("ecosia"))
menu_9.add_command(label=lang[106], command=lambda:
    internet_plugin.search_with_engine("qwant"))
menu_9.add_separator()
menu_9.add_command(label=lang[97], command=lambda:
    internet_plugin.search_with_engine("stack"))
menu_9.add_separator()
menu_9.add_command(label=lang[96], command=lambda:
    internet_plugin.search_with_engine("yt"))
menu_9.add_command(label=lang[103], command=lambda:
    internet_plugin.search_with_engine("soundcloud"))
menu_9.add_command(label=lang[125], command=lambda:
    internet_plugin.search_with_engine("spotify"))
menu_9.add_separator()
menu_9.add_command(label=lang[107], command=lambda:
    internet_plugin.search_with_engine("archive"))
menu_9.add_separator()
menu_9.add_command(label=lang[169], command=lambda:
    internet_plugin.search_with_engine("github"))
menu_9.add_command(label=lang[171], command=lambda:
    internet_plugin.search_with_engine("gitlab"))

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
    set_language("de", desktop_win), state='disabled')
menu_13.add_command(label='English (USA)', command=lambda:
    set_language('en', desktop_win))
menu_13.add_command(label='Español (España)', command=lambda:
    set_language('es', desktop_win), state='disabled')
menu_13.add_command(label='Français (France)', command=lambda:
    set_language('fr', desktop_win), state='disabled')
menu_13.add_command(label='Italiano (Italia)', command=lambda:
    set_language('it', desktop_win), state='disabled')
'''
menu_13.add_command(label='Ελληνικά (Ελλάδα)', command=lambda:
    LanguageSet("el", desktop_win), state='disabled')
menu_13.add_command(label="Norsk (Norge)", command=lambda:
    LanguageSet("nb", desktop_win), state='disabled')
'''
menu_13.add_command(label='Português (Brasil)', command=lambda:
    set_language('br', desktop_win), state='disabled')
menu_13.add_command(label='Português (Portugal)', command=lambda:
    set_language('pt', desktop_win))
menu_13.add_command(label='Slovenčina (Slovensko)', command=lambda:
    set_language('sk', desktop_win))
'''
menu_13.add_command(label="Svenska (Sverige)", command=lambda:
    LanguageSet("sv", desktop_win), state='disabled')
menu_13.add_command(label="Українська (Україна)", command=lambda:
    LanguageSet("uk", desktop_win), state='disabled')
'''

menu_12.add_cascade(label=lang[198], menu=menu_13)
menu_12.add_separator()

if sys.platform == "linux":
    menu_12.add_command(label=lang[192], command=create_window_desktop_file_linux)
    menu_12.add_separator()

menu_12.add_checkbutton(label=lang[191], variable=window_lock_status, command=lock_a_win)
menu_12.add_separator()
menu_12.add_command(label=lang[320], command=lambda:
    backup_system.run_action("zip"))
menu_12.add_command(label=lang[321], command=lambda:
    backup_system.run_action("load"))
menu_12.add_separator()
menu_12.add_command(label=lang[76], command=reset_writerclassic)
'''
menu_12.add_separator()
menu_12.add_command(label=lang[105], command=article_md, state='disabled')
'''


menu_15.add_command(label=lang[279], command=markdown_preview)
menu_15.add_separator()
menu_15.add_command(label=lang[341], command=lambda:
    snippet_picker(default_snippets))
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
    set_theme(bg='#fcfcfc', fg='#020202', ct='black', mbg='#f4f8f8', mfg='black', sv='light'), accelerator="Ctrl + L")
menu_5.add_command(label=lang[17], command=lambda:
    set_theme(bg='#020202', fg='#fcfcfc', ct='white', mbg='black', mfg='#f4f8f8', sv='dark'), accelerator="Ctrl + D")


menu_6.add_command(label='WriterClassic Codetime', command=lambda:
    set_theme(bg='#0f0e0e', fg='#3fdc24', ct='#33e814', mbg='black', mfg='#2af48e'))

menu_6.add_separator()

menu_6.add_command(label='WriterClassic Aqua', command=lambda:
    set_theme(bg='#12aace', fg='#040426', ct='#040426', mbg='#070755', mfg='#bcf6f1'))

menu_6.add_command(label='WriterClassic Earth', command=lambda:
    set_theme(bg='#4a0d0d', fg='#eccccc', ct='#e8bebe', mbg='#2b0808', mfg='#e8bebe'))

menu_6.add_separator()

menu_6.add_command(label='Darkest Night Ever', command=lambda:
    set_theme(bg='#040114', fg='#e8a78e', ct='#e8a78e', mbg='black', mfg='#e8a78e'))

menu_6.add_command(label='Dark Forest', command=lambda:
    set_theme(bg='#0e2414', fg='#c0db7b', ct='#c0db7b', mbg='#040d07', mfg='#ccf0c5'))

menu_6.add_command(label='Christmas Night', command=lambda:
    set_theme(bg='#020421', fg='#a5a9e8', ct='#a5a9e8', mbg='#020312', mfg='#cbcef2'))

menu_6.add_command(label='Silent Night', command=lambda:
    set_theme(bg='#020421', fg='pink', ct='pink', mbg='#020312', mfg='#ebd1ed'))

# [*] The PowerShell adapted theme has become builtin
menu_6.add_command(label='PowerShell Theme', command=lambda:
    set_theme(bg="#012456", fg="#eeedf0", ct="#fedba9", mbg="#eeedf0", mfg="#012456"))

ic(settings["advanced-mode"])
ic(settings["debugging"])


def adv_change():
    before_listeners.run_group(adv_change)
    writerclassic_call_history.register_call(id(adv_change))

    settings["advanced-mode"] = bool(advanced_mode_status.get())

    ic(settings["advanced-mode"])
    fast_dump()

    showinfo(message=lang[63], title=lang[1])

    after_listeners.run_group(adv_change)


menu_12.add_separator()
menu_12.add_checkbutton(label=lang[306], variable=advanced_mode_status, command=adv_change)


def show_debug():
    before_listeners.run_group(show_debug)
    writerclassic_call_history.register_call(id(show_debug))

    if settings["debugging"]:
        settings["debugging"] = False

    else:
        settings["debugging"] = True

    ic(settings["debugging"])
    fast_dump()

    showinfo(message=lang[63], title=lang[1])

    after_listeners.run_group(show_debug)


def dencrypt():
    before_listeners.run_group(dencrypt)
    writerclassic_call_history.register_call(id(dencrypt))

    def runx(pathx: str, parameters: str):
        settings["dencrypt"] = pathx
        fast_dump()

        if not current_file:
            showinfo(lang[1], lang[239])

        else:
            os.system(f'"{pathx}" "{current_file}" {parameters}')
            showinfo(lang[1], lang[275])

    new = Toplevel(desktop_win)

    if sys.platform == "win32":
        new.iconbitmap(f"{data_dir}/app_icon.ico")

    new.title(f"{lang[1]} - {lang[274]}")
    new.resizable(False, False)

    label_1 = Label(new, text=f"{lang[273]}: ", font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    entry_1 = Entry(new, width=58, font=Font(family=config_font.cget('family'), size=11, weight='normal', slant='roman', underline=False, overstrike=False))
    label_2 = Label(new, text=f"{lang[272]}: ", font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    entry_2 = Entry(new, width=58, font=Font(family=config_font.cget('family'), size=11, weight='normal', slant='roman', underline=False, overstrike=False))

    entry_1.insert(0, settings["dencrypt"])
    entry_2.insert(0, "-e")

    butt_1 = Button(new, text=f"{lang[178]}!", command=lambda:
        runx(entry_1.get(), entry_2.get()))
    butt_2 = Button(new, text=lang[271], command=lambda:
        simple_webbrowser.website("https://github.com/MF366-Coding/d3NCRYP7#d3ncryp7---simple-encryption-and-decryption-system"))

    label_1.grid(column=1, row=1)
    entry_1.grid(column=2, row=1)
    label_2.grid(column=1, row=2)
    entry_2.grid(column=2, row=2)
    butt_1.grid(column=1, row=3)
    butt_2.grid(column=2, row=3)

    after_listeners.run_group(dencrypt)

    new.mainloop()


def readme_gen(*entries):
    before_listeners.run_group(readme_gen)
    writerclassic_call_history.register_call(id(readme_gen))

    _title = entries[0]
    _describe = entries[1]
    _author_email = entries[2]
    _author_website = entries[3]
    _project_website = entries[4]
    _sponsor_site = entries[5]

    text_widget.delete(0.0, END)

    if _title.strip() == '':
        _title = lang[270]

    if _describe.strip() == '':
        _describe = f"{lang[269]} {_title}"

    readme_generated = f"""{_title}
**{_describe}**

"""

    if _author_email.strip() != '':
        readme_generated += f"""[{lang[268]}]({_author_email})\n"""

    if _author_website.strip() != '':
        readme_generated += f"""[{lang[267]}: {_author_website}]({_author_website})\n"""

    if _project_website.strip() != '':
        readme_generated += f"""[{lang[266]}: {_project_website}]({_project_website})\n"""

    if _sponsor_site.strip() != '':
        readme_generated += f"""[{lang[265]}]({_sponsor_site})\n"""

    text_widget.insert(chars=readme_generated, index=0.0)

    after_listeners.run_group(readme_gen)

    ic(readme_generated)


def readme_gen_win():
    # [i] Window Creation
    window = Toplevel(desktop_win)
    window.title(f"{lang[1]} - {lang[226]}")
    window.resizable(False, False)

    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    label_1 = Label(window, text=f'{lang[264]}:', font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_2 = Label(window, text=f'{lang[263]}:', font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_3 = Label(window, text=f'{lang[262]}:', font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_4 = Label(window, text=f'{lang[261]}:', font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_5 = Label(window, text=f'{lang[260]}:', font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_6 = Label(window, text=f'{lang[259]}:', font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_7 = Label(window, text=f"{lang[258]}:".upper(), font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_8 = Label(window, text=lang[257], font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))

    _title = Entry(window)
    _describe = Entry(window)
    _author_email = Entry(window)
    _author_website = Entry(window)
    _project_website = Entry(window)
    _sponsor_site = Entry(window)

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
    before_listeners.run_group(open_with_adv)
    writerclassic_call_history.register_call(id(open_with_adv))

    window = Toplevel(desktop_win)
    window.title(f"{lang[1]} - {lang[254]}")
    window.resizable(False, False)

    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')



    def action_1():
        if not current_file:
            showinfo(lang[1], lang[239])
        else:
            os.system(f'"{str(current_file)}"')

        after_listeners.run_group(open_with_adv)

        window.destroy()

    def action_2(requested_entry):
        if not current_file:
            showinfo(lang[1], lang[239])
        else:
            if " " in requested_entry:
                os.system(f'"{requested_entry}" "{str(current_file)}"')
            else:
                os.system(f'{requested_entry} "{str(current_file)}"')

        after_listeners.run_group(open_with_adv)

        window.destroy()

    butt_1 = Button(window, text=lang[253], command=action_1)
    label_1 = Label(window, text=lang[252].upper(), font=Font(family=config_font.actual('family'), size=15, weight='bold'))
    label_2 = Label(window, text=lang[251], font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    entry_1 = Entry(window)
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
        body += f"\n\n{signature_plugin.get_custom_sig()}"

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

        with open(current_file, "r", encoding="utf-8") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(current_file)}")
            message.attach(part)

        server.sendmail(sender_email, recipient_email, message.as_string())

    except (ConnectionError, TimeoutError) as e:
        showerror(lang[133], f"{lang[134]}\n{e}")

    except Exception as e:
        showerror(lang[1], f"{lang[247]}\n{lang[248]}\n{e}")

    finally:
        del sender_password

    server.quit()


def message_write(mail: str, pwd: str, _variable, win):
    win.destroy()

    if _variable == '1':
        settings["email"] = mail
        fast_dump()

    # [*] Window Creation
    window = Toplevel(desktop_win)
    window.title(f"{lang[1]} - {lang[246]}")
    window.resizable(False, False)

    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    label_1 = Label(window, text=f"{lang[245]}: ", font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_2 = Label(window, text=lang[244], font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_3 = Label(window, text=f"{lang[243]}: ", font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_4 = Label(window, text=f"{lang[242]}: ", font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))

    entry_1 = Entry(window)
    entry_2 = Entry(window)

    text_1 = WriterClassicEditor(window, borderwidth=5, font=config_font, insertbackground=settings['theme']["ct"], foreground=settings['theme']["fg"], background=settings['theme']["color"], height=10)

    butt_1 = Button(window, text=lang[241], command=lambda:
        send_email_with_attachment(window, False, mail, pwd, entry_2.get(), entry_1.get(), text_1.content))

    butt_2 = Button(window, text=lang[240], command=lambda:
        send_email_with_attachment(window, True, mail, pwd, entry_2.get(), entry_1.get(), text_1.content))

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
    if not current_file:
        showerror(lang[1], lang[239])
        return

    window = Toplevel(desktop_win)
    window.title(f"{lang[1]} - {lang[238]}")

    window.resizable(False, False)
    if sys.platform == 'win32':
        window.iconbitmap(f'{data_dir}/app_icon.ico')

    label_1 = Label(window, text=lang[237], font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_2 = Label(window, text=lang[236], font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_3 = Label(window, text=lang[235], font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_4 = Label(window, text=f"{lang[234]}: ", font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))
    label_5 = Label(window, text=f"{lang[233]}: ", font=Font(family=config_font.cget('family'), size=10, weight='normal', slant='roman', underline=False, overstrike=False))

    entry_1 = Entry(window)
    entry_2 = Entry(window, show="*")

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


def show_advanced_version():
    before_listeners.run_group(show_advanced_version)
    writerclassic_call_history.register_call(id(show_advanced_version))

    showinfo(lang[1], f"{lang[230]} {ADVANCED_VERSION}.")
    ic(ADVANCED_VERSION)

    after_listeners.run_group(show_advanced_version)


if ADVANCED:
    menu_14.add_command(label=lang[224], command=show_debug)
    if sys.platform == "win32":
        menu_14.add_command(label=lang[225], command=dencrypt)
    menu_14.add_command(label=lang[226], command=readme_gen_win)
    menu_14.add_command(label=lang[227], command=open_with_adv)
    menu_14.add_command(label=lang[228], command=adv_login)
    menu_14.add_command(label=lang[229], command=show_advanced_version)

if sys.platform == "linux":
    try:
        menu_10.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_11.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_1.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_5.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_4.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_6.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_12.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_8.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_9.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_13.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])

        if ADVANCED:
            menu_14.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])

        menu_15.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_16.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        menu_17.configure(background=settings['theme']["menu"], foreground=settings['theme']["mfg"])
        LOG.write(f"{str(now())} - The Menus have been themed [LINUX ONLY]: OK\n")

    except TclError:
        showerror(lang[150], f"{lang[151]}\n{lang[152]}")
        menu_10.configure(background="white", foreground="black")
        menu_11.configure(background="white", foreground="black")
        menu_1.configure(background="white", foreground="black")
        menu_5.configure(background="white", foreground="black")
        menu_4.configure(background="white", foreground="black")
        menu_6.configure(background="white", foreground="black")
        menu_12.configure(background="white", foreground="black")
        menu_8.configure(background="white", foreground="black")
        menu_9.configure(background="white", foreground="black")
        menu_13.configure(background="white", foreground="black")

        if ADVANCED:
            menu_14.configure(background="white", foreground="black")

        menu_15.configure(background="white", foreground="black")
        menu_17.configure(background="white", foreground="black")
        menu_16.configure(background="white", foreground="black")
        LOG.write(f"{str(now())} - The Menus have been themed [LINUX ONLY]: OK\n")

# [*] dropdowns/cascades
menu_bar.add_cascade(label=lang[2],menu=menu_10)
menu_bar.add_cascade(label=lang[3],menu=menu_1)
menu_1.add_cascade(label=lang[13], menu=menu_4)
menu_4.add_cascade(label=lang[15], menu=menu_5)
menu_4.add_cascade(label=lang[19], menu=menu_6)
menu_4.add_separator()
menu_4.add_command(label=lang[153], command=lambda:
    simple_webbrowser.website(url="https://github.com/MF366-Coding/WriterClassic-ExtraThemes"))
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
LOG.write(f"{str(now())} - The Menu bar has been configured correctly: OK\n")

toolbar = Frame(desktop_win, height=14, borderwidth=2, width=14)
toolbar.pack()

redo_img = None

toolbar_commands = [new_file,
                    open_file,
                    save_file,
                    # --
                    text_widget.edit_undo,
                    text_widget.edit_redo,
                    # --
                    copy,
                    paste,
                    cut,
                    # --
                    about_writerclassic,
                    APP_HELP,
                    # --
                    close_confirm]

__ico_paths = [os.path.join(data_dir, 'toolbar', f"{i + 1}.png") for i in range(TOOLBAR_LEN)]

icon_images = [Image.open(__ico_paths[i]) for i in range(TOOLBAR_LEN)]
tk_icon_images = [ImageTk.PhotoImage(icon_images[i]) for i in range(TOOLBAR_LEN)]

buttons: list[Button] = [Button(toolbar, image=tk_icon_images[i], command=toolbar_commands[i], width=10) for i in range(TOOLBAR_LEN)]

for j in range(TOOLBAR_LEN):
    buttons[j].grid(column=j, row=0)

text_widget.pack(expand=True)
cur_data = text_widget.content

if len(sys.argv) > 1:
    # [i] The first command-line argument is the file path
    file_path = sys.argv[1]
    ic(file_path)

    try:
        open_file_manually(file_path)

    except FileNotFoundError as e:
        desktop_win.destroy()
        ic(e)
        LOG.write(f"{str(now())} - Found error {e} while trying to open file at {str(file_path)}: INFO\n")
        sys.exit() # [*] Using sys.exit() instead of builtin quit()

    finally:
        ic(current_file)

else:
    if last_file:
        open_file_manually(file_path=last_file)

grp: GlobalRestorePoint = GlobalRestorePoint()
COMMANDS['Software:Reload'] = grp.restore

# [*] Auto WSCRIPTs
if os.path.exists(path=os.path.join(scripts_dir, "auto.wscript")):
    auto_script = WScript()
    auto_script.loadpath(location=os.path.join(scripts_dir, "auto.wscript"))

    _run_auto: bool = mb.askyesno(title=lang[1], message=f"{lang[289]}\n{lang[290]}\n{lang[291]}")

    if _run_auto:
        try:
            auto_script.run()

        # [*] in this case, a general Exception is used because any type of error can happen

        except Exception as e:
            showerror(lang[133], f"{lang[134]}\n{e}")

# [*] You can use the following syntax when running WriterClassic:
# [*] name [filepath] [debugscript]
# [*] name is the filepath of WriterClassic
# [*] the other 2 are optional
# [*] filepath is the filepath to open (duuh??!)
# [*] but debugscript (which must always come after a filepath)
# [!?] is the path to a wscript that runs with write perms
# [*] used mostly for debugging I guess
if len(sys.argv) > 2:
    startup_script: WScript = WScript()
    startup_script.loadpath(location=os.path.abspath(path=sys.argv[2]))

    startup_script.run(scope='write')

    ic(globals().copy())

style.configure(style='prev.TLabel', foreground='black')

desktop_win.protocol(name="WM_DELETE_WINDOW", func=close_confirm)

# [*] And done!
# [i] Now, it will continuously mainlooping! Enjoy!
desktop_win.mainloop()
