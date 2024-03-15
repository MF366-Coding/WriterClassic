# editor.py

# [*] Catching too general exception
# pylint: disable=W0718

# [*] Attribute defined outside init
# pylint: disable=W0201

# [*] Pointless string statement
# pylint: disable=W0105

# [i] General imports
from typing import Any, Callable, Literal, Iterable
import sys

# [i] Tkinter imports
from tkinter import Misc, END, WORD, INSERT, SEL, SEL_FIRST, SEL_LAST, Toplevel, IntVar, TclError
from tkinter.ttk import Checkbutton, Button, Frame, Label, Entry
from tkinter.scrolledtext import ScrolledText as _ScrolledText
from tkinter.font import Font
from tkinter import messagebox as mb
from tkinter import colorchooser as picker


class WriterClassicEditor(_ScrolledText):
    """
    Provides an editor interface for WriterClassic.
    """

    def __init__(self, master: Misc | None = None, **kwargs: Any) -> None:
        kwargs.update({'wrap': WORD})

        self._wrapline = WORD
        self.write = super().insert

        super().__init__(master, **kwargs)


    def change_wrapping(self, char_level: Literal['none', 'char', 'word'] = 'char'):
        self._wrapline: str = char_level
        super().configure(wrap=self._wrapline)


    def select_text(self, **kw) -> None:
        """
        select_text handles the task of selecting text with simplicity

        Possible args (all optional):
            start (TextIndex-like object): starting index for the selection. Defaults to 0.0.
            end (TextIndex-like object): end index for the selection. Defaults to `END` ('end').
            see (TextIndex-like object): the value to mark as INSERT. If `mark` is False, this argument will be ignored and the action won't be performed. Defaults to the value given by the `end` argument.
            mark (bool): whether to mark INSERT as the value given by the `see` argument or not. Defaults to True.
        """

        _start = kw.get('start', 0.0)
        _end = kw.get('end', END)
        _mark = kw.get('mark', True)

        super().tag_add(SEL, _start, _end)

        if _mark:
            _see = kw.get('see', _end)
            super().mark_set(INSERT, _see)

        super().see(INSERT)


    @property
    def wrapping(self) -> str:
        return self._wrapline


    @property
    def selection(self) -> str | Literal[False]:
        """
        Current selection.

        If nothing is selected, return False.
        """

        try:
            return self.get(SEL_FIRST, SEL_LAST)

        except TclError:
            return False


    @property
    def content(self) -> str:
        """
        Returns the text in the widget.
        """

        return self.get(0.0, END)


    @property
    def num_lines(self) -> int:
        """
        Returns the number of lines.
        """

        return int(self.index(f"{END} - 1 char").split('.')[0])


