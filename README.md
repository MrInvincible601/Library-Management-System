# Library Management System

A simple command-line library program written in Python.

## Features

- Add a book
- Search for a book by title or author
- Issue a book
- Return a book
- Exit the program

## Requirements

- Python 3.x
- No external libraries are required

## How to Run

1. Open the project folder in VS Code or a terminal.
2. Open the terminal in the project folder.
3. Run the following command:

```bash
python main.py
```

## How to Use

After starting the program, select an option from the menu:

1. Add Book - Enter the book title and author.
2. Search - Enter a keyword to search by title or author.
3. Issue - Enter the exact title of a book to issue it.
4. Return - Enter the exact title of a book to return it.
5. Exit - Close the program.

## Project Structure

```text
Library_Helper_Project/
├── main.py
└── README.md
```

## Notes

The program stores the books in memory while it is running. The data is reset when the program is closed.
