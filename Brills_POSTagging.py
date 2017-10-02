"""
    Transformation Based POS Tagging
    Desc : unigram model containing the most probable POS tag for each word in the corpus’s vocabulary
    Submitted by : Vidya Sri Mani
    vxm163230
"""
from collections import Counter

testSentence = "The president wants to control the board 's control"
correctTestSentenceTagged = """The_DT president_NN wants_VBZ to_TO
control_VB the_DT board_NN 's_POS control_NN"""

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
    allWords = []
    allTags = []

    print('Getting Tag count...')
    content = open(file).read()

    allWord=content.split()#split all words by space
    totalNumberOFWords = len(allWord)#Total Number of words
    for wordTag in allWord:
        word = wordTag.split('_')
        if(len(word)>1):
            allWords.append(word[0])
            allTags.append(word[1])
        else:
            allWords.append(word[0])
            allTags.append('')

    #tag word count
    tagWordCount = Counter(zip(allWords,allTags))
    tagWordCount = sorted(tagWordCount.items(), key=lambda x:x[1],reverse=True)

    mostProbableTag ={}
    for wordTag in tagWordCount:
        if(len(wordTag)>1):
            w=wordTag[0][0] #word
            t=wordTag[0][1] #tag
            c=wordTag[1]    #count
        else:
            w=word[0]
            t = ''
            c = 1
        if wordTag[0] not in mostProbableTag:
            mostProbableTag[wordTag[0]] = wordTag[1]
        else:
            if(wordTag[1]>mostProbableTag[wordTag[0]]):
                mostProbableTag[wordTag[0]] = wordTag[1]






    print('OKay')









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
