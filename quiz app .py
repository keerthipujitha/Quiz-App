# Quiz questions and answers
quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. James Gosling", "B. Guido van Rossum", "C. Elon Musk", "D. Dennis Ritchie"],
        "answer": "B"
    }
]

score = 0

print("🎯 Welcome to the Quiz App!")
print("--------------------------------")

for i, q in enumerate(quiz, start=1):
    print(f"\nQ{i}: {q['question']}")
    for opt in q['options']:
        print(opt)
    answer = input("Your answer (A/B/C/D): ").strip().upper()

    if answer == q['answer']:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {q['answer']}")

print("\n📊 Quiz Completed!")
print(f"Your score: {score}/{len(quiz)}")
