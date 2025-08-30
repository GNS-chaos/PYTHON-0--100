#Higher or Lower
import random

data = [
    {
        'name': 'insta',
        'followers': 346,
        'description': 'social media platform',
        'country': 'usa'
    },
    {
        'name': 'ronaldo',
        'followers': 215,
        'description': 'footballer',
        'country': 'portugal'
    },
    {
        'name': 'ariana grande',
        'followers': 183,
        'description': 'musician, actress',
        'country': 'usa'
    },
    {
        'name': 'dwayne johnson',
        'followers': 181,
        'description': 'actor, wrestler',
        'country': 'usa'
    },
    {
        'name': 'selena gomez',
        'followers': 194,
        'description': 'musician, actress',
        'country': 'usa'
    },
    {
        'name': 'kylie jenner',
        'followers': 190,
        'description': 'media personality, businesswoman',
        'country': 'usa'
    },
    {
        'name': 'lionel messi',
        'followers': 161,
        'description': 'footballer',
        'country': 'argentina'
    },
    {
        'name': 'kim kardashian',
        'followers': 180,
        'description': 'media personality, businesswoman',
        'country': 'usa'
    },
    {
        'name': 'beyonce',
        'followers': 150,
        'description': 'musician',
        'country': 'usa'
    },
    {
        'name': 'neymar jr',
        'followers': 140,
        'description': 'footballer',
        'country': 'brazil'
    },
    {
        'name': 'national geographic',
        'followers': 135,
        'description': 'magazine, nature photography',
        'country': 'usa'
    },
    {
        'name': 'taylor swift',
        'followers': 131,
        'description': 'musician',
        'country': 'usa'
    },
     {
        'name': 'justin bieber',
        'followers': 142,
        'description': 'musician',
        'country': 'canada'
    }
]
game="continue"
while game=="continue":



  def format_data(account):
    name=account["name"]
    desc=account["description"]
    country=account["country"]
    return (f"{name}, a {desc}, from {country}")

  account_a=random.choice(data)
  account_b=random.choice(data)

  if account_a==account_b:
    account_b=random.choice(data)
  followers_a=account_a["followers"]
  followers_b=account_b["followers"]

  score=0
 
    
  print(f"Compare A: {format_data(account_a)}.")
  print("VS")
  print(f"Against B: {format_data(account_b)}.")



  x=input("who has more followers? A or B? Press 'A' for A and 'B' for B ").lower()

  if followers_b>followers_a and x=="b":
    print(f"correct. Follower A: {followers_a} and Follower B: {followers_b}")
    score+=1

    account_a=account_b
    print("\n"*10)

  elif followers_a>followers_b and x=="a":
    print(f"correct. Follower A: {followers_a} and Follower B: {followers_b}")
    score+=1
    account_a=account_b
    print("\n"*10)
  else:
    print(f"Game is over now. Follower A: {followers_a} and Follower B: {followers_b}. Your score was: {score}")
    game="stop"
