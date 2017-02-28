import collections


shortdnaString = "ACAAGAACAAGTACAAGT"
dnaString = "ACAAGAACAAGTACAAGTCAACATACAAGAAGGCGT"
longdnaString = "AGAGTTACTTACCGGCCCTTTCCATGCGCGCGCCATACCCTCCTAGTTCCCCGGTTATCTCTCCGAGGAGAGAGTGAGCGATCC"

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
    
    for i in range(len(splitString)-1):
        #print len(splitString)
        print i
        splitString[9]
        if (i < len(splitString)):
            print i
            ngram = (splitString[i], splitString[i+1])
            if (i < len(splitString) - 2):
                nextPossibleCodon = splitString[i+2]
                nextPossibleCodonList = [splitString[i+2]]
                print nextPossibleCodon
                
                if ngram in ngramsDict:
                    ngramsDict[ngram].append(nextPossibleCodon)
                else:
                    ngramsDict[ngram] = nextPossibleCodonList 
            print ngram
    return ngramsDict


splitString = splitDnaIntoCodons(dnaString).split()
#print splitString
ngramsList = findNgrams(splitString)
#print ngramsList
countedNgrams = countNgrams(ngramsList)
#print countedNgrams
corpus = generateCorpus(splitString)
print corpus
