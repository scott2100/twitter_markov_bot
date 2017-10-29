import collections
from random import *
from post_tweet import *

text_file_name = 'trumpspeeches.txt'

def readTextFile(text_file_name):
    with open(text_file_name) as text_file:
        inputText = text_file.read().split(' ')
    text_file.closed
    return inputText

def findNgrams(inputText):
    ngrams = list()
    inputText = inputText.split()
    for i in range(len(inputText)-1):
        ngram = inputText[i], inputText[i+1]
        ngrams.append(ngram)
    return ngrams

def generateCorpus(inputText):
    ngramsDict = dict()
    ngram = tuple()

    #inputText = inputText.split()
    for i in range(len(inputText)-1):
        ngram = inputText[i], inputText[i+1]
    
        #add ngram to dictionary with no codon key
        if ngram not in ngramsDict:
            ngramsDict[ngram] = []
            
            #loop through all ngrams, find the next codon
            #then add append codons to ngram values
            if (i < len(inputText) - 2):
                nextPossibleCodon = inputText[i+2]
                nextPossibleCodonList = [inputText[i+2]]
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
    return seed
   

def generateText(seed):
    fullText = ""
    #print("SEED: " + seed)
    seedlist = seed.split()
    nextkey = seedlist[-2], seedlist[-1]
    
    nextvalue = choice(corpus[nextkey])
    keyandvalue = nextkey[-2] + " " + nextkey[-1] + " " + nextvalue
    fullText = fullText + " " + keyandvalue
    
    while (len(fullText)<140):
        fullTextSplit = fullText.split()
        nextkey = fullTextSplit[-2], fullTextSplit[-1]
        #print(len(nextkey))
        #print("NEXTKEY: " + str(nextkey))
        
        #print("NEXT VALUE LENGTH: ", len(corpus[nextkey]))
        #skip adding key if it's empty
        if(len(nextkey)>0 and len(corpus[nextkey])>0):
            nextvalue = choice(corpus[nextkey])
        else:
            #print("In else")
            nextvalue = ''
            #next value should be set to empty somehow...
        #print("NEXTVALUE: " + nextvalue)
        #print("keyandvalue: " + keyandvalue)
        #print("fulltext split length: ",  len(fullText.split()))
        if(len(fullText.split())>=3):
            #print("In Loop")
            if(len(fullText + " " + nextvalue) < 140):
                fullText = fullText + " " + nextvalue
            else:
                break
        #print("FullTextSplit: " + str(fullTextSplit))
        #print("Next key 2: " + str(nextkey))
        #print("TEXT: " + seed)
        print("FULL TEXT: " + fullText)
    return fullText


corpus = generateCorpus(readTextFile(text_file_name))
#print("Corpus: " + str(corpus))
with open('corpus.txt', 'w') as corpus_txt:
    corpus_txt.write(str(corpus))
corpus_txt.close()
seed = generateSeed(corpus)
#print("SEED " + seed)
tweet = generateText(seed)
print("TWEET " + tweet + " TWEET length: ", len(tweet))
post_tweet(tweet)

