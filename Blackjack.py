import random

print "Blackjack"


def shuffle():
    deck = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
            "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
            "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2,
            "A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    random.shuffle(deck)
    return deck


def deal(deck, i):
    cards = [deck[i], deck[i+1]]
    return cards

def hit(deck, i):
    return deck[i]

def total(hand):
    aces = 0
    total = 0
    for each in hand:
        if (each == "A"):
            aces += 1
        elif (each == "K"):
            total += 10
        elif (each == "Q"):
            total += 10
        elif (each == "J"):
            total += 10
        else:
            total += each
            
    if (aces > 0):
        for each in range(aces):
            if (total + 11 <= 21):
                total += 11
            else:
                total += 1
    
    return total
        
def evaluate(total, opponent):
    if ((total < 17) or (total < opponent)):
        return True
    else:
        return False

    

def dynamic(deck, i):
    options = []
    if (len(deck)-i < 4):
        return 0
    
    for p in range(2, len(deck) - i - 1):
        hand = deal(deck, i)
        dealer = deal(deck, i+1)
        if (len(deck[i+4:i+p+2]) > 0):
            hand += deck[i+4:i+p+2]

        if (total(hand) > 21):
            options.append(-1 + dynamic(deck, i + p + 2)) #bust
            break
        d = 0
        for d in range(2, len(deck)-i-p):
            if (len(deck[i+p+2:i+p+d]) > 0):
                dealer += deck[i+p+2:i+p+d]
            if (total(dealer) >= 17):
                break
        if (total(dealer) > 21): #dealer bust
            dealer = []
        options.append((cmp(total(hand), total(dealer)) + dynamic(deck, i + p + d)))

    return max(options)


def main():
    playing = True
    user = str(raw_input("Autoplay= 1\nDynamic Algorithm = 2\nPlay Blackjack = 3\n>>> "))

    if (user == '1'):
        wallet = 0
        walletArray = []
        totalWinnings = 0
        index = 0
        deck = shuffle()
        deckCount = 0
        while (deckCount < 100):
            if (index+4 > len(deck)): 
                deck = shuffle()
                index = 0
                deckCount += 1
                walletArray.append(wallet)
                totalWinnings += wallet
                wallet = 0
            hand = deal(deck, index)
            dealer = deal(deck, index+1)
            index += 4
            while ((evaluate(total(hand), total(dealer[1:])))and (index < len(deck))):
                hand.append(hit(deck, index))
                index += 1

            if (total(hand) > 21):
                wallet -= 1 #bust
                

            else:
                while ((total(dealer) < 17) and (index < len(deck))):
                    dealer.append(hit(deck, index))
                    index += 1
    
                if (total(dealer) < total(hand)):
                    wallet += 1 #Player has better hand

                elif (total(dealer) == total(hand)):
                       continue #Tie
                    
                elif (total(dealer) > 21):
                    wallet += 1 #Dealer busts
                       
                else:
                    wallet -= 1 #Dealer has better hand

        
        print "Total Autoplay Winnings: $" + str(totalWinnings)
        minimumValue = min(walletArray)-1
        stemPlot = [0] * abs(minimumValue)
        while len(walletArray) > 0:
            stemPlot[abs(walletArray.pop())] += 1
            
        
        print stemPlot
                       
    elif (user == '2'):
        answers = []
        for each in range(100):
            deck = shuffle()
            #print deck
            answers.append(dynamic(deck, 0))

        answers.sort()
        print answers
        maximumValue = max(answers)+1
        print "Total Winnings: $" + str(sum(answers))
        stemPlot = [0] * maximumValue
        while len(answers) > 0:
            stemPlot[answers.pop()] += 1
            
        
        print stemPlot
                       
    else:
        wallet = 0
        while (playing):
            deck = shuffle()
            hand = deal(deck, 0)
            dealer = deal(deck, 2)
            index = 4
            print "Your Hand: " + str(hand)
            print "Dealer showing: " + str(dealer[1])
            response = "Y"
            while ((total(hand) < 21) and response == "Y"):
                response = str(raw_input("\n Do you want to hit? (Y/N) "))
                if (response == "Y"):
                    hand.append(hit(deck, index))
                    index += 1
                    print "Your Hand: " + str(hand)
            if (total(hand) > 21):
                print "BUST! Dealer Wins"
                wallet -= 1
            elif (total(hand) == 21):
                print "Blackjack!!!"

            if (total(hand) <= 21):
                while (evaluate(total(dealer), total(hand[1:]))):
                    dealer.append(hit(deck, index))
                    index += 1
                #print total(dealer)
                if (total(dealer) < total(hand)):
                    print "Dealer's hand is: " + str(dealer)
                    print "YOU WIN!!!"
                    wallet += 1
                elif (total(dealer) == total(hand)):
                    print "Dealer's hand is: " + str(dealer)
                    print "You Tie!"
                elif (total(dealer) > 21):
                    print "Dealer's hand is: " + str(dealer)
                    print "YOU WIN!!!"
                    wallet += 1
                else:
                    print "Dealer's hand is: " + str(dealer)
                    print "You Lost."
                    wallet -= 1

            print "You've made $" + str(wallet)       
            if (str(raw_input("Play Again? ")) == "N"):
                playing = False
                
        
main()
