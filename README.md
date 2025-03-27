# Notepad++ Bingo Board Generator

This Notepad++ script takes each line of a text file and turns it into a randomly shuffled Bingo board. It uses the PythonScript plugin and supports automatic padding and a center "FREE SPACE".

---

## 📦 Features

- Converts any list of text lines into a Bingo board
- Automatically inserts a "FREE SPACE" in the center (for odd-sized grids)
- Pads with blank squares if there aren't enough lines
- Simple to run from Notepad++ using the PythonScript plugin

---

## ⚙️ Requirements

- [Notepad++](https://notepad-plus-plus.org/)
- PythonScript Plugin (installed via Notepad++ Plugin Manager)

---

## 🧑‍💻 Installation & Usage

### 1. Install PythonScript Plugin

1. Open Notepad++
2. Go to **Plugins > Plugins Admin**
3. Check **PythonScript** and click **Install**
4. Restart Notepad++ if prompted

### 2. Add the Bingo Script

1. Go to **Plugins > PythonScript > New Script**
2. Name the script: `MakeBingoBoard.py`
3. Paste the code from `MakeBingoBoard.py` in this repo

### 3. Use the Script
1. Open a text file with your Bingo items (one item per line)
2. Go to Plugins > PythonScript > Scripts > MakeBingoBoard
3. Your file will be replaced with a formatted Bingo board

