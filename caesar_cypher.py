
import caesar_cypher_functions as cc


#end bruteforce script
userContinue = False
userInput = input("Type in the sentence or word to decode: ")
print(cc.bruteforce(userInput))
userInput = input("Type 'y' to bruteforce another cipher: ")
if userInput == 'y':
    userContinue = True
while userContinue == True:
    userInput = input("Type in the sentence or word to decode: ")
    print(cc.bruteforce(userInput))
    userInput = input("Type 'y' to bruteforce another cipher: ")
    if userInput != "y":
        userContinue = False
        
else:
    print("Thank you for using this program!")