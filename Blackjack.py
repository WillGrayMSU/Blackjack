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
    #print i
    for p in range(2, len(deck) - i - 1):
        hand = deal(deck, i)
        dealer = deal(deck, i+1)
        if (len(deck[i+4:i+p+2]) > 0):
            hand += deck[i+4:i+p+2]
        #print i
        #print hand
        #print total(hand)
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
            #print "Dealer Bust: " + str(total(dealer))
        options.append((cmp(total(hand), total(dealer)) + dynamic(deck, i + p + d)))
        #print "i=" + str(i) + ", p=" + str(p) + ", d=" + str(d)
        #cont = raw_input(".")
    #print options
    return max(options)


def main():
    dynamicAlg = False
    if (str(raw_input("Dynamic Algorithm (Y/N) ")) == "Y"):
            dynamicAlg = True
    if (not dynamicAlg):
        while (not dynamicAlg):
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
                elif (total(dealer) == total(hand)):
                    print "Dealer's hand is: " + str(dealer)
                    print "You Tie!"
                elif (total(dealer) > 21):
                    print "Dealer's hand is: " + str(dealer)
                    print "YOU WIN!!!"
                else:
                    print "Dealer's hand is: " + str(dealer)
                    print "You Lost."
                    
            if (str(raw_input("Play Again? ")) == "N"):
                dynamicAlg = True
    else:
        deck = shuffle()
        print deck
        print dynamic(deck, 0)
                
        
main()
