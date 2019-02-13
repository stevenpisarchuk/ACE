import random

#Creating Word Dictionary

Questions = {
    "What day is it?": "Monday",
    "What Color is the sky?": "Blue",
    "What Color is grass?": "Green"


} 

#Increments correct and Incorrect Answers

print "How many questions would you like? "
questionamount = input()

def questiondisplay(questionamount):
    Correct = 0 
    Incorrect = 0

    
    i = 0
    while i < questionamount:
        thequestion = random.choice(list(Questions)) #generates a random question
       
        theanswer = Questions[thequestion] #stores the answer to the corresponding question
        
        print thequestion #prints the random question
        answerchoice = raw_input() #lets the user input an answer
        answerchoice
        if answerchoice == theanswer:
            Correct += 1
            i = i + 1
        else:
            Incorrect +=1
            i = i + 1

    print("Your total Correct is: {} ".format(Correct)) 
    print("Your total Incorrect is: {} ".format(Incorrect))
    
"""need to figure out how to make sure a question isn't duplicated if the user selects less questions than the
    dictionary has"""

questiondisplay(questionamount)