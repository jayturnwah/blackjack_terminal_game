import random
total = 0 
dealer_total = 0
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_values = {
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
    "A": 11
}
player_hand = []
dealer_hand = []

print("Welcome to Black Jack!!! Are you feeling lucky?!?")

welcome_input = input("Are you ready to play?: ")
if welcome_input == "Yes" or welcome_input == "yes":
    
    print("Let's play! Here are your cards!")
    player_hand.append((random.choice(cards)))
    player_hand.append((random.choice(cards)))
    print("Your hand:", player_hand)
    dealer_hand.append((random.choice(cards)))
    
    print("Dealer's hand:", dealer_hand)
    dealer_hand.append((random.choice(cards)))

while True:    
    total = 0
    
    for card in player_hand:
        
        total += card_values[card]
    if 'A' in player_hand and total > 21:
        total -= 10
    print("Total: ", total)
    

    if total == 21:
        print("Congratulations! You win!")
        play_again = input("Would you like to play again? Yes/No: ")
        if play_again == "yes".lower():
            player_hand = []
            dealer_hand = []
            player_hand.append(random.choice(cards)) 
            player_hand.append(random.choice(cards))
            print(player_hand)
            continue

    if total > 21:
        print("Bust! You lose!")
        play_again = input("Would you like to play again? Yes/No: ")
        if play_again == "yes".lower():
            player_hand = []
            dealer_hand = []
            player_hand.append(random.choice(cards)) 
            player_hand.append(random.choice(cards))
            dealer_hand.append(random.choice(cards))
            
            print("Your hand:",player_hand)
            print("Dealer's hand:",dealer_hand)
            continue
                            
        else:
            print("Thanks for playing!")
            break

    hit = input("Would you like to hit or stay?: ")

    if hit.lower() == "hit":
        new_card = random.choice(cards)
        player_hand.append(new_card)
        total += card_values[new_card] 
        print("Your hand:", player_hand)   
    elif hit.lower() == "stay":
        dealer_total = 0
        
        for card in dealer_hand:
            dealer_total += card_values[card]
            if 'A' in dealer_hand and dealer_total > 21:
                dealer_total -= 10
        
        print("Dealer hand:", dealer_hand)
        print("Dealer total:", dealer_total)
        
        while dealer_total <= total:
            new_card = random.choice(cards)
            dealer_hand.append(new_card)
            dealer_total += card_values[new_card]
        
            print("Dealer draws:", new_card)
            print("Dealer hand:", dealer_hand)
            print("Dealer total", dealer_total)
        
        if dealer_total > 21:
            print("Dealer busts! You win!")
            play_again = input("Would you like to play again? Yes/No: ")
            if play_again == "yes".lower():
                player_hand = []
                dealer_hand = []
                player_hand.append(random.choice(cards)) 
                player_hand.append(random.choice(cards))
                dealer_hand.append(random.choice(cards))
                
                print("Your hand:",player_hand)
                print("Dealer's hand:",dealer_hand)
                continue
                      
                      
                
            else:
                print("Thanks for playing!")
                break


        
       
        if dealer_total > total:
            print("Dealer wins!")
            play_again = input("Would you like to play again? Yes/No: ")
            if play_again == "yes".lower():
                player_hand = []
                dealer_hand = []
                player_hand.append(random.choice(cards)) 
                player_hand.append(random.choice(cards))
                dealer_hand.append(random.choice(cards))
                
                print("Your hand:",player_hand)
                print("Dealer's hand:",dealer_hand)
                continue                                
            else:
                print("Thanks for playing!")
                break
"""else: 
    print("House rules...Dealer wins ties!")
    play_again = input("Would you like to play again? Yes/No: ")
    if play_again == "yes".lower():
        print("Here are your cards:", random.choice(player_hand))
        continue
    else:
        print("Thanks for playing!")
        break
        break
    
if dealer_total == total:
    print("House Rules....Dealer wins all ties! Sorry!")
    play_again = input("Would you like to play again? Yes/No: ")
    if play_again == "yes".lower():
        print("Here are your cards:", random.choice(player_hand))
        continue
    else:
        print("Thanks for playing!")
        break
    
if total == 21:
        print("Congratulations! You win!")
        play_again = input("Would you like to play again? Yes/No: ")
        if play_again == "yes".lower():
            print("Here are your cards:", random.choice(player_hand))
            continue
        else:
            print("Thanks for playing!")
            break"""
        


        

    
    

    