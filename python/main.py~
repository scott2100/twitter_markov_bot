import collections

dnaString = "ACAAGAACAAGTACAAGT";

def splitDnaIntoCodons(dnaString): 
        j = 0
        splitDnaString = ""
        for i in range(len(dnaString)):
            if (j < 2):
              splitDnaString += dnaString[i]
              j += 1
            else:
              splitDnaString += dnaString[i]
              splitDnaString += " "
              j = 0 
        return splitDnaString

def findNgrams(splitString):
    ngrams = list()
    for i in range(len(splitString) - 1):
        ngrams.append(splitString[i] + " " + splitString[i+1])
    return ngrams

def countNgrams(ngramsList):
    countedNgramsList = ''
    countedNgrams = collections.Counter(ngramsList)
    for key, value in countedNgrams.most_common():
        countedNgramsList += key + ' : ' + str(value) + '\n'
    return countedNgramsList

def generateCorpus(splitString):
    ngramsDict = dict()
    ngram = tuple()
    print splitString
    print test = len(splitString -2)
    for i in range(len(splitString) -2):
        ngram = (splitString[i], splitString[i+1])
        nextPossibleCodon = [splitString[i+2]]
        #nextPossibleCodon = ['FAKE']
        #ngramsDict = {('FAKE', 'FAKE'): nextPossibleCodon}
        ngramsDict = {ngram: nextPossibleCodon}
    return ngramsDict


splitString = splitDnaIntoCodons(dnaString).split()
#print splitString
ngramsList = findNgrams(splitString)
#print ngramsList
countedNgrams = countNgrams(ngramsList)
#print countedNgrams
corpus = generateCorpus(splitString)
print corpus
