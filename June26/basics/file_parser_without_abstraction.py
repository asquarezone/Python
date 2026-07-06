class FileParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self): # This is considered concrete
        pass

class HtmlFileParser(FileParser):
    pass

class PlainHtmlFileParser(HtmlFileParser):
    pass

class WikiFileParser(HtmlFileParser):
    pass

class MarkdownFileParser(FileParser):
    def parse(self):
        # parse markdown
        pass

class TextFileParser(FileParser):
    def parse(self):
        # parse markdown
        pass 

if __name__ == "__main__":
    parser = HtmlFileParser("test.txt")
    parser.parse()