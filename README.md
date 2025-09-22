# PyTerm - Python-Based Command Terminal

## Overview

PyTerm is a beginner-friendly Python-based terminal emulator that replicates the behavior of a Unix-like shell. It supports common file and directory operations, command history, auto-completion, natural language queries (via GPT), and optional system monitoring.

This project is ideal for learning how shells work internally while practicing Python file system operations, subprocess management, and basic AI integration.

---

## Features

* **File & Directory Commands**: `ls`, `pwd`, `cd`, `mkdir`, `rm`, `cat`, `touch`, `cp`, `mv`
* **Utility Commands**: `echo`, `clear`, `whoami`, `date`, `uptime`
* **Session Management**: `history`, `help`, `exit` / `quit`
* **Optional Monitoring** (requires `psutil`): `cpu`, `mem`
* **Natural Language Queries**: Type `nl: <your request>` to translate into a shell command using GPT (requires API key)
* **Auto-completion & History**: Supports tab-completion and command history via `readline`

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/pyterm.git
   cd pyterm
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   *If you want system monitoring commands (`cpu`, `mem`):*

   ```bash
   pip install psutil
   ```

---

## Usage

Run the terminal with:

```bash
python pyterm.py
```

Example session:

```bash
PyTerm> pwd
/home/user
PyTerm> mkdir test_folder
PyTerm> cd test_folder
PyTerm> touch file.txt
PyTerm> echo "hello" > file.txt
PyTerm> cat file.txt
hello
PyTerm> history
PyTerm> nl: create a folder called logs
[nl ->] mkdir logs
```

---

## GPT Integration (Natural Language Commands)

1. Install OpenAI client:

   ```bash
   pip install openai
   ```

2. Add your API key as an environment variable:

   ```bash
   export OPENAI_API_KEY="your_api_key_here"   # Linux/macOS
   setx OPENAI_API_KEY "your_api_key_here"     # Windows
   ```

3. Use natural language in the terminal:

   ```bash
   PyTerm> nl: move file report.txt to archive/
   [nl ->] mv report.txt archive/
   ```

---

## Optional CLI Arguments

* `--no-readline` : Disable readline (auto-completion/history)
* `--history-file <path>` : Specify a custom history file path

---

## Project Structure

```
pyterm/
├── pyterm.py        # Main terminal implementation
├── requirements.txt # Dependencies list
└── README.md        # Project documentation
```

---

## Requirements

* Python 3.7+
* `psutil` (optional, for monitoring)
* `openai` (optional, for GPT natural language commands)

---

## Future Improvements

* Web-based UI (Flask/FastAPI)
* Sandbox execution environment for safety
* More advanced AI-based natural language support

---

## License

MIT License © 2025
