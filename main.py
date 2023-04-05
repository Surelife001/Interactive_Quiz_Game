# Building an Interactive Quiz

# creating an introductive function
def intro():
    print("Welcome to an interactive Quiz Game")
    print("Pick one the following ")
    print("Biology\nChemistry")

    # ask user to pick from the following
    user_input = input("Pick one: ").lower()

    if user_input ==  "biology":
        Biology()

    elif user_input == "chemistry":
        Chemistry()

    else:
        print("please make sure pick from the following listed above")

# creating the Biology function that will contain the questions
def Biology():

    # ask for the answer for question one
    ques1 = input("The human heart is ____ :").lower()

    if ques1 == "myorganic":
        print("Correct")

    else:
        print("Wrong answer")

    ques2 = input("Spermology is the study of ____ :").lower()

    if ques2 == "seed":
        print("Correct")

    else:
        print("Wrong answer")

    ques3 = input("Who is known as father of Zoology ____ : ").lower()

    if ques3 == "aristotle":
        print("Correct")

    else:
        print("Wrong answer")

    ques4 = input("The energy released by 1 gram of glucose is ____ : ").lower()

    if ques4 == "4kcal":
        print("Correct")

    else:
        print("Wrong answer")

    ques5 = input(" Chambered heart occurs in ____ : ").lower()

    if ques5 == "cockroach":
        print("Correct")

    else:
        print("Wrong answer")

    # to exit or continue
    yesno()

# creating the function on Chemistry questions

def Chemistry():
    q1 = input("The S.I unit of temperature is :").lower()

    if q1 == "kelvin":
        print("correct")

    else:
        print("Wrong answer")

    q2 = input("The product of atomic mass and metal specific heat is about 6.4. This information was provided by:").lower()

    if q2 == "dulong petit’s law":
        print("Correct")
    else:
        print("Wrong Answer")

    q3 = input("Among isomeric amines, tertiary amines have the lowest boiling points because:").lower()

    if q3 == "the don't have hydrogen bond":
        print("Correct")
    else:
        print("Wrong Answer")
    yesno()


# creating a function that will exist the or continue the game
def yesno():
    yes_no = input("Do you want exit the game yes or no : ").lower()

    if yes_no == "yes":
        print("thanks for playing")
        exit()
    else:
        intro()


def main():
    intro()

main()
