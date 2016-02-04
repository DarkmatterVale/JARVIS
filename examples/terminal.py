from jarvis import *

my_jarvis = JARVIS()

while True:
    user_input = raw_input("Human: ")

    # Leave if the user is done
    if user_input == "quit":
        exit(0)

    # Generate response
    response = my_jarvis.get_response(user_input)

    # Print response
    print response
