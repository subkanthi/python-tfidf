import string;

# File Parser  for read/write operations
# on file.

punctuationList = [",", ".", "'"]

# Function to remove all the punctuations.
# Iterate through array and remove punctuation.
def removePunctuation(array):
    for i, document in enumerate(array):
        translator = str.maketrans('', '', string.punctuation)
        array[i] = document.translate(translator)
        array[i] = document.replace('\n', " ")
        #array[i] = document.replace('\t', " ")

        print(array[i])
    return array


# Function to parse file and create
# a string array based on delimiter
def parseFileBasedOnDelimiter(fileName, delimiter):
    fileHandle = open(fileName, 'r')
    contents = fileHandle.read().strip('\n')


    entry = contents.split(delimiter)
    print(entry)
    # print(entry.__len__())

    fileHandle.close()
    return entry
