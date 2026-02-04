import os
import json
import random
from textblob import TextBlob

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "features.json")

try:
    with open(file_path, "r") as file:
        data = json.load(file)

except Exception as e:
    print("Exception: ", e , " occurred while loading file")


# function to detect mood
def detect_mood(mood):

    try:
        blob = TextBlob(mood)
        polarity = blob.sentiment.polarity

        if (polarity > 0.3):
            return "positive"
        elif (polarity < -0.3):
            return "negative"
        else:
            return "neutral"
        
    except Exception as e:
        print("Mood detection error:", e)
        return "neutral"


# function for guess number game
def guess_number():

    try:
        user_guess = int(input("Enter your guess: "))
        random_number = random.randint(1,10)

        if (user_guess == random_number):
            print("Correct Answer! I also guessed ", random_number)

        else:
            print("Wrong Answer! I guessed ", random_number, " Better luck next time :)")

    except ValueError:
        print("Enter a valid number")


# function for rock, paper and scissor game
def rock_paper_scissor():

    try:
        options = ["rock", "paper", "scissor"]
        user_choice = input("Enter your choice(rock, paper or scissor): ").lower().strip()
        bot_choice = random.choice(options)

        if (bot_choice == "rock" and user_choice == "scissor"):
            print(f"Bot wins! {bot_choice} beats {user_choice}")

        elif (bot_choice == "paper" and user_choice == "rock"):
            print(f"Bot wins! {bot_choice} beats {user_choice}")

        elif (bot_choice == "scissor" and user_choice == "paper"):
            print(f"Bot wins! {bot_choice} beats {user_choice}")

        elif (bot_choice == "rock" and user_choice == "paper"):
            print(f"You win! {user_choice} beats {bot_choice}")

        elif (bot_choice == "scissor" and user_choice == "rock"):
            print(f"You win! {user_choice} beats {bot_choice}")
          
        elif (bot_choice == "paper" and user_choice == "scissor"):
            print(f"You win! {user_choice} beats {bot_choice}")

        elif (user_choice == bot_choice):
            print("It's a tie")

        else:
            print("Invalid choice! Enter valid choice please")

    except Exception as e:
        print("Exception (", e, ") occured!")


# function to handle Chatbot
def bot_replies(user_input):

    try:
        if ("hi" in user_input or "hello" in user_input or "hey" in user_input):
            print("Bot: Hello how are you?")

        elif ("bye" in user_input or "good bye" in user_input or "okay, talk to you later" in user_input):
            print("Bot: Okay, Bye! Have a nice day")
            return False

        elif ("tell a joke" in user_input or "joke" in user_input or "tell me something funny" in user_input or "say something funny" in user_input or "make me laugh" in user_input):
            print("Bot: ", random.choice(data["jokes"]))

        elif ("tell me a fact" in user_input or "tell something interested" in user_input or "fact" in user_input):
            print("Bot: ", random.choice(data["facts"]))

        elif ("tell me a riddle" in user_input or "riddle" in user_input):
            key = random.choice(data["riddles"])
            print(key["question"])
            user_answer = input("Answer: ").lower().strip() 
            if (key["answer"].lower().strip() == user_answer):
                print("Bot: Correct Answer. Bravo!")
            
            else:
                print("Wrong the answer is: ", key["answer"])

        elif("number game"in user_input or "guess number"in user_input or"number guess"in user_input or "number guess game"in user_input):
            guess_number()

        elif ("game" in user_input):
            print("Bot: Which game you anna play? \nnumber game \nrock paper scissor")

        elif("rock paper" in user_input or "rock-paper" in user_input or "rock paper game" in user_input or "rock paper game" in user_input ):
            rock_paper_scissor()
            
        elif ("wow" in user_input or "hurrah" in user_input  or "haha" in user_input or "good one" in user_input):
            print("Bot: Haha! that sounds great :)")

        elif ("really"in user_input or "oh okay" in user_input or "oh" in user_input or "okay" in user_input or "ok" in user_input):
            print("Bot: Yes you got it right!")

        elif ("Thank you" in user_input or "thank you" in user_input or "thanks" in user_input):
            print("Bot: My pleasure! \nWhat's next? \na riddle or a joke or a fact or any suggestion?")

        elif ("ugh" in user_input or "ahh" in user_input or "argh" in user_input or"urgh" in user_input or "uff" in user_input or "annoying" in user_input or "tired" in user_input):
            print("Bot: Oh no! seems like you're frustrated. \nWant to play a game or hear a joke or cheer up?")
           
        elif("smart"in user_input or "nice" in user_input or "good job" in user_input):
            print("Thanks! You are awesome and gentle. ")

        elif ("suggestions" in user_input or "suggestion" in user_input or "what should i do" in user_input):
            print("Bot: ", random.choice(data["suggestions"]))

        elif("who are you" in user_input or "what are you" in user_input or "your name" in user_input or "how are you" in user_input):
            print("I'm just a simple chatbot made of python. \n And secret is that I will be updated too")
        
        elif ("what can you do" in user_input or "what you can do" in user_input or "services" in user_input or "entertain me" in user_input or "how you work" in user_input):
            print("I can tell you a joke,or fact, play number guessing game , rock paper scissor game even can ask you riddle.")

        else:
            print("Sorry! I couldn't understand. \n I can tell you a joke or fact, play number guessing game ,rock paper scissor game or even ask you riddle.\n What do you want?")

    except Exception as e:
        print("Exception: (", e, ") occurred!")

    return True


print("\n************************* Welcome To Basic Chatbot **************************\n")

# greeting the user
print("Hello! How's it going?")

mood = input("You: ").lower().strip()
result = detect_mood(mood)

if (result == "positive"):
    print("Hah Great! so let's chat..")
    print("\n Would you like to play number game? \n Play rock-paper-scissor \n Wanna hear a joke? \n Wanna answer a riddle? \n Wanna know some facts \n Wanna have some suggestions?" )

elif (result == "negative"):
    print("Oh looks like you are feeling low. \n Do you want a suggestion for making you feel better?")

else:
    print("Bot: Got it, I am here to help or entertain you")


# Through while loop chatbot continues to chat
while True:

    user_input = input("You: ").lower().strip()
    continue_chat = bot_replies(user_input)

    if not continue_chat:
        break










        





    