class SearchReplace(Toplevel):
    def __init__(self, master: Misc | None = None, widget: WriterClassicEditor | None = None, regexp: bool = False, lang_exps: Iterable[str] | None = None, **kwargs) -> None:
        ico = kwargs.pop('ico', None)

        if not isinstance(lang_exps, (list, tuple)):
            raise ValueError('lang expressions must be tuple or list')

        if not widget:
            raise TypeError('a widget must be specified and match type WriterClassicEditor')

        self._regexp = regexp
        self._exps = lang_exps

        self._MARKED: bool = False

        widget.tag_configure('found', background='yellow', foreground='black', font=Font(weight='bold', slant='roman', overstrike=False, underline=True))
        widget.tag_remove("found", 0.0, END)

        self.editor: WriterClassicEditor = widget
        self.master = master

        super().__init__(master, **kwargs)
        super().title(f"{self.lang[1]} - {self.lang[345]}")

        if sys.platform == 'win32':
            super().iconbitmap(ico)

    # [!?] exact is not working for some reason
    # [i] this is something related to tkinter tho and not this class
    # [?] I might do a bit more research on this topic ig
    def initiate_setup(self, widget: Toplevel | Misc):
        self._F1 = Frame(widget)
        self._F2 = Frame(widget)

        self._L1 = Label(self._F1, text=self.lang[346].strip() + ' ')
        self._E1 = Entry(self._F1)
        self._PREVBUTT = Button(self._F1, text=chr(9650), command=lambda:
            self._find('prev'))
        self._NEXTBUTT = Button(self._F1, text=chr(9660), command=lambda:
            self._find('next'))

        self._CASING = IntVar(widget, value=0)

        self._C2 = Checkbutton(self._F2, text=self.lang[347], variable=self._CASING)

        # [*] Frame 1 content
        self._L1.grid(column=0, row=0)
        self._E1.grid(column=1, row=0)
        self._PREVBUTT.grid(column=2, row=0)
        self._NEXTBUTT.grid(column=3, row=0)

        # [*] Frame 2 content
        self._C2.pack()

        # [*] super() / window content
        self._F1.pack()
        self._F2.pack()

    def _find(self, direction: Literal['prev', 'next']):
        self.editor.tag_remove(SEL, 0.0, END)

        if not self.pattern:
            mb.showwarning(self.lang[1], self.lang[348])
            return

        match direction:
            case 'next':
                first_index, last_index = self.__n()

            case 'prev':
                first_index, last_index = self.__p()

            case _:
                raise ValueError('must be next/prev')

        self.editor.mark_set(INSERT, last_index if direction == 'next' else first_index)
        self.editor.tag_add(SEL, first_index, last_index)
        self.rf()
        self.editor.see(INSERT)

    def __n(self, ind: str | float = INSERT) -> tuple[str | None, str | None]:
        first_index = self.editor.search(self.pattern, ind, END, True, False, False, self.regexp, self.nocasing)

        if not first_index:
            mb.showwarning(self.lang[1], self.lang[349])
            return None, None

        first_index = self.editor.index(first_index)
        last_index = first_index

        for _ in range(len(self.pattern)):
            index_iter = last_index.split('.')
            line_index = int(index_iter[1]) + 1

            last_index = '.'.join((index_iter[0], str(line_index)))

        return first_index, last_index

    def __p(self) -> tuple[str | None, str | None]:
        first_index = self.editor.search(self.pattern, INSERT, 0.0, False, True, False, self.regexp, self.nocasing)

        if not first_index:
            mb.showwarning(self.lang[1], self.lang[350])
            return None, None

        first_index = self.editor.index(first_index)
        last_index = first_index

        for _ in range(len(self.pattern)):
            index_iter = last_index.split('.')
            line_index = int(index_iter[1]) + 1

            last_index = '.'.join((index_iter[0], str(line_index)))

        return first_index, last_index

    def return_focus(self):
        self.editor.focus_set()

    rf = return_focus

    @property
    def lang(self) -> list | tuple:
        if isinstance(self._exps, list):
            return self._exps.copy()

        return self._exps

    @property
    def regexp(self) -> bool:
        return self._regexp

    @property
    def pattern(self) -> str:
        return self._E1.get()

    @property
    def nocasing(self) -> bool:
        return not bool(self._CASING.get())


