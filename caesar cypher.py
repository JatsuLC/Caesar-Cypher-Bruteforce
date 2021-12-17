from genericpath import samefile
import json
import os
import sys
import string

#JSON import alpha words - dictionary

sameDir = os.path.dirname(sys.argv[0])
print(sameDir)
with open(sameDir + '/words_dictionary.json') as f:
  wordList = json.load(f)

#Json Import finish

alphabetList = list(string.ascii_lowercase)
specialChar = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/' ]
# Caesar letter shift function
def letterShift(letterShift, userInput):
    mesOutput = []
    mesList = []
    listInput = list(userInput)
    for x in listInput:
        if x == " ":
            mesList.append(x)
        if x in specialChar:
            mesList.append(x)
        if x in alphabetList:
            tmp = int(alphabetList.index(x)) + int(letterShift)
            if tmp > 25:
                tmp = tmp - 26
                mesList.append(alphabetList[tmp])
            else:
                mesList.append(alphabetList[tmp])

    mesOutput.append("".join(mesList))
    return(mesOutput)

#convert sentence to words as a list
def convert(lst):
    return (lst[0].split())

#start of bruteforce script
def bruteforce(input):
    sortedResult = {}
    orderedResult = {}
    for x in range(1, 26):
        decodedListValue = 0
        tmpDecodedList = []
        decodedSen = letterShift(x, input)
        tmpDecodedList.append(convert(decodedSen))
        for x in tmpDecodedList:
            for i in x:
                if str(i) in wordList:
                    decodedListValue = decodedListValue + 1
            orderedResult.update({str(decodedSen): decodedListValue})
    sortedResult = sorted(orderedResult.items(), key=lambda x: x[1], reverse=True)
   #probably a really bad way of doing this but hey. dont wanna go back and fix the code
    resultKeys = sortedResult[0]
    resultKeys = resultKeys[0]
    return(resultKeys)

#end bruteforce script
userContinue = False
userInput = input("Type in the sentence or word to decode: ")
print(bruteforce(userInput))
userInput = input("Type 'y' to bruteforce another cipher: ")
if userInput == 'y':
    userContinue = True
while userContinue == True:
    userInput = input("Type in the sentence or word to decode: ")
    print(bruteforce(userInput))
    userInput = input("Type 'y' to bruteforce another cipher: ")
    if userInput != "y":
        userContinue = False
        
else:
    print("Thank you for using this program!")