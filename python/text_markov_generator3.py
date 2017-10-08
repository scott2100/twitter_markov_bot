import collections
from random import *

inputString = "Presidents and their administrations have been talking to North Korea for 25 years, agreements made and massive amounts of money paid hasn't worked, agreements violated before the ink was dry, makings fools of U.S. negotiators. Sorry, but only one thing will work! Stock Market hits an ALL-TIME high! Unemployment lowest in 16 years! Business and manufacturing enthusiasm at highest level in decades! Wow, so many Fake News stories today. No matter what I do or say, they will not write or speak truth. The Fake News Media is out of control! It is a miracle how fast the Las Vegas Metropolitan Police were able to find the demented shooter and stop him from even more killing! Wow, so many Fake News stories today. No matter what I do or say, they will not write or speak truth. The Fake News Media is out of control! I call my own shots, largely based on an accumulation of data, and everyone knows it. Some FAKE NEWS media, in order to marginalize, lies!"

def findNgrams(inputString):
    ngrams = list()
    inputString = inputString.split()
    for i in range(len(inputString)-1):
        ngram = inputString[i], inputString[i+1]
        ngrams.append(ngram)
    return ngrams

def generateCorpus(inputString):
    ngramsDict = dict()
    ngram = tuple()

    inputString = inputString.split()
    for i in range(len(inputString)-1):
        ngram = inputString[i], inputString[i+1]
    
        #add ngram to dictionary with no codon key
        if ngram not in ngramsDict:
            ngramsDict[ngram] = []
            
            #loop through all ngrams, find the next codon
            #then add append codons to ngram values
            if (i < len(inputString) - 2):
                nextPossibleCodon = inputString[i+2]
                nextPossibleCodonList = [inputString[i+2]]
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
    
    nextvalue = choice(corpus[nextkey])
    keyandvalue = nextkey[-2] + " " + nextkey[-1] + " " + nextvalue
    fullText = fullText + " " + keyandvalue
    
    while (len(fullText)<100):
        fullTextSplit = fullText.split()
        nextkey = fullTextSplit[-2], fullTextSplit[-1]
        print(len(nextkey))
        print("NEXTKEY: " + str(nextkey))
        #skip adding key if it's empty
        if(len(nextkey)>0):
         nextvalue = choice(corpus[nextkey])
        print("NEXTVALUE: " + nextvalue)
        print("keyandvalue: " + keyandvalue)
        print("fulltext split length: ",  len(fullText.split()))
        if(len(fullText.split())>=3):
           print("In Loop")
           fullText = fullText + " " + nextvalue
        print("FullTextSplit: " + str(fullTextSplit))
        print("Next key 2: " + str(nextkey))
        print("TEXT: " + seed)
        print("FULL TEXT: " + fullText)

ngramsList = findNgrams(inputString)
corpus = generateCorpus(inputString)
#print("Corpus: " + str(corpus))
generateSeed(corpus)