class CustomThemeMaker(Frame):
    def __init__(self, language_data: list[str], settings: dict[str, Any], dump_func: Callable, master: Toplevel | None = None, **kw) -> None:
        super().__init__(master, *kw)

        self._lang = language_data.copy()
        self._dump_func = dump_func
        self._config = settings
        self._master = master

        master.resizable(False, False)

        self._F1 = Frame(master)
        self._exit_butt = Button(master, text='Ok', command=lambda:
            self.save_and_leave(self._dump_func))

        self._L1 = Label(self._F1, text=str(self._lang[360]))
        self._L2 = Label(self._F1, text=str(self._lang[361]))
        self._L3 = Label(self._F1, text=str(self._lang[362]))
        self._L4 = Label(self._F1, text=str(self._lang[363]))
        self._L5 = Label(self._F1, text=str(self._lang[364]))

        self._B1 = Button(self._F1, text=str(self._config['theme']['color']), command=lambda:
            self.askcolor(self._B1))
        self._B2 = Button(self._F1, text=str(self._config['theme']['fg']), command=lambda:
            self.askcolor(self._B2))
        self._B3 = Button(self._F1, text=str(self._config['theme']['ct']), command=lambda:
            self.askcolor(self._B3))
        self._B4 = Button(self._F1, text=str(self._config['theme']['menu']), command=lambda:
            self.askcolor(self._B4))
        self._B5 = Button(self._F1, text=str(self._config['theme']['mfg']), command=lambda:
            self.askcolor(self._B5))

        self._butt_text_rel: dict[Button, str | bytes] = {
            self._B1: self._config['theme']['color'],
            self._B2: self._config['theme']['fg'],
            self._B3: self._config['theme']['ct'],
            self._B4: self._config['theme']['menu'],
            self._B5: self._config['theme']['mfg']
        }

        self._L1.grid(column=0, row=0, padx=10, pady=10)
        self._L2.grid(column=1, row=0, padx=10, pady=10)
        self._L3.grid(column=2, row=0, padx=10, pady=10)
        self._L4.grid(column=3, row=0, padx=10, pady=10)
        self._L5.grid(column=4, row=0, padx=10, pady=10)

        self._B1.grid(column=0, row=1, padx=10, pady=10)
        self._B2.grid(column=1, row=1, padx=10, pady=10)
        self._B3.grid(column=2, row=1, padx=10, pady=10)
        self._B4.grid(column=3, row=1, padx=10, pady=10)
        self._B5.grid(column=4, row=1, padx=10, pady=10)
        
        self._F1.pack(pady=5)
        self._exit_butt.pack(pady=5)

    def askcolor(self, butt_scope: Button):        
        color: str = picker.askcolor(self._butt_text_rel[butt_scope], title=self._lang[365])[1]

        self.focus_set()

        if not color:
            return
        
        self._butt_text_rel[butt_scope] = color
        butt_scope.configure(text=str(color))

    def _leave(self):
        self._master.destroy()

    def _save(self, dump_func: Callable, **kwargs):
        dump_func(**kwargs)

    def save_and_leave(self, dump_func: Callable, **kw):
        self._save(dump_func, bg=self._butt_text_rel[self._B1], fg=self._butt_text_rel[self._B2], ct=self._butt_text_rel[self._B3], mbg=self._butt_text_rel[self._B4], mfg=self._butt_text_rel[self._B5], *kw)
        self._leave()


