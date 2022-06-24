# Dont-Get-Expelled - The Batory Game (Beta)

# Installation

Here is an instruction on how
to install the game step-by-step.

<details>
<summary><b>Step-by-step installation</b></summary>

## Install the game

When downloading materials to your laptop, it is easiest to download the entire repository.
To do this, go to the GitHub page for the game, click on the green Code button, then download the repository as a ZIP file.

![github installation](https://raw.githubusercontent.com/TableFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/install_repo.png)

### Unzip the game

Use your favorite unzip tool to unzip the game files onto your computer.

### Install Python (if not already installed)

Go to Python's website (<https://www.python.org>), then **Downloads** section and
click the *Download* button. Save the installation file and open it. Follow instructions
of the Python installer. **Make sure that the *add Python to Path* box is checked, otherwise you will have to do several more things you don't want to do** (Forgot to do it anyway? See the Q&A section for instructions on how to fix it).
![python and path](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/python_install.png)

### Install Python libraries

*Don't Get Expelled!* needs several important files to run properly. In order to install them:

1. Go to *Start*, find the search box and type *cmd*, then press Enter.
2. You should see something like this
![commandline](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/cmd.png)
3. Type the following lines:

- `python -m pip install --user pygame` and press Enter.
- `python -m pip install --user pytmx` and press Enter again.

Make sure to type in exactly these, without any typos. After pressing Enter both times, you should see something like this:

![instaling libraries](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/libs.png)

4. Close the black window

## To run the game you need to double click on the 'dontgetexpelled.py' file  in ../%GAMEDIRECTORY%/gamefiles/dontgetexpelled.py


## :question: Q&A


- <details><summary>You don't have the latest version of the game:</summary>

    If you are having trouble running the game, or see an error message saying that the game is out of date (look up), you can try to update the game by repeating the process form the installation tab.
  </details>

- <details><summary>You've forgotten to add Python to PATH:</summary>

    1. Go to *Start*, find the search box, type *python*
    2. You should see something like this:
    ![finding python](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/finding_python.png)
    3. Find *Python 3.9 (64-bit)* (the numbers are not important at all - it
    might be 3.10 (32-bit) or whatever else, depending on the version of Python
    on your computer) and **right-click** it
    4. Click *Otwórz lokalizację pliku*
    5. You should see something like this:
    ![Python lnk dir](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/python_env.png)
    (if instead you see something like in point 7., skip point 6.)
    6. Repeat steps 3. and 4.
    7. You should see something like this:
    ![Python environment](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/python_env2.png)
    8. Copy the path above (highlighted on blue)
    9. Go again to *Start*, find the search box and type *zmienne środowiskowe* (english: *environmental variables*)
    10. You should see this:
    ![Advanced system settings](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/adv_sys_set.png)
    11. Click *Zmienne środowiskowe...*
    12. You should see something like this:
    ![env vars](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/envars.png)
    :exclamation: **WARNING: Be careful not to delete anything here, or you might damage your operating system!** :exclamation:
    13. In the top box, find *Path* (highlighted on blue) and **double-click** it
    14. See something like this:
    ![PATH](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/PATH.png)
    15. Click *Nowy*
    16. Paste the path from point 8.
    17. Click *OK*
    18. Click *OK* again
    19. ...and yet again (you should have got rid of all tabs opened from point 9 and on)
    20. You have successfully added Python to PATH. Phew, that was easy!
  </details>
  </details>

## Game Manual file

Welcome! This manual should be an in-game feature but the **programmers** are lazy sleaze bags so here comes a markdown file!

## Main objective

Your main task in this game is to survive several days in Batory without ending up expelled for crimes against humanity (in this beta version there is only one day). There will be many opportunities to do something bad: doing so will make you closer to being expelled!

# Some mechanics :wrench:

## Controls

- :video_game: In game:
  - **Arrow Keys** – Move

  - **SHIFT**– Sprint

  - **I** – Toggle Inventory

  - **E** – Interact (Enter a dialogue with an NPC or pick up an item)

  - **ESC** – Toggle Saving Menu and exit from any other window

  - **M** – Minimap

- :phone:  In dialogue with NPC:
  - **Arrow Keys (up and down)** – Change Selection

  - **ENTER** – Select Answer

## The Fault Counter :exclamation:

This is the Fault Counter – it shows how many bad things you can commit before saying goodbye to the school. Every time you commit a fault, this counter will decrease (you will be notified by an unpleasant sound). If it reaches zero – Bye! Bye!

![the corner img](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/faults.png)

Some faults are significant enough to subtract **more than one point** from this counter, so can put the skids under you faster. The most serious crimes can even get you expelled instantly! But do not worry – helping others selflessly is a valued quality in this school! There are some deeds you can commit that can **increase** the Fault Counter, that is to avert you from expulsion.

## Quests  :question:

Quests in this game are divided into 2 types:

- **main quests** you need to complete in order to win the level
- **side quests** – not obligatory but they may help you one way or another.

Both types of quests are displayed in the bottom-left corner of the screen:
![Quests](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/quests.png)

## NPCs :bust_in_silhouette:

There are many Non-Person Characters in the game; their main (and only) task is
to talk to you. Some NPCs you can talk to instantly, any-time; another ones will only
want to talk after you complete certain actions; finally, there are freaks who will remain silent no matter what you do.
So don't get mad if you spam E near an NPC and nothing happens - it's not a bug, it's a feature :wink:

## Save system :heavy_check_mark:

This game has a save system - any time you want, you can save the game (press ESC and click the 'Save' button), close it,
get some rest (get a life you nerd!) and then load it from main menu and continue
playing from the very point you have finished. If you don't have a game saved,
you cannot load it, so please don't spam the 'Load Game' button like a maniac.

Keep in mind that there is no auto-save on quit; if you forget to save and close the game, losing all progress,
this is entirely your problem.

Due to technical issues, saving game in the very top-left corner of the screen
will make you unable to load it. So don't do it. Or do. But never try.

## Inventory  :hand:

![inventory](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/inventory.png)

This is your inventory – should you not know, you store your items here.
The slots are divided into two types:

- **storage slots** (the two rows of eight slots)
- **drop slot** (the single slot on the bottom).

You can move your items freely between the storage slots by **clicking** on them and **dragging** them to target slot.
> In order to throw an item out of the inventory, put it in the drop slot.

## Minimap  :round_pushpin:

![minimap](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/manual_images/minimap.png)

This is the Minimap. It shows the entire map with all rooms and NPC marked on it. Use it, if you do not know where to go.

##

[^1]:
 **TABEFLIP STUDIO** :laughing:

![studio](https://raw.githubusercontent.com/TabeFlipStudio/Dont-Get-Expelled/main/gamefiles/images/logo.jpeg)
