import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
rps_data = [
    {'name': 'rock', 'image': rock},
    {'name': 'paper', 'image': paper},
    {'name': 'scissors', 'image': scissors}
]

win_message = 'You win!'
lose_message = 'You lose!'
draw_message = 'Draw!'

results = [
    [draw_message, lose_message, win_message],
    [win_message, draw_message, lose_message],
    [lose_message, win_message, draw_message]
]

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")

try:
    player_choice = int(player_choice)
except ValueError:
    print('Please enter a number!')
    exit()

if player_choice < 0 or player_choice > 2:
    print('Invalid choice!')
    exit()

cpu_choice = random.randint(0, 2)

print(f"You have chosen {rps_data[player_choice]['name']}: {rps_data[player_choice]['image']}")
print(f"The CPU has chosen {rps_data[cpu_choice]['name']}: {rps_data[cpu_choice]['image']}")

print(results[player_choice][cpu_choice])
