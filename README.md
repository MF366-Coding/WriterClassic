# Writer Classic
Writer Classic's GitHub repository.

![WriterClassic's New Logo, from v7.0.1](/data/logo.png?raw=true "WriterClassic Logo")

Writer Classic is a rather small Python project that brings to the user a whole new text editing experience. :thinking:

## Welcome...
...and thanks for visiting this repository. :heart:

I also would love if you waste some time testing Writer Classic or just exploring this GitHub repository.

## Important info
**VERY IMPORTANT!**
- LICENSE -> https://github.com/MF366-Coding/WriterClassic/blob/main/LICENSE

# Installing Writer Classic
To install Writer, you can choose between 2 ways of installing.

## Stable Releases
Choose this instalation method for a non-crashing environment.

### 1. Downloading
Go to https://github.com/MF366-Coding/WriterClassic/releases/latest to get the latest release and download the <code>*.zip</code> file.

### 2. Extraction
With the file on your computer, extract it to a folder you have or to the same location of the zipped file.

All files and folders inside the zipped one **must** be on the same location!

### 3. Running the program
Go to the right folder.

For MacOS or Windows use:
```python3 WriterClassic.py```

...and you can now use Writer Classic.

For Windows do:
```python WriterClassic.py```

This app only runs os Python 3!

##### Additional Setup: Start Menu Shortcut (Windows)
**NOTE:** *this doesn't reffer to the "Pin in Start Menu", however feel free to use that one if you prefer.*

To make a Start Menu shortcut, you must follow the following steps:

1. Open two windows of **File Explorer**.
2. In one of them, go to the location `%AppData%\Microsoft\Windows\Start Menu`. 
3. In the other File Explorer window, go to the folder where you extracted WriterClassic's zipped folder.
4. Now, place the windows side-by-side (not necessary but makes the process a bit easier).
5. Finally, and most important of all, **while holding `Ctrl` and `Shift` at the same time**, grab the `WriterClassic.py` file and throw it into the `StartMenu` folder.
6. You should probably rename the file to "`WriterClassic`" for easier acess, that is, without the file extension (because it's a shortcut - the extension is hidden in Windows by default and is not `*.exe`).
7. You can, afterwards, make shortcuts in Desktop, Pin in Start Menu, Taskbar, as you wish...

## Unstable Releases
Maybe you are a developer who wants acess to the latest update to Writer...

### 1. Clone the repo
Open the Terminal and use:
```git clone https://github.com/MF366-Coding/WriterClassic.git</```

However, that will only work if you have Git installed on your device...

### 2. Running the program
Go to the folder where the repo was cloned.

#### For Linux and MacOS
Use the following command on your commandline:
```python3 WriterClassic.py```

This app only runs os Python 3, so using the command <code>python WriterClassic.py</code> won't work (in Unix based OSes, <code>python</code> is Python 2).

#### For Windows
Follow the steps in [here](https://github.com/MF366-Coding/WriterClassic#additional-setup-start-menu-shortcut) after cloning the repo and getting everything set.

# What do I need to be able to be able to use Writer Classic? :heavy_check_mark:
You need:

* [X] Python 3 (Comes with MacOS and Linux, usually | Requires installation on Windows, unless you use the executable version of WriterClassic)

* [X] tkinter (Python3 Module)

* [X] datetime (Python3 Module - Standard, usually)

* [X] sys (Python3 Module, Standard, usually)

* [X] requests (Python3 Module)

* [X] json (Python3 Module - Standard, usually)

* [X] the `data` folder that comes with WriterClassic

* [X] the `config` folder that comes with WriterClassic

## Small information
If you want to redistribute this software, you need its LICENSE: this is **mandatory**!

# Let me know of any bug you find :desktop_computer:
If you found a bug, please tell me the details by creating a new Issue in this Repository.

# Help :question:
Here, you can find all sorts of help topics about Writer Classic.

## Features
### Open :open_file_folder:
Writer Classic is a basic text editor yet very fun to use and offering a lot of features while it's development is happening at a very fast pace.  
With Writer Classic you can open files of type (in no particular order):
  
* text
* python
* markdown
* html
* javascript
* ini
* desktop
* xml

... and much more!

### Edit :memo:
You can make changes to text files, python files, markdown files and save them, either with new name and extension or replacing existent files.

### Looks :paintbrush:
You can choose from several themes and change interface / window size. So taht you will always be confortable and use Writer Classic the way you want and fits your taste and feelings.


#### Change the font (type and size)
Now, you can change font type and size (only affects the editor - not the edited file).

You can find this feature in the *Appearence* settings.

Once again, thank you for ckecking out this repository. :+1:

### Plugins :heavy_plus_sign:
Writer Classic author and programmer is always developing new plugins in order to make this simple editor more and more powerful and in line with the features you most use and wish. For the time being you can choose from:

* **Notepad** (you can take notes aside what you're writing and editing)
* **Clock** (because it's always useful to know if it's time to start coding)
* **File Wiper** (wipes a file you pick - does not delete it)

### Settings :hammer_and_wrench:
Within settings you can choose from several languages. For now it's only available in:

- English

- Portuguese (european and brazilian)

- French

- Spanish

- Italian

- Slovak

### Information :information_source:
Here you can find help, some about information and the links for the official repo and website.

Stay up to date, don't forget to read what's going on with Writer Classic.

### Command Menu
You can press **Ctrl + W** (check the Shotcuts area for more info) to open this **hidden** feature.

In here, you can type a command and click 'OK' and something will happen.

Available commands:

- **open** or **openfile** - Opens the 'Open a file to read' dialog
- **about** - Opens the 'About' dialog
- **help** - Opens the Help at GitHub
- **fun** or **egg** - Opens the Super Secret Easter Egg (a.k.a *SSEE*)
- **data** - Opens the 'Who made this app?' dialog (hint: it was me LMAO)
- **exit** or **quit** - Shows the 'Confirm exit' dialog
- **clear** - Opens the 'Pick a file to erase' dialog
- **newfile** - Creates a new file
- **save** - Shows the 'Save as' dialog
- **clock open** - Opens the Clock Plugin
- **font family** - Shows the 'Pick a font family' dialog
- **font size** - Shows the 'Pick a font size' dialog
- **ragequit** - Kills the app without confirmation **(NOT RECOMMENDED)**
- **repo** - Opens the GitHub repo
- **notes** - Opens the 'Notes' Plugin
- **win size** - Shows the 'Pick window dimensions/size' dialog

In case you don't pick any of these, you'll just get an error.

## Shortcuts :keyboard:
### Useful shortcuts
You can use some useful shortcuts instead of menu itens to use Writer Classic faster.
All of those make use of control key plus another key so that you have to press both at once. **Ctrl** stands for control key. Here are some of the most useful shortcuts available:  

* __Ctrl + S__ - Save the file/save as :floppy_disk:
* __Ctrl + O__ - Open file :open_file_folder:
* __Ctrl + W__ - Opens the Command Menu 💻️
* __Ctrl + L__ - Changes to light mode :sunny:
* __CTRL + D__ - Changes to dark mode :crescent_moon:
* __Ctrl + G__ - Chooses default window size (600x400 px) :desktop_computer:
* __Ctrl + H__ - Leads you to help :question:
* __Ctrl + A__ - Opens about dialog :information_source:
* __Ctrl + R__ - Opens the clock plugin :clock2:

## New stuff
### Need some help?
Don't have a web browser open? Need to search something? Search directly from WriterClassic using one of the available Search Engines:
- Google
- Bing
- Ecosia
- DuckDuckGo
- Yahoo! 
- StackOverflow

### Wanna listen to some tunes?
Maybe you just want to relax while listening to music... 

You can do that using... 
- YouTube
- SoundCloud (v7.0.1+) 

### A fresh look (v7.0.1+)
The menu bug has been fixed. They look **way** better now! 

New logo for WriterClassic, truly amazing! 

An exclusive color theme just for Windows, with the official colors from the Windows 10 PowerShell. 

Light and Dark themes have been fixed, they look better now. 

> ## Thanks for using WriterClassic! :heart:
