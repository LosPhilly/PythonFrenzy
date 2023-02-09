questions = [    {        "question": "What is the capital of France?",        "answer": "Paris"    },    {        "question": "What is the currency of Japan?",        "answer": "Yen"    },    {        "question": "Who is the lead singer of Queen?",        "answer": "Freddie Mercury"    }]
for question in questions:
    user_answer = input(question["question"] + ": ")
    if user_answer.lower() == question["answer"].lower():
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", question["answer"])
score = 0
for question in questions:
    user_answer = input(question["question"] + ": ")
    if user_answer.lower() == question["answer"].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect. The correct answer is", question["answer"])
print("You got", score, "out of", len(questions), "questions correct.")
