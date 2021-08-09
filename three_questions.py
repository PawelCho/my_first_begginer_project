def question():
    rules=input("you need to answer by yes or not. Do you understeand?")
    if rules!="yes":
        return print("try again!")
    else: print("next question")
    question1=input("are you hungry?")
    if question1!="yes":
        return print("go to the walk")
    else: print("next question")
    question2= input("do you want to eat at restaurant")
    if question2!="yes":
        return print("go eat at my place")
    else: input("next question")
    question3= input("do you wanna eat a pizza?")
    if question3!="yes":
        return print("lets go eat a burger than")
    else: print("lest go eat an pizza :)")

question()
