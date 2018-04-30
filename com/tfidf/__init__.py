import argparse;
from com.tfidf import FileParser
from com.tfidf import TermFrequency
from com.tfidf import InverseDocumentFrequency

def main():
    parser = argparse.ArgumentParser(description='TF-IDF and Luigi pipeline.')

    parser.add_argument('--file',
                        help='pass the file to parse the text')
    parser.add_argument('--delimiter', help='delimiter in the file')

    args = parser.parse_args()
    print(args.file)

    if args:
        if args.file:
            array = FileParser.parseFileBasedOnDelimiter(args.file, args.delimiter)

            removedPunctuationArray = FileParser.removePunctuation(array)

            numberOfDocuments = removedPunctuationArray.__len__()

            termFrequencyDocuments = TermFrequency.calculateTermFrequency(removedPunctuationArray)
            inverseDocumentFrequencyDocuments = InverseDocumentFrequency.calculateNumberOfDocumentsPerWord(termFrequencyDocuments)

            InverseDocumentFrequency.calculateInverseDocumentFrequency(inverseDocumentFrequencyDocuments, termFrequencyDocuments.__len__())

main()