import pandas as pd
import random

class UserInterface:
    def mainInterface(self):
        print("         -----------------Welcome to Quiz Game-------------------")
        print()
        user_name = input("Enter your name: ")
        print()
        print(f"Hey {user_name}! Are you ready for the quiz?")
        print('|--------------------------------------------------------------|')
        print("| Here are some rules to follow before starting the quiz.      |")
        print("| * There are 10 question to answer in this quiz.              |")
        print("| * Each question consists of three choices.                   |")
        print("| * You have to select only one valid answer.                  |")
        print("| * Each question carry 1 marks.                               |")
        print("| * There is no negative marking.                              |")
        print("| * Total marks of this quiz are 10.                           |")
        print('|--------------------------------------------------------------|')
        print()
        a = input("Press C to continue or any other key to exit!\n").lower()
        if a == "c":
            ques = Question()
            ques.display()
            if ques.count == 10:
                print("--------------------------------------------------------------")
                print(f"Congratulations {user_name}! your total score is: {ques.count}")
                print("--------------------------------------------------------------")
            else:
                print("--------------------------------------------------------------")
                print(f"Hey {user_name}! your total score is: {ques.count}")
                print("--------------------------------------------------------------")
        else:
            print("You have logged out.")
            quit()

class Question:
    def fetchRabdomQuestions(self,asked_indices):
        quest_data = pd.read_csv("questions.csv")
        while True:
            random_index = random.randint(0, len(quest_data) - 1)
            if random_index not in asked_indices:
                asked_indices.add(random_index)
                question = quest_data.loc[random_index,"question"]
                choice = [quest_data.loc[random_index,f"choice{i}"] for i in range(1,5)]
                correct_ans = quest_data.loc[random_index,"correct_choice"]
                return question, choice, correct_ans
    def display(self):
        self.count = 0
        self.ask_indices = set()
        for i in range(10):
            question, choices, correct_choice = self.fetchRabdomQuestions(self.ask_indices)
            print(question)
            for i, choice in enumerate(choices,start=1):
                print(f'{i} {choice}')
            user_choice = int(input("Enter your choice: "))
            if user_choice == correct_choice:
                print("Correct!")
                print("------------------------------------------------------")
                self.count+=1
            else:
                print("Incorrect!")
                print("------------------------------------------------------")

obj = UserInterface()
obj.mainInterface()