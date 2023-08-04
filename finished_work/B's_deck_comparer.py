import os
deck_1_list = []
deck_2_list = []
deck_1_cards = []
deck_2_cards = []
with open("junk/decklist copy.txt") as deck1:
    for line in deck1:
        line = line.strip()
        line = line.split("1")
        line = line[-1].strip()
        if line != "":
            deck_1_list.append(line)

#spaceing
with open("junk/decklist.txt") as deck2:
    for line in deck2:
        line = line.strip()
        line = line.split("1")
        line = line[-1].strip()
        if line != "":
            deck_2_list.append(line)

for card in deck_1_list:
    if card not in deck_2_list:
        deck_1_cards.append(card)

for card in deck_2_list:
    if card not in deck_1_list:
        deck_2_cards.append(card)
#spaceing
deck_1_cards.sort()
deck_2_cards.sort()
#spaceing
os.system("cls")
for x in range(100):
    print()
#spaceing
print(f"deck 1 diffrence's ")
for x in deck_1_cards:
    print(x)
print()
#spaceing
print(f"deck 2 diffrence's # ")
for x in deck_2_cards:
    print(x)