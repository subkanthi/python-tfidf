#IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

# Create dictionary with key(word)
# to number of documents(value)
def calculateNumberOfDocumentsPerWord(documents):
    numDocumentsPerWord = dict()
    for document in documents:
        for word in document:
            numDocumentsPerWord[word] = numDocumentsPerWord.get(word, 0) + 1;

    # Debugging
    for key, value in numDocumentsPerWord.items():
        print(key, value)
    return numDocumentsPerWord

def calculateInverseDocumentFrequency(documents, totalNumOfDocuments):
    for key, value in documents.items():
        documents[key] = value / totalNumOfDocuments

    # Debugging
    for key, value in documents.items():
        print(key, value)

    return documents
