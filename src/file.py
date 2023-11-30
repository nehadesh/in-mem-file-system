SUPPORTED_EXTENSION = 'txt'

class File:
    """
        A class to represent a file.

        Attributes:
        -------------
        name (str) -> The name of this file object (ex: hello.txt).
        content (str) -> The contained string text within the file.
    """
    def __init__(self, name: str, content: str = None):
        file_name, file_extension = self.__parse_name(name)
        self.__name: str = f'{file_name}.{file_extension}'
        self.__content: str = content

    def __str__(self):
        return self.__name

    def __parse_name(self, name: str) -> [str, str]:
        file_name_parts = name.split('.')

        if len(file_name_parts) != 2:
            raise Exception('Unsupported file name, correct format: <file_name>.txt')

        file_name = file_name_parts[0]
        file_extension = file_name_parts[1]

        if file_extension != SUPPORTED_EXTENSION:
            raise Exception(f'Unsupported file type {file_extension}, accepted types: <file_name>.txt')
                
        return file_name, file_extension

    def get_name(self) -> str:
        return self.__name
    
    def get_raw_name(self) -> str:
        file_name, _ = self.__parse_name(self.__name)
        return file_name
    
    def get_extension(self) -> str:
        _, file_extension = self.__parse_name(self.__name)
        return file_extension
    
    def set_name(self, new_name: str):
        self.__name = new_name
    
    def get_content(self) -> str:
        return self.__content
    
    def set_content(self, content: str) -> None: 
        self.__content = content
    


