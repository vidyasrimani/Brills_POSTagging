"""
    Transformation Based POS Tagging
    Desc : unigram model containing the most probable POS tag for each word in the corpus’s vocabulary
    Submitted by : Vidya Sri Mani
    vxm163230
"""
from collections import Counter

testSentence = "The president wants to control the board 's control"

#writes the Probability to specified file
def writeToFile(filename,Lst):
    with open(filename, 'w') as f:
        for entry in Lst:
            f.write((str(entry)+'\t Probability '+str(Lst[entry])+"\n"))

#Gets the count of each tag
def getTagCount(file):
    WordTagCount={}
    WordTagProb = {}
    WordCount={}
    print('Getting Tag count...')
    content = open(file).read()

    allWords=content.split()#split all words by space
    totalNumberOfWords= len(allWords)

    #For each word get the word and tag which is joined by '_'
    for wordTag in allWords:
        word,tag = wordTag.split('_')#every word is joined by '_'
        if word not in WordCount.keys():
            WordCount[word]=1
        else:
            WordCount[word] += 1#inclement the word tag count

        if word not in WordTagCount.keys():
            WordTagCount[word] = {}#every entry will have a word and tag
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

    #The probability of the most probable tag is calculated
    for word,tag in mostProbTag.items():
        pWord = WordCount[word]/totalNumberOfWords
        pMostProbability = WordTagCount[word][tag]/totalNumberOfWords
        if word not in WordTagProb.keys():
            WordTagProb[word] = {}
            WordTagProb[word][tag] = pMostProbability/pWord

    #Write the unigram model probability for most probable tag
    filename = 'Q3-UnigramMostProbableTag.txt'
    writeToFile(filename,WordTagProb)
    print('Unigram Most Probable POS Probability written to file!')
    print('------------------------------------------------------')

    #Calculating probability without Brill's transformation
    sentProbability = 1
    testSentenceWords = testSentence.split()

    for w in testSentenceWords:
        if (w in WordTagProb.keys()):
            wTagProbKey = WordTagProb[w]
            wTag=wTagProbKey.keys()
            wProb=str(wTagProbKey.values())
            str1=wProb.split('[')
            str2=str1[1].split(']')
            wFloatProb = float(str2[0])
            #wTag,wProb = WordTagProb[w]#getting the tag, and probabilty of the word from test sentence
            sentProbability *= wFloatProb
            print('Here')

    print("Probabilty of sentence before Brill's transformation : ")
    print(sentProbability)




    print('Implementing Brills Transformation rules')
    print('Generating rules that correct atleast one error')
    """
    Rule1 : NN VB previous tag is TO
            to/TO conflict/NN NB

    Rule2 : VBP VB one of the previous 3 tags is MD
            might/MD vanish/VBP VB

    Rule3 : NN VB one of the previous two tags is MD
            might/MD not reply/NN VB

    Rule4 : VB NN one of the previous two tags is DT
            the/DT amazing play/VB NN

    """

#PROGRAM EXECUTION BEGINS HERE
#input file
file ='C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\POSTrained.txt'
#file=input("Enter file path to tagged corpus(format: C:\\Users\\Vidya\\Desktop\\NLP\\Homework2\\POSTrained.txt):\n")

print("The default test sentence is: " + testSentence)
choice=input("Do you want to try another sentence?(Y?N)\n")
if choice == "Y":
    testSentence = input('Enter new sentence:\n')
print('Calculating count of tokens')

getTagCount(file)

print ('Done')
