# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 

phrase = ""

# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
while phrase != "quit":
    phrase = input('enter a phrase: ')
    print(f"what you entered is {len(phrase)} characers long")