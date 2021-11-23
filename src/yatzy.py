from dice import Dice
from scorecolumn import ScoreColumn

def play():
    dice = Dice()
    player1 = ScoreColumn(input("Player\'s name: "))
    player2 = ScoreColumn(input("Other player's name: "))
    player1s_turn = True
    while not (player1.is_full() and player2.is_full()):
        if player1s_turn:
            player = player1
            player1s_turn = False
        else:
            player = player2
            player1s_turn = True
        print(player)
        dice.roll()
        print(player.name, "rolled:")
        print(dice)
        while True:
            to_reroll = input("Which dice you want to reroll? (give indices separated by spaces): ").split(" ")
            try:
                for i, s in enumerate(to_reroll):
                    to_reroll[i] = int(s)
                break
            except Exception as e:
                print("Error with rerolling, try again")
                print(e)
        dice.reroll(to_reroll)
        print(player.name, "re-rolled:")
        print(dice)
        scorebox_str = input("Choose score box to use the rolled dice (1-15): ")
        while True:
            try:
                scorebox = int(scorebox_str)
                if 1 <= scorebox <= 15:
                    break
                else:
                    print("Score box index out of range, try again")
            except Exception as e:
                print("Error with choosing score box, try again")
                print(e)
        if 1 <= scorebox <= 6:
            player.check_upper(scorebox, dice.get(), write = True)
        elif scorebox == 7:
            player.check_one_pair(dice.get(), write = True)
        elif scorebox == 8:
            player.check_two_pairs(dice.get(), write = True)
        elif scorebox == 9:
            player.check_three_of_a_kind(dice.get(), write = True)
        elif scorebox == 10:
            player.check_four_of_a_kind(dice.get(), write = True)
        elif scorebox == 11:
            player.check_small_straight(dice.get(), write = True)
        elif scorebox == 12:
            player.check_large_straight(dice.get(), write = True)
        elif scorebox == 13:
            player.check_full_house(dice.get(), write = True)
        elif scorebox == 14:
            player.check_chance(dice.get(), write = True)
        elif scorebox == 15:
            player.check_yatzy(dice.get(), write = True)
        else:
            print("Something went terribly wrong, scorebox index out of range")
        print(player)
        input("Press enter to swap turn...")
    if player1.get_total() > player2.get_total:
        print(player1.name, "won!")
    elif player2.get_total() > player1.get_total:
        print(player2.name, "won!")
    else:
        print("Draw!")
    again = ""
    while not (again == "y" or again == "n"):
        again = input("Play again? [y/n]: ")
    if again == "y":
        play()
    

        