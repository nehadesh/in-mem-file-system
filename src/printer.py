from directory import Directory
from file import File 

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "

class Printer:
    """
        A class that handles printing the tree.
    """
    
    def __init__(self, root: Directory=None):
        self.__root = root

    def print_sub_file_system(self, dir=None):
        if dir == None:
            return
        
        print(dir.get_name())
        self._pretty_print(dir)

    
    def print_file_system(self):
        if self.__root == None:
            return
        
        print(self.__root.get_name())
        self._pretty_print(self.__root)

    def _pretty_print(self, directory: Directory, prefix=""):
            items = directory.get_directories().items()
            items_count = len(items)
            for index, entry in enumerate(items):
                _, dir = entry
                connector = ELBOW if index == items_count - 1 else TEE
                self._pretty_print_directory(dir, index, items_count, prefix, connector)
        
    def _pretty_print_directory(
        self, directory: Directory, index: int, items_count: int, prefix: str, connector: str
    ):
        print(f"{prefix}{connector} {directory.get_name()}")
        if index != items_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._pretty_print(
            directory=directory,
            prefix=prefix,
        )

    def _pretty_print_file(self, file, prefix, connector):
        print(f"{prefix}{connector} {file.name}")

    def print_directory(self, directory: Directory):
        print(f"📁 {directory.get_name()}")
    
    def print_file(self, file: File): 
        print(f"📄 {file.get_name()}")