# Writer Classic
Writer Classic's GitHub repository.

![WriterClassic's New Logo, by Norb](/data/logo.png?raw=true "WriterClassic's Logo")

Writer Classic is a rather small Python project that brings to the user a whole new text editing experience. :thinking:

## Welcome...
...and thanks for visiting this repository. :heart:

I also would love if you waste some time testing Writer Classic or just exploring this GitHub repository.

## Important info
**VERY IMPORTANT!**
- LICENSE -> https://github.com/MF366-Coding/WriterClassic/blob/main/LICENSE

# Installing Writer Classic
To install Writer, you can choose between 2 ways of installing.

## 1. Downloading
Go to https://github.com/MF366-Coding/WriterClassic/releases/latest to get the latest release and download the <code>*.zip</code> file.

## 2. Extraction
With the file on your computer, extract it to a folder you have or to the same location of the zipped file.

All files and folders inside the zipped one **must** be on the same location!

## 3. Running the program
Go to the right folder.

### For Linux and MacOS
Use:

```python3 WriterClassic.py```

...and you can now use Writer Classic.

This app only runs os Python 3, so using the command `python WriterClassic.py` won't work (in Unix based OSes, <code>python</code> is Python 2).

### For Windows
For Windows, the setup might be a bit more complicated.

The Python app has been converted into an executable for easier acess.

Download the zipped folder in Releases (only v4.2.1+ have the Windows converted executable).

The zipped folder should contain several folders and *.py files.

Extract **EVERYTHING** to a different folder.

Then run the executable named `WriterClassic.exe`.

Note running the file does **NOT** install any shortcuts or dependencies. You mustn't remove anything from the now extracted folder!

#### Additional Setup: Start Menu Shortcut
**NOTE:** *this doesn't reffer to the "Pin in Start Menu", however feel free to use that one if you prefer.*
To make a Start Menu shortcut, you must follow the following steps:
1. Open two windows of **File Explorer**.
2. In one of them, go to the location `%AppData%\Microsoft\Windows\Start Menu`. 
3. In the other File Explorer window, go to the folder where you extracted WriterClassic's Windows-only zipped folder.
4. Now, place the windows side-by-side (not necessary but makes the process a bit easier).
5. Finally, and most important of all, **while holding `Ctrl` and `Shift` at the same time**, grab the `WriterClassic.exe` file and throw it into the `StartMenu` folder.
6. You should probably rename the file to "`WriterClassic`" for easier acess, that is, without the file extension (because it's a shortcut - the extension is hidden in Windows by default and is not `*.exe`).
7. You can, afterwards, make shortcuts in Desktop, Pin in Start Menu, Taskbar, as you wish...

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

* [X] the `simple_webbrowser` folder that comes with WriterClassic

## Small information
If you want to redistribute this software, you need its LICENSE: this is **mandatory**!

# Let me know of any bug you find :desktop_computer:
If you found a bug, please tell me the details by creating a new Issue in this Repository.

# Help :question:
## Editing
You can do regular file editing like **opening**, **saving** and simply typing!

To open a plain text file, go to **File** > **Open...** and pick the file you want to open.

To save a document, go to **File** > **Save...** and name the file. Pick its location and click Save. Boom!

## Sparkles and sparkles
To change the default window size of WriterClassic, go to **Appearance** > **Window dimensions** and follow the instructions.

To pick a theme, just go to **Appearance** and pick, from Default and Modern themes, the one you like the best.

## Plugins
Enjoy default plugins and custom plugins.

This powerful feature... I'll let you explore it by yourself...

## Internet
The Internet plugin, on the tab next to Plugins...

Search with Google, Ecosia, Bing, Yahoo, YouTube and much more directly from your favorite text editor.

You can also go to an URL.

## Settings and info
Customize your language. Go ahead, pick yours!

Yours isn't available? Consider creating your own custom translation or report it to Issues as an enhancement.

You can also enjoy WriterClassic offline, by just changing one simple setting: Checking for Updates on Startup. If ON, you gotta be online. If OFF, doesn't matter where you are and mostly, if you have internet connection, because WriterClassic won't need it to launch.

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
- **save** - Saves the document
- **save as** - Saves the document as/at...
- **clock open** - Opens the Clock Plugin
- **font family** - Shows the 'Pick a font family' dialog
- **font size** - Shows the 'Pick a font size' dialog
- **ragequit** - Kills the app without confirmation **(NOT RECOMMENDED)**
- **repo** - Opens the GitHub repo
- **notes** - Opens the 'Notes' Plugin
- **win size** - Shows the 'Pick window dimensions/size' dialog

In case you don't pick any of these, you'll just get an error.

## Shortcuts :keyboard:
### Useful shortcuts (v8.3.0+)
You can use some useful shortcuts instead of menu itens to use Writer Classic faster.
All of those make use of control key plus another key so that you have to press both at once. **Ctrl** stands for control key. Here are some of the most useful shortcuts available:  

* __Ctrl + S__ - Save the file :floppy_disk:
* __Ctrl + Z__ - Save as... :floppy_disk:
* __Ctrl + O__ - Open file :open_file_folder:
* __Ctrl + W__ - Opens the Command Menu 💻️
* __Ctrl + L__ - Changes to light mode :sunny:
* __Ctrl + D__ - Changes to dark mode :crescent_moon:
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
- Qwant (v7.0.2+)
- The Internet Archive (v7.0.2+)
- Brave Search (v8.2.0+)

### Wanna listen to some tunes?
Maybe you just want to relax while listening to music... 

You can do that using... 
- YouTube
- SoundCloud (v7.0.1+) 
- Spotify Online (v7.0.4+)

> ## Thanks for using WriterClassic! :heart:
