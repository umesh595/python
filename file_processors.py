from abc import ABC, abstractmethod
class FileProcessor(ABC):
    def process(self):
        self.open_file()
        self.read()
        self.parse()
        self.close_file()
    def open_file(self):
        print("Opening file")
    def read(self):
        print("Reading file")
    @abstractmethod
    def parse(self):
        pass
    def close_file(self):
        print("Closing file")
class CSVProcessor(FileProcessor):
    def parse(self):
        print("Parsing CSV")
class JSONProcessor(FileProcessor):
    def parse(self):
        print("Parsing JSON")