# editor.py

# [*] Catching too general exception
# pylint: disable=W0718

# [*] Attribute defined outside init
# pylint: disable=W0201

# [*] Pointless string statement
# pylint: disable=W0105

# [i] General imports
from typing import Any, Literal, Iterable
import sys

# [i] Tkinter imports
from tkinter import Misc, END, WORD, INSERT, SEL, SEL_FIRST, SEL_LAST, Toplevel, IntVar
from tkinter.ttk import Checkbutton, Button, Frame, Label, Entry
from tkinter.scrolledtext import ScrolledText as _ScrolledText
from tkinter.font import Font
from tkinter import messagebox as mb


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
        self._wrapline = char_level
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

        except Exception:
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
    def __init__(self, master: Misc | None = None, widget: WriterClassicEditor | None = None, regexp: bool = False, lang_exps: Iterable[str] | None = None, ico: str | None = None, **kwargs) -> None:
        if not isinstance(lang_exps, (list, tuple)):
            raise ValueError('lang expressions must be tuple or list')

        if not widget:
            raise TypeError('a widget must be specified and match type WriterClassicEditor')

        self._regexp = regexp
        self._exps = lang_exps

        self._MARKED: bool = False
        
        widget.tag_configure('found', background='blue', foreground='white', font=Font(weight='bold', slant='roman', overstrike=False, underline=True))
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
        # /-/ self._F3 = Frame(widget)
        # /-/ self._F4 = Frame(widget)
        # /-/ self._B3 = Button(widget, text='Mark all matches', command=self._mark_matches)

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

        self._REPLACE = IntVar(widget, value=0)

        '''
        # [!] Removed until fixed
        self._C3 = Checkbutton(self._F3, text='Replace: ', variable=self._REPLACE, command=self._replace_swap)
        self._E2 = Entry(self._F3, state=DISABLED)

        self._B1 = Button(self._F4, text='Replace', state=DISABLED)
        self._B2 = Button(self._F4, text='Replace All', state=DISABLED)
        '''

        # [*] Frame 1 content
        self._L1.grid(column=0, row=0)
        self._E1.grid(column=1, row=0)
        self._PREVBUTT.grid(column=2, row=0)
        self._NEXTBUTT.grid(column=3, row=0)
        
        # [*] Frame 2 content
        # /-/ self._C1.pack()
        self._C2.pack()
        
        # [*] Frame 3 content (currently, nothing)
        '''
        self._C3.grid(column=0, row=0)
        self._E2.grid(column=1, row=0)
        '''
        
        # [*] Frame 4 content (currently, nothing)
        '''
        self._B1.grid(column=0, row=0)
        self._B2.grid(column=1, row=0)
        '''
        
        # [*] super() / window content
        self._F1.pack()
        self._F2.pack()
        # /-/ self._F3.pack()
        # /-/ self._F4.pack()
        # /-/ self._B3.pack()


    # [!!] Replace method not working
    # [!] Doesn't replace anything
    """
    def _replace(self):
        \"""
        XXX Not working XXX
        \"""
        
        s1, s2 = None, None
        
        try:
            s1, s2 = SEL_FIRST, SEL_LAST
            
        except Exception:
            mb.showerror(self.lang, 'Nothing to replace.\nThe area to replace must be selected, which the find feature already does automatically.')
        
        else:            
            self.editor.replace(s1, s2, self.replacewith)
    """
            
    
    # [!] Not working becuase it relies on the replace method, which is not working
    # [!?] It might work or might fail just like 'Mark all occurences'
    """
    def _replace_all(self):
        \"""
        XXX Not working XXX
        \"""
        
        cur_index = "0.0"
        
        while True:
            a = self.__n(cur_index)
            
            if a:
                mb.showwarning(self.lang[1], "Replaced all occurences.")
                
            cur_index = INSERT
            
            self._replace()
    """
            

    # [!!] Not working, will be isolated from the UI
    # [!] I think I messed up and made this an infinite loop somehow
    def _mark_matches(self):
        """
        XXX Not working XXX
        """
        
        self.editor.tag_remove('found', 0.0, END)
        
        if not self.pattern:
            mb.showwarning(self.lang[1], "Cannot mark occurences of an empty pattern in the editor!")
            return
        
        while True:
            first_index = self.editor.search(self.pattern, 0.0, END, True, False, self.isexact, self.regexp, self.nocasing)
        
            if not first_index:
                mb.showinfo(self.lang[1], 'Done!')
                break
            
            first_index = self.editor.index(first_index)
            last_index = first_index
            
            for _ in range(len(self.pattern)):
                index_iter = last_index.split('.')
                line_index = int(index_iter[1]) + 1
                
                last_index = '.'.join((index_iter[0], str(line_index)))
            
            self.editor.tag_add('found', first_index, last_index)

    '''
    # [!] Not working and not necessary rn
    def _replace_swap(self):
        for i in (self._E2, self._B1, self._B2):            
            match i.__getitem__('state'):
                case 'normal' | 'active':
                    i.configure(state=DISABLED)
    
                case 'disabled':
                    i.configure(state=NORMAL)
                    
                case _:
                    i.configure(state=DISABLED)
                    
            if i.__getitem__('state') == 'normal':
                i.configure(state='disabled')
                
            else:
                i.configure(state='normal')
    '''

    def _find(self, direction: Literal['prev', 'next']):
        self.editor.tag_remove(SEL, 0.0, END)
        
        if not self.pattern:
            mb.showwarning(self.lang[1], self.lang[348])
            return
        
        match direction:
            case 'next':
                self.__n()
            
            case 'prev':
                self.__p()
            
            case _:
                raise ValueError('must be next/prev')
            
        self.rf()
        

    def __n(self, ind: str | float = INSERT) -> Literal[True] | None:        
        first_index = self.editor.search(self.pattern, ind, END, True, False, self.isexact, self.regexp, self.nocasing)
        
        if not first_index:
            mb.showwarning(self.lang[1], self.lang[349])
            return True
        
        first_index = self.editor.index(first_index)
        last_index = first_index
        
        for _ in range(len(self.pattern)):
            index_iter = last_index.split('.')
            line_index = int(index_iter[1]) + 1
            
            last_index = '.'.join((index_iter[0], str(line_index)))
        
        self.editor.mark_set(INSERT, last_index)
        self.editor.tag_add(SEL, first_index, last_index)
        self.rf()
        self.editor.see(INSERT)
        
    
    def __p(self):
        first_index = self.editor.search(self.pattern, INSERT, 0.0, False, True, self.isexact, self.regexp, self.nocasing)
        
        if not first_index:
            mb.showwarning(self.lang[1], self.lang[350])
            return
        
        first_index = self.editor.index(first_index)
        last_index = first_index
        
        for _ in range(len(self.pattern)):
            index_iter = last_index.split('.')
            line_index = int(index_iter[1]) + 1
            
            last_index = '.'.join((index_iter[0], str(line_index)))
        
        self.editor.mark_set(INSERT, first_index)
        self.editor.tag_add(SEL, first_index, last_index)
        self.rf()
        self.editor.see(INSERT)
                

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
    
    
    '''
    @property
    def replacewith(self) -> str | Literal[False]:
        if not self.replace_on:
            return False
        
        return self._E2.get()
    '''


    @property
    def isexact(self) -> bool:
        return bool(self._EXACT.get())
    
    
    @property
    def nocasing(self) -> bool:
        return not bool(self._CASING.get())
    
    
    @property
    def replace_on(self) -> bool:
        return bool(self._REPLACE.get())
