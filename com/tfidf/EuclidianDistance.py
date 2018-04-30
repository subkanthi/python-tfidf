import itertools;
import math;

# Function to calculate Euclidean distance between documents.
# Function will have two pointers to iterate until the end

def calculateSimilarityInDocuments(tfIdfDocuments):
    index = 0


    for x in range(0, tfIdfDocuments.__len__()):
        for j in range(x + 1, tfIdfDocuments.__len__()):
            calculateSimilarity(tfIdfDocuments[x], tfIdfDocuments[j], x, j)
            print(x, j)

        # for current_item, next_item in zip(tfIdfDocuments, itertools.islice(tfIdfDocuments, 1, None)):
        #    print(current_item, next_item)
        #   print(index)
        #  index = index + 1;
        # print(index)



def calculateSimilarity(document1, document2, index1, index2):
    print(document1, document2)
    euclideanDistance = 0
    with open('out.txt', 'a') as out:
        for word1 in document1:
            euclideanDistance= euclideanDistance + math.sqrt((document1[word1] - document2[word1])** 2)


        out.write('[Document'
           + str(index1) +
    '] '+
          '[Document'
           + str(index2) + '] ' + str(euclideanDistance) + '\n')




