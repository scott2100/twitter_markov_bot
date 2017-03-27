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
        print "i: ",  i
        if (i < len(splitString)):
            print "splitString 1: ", splitString[i], "splitString 2: ", splitString[i+1]
            print "SplitString length: ",  len(splitString)
            ngram = (splitString[i], splitString[i+1])

            #add ngram to dictionary with no codon key
            ngramsDict[ngram] = []
            
            #loop through all ngrams, find the next codon
            #then add append codons to ngram values
            if (i < len(splitString) - 2):
                nextPossibleCodon = splitString[i+2]
                nextPossibleCodonList = [splitString[i+2]]
                print "nextPossibleCodon: " + nextPossibleCodon
                print "ngram: ",  ngram
                if nextPossibleCodon:
                    if ngram in ngramsDict:
                        ngramsDict[ngram].append(nextPossibleCodon)
                    else:
                        ngramsDict[ngram] = nextPossibleCodonList 
    return ngramsDict


splitString = splitDnaIntoCodons(dnaString).split()
#print splitString
ngramsList = findNgrams(splitString)
#print ngramsList
countedNgrams = countNgrams(ngramsList)
#print countedNgrams
corpus = generateCorpus(splitString)
print corpus
