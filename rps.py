import random

def get_choices():
  player_choice = input('Enter a choice (rock, paper, scissors):')
  options = ['rock', 'paper', 'scissors']
  computer_choice = random.choice(options)
  choices = {'computer' : computer_choice , 'player' : player_choice}
  return choices
  
def check_win(player, computer):
  print (f'You chose {player}, computer chose {computer}')
  if player == computer:
    return 'It is a tie!'
  elif player == 'rock' :
    if computer == 'scissors':
      return "Rock Smashes Scissors! You Win!"
    else:
      return "Paper Covers Rock! You Lose!"
    
  elif player == 'scissors':  
    if computer == 'rock':
      return "Rock Smashes Scissors! You Lose!"
    else:
      return "Scissors Cuts Paper! You Win!"
    
  elif player == 'paper' :
    if computer == 'scissors':
      return "Scissors Cuts Paper! You Lose!"
    else:
      return "Paper Covers Rock! You Win!"

choices= get_choices()
result = check_win(choices['player'], choices['computer'])
print(result)