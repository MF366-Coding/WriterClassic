# editor.py

# [i] General imports
from typing import Any, Literal

# [i] Tkinter tools
from tkinter import Misc, END, WORD, INSERT, SEL, SEL_FIRST, SEL_LAST
from tkinter.scrolledtext import ScrolledText as _ScrolledText


class WriterClassicEditor(_ScrolledText):
    """
    Provides an editor interface for WriterClassic.
    """
    
    def __init__(self, master: Misc | None = None, **kwargs: Any) -> None:        
        kwargs.update({'wrap': WORD})
        
        self._wrapline = WORD
        self.write = super().insert
        
        super().__init__(master, **kwargs)
    
    
    def get_wrapping(self) -> Literal['none', 'char', 'word']:
        return self._wrapline
    
    
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

