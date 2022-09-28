# blackjack game
import random
print("Welcome to Blackjack!")
print("The rules are simple: get as close to 21 as you can without going over.")
print("Dealer hits until she reaches 17. Aces count as 1 or 11.")
print("Jack, Queen, and King count as 10.")
print("Let's play!")

def deal():
    """Returns a random card from the deck."""
    card = random.randint(1, 13)
    return card

def value(card):
    """Returns the blackjack value of the card."""
    if card == 1:
        return 11
    elif card > 10:
        return 10
    else:
        return card

def total(hand):
    """Returns the total value of the hand."""
    t = 0
    for card in hand:
        t += value(card)
    return t

def hit(hand):
    """Adds a card to the hand and returns the total value."""
    hand.append(deal())
    return total(hand)

def play():
    """Plays a single game of blackjack."""
    player_hand = []
    dealer_hand = []
    player_hand.append(deal())
    dealer_hand.append(deal())
    player_hand.append(deal())
    dealer_hand.append(deal())
    print("You were dealt", player_hand)
    print("The dealer has a", dealer_hand[0], "showing, and a hidden card.")
    print("Your total is", total(player_hand))
    while total(player_hand) < 21:
        ans = input("Would you like to hit? ")
        if ans.lower().startswith("y"):
            hit(player_hand)
            print("You were dealt a", player_hand[-1])
            print("Your total is", total(player_hand))
        else:
            break
    if total(player_hand) > 21:
        print("You busted!")
    else:
        print("Dealer's turn.")
        print("His hidden card was a", dealer_hand[1])
        print("His total was", total(dealer_hand))
        while total(dealer_hand) < 17:
            hit(dealer_hand)
            print("Dealer chooses to hit.")
            print("He draws a", dealer_hand[-1])
            print("His total is", total(dealer_hand))
        if total(dealer_hand) > 21:
            print("Dealer busts. You win!")
        elif total(dealer_hand) >= total(player_hand):
            print("Dealer wins.")
        else:
            print("You win!")

play()

# ask user to play again
while True:
    ans = input("Would you like to play again? ")
    if ans.lower().startswith("y"):
        play()
    else:
        print("Thanks for playing!")
        break

