"""
Instructions:

The dice game Yacht is from the same family as Poker Dice, Generala and particularly Yahtzee, of which it is a precursor. In the game, five dice are rolled and the result can be entered in any of twelve categories. The score of a throw of the dice depends on category chosen.
If the dice do not satisfy the requirements of a category, the score is zero. If, for example, Four Of A Kind is entered in the Yacht category, zero points are scored. A Yacht scores zero if entered in the Full House category.

Task
Given a list of values for five dice and a category, your solution should return the score of the dice for that category. 
If the dice do not satisfy the requirements of the category your solution should return 0. 
You can assume that five values will always be presented, and the value of each will be between one and six inclusively. You should not assume that the dice are ordered.
"""

# Globals
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    total_score = 0
    if category == YACHT:
        if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
            total_score += 50
    elif category == ONES:
        total_score += dice.count(1)
    elif category == TWOS:
        total_score += dice.count(2) * 2
    elif category == THREES:
        total_score += dice.count(3) * 3
    elif category == FOURS:
        total_score += dice.count(4) * 4
    elif category == FIVES:
        total_score += dice.count(5) * 5
    elif category == SIXES:
        total_score += dice.count(6) * 6
    elif category == FULL_HOUSE:
        list_ = [i for i in dice if dice.count(i) == 2 or dice.count(i) == 3]
        if len(list_) == 5:
            total_score += dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
    elif category == FOUR_OF_A_KIND:
        list_ = [i for i in dice if dice.count(i) > 3]
        if not list_ == []:
            total_score += list_[0] * 4
    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            total_score += 30
    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            total_score += 30
    elif category == CHOICE:
        total_score += dice[0] + dice[1] + dice[2] + dice[3] + dice[4]
    return total_score
