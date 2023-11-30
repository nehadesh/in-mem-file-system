from file import File
from sortedcontainers import SortedDict

class Directory:
    """
        A class to represent a directory node.
        The file system tree is built from these nodes. 

        Attributes:
        -------------
        name (str) -> The name of this directory object.
        parent (Directory) -> A link to the parent directory object that contains 
        this directory.
        files (SortedDict<File>) -> A sorted mapping from names of contained files 
        to File objects.
        directories (SortedDict<Directory>) -> A sorted mapping from names of 
        contained directories to Directory objects. 
    """
    def __init__(self, name: str):
        self.__name: str = name
        self.__parent: 'Directory' = None
        self.__files: SortedDict = SortedDict()
        self.__directories: SortedDict = SortedDict()

   
    @property
    def path(self):
        if self.__parent is None:
            return "/"  
        elif self.__parent.path == "/":      
            return self.__parent.path + f"{self.__name}"
        return self.__parent.path + f"/{self.__name}"
    
    @property 
    def depth(self):
        if self.__parent is None:
            return 0
        return self.__parent.depth + 1
    
    def __str__(self):
        return self.__name

    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, new_name: str):
        self.__name = new_name
    
    def get_parent(self) -> 'Directory':
        return self.__parent

    def set_parent(self, parent_dir: 'Directory') -> None: 
        self.__parent = parent_dir
    
    def get_files(self):
        return self.__files
    
    def get_directories(self):
        return self.__directories
    
    def get_file(self, file_name: str) -> File:
        return self.__files.get(file_name)

    def add_file(self, file: File) -> File:
        if self.__files.get(file.get_name()):
            # File already exists with this name, rename to resolve conflicts
            # TODO: Ideally this would be handled cleaner, file(1), file(2)
            # with an auto-increment functionality so that we don't create super
            # long file names
            new_raw_name = f'{file.get_raw_name()}_copy'
            new_name = f'{new_raw_name}.{file.get_extension()}'
            while self.__files.get(new_name):
                new_raw_name = f'{new_raw_name}_copy'
                new_name = f'{new_raw_name}.{file.get_extension()}'
            print(f'Creating file with name {new_name}, after resolving name conflicts')
            file.set_name(new_name)
        
        self.__files.setdefault(file.get_name(), file)
        return file

    def remove_file(self, file_name: str) -> bool:
        if self.get_file(file_name) != None:
            self.__files.pop(file_name)
            return True
        return False
    
    def get_directory(self, dir_name: str) -> 'Directory':
        return self.__directories.get(dir_name)
    
    def add_directory(self, dir: 'Directory'): 
        if self.__directories.get(dir.get_name()):
            # Directory already exists with this name, rename to handle collision
            new_name = f'{dir.get_name()}_copy'
            while self.__directories.get(new_name):
                new_name = f'{new_name}_copy'
            print(f'Creating directory with name {new_name}, after resolving name conflicts')
            dir.set_name(new_name)
        
        dir.set_parent(self)
        self.__directories.setdefault(dir.get_name(), dir)
    
    def remove_directory(self, dir_name: str) -> bool:
        if self.get_directory(dir_name) != None:
            self.__directories.pop(dir_name)
            return True
        return False
    
    def print_contents(self):
        for key in self.__directories.keys():
            print(f"📁 {key}")
        for key in self.__files.keys():
            print(f"📄 {key}")    
