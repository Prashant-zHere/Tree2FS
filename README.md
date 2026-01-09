# Tree2FS

**Tree2FS** is a simple Python tool that reads a `.txt` file describing a project directory structure and automatically creates the corresponding **folders and files** on your system.

Perfect for quickly scaffolding new projects, replicating existing structures, or setting up development environments from documentation.

## Features

- 🏗️ Create complete directory structures from text files
- 📁 Supports nested folders and files
- 🔧 Works on **Linux, macOS, and Windows**
- 📄 Creates empty files as placeholders
- 🎯 Simple, lightweight, and easy to use
- ✅ Handles tree-style formatting with box drawing characters

## Installation

No installation required! Just download `structure.py` and run it with Python 3.

```bash
git clone <repository-url>
cd tree2fs
```

## Usage

1. Create a text file with your desired directory structure
2. Run the script:

```bash
python structure.py
```

3. Enter the path to your structure file when prompted
4. The tool will create the directory structure in the current directory

## Input File Format

The text file should describe your project structure using tree-style formatting:

- **Folders** should end with `/`
- **Files** should have proper extensions (`.py`, `.js`, `.md`, etc.)
- Use tree characters (`├──`, `└──`, `│`) for visual structure

### Example Structure File

```
my_project/
├── src/
│   ├── main.py
│   ├── utils/
│   │   └── helpers.py
│   └── config.json
├── tests/
│   └── test_main.py
├── docs/
│   └── README.md
└── requirements.txt
```

This will create:
```
my_project/
├── src/
│   ├── main.py (empty file)
│   ├── utils/
│   │   └── helpers.py (empty file)
│   └── config.json (empty file)
├── tests/
│   └── test_main.py (empty file)
├── docs/
│   └── README.md (empty file)
└── requirements.txt (empty file)
```

## How It Works

1. **Parses** the input file line by line
2. **Analyzes** indentation levels using tree characters
3. **Creates** directories for items ending with `/`
4. **Creates** empty files for items with extensions
5. **Maintains** the hierarchical structure using a path stack

## Requirements

- Python 3.x
- No external dependencies

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve Tree2FS!


