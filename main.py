import random

responses = ["yes", "no", "maybe", "IDK", "of course"]

while True:
    question = input("Ask me a question (or type 'quit' to exit): ")
    
    # Check if the user wants to quit
    if question.lower() == 'quit':
        print('Goodbye!')
        break
    
    # Validate the question
    if len(question.strip()) < 3:
        print("Please ask a valid question.")
        continue
    
    print(random.choice(responses))
