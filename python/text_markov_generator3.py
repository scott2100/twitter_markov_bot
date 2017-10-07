import collections
from random import *

inputString = "Presidents and their administrations have been talking to North Korea for 25 years, agreements made and massive amounts of money paid hasn't worked, agreements violated before the ink was dry, makings fools of U.S. negotiators. Sorry, but only one thing will work! "

def findNgrams(inputString):
    ngrams = list()
    for word in inputString.split()):
        print(word)
        #need code to get word pairs
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
        if (i < len(splitString)):
            ngram = (splitString[i], splitString[i+1])
            
            #add ngram to dictionary with no codon key
            if ngram not in ngramsDict:
                ngramsDict[ngram] = []
            
            #loop through all ngrams, find the next codon
            #then add append codons to ngram values
            if (i < len(splitString) - 2):
                nextPossibleCodon = splitString[i+2]
                nextPossibleCodonList = [splitString[i+2]]
                if nextPossibleCodon:
                    if ngram in ngramsDict:
                        ngramsDict[ngram].append(nextPossibleCodon)
                    else:
                        ngramsDict[ngram] = nextPossibleCodonList 
    return ngramsDict

    
def generateSeed(corpus):
    seed = choice(list(corpus.keys()))
    joinseed = ' '.join(seed)
    seed = str(joinseed)
    generateText(seed)
   

def generateText(seed):
    fullText = ""
    print("SEED: " + seed)
    seedlist = seed.split()
    nextkey = seedlist[-2], seedlist[-1]
    while (len(fullText)<100):
        print("NEXTKEY: " + str(nextkey))
        nextvalue = choice(corpus[nextkey])
        print("NEXTVALUE: " + nextvalue)
        keyandvalue = nextkey[-2] + " " + nextkey[-1] + " " + nextvalue
        print("keyandvalue: " + keyandvalue)
        fullText = fullText + " " + keyandvalue
        fullTextSplit = fullText.split()
        nextkey = fullTextSplit[-2], fullTextSplit[-1]
        print("TEXT: " + seed)
        print("FULL TEXT: " + fullText)

ngramsList = findNgrams(inputString)
print(ngramsList)
###countedNgrams = countNgrams(ngramsList)
#print countedNgrams
#corpus = generateCorpus(splitString)
#print corpus
#generateMarkovText(corpus)
#generateSeed(corpus)


