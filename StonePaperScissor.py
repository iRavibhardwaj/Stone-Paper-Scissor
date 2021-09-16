from random import randint


def choice(player):
    """Assign a choice to each number possible"""
    if player == 1:
        return "Stone"
    elif player == 2:
        return "Paper"
    return "Scissor"


def print_choice():
    """Print the choices of both players"""
    print("Your choice --> ", choice(user))
    print("Computer's choice --> ", choice(comp))


def check_condition(u, c):
    """Checks weather either player is winning or not"""
    if u == 3 and c == 1:
        return False
    elif u == 1 and c == 3:
        return True
    elif u > c:
        return True
    return False


def update_scoreboard(sb, r, n1, n2):
    """Maintain all the scores in a scoreboard"""
    if r >= 10:
        sb = sb[:-28] + f"\n|   {r}. |  {n1}   |    {n2}     |" + sb[-28:]
    else:
        sb = sb[:-28] + f"\n|   {r}.  |  {n1}   |    {n2}     |" + sb[-28:]
    return sb

#Scoreboard Layout
scoreboard = "| Round | User | Computer |\n|-------|------|----------|\n|_______|______|__________|"
name = input("Enter your name --> ")
print("Good Luck!", name.title())
usr = 0
com = 0
itr = 1
i = 5
while i > 0:
    user = input("Enter\n\t 1 -> for stone\n\t 2 -> for paper\n\t 3 -> for scissor\n --> ")
    # Only accepting valid inputs
    if not (user.isnumeric()) or int(user) < 0 or int(user) > 3:
        print('Invalid input\nTry again...')
    else:
        user = int(user)
        comp = randint(1, 3) #Computer makes a random choice
        print_choice()
        if user == comp:
            print("Match Draw")
            scoreboard = update_scoreboard(scoreboard, itr, 0, 0)
            itr += 1
        else:
            if check_condition(user, comp):
                print("You win..")
                scoreboard = update_scoreboard(scoreboard, itr, 1, 0)
                usr += 1
            else:
                print("You lose..")
                scoreboard = update_scoreboard(scoreboard, itr, 0, 1)
                com += 1
            itr += 1
            i -= 1
print("Scoreboard...")
print(scoreboard)
if usr > com:
    print(f"You won {usr}:{com}")
else:
    print(f"Computer won {com}:{usr}")
