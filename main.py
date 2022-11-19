import os
import utils

data = utils.get_data()
categories = [cat for cat in data]


def ask_question(data):
    print(f"Question {data['id']}")
    print(data["question"])
    for i, p in enumerate(data["proposals"]):
        print(f"{i+1}. {p}")

    ans = int(input("Enter your choice (1 - 4): "))

    result = 0
    if ans > 0 and ans < 5:
        if data["proposals"][ans - 1] == data["answer"]:
            print("Correct")
            result = 1
        else:
            print("Wrong")
    else:
        print("Invalid data. It will be considered as wrong answer")

    return result


def game():
    for i, cat in enumerate(categories):
        print(f"{i+1}. {cat}")
    
    choosen = int(input("Enter a category number: "))

    if choosen > 0 and choosen < len(categories) + 1:
        score = 0
        for q in data[categories[choosen - 1]]:
                score +=  ask_question(q)

        print(f"Your score is {score} out of {len(data[categories[choosen - 1]])}")      


def main():
    play = True
    while play:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        game()
        play = input("Do you want to play again? (Y/n): ") in ["y", "Y"]


if __name__ == "__main__":
    main()