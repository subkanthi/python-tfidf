from collections import Counter;

# Function to calculate Term frequency
# Frequency of words appearing
# in a document.
def calculateTermFrequency(array):
    for document in array :
        array = numberOfWords(document)
    #termFrequency(array)
    #mapFrequencyWords = Counter(array).most_common()
    #print(mapFrequencyWords)
    #return mapFrequencyWords


def termFrequency(counterArray):
    for element in counterArray:
        element.value = element.value / counterArray.__len__
        print(element)





# Function to calculate number of words in a document
def numberOfWords(document):
    count = Counter(document.split());
    print(count)
    return count;


