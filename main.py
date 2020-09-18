#Pocket Pen Pal

#Username Input 
print ("Welcome to Pocket Pen Pal! Let's get started!")
username = input(str("What is your name? "))
print (f"Well... Hello there, {username}!")

#Have user choose city
city = input(str("Where would you like your Pen Pal to be from? (Choose from either Paris, Tokyo, or Los Angeles) "))

if city.lower() == "paris":
    print ("Bonjour! I am from Paris, the most romantic city in the world!")
elif city.lower() == "tokyo":
    print ("Kon'nichiwa! I am from Tokyo, the jungle of electric lights and colors at night!")
elif city.lower() == "los angeles":
    print ("Hey! I am in Hollywood, the land of fame, palm trees, and sunny skies!")
else:
    print ("You need to select from Paris, Tokyo, or Los Angeles. :)")

#Ask user for their city
user_city = input (str("What city are you in? :) "))
print (f"So you're from {user_city}! Sweet! I've heard nice things about your city. :)")

#Import your choice module
from random import choice

#Create function for user's mood
def get_bot_response(user_response):
  bot_response_happy = ["That's so good to hear!", "That makes ME happy to hear!", "There is nothing that makes me happier!"]
  bot_response_sad = ["Don't worry. You're not alone!", "I wish there was something I could do to help you feel better!", "Well I'm sorry, but hey, I'm sending you only the best of vibes!"]
  if user_response == "happy":
    return choice(bot_response_happy)
  elif user_response == "sad":
    return choice(bot_response_sad)
  else:
      return "You do you! :)"
      
#Get user mood
#user_response = ""
while True:
  user_response = input("How are you feeling today? (Happy or sad? Type 'done' for next question.) ")
  if user_response == 'done':
    break
  bot_response = get_bot_response(user_response)
  print(bot_response)

#Ask user what awesome activity they did today
activity = input (str("Can you tell me one cool thing you did today? "))
print ("That is pretty rad.")

#Ask user if they want to hear what you did today
bot_activity = input (str("Do you want to hear what I did today? (Yes or No?) "))
if bot_activity.lower() == "yes":
  print ("I actually was a tourist in my own city today! I visited all the hot travel destinations in my area!")
elif bot_activity.lower() == "no":
  print ("That's alright. :)")
else:
  print (f"Well, no worries! It seems as if you are no longer interested in chatting, so I hope you have a great rest of your day, {username}!")

#Get user's favorite game
game = input (str("Let's move on to something way more fun! What is your favorite video game?"))
print (f"OMG! Your favorite game is {game}! I personally LOVE Call of Duty... Mobile. Don't laugh. I know they say mobile gaming doesn't count. But hey, it does to me. ;)")

#Create function for user's favorite food
def get_user_food(user_food):
  user_food_sushi = ["I love California rolls!", "I absolutely adore Spider rolls!", "OMG, tempura with ANY sushi and then add miso soup... Yuuuums."]
  user_food_burritos = ["A steak burrito can hit the spot!", "I'm such a huge fan of any burrito bowl known to man AND woman!", "Burritos without chips and salsa? Whaaaat?! AM I RIGHT OR AM I RIGHT?"]
  user_food_burgers = ["In N Out is my favorite burger joint!", "I can't blame you... a burger and fries is classic. Oh, can't forget the milkshake... strawberry for me, please!", "Yes! Just don't forget to pair it with a nice side of fries and a shake! :)"]
  if user_food == "sushi":
    return choice(user_food_sushi)
  elif user_food == "burritos":
    return choice(user_food_burritos)
  elif user_food == "burgers":
    return choice(user_food_burgers)
  else:
      return "I am always open to trying out new dishes! :)"

#Get user's favorite food
#user_food = ""
while True:
  user_food = input("Geez... all this talk about gaming is making me hungry. I usually love to top off a great gaming session with a savory meal! Hmm... Which food is your favorite: sushi, burritos, or burgers? (Type 'done' for next question.) ")
  if user_food == 'done':
    break
  user_food = get_user_food(user_food)
  print(user_food)

#Goodbye for now
print ("I think it is time for me to go ahead and make a meal! All that talk about food.... Hehe, but it was so wonderful chatting with you! Hope you can visit sometime soon!")