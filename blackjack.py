import random
print(""" ___   ___
|A  | |10 |
| ♣ | | ♦ |
|__A| |_10|
 
        _     _            _    _            _    
        | |   | |          | |  (_)          | |   
        | |__ | | __ _  ___| | ___  __ _  ___| | __
        | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        | |_) | | (_| | (__|   <| | (_| | (__|   < 
        |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                            _/ |                
                            |__/                             """)
def deal_card():
    cards =[11 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,10 ,10 ,10]
    card =random.choice(cards)
    return card

user_cards =[]
comp_cards =[]

isGameOver = False

for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())

def calculate_score(cards):
    return sum(cards)
    if sum (cards) ==  21 and len (cards) == 2 :   #only 2 cards are there i.e. ace & a blackjack
        return  0

    if 11 in cards and sum (cards) > 21 :   #we're choosing ace as 1 and not as 11 over here
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(user_score , comp_score):
    if user_score == comp_score:
        return "NEVERMIND, IT'S A DRAW"
    elif user_score > 21:
        return "CONGRATS, YOU WIN!"
    elif comp_score > 21 :
        return "YOU LOSE!!"
    elif comp_score == 0:
        return "WIN, WITH A BLACKJACK"
    elif user_score == 0:
        return "LOSE, OPPONENT HAS A BLACKJACK"
    elif user_score > comp_score :
      return "CONGRATS, YOU WIN!"
    elif user_score < comp_score:
        return "YOU LOSE!!"



while not isGameOver:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    print(f"      Your cards: {user_cards}  ||  Current score: {user_score} ")
    print(f"Computer's cards: {comp_cards}  ||  Current score: {comp_score}")
    while comp_score != 0 and comp_score < 17 :
        comp_cards.append(deal_card())
        comp_score = calculate_score(comp_cards)

    if user_score == 0 or comp_score == 0 or user_score > 21:
        isGameOver = True
    else:
        user_should_deal = input("Type 'y' to get another card or 'n' to pass:   ")
        if user_should_deal =='y':
            user_cards.append(deal_card())
        else:
            isGameOver = True


