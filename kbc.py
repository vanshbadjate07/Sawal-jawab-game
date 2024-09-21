import json
import random

f = open("/Users/vanshbadjate/Documents/Vansh/Programs/Python Program/Projects/kbc/questions.json", 'r')
questions = json.load(f)
f.close() 

def kbc():
    score = 0
    random.shuffle(questions)

    for q in questions:
        print("\n" + q["question"])  
        opt = q["options"]  
        
        for i in range(len(opt)):
            print(f"{opt[i]}")  

        user_input = input("Select the correct option (1-4) or type 'exit' to leave: ")
        
        if user_input.lower() == 'exit':
            print("Thank you for playing! Your final score is:", score)
            break
        
        try:
            user_ans = int(user_input)

            if user_ans == q["ans"]:
                score += 1
                print(f"Correct Option! Current score is: {score} \nMoving to the next question")

                if score >= 30:
                    print("7 Crore!! \nKya karoge itne dhanrashi ka!")
                    break
            else:
                print("Wrong Answer!")
                print(f"correct answer was: {opt[q['ans'] - 1]} \n Game Over.")
                break
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4 or 'exit'.")

    print(f"Your Final score is: {score}")

def main():
    print("Welcome to Sawal Jawab Game")
    print("Developed By Vansh Badjate")
    print("Answer questions and win points")
    
    start = int(input("Press 1 to begin: "))
    
    if start == 1:
        kbc()

if __name__ == "__main__":
    main()
