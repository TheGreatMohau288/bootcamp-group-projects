rank_values = {
    "2": 2, 
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8, 
    "9": 9, 
    "10": 10,
    "J": 10, 
    "Q": 10, 
    "K": 10, 
    "A": 11,
}

# print(rank_values)
def hand_values(cards):
    total = 0 # This is total possible drawn cards by the player
    aces = 0 # this is total number of posible aces drawn by the player and dealer

    for card in cards: # Loop through the keys in the "rank_values" dictionery
        
        total += rank_values[card] # add keys to the total possible cards drawn by player
        if card == "A": 
            aces += 1 # add 1 to the ace total everytime an ace is drawn  

    while total > 21 and aces > 0: # l
        total -= 10
        aces -= 1
    return total

# print(hand_values("9"))
# "10, 6 | 9 | first"



def parse_state(text):
    parts = text.split("|") # split the player's drawn cards from the dealer's cards and the first decision
    # print("Parts:", parts)

    cleaned_parts = [] # create new list of cleaned separate parts

    for part in parts:
        # print("Part",part)
        cleaned_parts.append(part.strip()) 
        # separate each value in the parts list, strip any spaces and then add to the "cleaned_parts" list
        # print("cleaned", cleaned_parts)

    hand_str, dealer_upcard, flag = cleaned_parts # assign variables to each value in the list 

    hand = [] # create an empty list to separate the cards dealt to the player 
    for rank in hand_str.split(","): 
        hand.append(rank.strip()) # loop through the list to strip and separate the two values to add to the "hand" list 
    # print("Hand =", hand)
    return hand, dealer_upcard, flag # Return the hand list, the dealer's card and the flag


    print(parse_state("10, 6 | 9 | first"))


def generate_actions(state): 
    actions = [] # Create a list called actions to insert all possible actions during each round
    player_points = 0
    for a, b in enumerate(state):
        player_points  = int(b[0]) + int(b[1])
        break
        

    if state[2] == "busted" or state[2] == "done":
        return actions
        
    actions.append("hit")
    actions.append("stand")

    if player_points < 21 and state[2] == "first":
        if player_points % player_points == 0: # Compare both player cards to see if they are equal to return "split"
            actions.append("split")

        actions.append("surrender")

        if state[1] == "A":
            actions.append("insurance")
    if player_points > 21:
        actions.append("bust")
    return actions
        
print(generate_actions(new_state))


def apply_action(state, action, next_card=None):
    raise NotImplementedError("This function is not implemented yet.")
