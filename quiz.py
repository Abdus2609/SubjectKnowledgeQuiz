# enter name and age in order to create username and enter password
def make_username_password():
    name = input("Please enter your name: ").capitalize()
    age = input("Please enter your age: ")
    username = name[:3] + age

    print("Hi, " + name + ", your username will be: " + username)
    password = input("Please enter a password: ")

    return name, username, password


# saves username and password to external file
def save_username_password(username, password):
    print()
    print("Saving username and password...")
    file = open("usernamepassword.txt", "a")
    outputData = username + "," + password + "\n"
    file.write(outputData)
    file.close()
    print()


# enter subject choice and direct to corresponding quiz
def subject_choice(name):
    subject = input(
        name + ", what subject would you like to be quizzed on? ").capitalize()
    if subject == "Maths":
        print("The subject you have chosen is: Maths")
        difficulty = maths()
    elif subject == "English":
        print("The subject you have chosen is: English")
        difficulty = english()
    else:
        print("We haven't made a quiz on that subject yet. We will try and make one on this topic soon.")

    return subject, difficulty


# enter difficulty for maths and read corresponding quiz
def maths():
    difficulty = input(
        "What difficulty quiz would you like out of Easy, Medium, and Hard? ").capitalize()
    if difficulty == "Easy":
        file = open("MathsEasy.txt", "r")
    elif difficulty == "Medium":
        file = open("MathsMedium.txt", "r")
    elif difficulty == "Hard":
        file = open("MathsHard.txt", "r")
    print("You have chosen the difficulty: " + difficulty)
    print(file.read())
    file.close()
    print()

    return difficulty


# enter difficulty for english and read corresponding quiz
def english():
    difficulty = input(
        "What difficulty quiz would you like out of Easy, Medium, and Hard? ").capitalize()
    if difficulty == "Easy":
        file = open("EnglishEasy.txt", "r")
    elif difficulty == "Medium":
        file = open("EnglishMedium.txt", "r")
    elif difficulty == "Hard":
        file = open("EnglishHard.txt", "r")
    print("You have chosen the difficulty: " + difficulty)
    print()
    print(file.read())
    file.close()
    print()

    return difficulty


# enter answers for quiz and calculate score and percentage
def calculate_score():
    score = 0
    for i in range(5):
        answer = input("Please enter your answer for Q" +
                       str(i + 1) + ": ").lower()
        if answer == "a":
            score += 1
    print()
    percentage = int((score / 5) * 100)

    return score, percentage


# calculate a grade based on the percentage of user
def calculate_grade(percentage):
    if percentage == 0:
        grade = "FAIL"
    elif percentage == 20:
        grade = "D"
    elif percentage == 40:
        grade = "C"
    elif percentage == 60:
        grade = "B"
    elif percentage == 80:
        grade = "A"
    elif percentage == 100:
        grade = "A*"

    return grade


# print the results of the user
def print_results(name, username, subject, difficulty, score, percentage, grade):
    print(name + ", here are your results for your quiz:")
    print()
    print("*" * 40)
    print("SUBJECT KNOWLEDGE QUIZ - RESULTS")
    print()
    print("         Username: " + username)
    print("          Subject: " + subject)
    print("       Difficulty: " + difficulty)
    print("            Score: " + str(score))
    print("       Percentage: " + str(percentage))
    print("            Grade: " + grade)
    print("*" * 40)
    print()


# save the user's details to an external text file
def save_data(username, subject, difficulty, grade):
    print("Saving your results...")
    file = open("results.txt", "a")
    outputData = username + "," + subject + "," + difficulty + "," + grade + "\n"
    file.write(outputData)
    file.close()
    print()


# load the data from the text file and store in a database which can be extracted from
def load_data():
    dataBase = []
    file = open("results.txt", "r")
    line = file.readline().rstrip()
    while line != "":
        record = []
        username, subject, difficulty, grade = line.split(",")
        record.extend((username, subject, difficulty, grade))
        dataBase.append(record)
        line = file.readline().rstrip()
    file.close()

    return dataBase


# display a leaderboard showing the top five grades and their usernames and quiz choice
def leaderboard(dataBase):
    print("*" * 40)
    print("LEADERBOARD")
    print()
    sortedDataBase = sorted(dataBase, key=lambda x: x[3])
    if len(sortedDataBase) < 5:
        for record in sortedDataBase:
            print(record)
    else:
        for record in sortedDataBase[:5]:
            print(record)
    print("*" * 30)
    print()


print("Welcome to the Subject Knowledge Quiz.")
name, username, password = make_username_password()
save_username_password(username, password)
subject, difficulty = subject_choice(name)

score, percentage = calculate_score()
grade = calculate_grade(percentage)

print_results(name, username, subject, difficulty, score, percentage, grade)
save_data(username, subject, difficulty, grade)
dataBase = load_data()
leaderboard(dataBase)

print("Thank you for playing the Subject Knowledge Quiz.")
print("\n")
