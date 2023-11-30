from directory import Directory

class FileSystem:
    """
        A class to represent the overall FileSystem.
        The overall file system tree originates within this class.

        Attributes:
        -------------
        root (Directory) -> The root directory object from which the tree starts.
        pwd (Directory) -> A link to the current directory a user is in.
    """
    def __init__(self):
        self.__root = Directory(name="/")
        self.__pwd = self.__root
            
    def __str__(self):
        return self.__name

    def get_root(self) -> Directory:
        return self.__root
    
    def get_pwd(self) -> Directory:
        return self.__pwd
    
    def set_pwd(self, dir: Directory) -> None:
        self.__pwd = dir
    


