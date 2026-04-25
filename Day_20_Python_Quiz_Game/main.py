
# List of questions and accepted answers
questions = [
    {'q': 'what keyword starts a func? ',
     'a': ['def']},
    {'q': 'how to find length of a list? ',
     'a': ['len()', 'len']},
    {'q': 'how do you check data type of a variable? ',
     'a': ['type()', 'type']},
    {'q': 'what symbol is used to start a single line comment? ',
     'a': ['#']},
    {'q': 'which keyword is used to import a module? ',
     'a': ['import']},
    {'q': 'how to convert a string into upper? ',
     'a': ['upper', '.upper', '.upper()']},
    {'q': 'what is the operator for exponentiation? ',
     'a': ['**']},
    {'q': 'which loop is used when number of iterables are known? ',
     'a': ['for']},
    {'q': 'can a variable name start with a number? ',
     'a': ['no','no it cannot']},
    {'q': 'through which operator the method is accessed? ',
     'a': ['dot', '.']}
]

score = 0
for index, q in enumerate(questions, start=1):
    prompt = f"Question {index}: {q['q']}"
    answer = input(prompt).lower().strip()
    valid_answers = [v.lower().strip() for v in q['a']]
    if answer in valid_answers:
        score += 10
        print("Correct")
    else:
        correct_answers = ', '.join(q['a'])
        print(f"Wrong answer. The correct answer was: {correct_answers}")

print("----- Final Result -----")
if score >= 90:
    print("Well done! Your grade is A.")
elif score >= 80:
    print("Great work! Your grade is B.")
elif score >= 70:
    print("Good! Your grade is C.")
elif score >= 60:
    print("Great effort! Your grade is D.")
else:
    print("Good try! Your grade is F.")

print(f"Your final score is {score}")