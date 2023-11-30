from file_system import FileSystem
from directory import Directory
from printer import Printer
from file import File, SUPPORTED_EXTENSION

class CommandCenter:
    """
        A class to handle command execution.

        Attributes:
        -------------
        fs (FileSystem) -> The overall file system to execute commands on.
        printer (Printer) -> The object to print various portions of the tree.
    """
    def __init__(self, fs: FileSystem):
        self.__fs = fs
        self.__printer = Printer()
    
    def execute_command(self, args):
        try:
            if args == None or len(args) < 1:
                return
            
            command = args[0]
            params = None if len(args) == 1 else args[1:]

            if command == "mkdir":
                self._mkdir(params)
            elif command == "cd":
                self._cd(params)
            elif command == "pwd":
                self._pwd(params)
            elif command == "ls":
                self._ls(params)
            elif command == "rmdir":
                self._rmdir(params)
            elif command == "rm":
                self._rm(params)
            elif command == "touch":
                self._touch(params)
            elif command == "write":
                self._write(params)
            elif command == "read":
                self._read(params)
            elif command == "find":
                self._find(params)
            elif command == "mv":
                self._mv(params)
            elif command == "explore":
                self._explore(params)
            elif command == "help":
                self._help(params)
            elif command != None and len(command) != 0:
                raise Exception(f'Unknown command: {command}')
        
        except Exception as error:
            print(error)
    
    def _help(self, params):
        '''
            Displays a key for different commands.
        '''
        if params != None and len(params) > 0:
            raise Exception(f'Incorrect number of parameters, correct usage: help')
      
        print('explore - Visual depiction of file system starting from the current working directory')
        print('mkdir   - Create directory - [mkdir dir_name]')
        print('cd      - Change directory - [cd dir_name | cd .. | cd . | cd ~]')
        print('pwd     - Path to working directory - [pwd]')
        print('ls      - List files/directories in pwd [ls]')
        print('rmdir   - Delete directory in pwd - [rmdir dir_name]')
        print('touch   - Create a file in pwd - [touch file_name.txt]')
        print('write   - Write content to an existing file in pwd (or create it) - [write hello.txt "hello world"]')
        print('rm      - Delete file in pwd - [rm file_name]')
        print('read    - Reads content of file to terminal - [read hello.txt]')
        print('find    - Finds files/directories with matching name - [find hello.txt | find folder]')
        print('mv      - Moves files/directories into specified sub-directory of pwd - [mv hello.txt folder]')

    
    def _mkdir(self, params):
        '''
            Create a new directory in the current working directory.
            If there is a directory already with the same name, it will append "_copy"
            to the name as many times as necessary until it finds no name clashes.

            Usage: mkdir <directory_name>
        '''
        if params == None or len(params) != 1:
            raise Exception('Incorrect number of parameters, correct usage: mkdir <dir_name>')
        
        dir_name = params[0]
        self.__fs.get_pwd().add_directory(Directory(dir_name))

   
    def _cd(self, params):
        '''
            Changes the current working directory to this directory.
            You can only change to a directory within the present working directory
            or to one of the parent, root or current directory.

            Usage:
            - cd <directory_name> - changes pwd to this directory.
            - cd .. - changes pwd to parent directory of the current working directory.
            - cd . - stays in pwd
            - cd ~ - changes pwd to root directory
        '''
        if params == None or len(params) != 1:
            raise Exception('Incorrect number of parameters, correct usage: cd <dir_name>')
        
        dir_name = params[0]
        if dir_name == "..":
            parent_dir = self.__fs.get_pwd().get_parent()
            if parent_dir != None: 
                self.__fs.set_pwd(parent_dir)
        elif dir_name == ".":
            return
        elif dir_name == "~":
            self.__fs.set_pwd(self.__fs.get_root())
        else:
            new_curr_dir = self.__fs.get_pwd().get_directory(dir_name)
            if new_curr_dir == None:
                raise Exception(f'No such directory found: {dir_name}')
            self.__fs.set_pwd(new_curr_dir)

        self.__fs.get_pwd().get_directory(dir_name)
        
    def _pwd(self, params):
        '''
            Returns the path of the current working directory.
            This is a computed field for each directory that is derived 
            from the parent directory. When the parent changes, the path
            gets recomputed.

            Usage: pwd
        '''
        if params != None and len(params) != 0:
            raise Exception('Incorrect number of parameters, correct usage: pwd')
        print(self.__fs.get_pwd().path)
    
    def _ls(self, params):
        '''
            Lists the directories and files in the present working directory.
            
            Usage: ls
        '''
        if params != None and len(params) != 0:
            raise Exception('Incorrect number of parameters, correct usage: ls')
        self.__fs.get_pwd().print_contents()

    def _rmdir(self, params):
        '''
            Deletes directory matching the provided name in the pwd. 
            Also deletes all sub-files and sub-directories.

            Usage: rmdir <directory_name>
        '''
        if params == None or len(params) != 1:
            raise Exception('Incorrect number of parameters, correct usage: rmdir <dir_name>')
        dir_name = params[0]
        success = self.__fs.get_pwd().remove_directory(dir_name)
        if success == False:
            raise Exception(f'No dir found with name: {dir_name}') 

    def _rm(self, params):
        '''
            Deletes a file in the pwd with a matching name.

            Usage: rm <file_name>
        '''
        if params == None or len(params) != 1:
            raise Exception('Incorrect number of parameters, correct usage: rm <file_name>')
        file_name = params[0]
        success = self.__fs.get_pwd().remove_file(file_name)
        if success == False:
            raise Exception(f'No file found with name: {file_name}')            

    def _touch(self, params):
        '''
            Creates a file in the pwd with provided name.
            At the moment, it only allows .txt file type creations.

            Usage: touch <file_name>.txt
        '''
        if params == None or len(params) != 1:
            raise Exception('Incorrect number of parameters, correct usage: touch <file_name>[.txt]')
        
        file_name = params[0]
        self.__fs.get_pwd().add_file(File(name=file_name))
    
    def _write(self, params):
        '''
            Writes provided content to an existing file in the pwd with given name.
            If one does not exist, it creates one and then writes content to the file.

            Usage: write hello.txt "hello world"
        '''
        if params == None or len(params) < 2:
            raise Exception('Incorrect number of parameters, correct usage: write <file_name>[.txt] "<contents>"')
        file_name = params[0]

        content = " ".join(params[1:])
        if not content.startswith('"') or not content.endswith('"'):
            raise Exception('Content must be surrounded by quotes, correct usage: write <file_name>[.txt] "<contents>"')
        
        content = content[1 : len(content) - 1]
        file = self.__fs.get_pwd().get_file(file_name)
        
        if file == None:
            file = self.__fs.get_pwd().add_file(File(name=file_name))
        file.set_content(content)
    
    def _read(self, params):
        '''
            Outputs content of an existing file to the terminal.
            If file does not exist, it outputs an error.
            If file contains no content, nothing is output.

            Usage: read hello.txt
            Output: "hello world"
        '''
        if params == None or len(params) != 1: 
            raise Exception('Incorrect number of parameters, correct usage: read <file_name>[.txt]')
        
        file_name = params[0]
        file = self.__fs.get_pwd().get_file(file_name)
        if not file:
            raise Exception(f'No file {file_name} found in current directory')
        
        content = file.get_content()
        if content != None: print(content)
    
    def _find(self, params):
        '''
            Outputs all files and directories with matching name or a
            message saying none were found.
            Note: for files, the name includes the extension.
        '''
        if params == None or len(params) != 1:
            raise Exception('Incorrect number of parameters, correct usage: find <dir_or_file_name>[.txt]')
        dir_or_file_name = params[0]
        found_dir = self.__fs.get_pwd().get_directory(dir_or_file_name)
        found_file = self.__fs.get_pwd().get_file(dir_or_file_name)

        if not found_dir and not found_file:
            print(f'No file or directory found with name: {dir_or_file_name}')
        if found_dir:
            self.__printer.print_directory(found_dir)
        if found_file:
            self.__printer.print_file(found_file)
    
    def _mv(self, params):
        '''
            Moves a directory or file from the current working directory to
            a specified target directory also within the current directory.

            Usage: 
            - mv hello.txt folder
            - mv child_folder folder
        '''
        if params == None or len(params) != 2:
            raise Exception('Incorrect number of parameters, correct usage: mv <dir_or_file>[.txt] new_location_dir_name')
        
        dir_or_file_name, new_dir_location = params

        dir_to_move = self.__fs.get_pwd().get_directory(dir_or_file_name)
        file_to_move = self.__fs.get_pwd().get_file(dir_or_file_name)
        new_dir_location = self.__fs.get_pwd().get_directory(new_dir_location)

        if not dir_to_move and not file_to_move:
            raise Exception(f'No file or directory to move was found with name: {dir_or_file_name}')
        
        if not new_dir_location:
            raise Exception(f'No target directory found with name: {dir_or_file_name}')
                
        if dir_to_move:
            self._rmdir([dir_to_move.get_name()])
            new_dir_location.add_directory(dir_to_move)
        if file_to_move: 
            self._rm([file_to_move.get_name()])
            new_dir_location.add_file(file_to_move)
    
    def _explore(self, params):
        '''
            Prints out a visual sub-tree representation with the current working
            directory as the root. 
        '''
        if params != None:
            raise Exception('Incorrect number of parameters, correct usage: explore')
        self.__printer.print_sub_file_system(self.__fs.get_pwd())
        
    