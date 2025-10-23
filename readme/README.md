

# Pig Dice Game

A Python terminal-based implementation of the classic Pig Dice Game.  
Play against another player or a computer with adjustable difficulty levels.  
Includes persistent high scores, cheat functionality, and a menu-driven interface.

---

## 🎮 Features

- Single-player mode (Player vs Computer)
- Two-player mode (Player vs Player)
- Persistent high scores (`data/scores.json`)
- Cheat feature for testing
- Computer AI with configurable difficulty
- Menu system with options:
  - Play Single Player
  - Play Two Players
  - Show Rules
  - Quit
- Full terminal graphics using UTF-8 characters
- Resilient to invalid user input

---


### Player Naming and Persistent Scores
- Each player can enter a custom name when starting the game.
- Names can be changed mid-game; the high score and statistics are preserved under the original player record.

### Cheat Mode
During a turn, press `c` instead of `r` or `h` to activate cheat mode.
This rolls a guaranteed high number (e.g., 6) for testing purposes.



### Computer AI
- The computer opponent has configurable difficulty levels: `easy`, `normal`, `hard`.
- Difficulty affects the computer’s strategy for rolling or holding.
- Select difficulty at the start of a single-player game.



### Restarting or Quitting
- You can quit the current game at any time via the menu.
- Restart the game from the main menu without losing high scores.


## 🏁 Getting Started

### Prerequisites

- Python 3.8 or newer
- `pip` package manager

### Installation

1. Clone the repository:


git clone https://github.com/HusseinH101/Project1.git
cd Project1

---
### How to run program:

python main.py


---

### Rules of the game


1. Roll the dice and collect points each turn

2. If you roll a 1, you lose your current turn points

3. You can choose to "hold" to save points and end your turn

4. First player to reach 100 points wins

5. Cheat option allows testing by rolling a guaranteed high number

---

## Advanced



### Project Structure


├─ main.py           # Entry point, runs the menu

├─ game.py           # Game logic and turn handling

├─ player.py         # Player class

├─ bot.py            # ComputerPlayer class and AI

├─ dice.py           # Dice rolling logic

├─ scoreboard.py     # Persistent scores management

├─ data/  # High score storage

├─ test/ # Unittests Folder


├─ Makefile          # Linting target

└─ README.md         # ReadMe


---

### How to run unit tests


## 🧪 Run Tests and Coverage
🔹To run all tests:
```bash
python -m unittest discover -s tests

🔹To measure code coverage:
coverage run -m unittest discover -s tests
coverage report -m

🔹To generate an HTML report:
Coverage HTML

🔹Open the report in your browser:

start htmlcov/index.html #For Windows
open htmlcov/index.html #For macOS


To install all dependencies:
pip install -r requirements.txt

```

### Linting / Code Style
```bash
make lint
```

## Create the virtual environment
make venv

### Activate on Windows
. .venv/Scripts/activate

### Activate on Linux/Mac
. .venv/bin/activate


When you are done you can leave the venv using the command deactivate.


The project uses Sphinx for generating automatic documentation from docstrings in the code.

🔹To create a HMTL documentation use the command:
🔹Make first sure you have sphinx installed, if not use the command:

<< pip install sphinx>> All the dependencies are in requirements.txt. You can install them with:
pip install -r requirements.txt

🔹To see the documentation, use the command: 
make doc 

This command runs sphinx-build to generate dokumentation to the folder:
<< doc/api/build/html >>

🔹To open the documentation open the file:
doc/api/build/html/index.html - make sure to click on the
go live button go see the documentation in your web browser-



## UML Diagrams

The project includes automated UML documentation for class and package structures.  
These diagrams are stored in `doc/uml/` and can be regenerated at any time.

### Regenerate UML Diagrams

1. Ensure you have the required dependencies installed:

```bash
pip install pylint graphviz


To generate:

make uml
```

