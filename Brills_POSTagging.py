"""
    Transformation Based POS Tagging
    Desc : unigram model containing the most probable POS tag for each word in the corpus’s vocabulary
    Submitted by : Vidya Sri Mani
    vxm163230
"""
from collections import Counter

def writeToFile(filename,Lst):
    with open(filename, 'w') as f:
        for entry in Lst:
            f.write((str(entry)+'\t Probability '+str(Lst[entry])+"\n"))

def getTagCount(file):
    WordTagCount={}
    WordTagProb = {}
    WordCount={}
    print('Getting Tag count...')
    content = open(file).read()

    allWords=content.split()
    totalNumberOfWords= len(allWords)



    for wordTag in allWords:
        word,tag = wordTag.split('_')
        if word not in WordCount.keys():
            WordCount[word]=1
        else:
            WordCount[word] += 1
        if word not in WordTagCount.keys():
            WordTagCount[word] = {}
            WordTagCount[word][tag] = 1
        else:
            if tag not in WordTagCount[word]:
                WordTagCount[word][tag] = 1
            else:
                WordTagCount[word][tag] += 1
    #Getting most probable tag
    print('Finding Most Probable Tag...')
    mostProbTag = {}
    for key,value in WordTagCount.items():
        mostProbTag[key]=max(value,key=value.get)
    for word,tag in mostProbTag.items():
        pWord = WordCount[word]/totalNumberOfWords
        pMostProbability = WordTagCount[word][tag]/totalNumberOfWords
        if word not in WordTagProb.keys():
            WordTagProb[word] = {}
            WordTagProb[word][tag] = pMostProbability/pWord


    #Write the unigram model probability for most probable tag
    filename = 'C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\UnigramMostProbableTag.txt'
    writeToFile(filename,WordTagProb)
    print('Unigram Most Probable POS Probability written to file...')

#PROGRAM EXECUTION BEGINS HERE
#input file
file ='C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\POSTrained.txt'
#file=input("Enter file path to tagged corpus in the format : C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\POSTrained.txt")
print('Calculating count of tokens')
getTagCount(file)

print ('Done')
