import random # generates a random number

def roll():
    min_value = 1 
    max_value = 6

    roll = random.randint(min_value,max_value)

    return roll

while True:
    players = input(" Please enter the number of players(1-4):")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("The input must be between 2-4 players. ")
    else:
        print("Invalid input, Please try again with the valid input.")

max_score =50
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

    for player_index in range(players):
        print("\nPlayer number",player_index +1, "Your turn has just started\n")
        print("Your total score is: ",players_scores[player_index],"\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll(y)? ")
            if should_roll.lower() != "y":
                break
        
            value = roll()
            if value == 1:
                print("You rolled a 1! Your turn is done!")
                current_score = 0
                break
            else:
                current_score += value
            print("You rolled a:", value)

            print("Your score is:", current_score)
    
    players_scores[player_index] += current_score
    print("Your total score is:",players_scores[player_index])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx +1,
      "is the winner with the max score of:",max_score)