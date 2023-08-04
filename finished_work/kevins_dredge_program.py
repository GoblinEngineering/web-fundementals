from cProfile import label
import random
import os
import matplotlib.pyplot as plt
#spaceing
deck = []
grave = []
hand = []
chain_resolutions = []
relative_hand_size = []
relative_deck_size = []
relative_grave_size = []
relative_deck_land_size = []
relative_hand_size_land = []
#spaceing
def mill(x):
    global hand, deck, grave, itteration_count
    draw_trigger = False
    for y in range(x):
        try:
            grave.append(deck[0])
        except:
            print(f"card in grave : {len(grave)}")
            print(f"card in deck : {len(deck)}")
            print(f"card in hand : {len(hand)}")
            print(f"you decked yourself {itteration_count} not enough cards in libary to dredge.")
            plot()
            quit()
        deck.pop(0)
        if grave[-1] == "land":
            draw_trigger = True
    #spaceing
    if draw_trigger:
        draw()
    if "titan" in grave:
        titan_shuffle()
#spaceing
def draw():
    global hand, deck, grave, dredger, itteration_count
    if "dredge_card" in grave:
        grave.remove("dredge_card")
        hand.append("dredge_card")
        mill(dredger)
    else:
        try:
            hand.append(deck[0])
        except:
            print(f"card in grave : {len(grave)}")
            print(f"card in deck : {len(deck)}")
            print(f"card in hand : {len(hand)}")
            print(f"you decked yourself {itteration_count} too many draw triggers.")
            plot()
            quit()
        deck.pop(0)
#spaceing
def titan_shuffle():
    global hand, deck, grave
    if "titan" in hand:
        hand.remove("titan")
        grave.append("titan")
    deck = deck + grave
    grave = []
#spaceing
def chain():
    global hand, deck, grave, dredger
    if "titan" in hand:
        mill(2)
        titan_shuffle()
    elif "dredge_card" in hand:
        grave.append("dredge_card")
        hand.remove("dredge_card")
        mill(2)
    elif "land" in hand:
        hand.remove("land")
        grave.append("land")
        mill(2)
        draw()
    elif "blank_card" in hand:
        hand.remove("blank_card")
        grave.append("blank_card")
        mill(2)
    else:
        mill(2)
#spaceing
def plot():
    global chain_resolutions, relative_deck_size, relative_hand_size, relative_deck_land_size, relative_hand_size_land
    # plotting the points  
    plt.plot(chain_resolutions, relative_hand_size, label = "hand size") 
    plt.plot(chain_resolutions, relative_deck_size, label = "deck size")
    plt.plot(chain_resolutions, relative_deck_land_size, label = "lands in deck") 
    plt.plot(chain_resolutions, relative_hand_size_land, label = "lands in hand")
    # plt.plot(chain_resolutions, relative_grave_size) 

    # naming the x axis 
    plt.xlabel('# of chain reolutions') 
    # naming the y axis 
    plt.ylabel('#of cards') 
    
    # giving a title to my graph 
    plt.title('My first graph!') 
    
    plt.legend() 
    # function to show the plot 
    plt.show()
        
        
#spaceing
os.system("cls")
print("Welcome to the bad frog line sim")
print("Please enter the folowing prompts")
print("we are going to assume that dakmor, and a titan are in your list.")
while True:
    try:
        land_count = int(input("How many lands in addition to dakmor do you have in your list? : "))
    except:
        print("Please only enter whole numbers")
    else:
        if land_count > 95:
            print("you have over 95 lands in your deck, please lower that to alow room for the 3 cards we are assumeing are in the deck and our choice dredge card.")
        else:
            break
#spaceing
print()
print(f"we have {land_count} lands in the deck, moving on.")
print()
#spaceing
print("what dredge card do you want to use? enter the letter for the card you are useing")
while True:
    dredger = input("golgari grave-troll ('G'), life from the loam ('L') : ").lower()
    if dredger == "g" or dredger == "l":
        if dredger == "g":
            dredger = 6
        elif dredger == "l":
            dredger = 3
        #spaceing
        break
    else:
        print("Please enter the first letter of the card you are useing.")
#spaceing
print()
print(f"you choose a dredge card with dredge{dredger}")
print()
#spaceing
print("your going to be put into a situation where there is a titan in your deck that you can hit.")
print("you will also have dakmor and the chosen dredge card in hand with a chain of smog on the stack.")
print("additionaly, frog is on the feild.")
#spaceing
for x in range(land_count):
    deck.append("land")
for x in range((94-land_count)):
    deck.append("blank_card")
#spaceing
deck.append("titan")
deck.append("titan")
#sapceing
hand.append("dakmor")
hand.append("dredge_card")
random.shuffle(deck)
#spaceing
itteration_count = 0
for x in range(2000):
    chain()
    print(f"{len(hand)} cards in hand with {len(deck)} cards left")
    itteration_count += 1
    random.shuffle(deck)
    chain_resolutions.append(itteration_count)
    relative_deck_land_size.append(deck.count("land"))
    relative_grave_size.append(len(grave))
    relative_hand_size.append(len(hand))
    relative_deck_size.append(len(deck))
    relative_hand_size_land.append(hand.count("land"))
print(f"card in grave : {len(grave)}")
print(f"card in deck : {len(deck)}")
print(f"card in hand : {len(hand)}")
print(f"{itteration_count} succsessful chain resolutions")
plot()