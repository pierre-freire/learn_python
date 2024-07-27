import random

def play():
    user = input('What\'s yout coice? type (r) for rock, (p) for paper, (s) for scissor:\n')
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie!'
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lose!'
    
def is_win(player, oponnent):
    if(player == 'r' and oponnent == 's') \
        or (player == 's' and oponnent == 'p') \
        or (player == 'p' and oponnent == 'r'):
        return True


print(play())