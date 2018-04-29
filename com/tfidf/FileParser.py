class FileParser:
    'File Parser class for all functionality related to parsing a class'


    def parseFileBasedOnDelimiter(self, fileName):
        self.fileHandle = open(fileName, 'r')

        for line in self.fileHandle:
            fields = line.split('|')

            print(fields[0])  # prints the first fields value
            print(fields[1])  # prints the second fields value

        self.fileHandle.close()
