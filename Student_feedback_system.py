feedback_dictionary = {}
list_good = ["good", "best", "ok", "better", "fine"]
list_bad = ["not good", "can be better", "bad"]


def add_feedback(name, feedback):
    with open("feedback_form.txt", "a") as f1:
        f1.write(f"{name} : {feedback}\n\n")
        feedback_dictionary[name] = feedback




def showAllFeedbacks():
    with open("feedback_form.txt", "r") as f2:
        content = f2.read()
        print(content)

def show_single_feedback():
    with open("feedback_form.txt", "r") as f3:
        check_feedback = input("Enter the name whose feedback you want to see : ")

        content = f3.read()
        if check_feedback in feedback_dictionary:
            print(f"feedback : {feedback_dictionary[check_feedback]}")
        else :
            print("Not found")


def analyze(search):
    if search in feedback_dictionary:
        type = feedback_dictionary[search].split()
        for i in type :
            if i in list_good:
                print(f"feedback of {search} : Positive")
            elif i in list_bad:
                print(f"feedback of {search} : Negative")

while True:
    choice = int(input("1. add feedback\n2. show feedbacks\n3. search feedback of a student\n4. analyze feedback\n\n\nEnter the choice : "))
    if(choice == 1):
        name = input("Enter the name of the student : ")
        feedback = input("Enter your feedback : ")
        add_feedback(name, feedback)
    elif(choice == 2):
        showAllFeedbacks()
    elif(choice == 3):
        show_single_feedback()
    elif(choice == 4):
        search = input("Enter the name of student to check his feedback type : ")
        analyze(search)
    elif(choice == 5):
        print("Thank you!")
        break
