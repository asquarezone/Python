from abc import ABC, abstractmethod

class FileParser(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod #decorators
    def parse(self):
        pass

class HtmlFileParser(FileParser):
    
    def parse(self):
        return ["How are you"]

if __name__ == "__main__":
    # parser = FileParser("test.txt")
    parser = HtmlFileParser("test.html")