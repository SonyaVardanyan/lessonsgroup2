#!/usr/bin/python3
def add_question(existing_questions):
    question = input("Enter the question: ")
    if question in existing_questions:
        print("Question already exists. Skipping.")
        return None
    correct_answer = input("Enter the correct answer: ")
    wrong_answers = input("Enter three wrong answers separated by commas: ").split(",")
    return f"{question}?{correct_answer},{','.join(wrong_answers)}"

def main():
    try:
        with open("questions.txt", "r") as file:
            existing_questions = set(line.strip() for line in file)
    except FileNotFoundError:
        existing_questions = set()

    questions = []
    while True:
        choice = input("Do you want to add a question? (yes/no): ")
        if choice.lower() != "yes":
            break
        question_data = add_question(existing_questions)
        if question_data:
            existing_questions.add(question_data)
            questions.append(question_data)
    
    with open("questions.txt", "a") as file:
        for question in questions:
            file.write(question + "\n")
    
    print("Questions added to questions.txt")

if __name__ == "__main__":
    main()
