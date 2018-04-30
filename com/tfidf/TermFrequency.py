from collections import Counter;

# Function to calculate Term frequency
# Frequency of words appearing
# in a document.
def calculateTermFrequency(array):
    for i, document in enumerate(array) :
        array[i] = termFrequencyForDocument(document)
    return array


# Function to calculate term Frequency of a document
# Term frequency is number of times the word appears
# in a document divided by number of words in the document
def termFrequencyForDocument(document):
    count = Counter(document.split())
    totalLength = count.__len__()
    for item in count:
        count[item] = count[item] / totalLength
    print(count)
    return count