class _SearchReplaceBackup(Toplevel):
    def __init__(self, master: Misc | None = None, widget: WriterClassicEditor | None = None, regexp: bool = False, lang_exps: Iterable[str] | None = None, **kwargs) -> None:
        ico = kwargs.pop('ico', None)

        if not isinstance(lang_exps, (list, tuple)):
            raise ValueError('lang expressions must be tuple or list')

        if not widget:
            raise TypeError('a widget must be specified and match type WriterClassicEditor')

        self._regexp = regexp
        self._exps = lang_exps

        self._MARKED: bool = False

        widget.tag_configure('found', background='yellow', foreground='black', font=Font(weight='bold', slant='roman', overstrike=False, underline=True))
        widget.tag_remove("found", 0.0, END)

        self.editor: WriterClassicEditor = widget
        self.master = master

        super().__init__(master, **kwargs)
        super().title(f"{self.lang[1]} - {self.lang[345]}")

        if sys.platform == 'win32':
            super().iconbitmap(ico)


    # [!?] exact is not working for some reason
    # [i] this is something related to tkinter tho and not this class
    # [?] I might do a bit more research on this topic ig
    def initiate_setup(self, widget: Toplevel | Misc):
        self._F1 = Frame(widget)
        self._F2 = Frame(widget)
        self._F3 = Frame(widget)
        self._F4 = Frame(widget)
        self._B3 = Button(widget, text='Mark all matches', command=self._mark_matches)

        self._L1 = Label(self._F1, text=self.lang[346].strip() + ' ')
        self._E1 = Entry(self._F1)
        self._PREVBUTT = Button(self._F1, text=chr(9650), command=lambda:
            self._find('prev'))
        self._NEXTBUTT = Button(self._F1, text=chr(9660), command=lambda:
            self._find('next'))

        self._EXACT = IntVar(widget, value=0)
        self._CASING = IntVar(widget, value=0)

        # /-/ self._C1 = Checkbutton(self._F2, text="Exact matches only", variable=self._EXACT)
        self._C2 = Checkbutton(self._F2, text=self.lang[347], variable=self._CASING)

        self._E2 = Entry(self._F3)

        self._B1 = Button(self._F4, text='Replace')
        self._B2 = Button(self._F4, text='Replace All')

        # [*] Frame 1 content
        self._L1.grid(column=0, row=0)
        self._E1.grid(column=1, row=0)
        self._PREVBUTT.grid(column=2, row=0)
        self._NEXTBUTT.grid(column=3, row=0)

        # [*] Frame 2 content
        # /-/ self._C1.pack()
        self._C2.pack()

        # [*] Frame 3 content
        self._E2.grid(column=1, row=0)

        # [*] Frame 4 content
        self._B1.grid(column=0, row=0)
        self._B2.grid(column=1, row=0)

        # [*] super() / window content
        self._F1.pack()
        self._F2.pack()
        self._F3.pack()
        self._F4.pack()
        self._B3.pack()

    def _replace(self):
        """
        XXX Not working XXX
        """

        s1, s2 = None, None

        try:
            s1, s2 = SEL_FIRST, SEL_LAST

        except TclError:
            mb.showerror(self.lang, 'Nothing to replace.\nThe area to replace must be selected, which the find feature already does automatically.')

        else:
            self.editor.replace(s1, s2, self.replacewith)

    def _replace_all(self):
        """
        XXX Not working XXX
        """

        while True:
            first_index, last_index = self.__n(0.0)

            if not first_index or not last_index:
                break

            self.editor.replace(first_index, last_index, self.replacewith)

    def _mark_matches(self):
        """
        Internal function
        """

        self.editor.tag_remove('found', 0.0, END)

        if not self.pattern:
            mb.showwarning(self.lang[1], "Cannot mark occurences of an empty pattern in the editor!")
            return

        while True:
            first_index, last_index = self.__n(0.0)

            if not first_index or not last_index:
                break

            self.editor.tag_add('found', first_index, last_index)

    def _find(self, direction: Literal['prev', 'next']):
        self.editor.tag_remove(SEL, 0.0, END)

        if not self.pattern:
            mb.showwarning(self.lang[1], self.lang[348])
            return

        match direction:
            case 'next':
                first_index, last_index = self.__n()

            case 'prev':
                first_index, last_index = self.__p()

            case _:
                raise ValueError('must be next/prev')

        self.editor.mark_set(INSERT, last_index if direction == 'next' else first_index)
        self.editor.tag_add(SEL, first_index, last_index)
        self.rf()
        self.editor.see(INSERT)

    def __n(self, ind: str | float = INSERT) -> tuple[str | None, str | None]:
        first_index = self.editor.search(self.pattern, ind, END, True, False, self.isexact, self.regexp, self.nocasing)

        if not first_index:
            mb.showwarning(self.lang[1], self.lang[349])
            return None, None

        first_index = self.editor.index(first_index)
        last_index = first_index

        for _ in range(len(self.pattern)):
            index_iter = last_index.split('.')
            line_index = int(index_iter[1]) + 1

            last_index = '.'.join((index_iter[0], str(line_index)))

        return first_index, last_index

    def __p(self) -> tuple[str | None, str | None]:
        first_index = self.editor.search(self.pattern, INSERT, 0.0, False, True, self.isexact, self.regexp, self.nocasing)

        if not first_index:
            mb.showwarning(self.lang[1], self.lang[350])
            return None, None

        first_index = self.editor.index(first_index)
        last_index = first_index

        for _ in range(len(self.pattern)):
            index_iter = last_index.split('.')
            line_index = int(index_iter[1]) + 1

            last_index = '.'.join((index_iter[0], str(line_index)))

        return first_index, last_index

    def return_focus(self):
        self.editor.focus_set()

    rf = return_focus

    @property
    def lang(self) -> list | tuple:
        if isinstance(self._exps, list):
            return self._exps.copy()

        return self._exps

    @property
    def regexp(self) -> bool:
        return self._regexp

    @property
    def pattern(self) -> str:
        return self._E1.get()

    @property
    def replacewith(self) -> str:
        return self._E2.get()

    @property
    def isexact(self) -> bool:
        return bool(self._EXACT.get())

    @property
    def nocasing(self) -> bool:
        return not bool(self._CASING.get())
