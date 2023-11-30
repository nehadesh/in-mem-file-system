# File System

An in-memory filesystem built in Python! This is a simplified file system that supports storing both files and
directories in-memory. The UI is a terminal interface through which a user can input familiar file system commands to create/read/update/delete files and directories.

## Setup Instructions

Open up a terminal window. Clone this repository and navigate into the repo.

1. Do you have python3 installed? `python3 --version`.

- No? Install python on your local machine `brew install python`
- I used Python 3.9.6 for this project

2. Create a virtual environment to install requirements in `python3 -m venv file_system_venv`

3. Activate the virtual environment `source file_system_venv/bin/activate`

4. Install requirements `pip install -r requirements.txt`

5. Run the program `python3 src/main.py`

## Implementation Details

I chose to use a sorted key tree structure to store the file system.

- Offers quick access to access/modify/delete children of a directory
- One can iterate/ access keys sorted by default - rather than needing to sort before returning output.

The main entities or relevant classes include:

- **FileSystem**: The overall wrapper around the tree structure, that keeps track of the pwd, and the root of the tree.
- **Directory**: A node in the tree structure that can have multiple child directories. Each directory can also store multiple files. This is implemented by storing two dictionaries (with sorted keys) on each Directory. One for files, and one for directories. One can navigate, lookup and modify child directories quickly with this HashMap tree structure. Directories also maintain links to the parent so one can traverse back up the tree easily.
- **File**: A file stores string content and is nested within one of the directory nodes in the tree. It can be read from, written to and moved around within the file system.
- **CommandCenter**: This class handles functional execution and manipulation of the overall file system. It also handles error handling, command evaluation, and command validation.

### Implementation Choices

- Resolving naming conflicts when moving or adding files/directories - recursively add "\_copy" to the name of the file / directory until it is unique
- Path to pwd is a calculated field that updates whenever the parent changes

## Command Implementation

- `mkdir` [Create a directory]
  - Usage: `mkdir <directory_name>`
  - Example: `mkdir folder` - Creates a directory called "folder" in the current directory (initially root)
  - Implementation: Adds a child directory to the sorted dictionary by name for the current directory.
- `cd` [Change current directory]
  - Usage: `cd <directory_name>`
  - Example: `cd folder`, `cd ..`, `cd .`, `cd ~`
- `pwd` [Path to current directory]
  - Usage: `pwd`
- `ls` [List files and directories in pwd]
  - Usage: `ls`
- `rmdir` [Delete directory in pwd]
  - Usage: `rmdir <directory_name>`
  - Example: `rmdir folder`
- `rm` [Delete file in pwd]
  - Usage: `rm <file_name>`
  - Example: `rm hello.txt`
- `touch` [Create a file in pwd]
  - Usage: `touch <file_name>`
  - Example: `touch hello.txt`
- `write` [Write to/ create file in pwd with content]
  - Usage: `write <file_name>.txt "<content>"`
  - Example: `write hello.txt "hello world"`
- `read` [Output file contents to terminal]
  - Usage: `read <file_name>.txt`
  - Example: `read hello.txt`
- `find` [Outputs files/directories that match the search input]
  - Usage: `find <file_name>.txt` or `find <directory_name>`
  - Example: `find hello.txt` or `find folder`
- `mv` [Moves files/directories from current directory to specified child directory]
  - Usage: `mv <file_name>.txt <dir_name>` or `mv <directory_name> <dir_name>`
  - Example: `mv hello.txt folder` or `mv folder another_folder`
- `explore` [Pretty print the file system tree from the current working directory onwards]
  - Usage: `explore`

## Future Improvements

- It wouldn't be hard to add absolute paths and operate on those.
  - We could traverse the file system tree one folder in the path at a time until a part of the path is not found/ until we reach the folder/file we're looking for.
  - If we return a reference to the file it would be easy to operate on it. For example we could `cd` into an absolute path to a folder by changing the `pwd` to point to it.
- User auth rules would also be relatively easy to add. We could assume a set of auth rules by default (read-only) and then for each file or directory we could add a map for user auth rules. Lookup by username before we let users write to file/ read from file for specific permissions.
