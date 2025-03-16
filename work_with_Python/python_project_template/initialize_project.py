"""
This script creates the my_new_project directory with the specified subdirectories and files.
It can be useful when you are starting new projects, ensuring a consistent and organized setup:

my_new_project_YYYYMMDD/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_main.py
│   └── test_utils.py
└── docs/
    ├── readme.md
    └── changelog.md

"""

import os
from pathlib import Path
from datetime import datetime as dt

# define the directory structure and file names
project_structure = {
    "src": ["main.py", "utils.py"],
    "tests": ["test_main.py", "test_utils.py"],
    "docs": ["readme.md", "changelog.md"]
}


# function to create directories and files
def create_project_structure(base_path: str, structure: dict) -> None:
    base_path = Path(base_path)

    for folder, files in structure.items():
        folder_path = base_path / folder
        try:
            folder_path.mkdir(parents=True, exist_ok=True)
            print(f"Folder {folder_path} created successfully.")
        except Exception as e:
            print(f"Failed to create folder {folder_path}, the error: {e}")
            continue

        for file in files:
            file_path = folder_path / file
            try:
                file_path.touch(exist_ok=True)
                print(f"File {file_path} created successfully.")
            except Exception as e:
                print(f"Failed to create file {file_path}, the error: {e}")


# define today's dat as YYYY-MM-DD
today = dt.datetime.today().strftime('%Y-%m-%d')

# specify the base path for the new project
base_path = f"new_project_{today}"

# create the project structure
create_project_structure(base_path, project_structure)

print(" :) ")
