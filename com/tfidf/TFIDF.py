# Function to calculate TF-IDF

# Function to iterate through the original document with TF and update
# it with TF-IDF values.
def calculateTfIdf(termFrequencyDocuments, inverseTermFrequencyDocuments):
    for document in termFrequencyDocuments :
        for word in document:
            # Get corresponding IDF value for word.
            if inverseTermFrequencyDocuments.get(word, -1) != -1:
                document[word] = document[word] * inverseTermFrequencyDocuments.get(word)

    # Debugging
    return termFrequencyDocuments

