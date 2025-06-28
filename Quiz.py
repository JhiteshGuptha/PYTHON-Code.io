# Quiz game in python

questions = ("Which is the largest ocean on Earth?",
             "What is the largest planet in our solar system?",
             "What is the capital city of Japan?",
             "Which of the following is an element?")

choices = (("A. Atlantic Ocean", "B. Arctic Ocean", "C. Indian Ocean", "D. Pacific Ocean"),
           ("A. Earth", "B. Saturn", "C. Mars", "D. Jupiter"),
           ("A. Tokyo", "B. Beijing", "C. Paris", "D. Seoul"),
           ("A. Oxygen", "B. Salt", "C. Carbon Dioxide", "4. Water"))

hints = ("Think about the ocean that covers the most surface area and reaches the greatest depths",
         "Consider which planet is a gas giant and has the greatest mass",
         "This city is also one of the world's most populous metropolitan areas and is located on the island of Honshu",
         "Think about the basic building blocks of matter that cannot be broken down into simpler substances by chemical means")

answers = ("D", "D", "A", "A")

question_number = 0
score = 0

for question in questions:
    print("-------------------------------------------")
    print(question)
    for choice in choices[question_number]:
        print(choice)
    userChoice = input("Select your choice [A,B,C,D]: ").upper()
    if userChoice == answers[question_number]:
        print("Correct Answer")
        score += 1
    else:
        print(f"{answers[question_number]} is the correct option")
    question_number += 1

print("-------------------------------------------")

print(f"Final Score: {score} / 4")
