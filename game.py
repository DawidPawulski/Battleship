import random
import os
import time
from colorama import Style, Fore

# time.sleep(6)
os.system("clear")


player_1_board = list(range(1, 37))
player_2_board = list(range(1, 37))
ai_board = list(range(1, 37))
player_1_board_position = list(range(1, 37))
player_2_board_position = list(range(1, 37))
ai_random_shooting = list(range(1, 37))

ship1, ship2, ship3 = setting_position_pl_1()

global board_radical


def board_drawing(board):
    board_lenght = len(board)
    board_radical = int(board_lenght**(1/2))
    i = 0
    k = 0
    while i < board_radical:
        j = 0
        print(" | ", end=" ")
        while j < board_radical:
            if len(str(board[k])) == 1:
                print(str("{}".format(board[k])).center(6) + " | ", end=" ")
            else:
                print(str("{}".format(board[k])).center(6) + " | ", end=" ")
            j += 1
            k += 1
        print("\n")
        i += 1


def setting_ships_position(board, ship_class, ship_lenght):
    while True:
        try:
            i = 0

            position = input("Set the position of your {}: ".format(ship_class))
            position = position.split(" ")
            if len(position) != int(ship_lenght):
                print(f"It must be {ship_lenght} values")
                continue

            for i in range(int(ship_lenght)-1):
                if int(position[i])+1 != int(position[i+1]) and int(position[i])+6 != int(position[i+1]):
                    print("\t Every position must be next to each other!! ")
                    break

            if int(position[i])+1 != int(position[i+1]) and int(position[i])+6 != int(position[i+1]):
                continue

            str(position)

            for n in position:
                # boom = u"\U0001F4A5"
                # ship = u"\U0001F6A2"
                board[int(n)-1] = "+"
            return position
        except ValueError:
            print("Please write only integers!")
            continue
        except IndexError:
            print("Number must be between 1 and 36")
            continue  # to delete


def setting_position_pl_1():
    print("Player 1 please enter position of your ships")
    ships_4_position_player_1 = setting_ships_position(player_1_board_position, "aircraft carrier", "4")

    ship_3_position_player_1 = setting_ships_position(player_1_board_position, "destroyer", "3")

    ship_2_position_player_1 = setting_ships_position(player_1_board_position, "submarine", "2")

    return ships_4_position_player_1, ship_2_position_player_1, ship_3_position_player_1

def setting_position_pl_2():
    print("Player 2 please enter position of your ships")

    global ships_4_position_player_2
    ships_4_position_player_2 = setting_ships_position(player_2_board_position, "aircraft carrier", "4")

    global ship_3_position_player_2
    ship_3_position_player_2 = setting_ships_position(player_2_board_position, "destroyer", "3")

    global ship_2_position_player_2
    ship_2_position_player_2 = setting_ships_position(player_2_board_position, "submarine", "2")


def setting_position_ai():

    horizontal_or_vertical = [1, 0]

    position_ships_4_list_vert = [1, 7, 13, 2, 8, 14, 3, 9, 15, 4, 10, 16, 5, 11, 17, 6, 12, 18]

    position_ship_3_list_vert = [1, 7, 13, 2, 8, 14, 3, 9, 15, 4, 10, 16, 5, 11, 17, 6, 12, 18, 19, 20, 21, 22, 23, 24]

    position_ship_2_list_vert = [1, 7, 13, 2, 8, 14, 3, 9, 15, 4, 10, 16, 5, 11, 17, 6, 12, 18, 19, 20, 21, 22, 23, 24,
                                 25, 26, 27, 28, 29, 30]

    position_ships_4_list_horiz = [1, 2, 3, 7, 8, 9, 13, 14, 15, 19, 20, 21, 25, 26, 27, 31, 32, 33]

    position_ship_3_list_horiz = [1, 2, 3, 4, 7, 8, 9, 10, 13, 14, 15, 16, 19, 20, 21, 22, 25, 26, 27,
                                  28, 31, 32, 33, 34]

    position_ship_2_list_horiz = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22,
                                  23, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35]

    random_direction_s4 = random.choice(horizontal_or_vertical)

    global ships_4_ai_position
    if random_direction_s4 == 1:
        random_num = random.choice(position_ships_4_list_horiz)
        ships_4_first_position = ai_random_shooting[random_num-1]
        ships_4_ai_position = [str(ships_4_first_position), str(ships_4_first_position+1),
                               str(ships_4_first_position+2), str(ships_4_first_position+3)]
    elif random_direction_s4 == 0:
        random_num = random.choice(position_ships_4_list_vert)
        ships_4_first_position = ai_random_shooting[random_num-1]
        ships_4_ai_position = [str(ships_4_first_position), str(ships_4_first_position+6),
                               str(ships_4_first_position+12), str(ships_4_first_position+18)]

    for n in ships_4_ai_position:
        if n in position_ship_3_list_horiz:
            position_ship_3_list_horiz.remove(n)
        if n in position_ship_3_list_vert:
            position_ship_3_list_vert.remove(n)
        if n in position_ship_2_list_horiz:
            position_ship_2_list_horiz.remove(n)
        if n in position_ship_2_list_vert:
            position_ship_2_list_vert.remove(n)

    running = True
    while running:
        random_direction_s3 = random.choice(horizontal_or_vertical)
        global ship_3_ai_position
        if random_direction_s3 == 1:
            random_num = random.choice(position_ship_3_list_horiz)
            ship_3_first_position = ai_random_shooting[random_num-1]
            ship_3_ai_position = [str(ship_3_first_position), str(ship_3_first_position+1),
                                  str(ship_3_first_position+2)]
            for n in ship_3_ai_position:
                if n in ships_4_ai_position:
                    continue
            running = False
        elif random_direction_s3 == 0:
            random_num = random.choice(position_ship_3_list_vert)
            ship_3_first_position = ai_random_shooting[random_num-1]
            ship_3_ai_position = [str(ship_3_first_position), str(ship_3_first_position+6),
                                  str(ship_3_first_position+12)]
            for n in ship_3_ai_position:
                if n in ships_4_ai_position:
                    continue
            break

    for n in ship_3_ai_position:
        if n in position_ship_2_list_horiz:
            position_ship_2_list_horiz.remove(n)
        if n in position_ship_2_list_vert:
            position_ship_2_list_vert.remove(n)

    while True:
        random_direction_s2 = random.choice(horizontal_or_vertical)
        global ship_2_ai_position
        if random_direction_s2 == 1:
            random_num = random.choice(position_ship_2_list_horiz)
            ship_2_first_position = ai_random_shooting[random_num-1]
            ship_2_ai_position = [str(ship_2_first_position), str(ship_2_first_position+1)]
            for n in ship_2_ai_position:
                if n in ships_4_ai_position:
                    continue
                if n in ship_3_ai_position:
                    continue
            break
        elif random_direction_s2 == 0:
            random_num = random.choice(position_ship_2_list_vert)
            ship_2_first_position = ai_random_shooting[random_num-1]
            ship_2_ai_position = [str(ship_2_first_position), str(ship_2_first_position+6)]
            for n in ship_2_ai_position:
                if n in ships_4_ai_position:
                    continue
                if n in ship_3_ai_position:
                    continue
            break

    print("Computer picked position for his ships")


def players_shooting(which_player, opponents_board, score_board, ships_4, ship_3, ship_2):
    i = 0
    print("(PLAYER {})BOARD WHEN YOU SHOOT EARLIER".format(which_player))
    board_drawing(opponents_board)
    shoot_board = []
    while i < 3:
        while True:
            try:
                player_input = input("(PLAYER {})Where you shoot: ".format(which_player))
                int(player_input)
                if int(player_input) in range(1, 37):
                    shoot_board.append(player_input)
                    break
                else:
                    print("Number must be between 1 and 36")
                    continue
            except ValueError:
                print("Please write only integers!")
                continue
        hit = "X".center(6)
        miss = "0".center(6)
        if shoot_board[i] in ships_4:
            opponents_board[int(shoot_board[i])-1] = f"{Fore.GREEN}{hit}{Style.RESET_ALL}"
            print("\n\n YOU HIT!")
            ships_4.remove(shoot_board[i])
            ships_sinked(ships_4, ship_3, ship_2)
            score_board = int(score_board)+1
        elif shoot_board[i] in ship_3:
            opponents_board[int(shoot_board[i])-1] = f"{Fore.GREEN}{hit}{Style.RESET_ALL}"
            print("\n\n YOU HIT!")
            ship_3.remove(shoot_board[i])
            ships_sinked(ships_4, ship_3, ship_2)
            score_board = int(score_board)+1
        elif shoot_board[i] in ship_2:
            opponents_board[int(shoot_board[i])-1] = f"{Fore.GREEN}{hit}{Style.RESET_ALL}"
            print("\n YOU HIT!")
            ship_2.remove(shoot_board[i])
            ships_sinked(ships_4, ship_3, ship_2)
            score_board = int(score_board)+1
        else:
            opponents_board[int(shoot_board[i])-1] = f"{Fore.RED}{miss}{Style.RESET_ALL}"
            print("\n\n YOU MISSED")
        board_drawing(opponents_board)
        time.sleep(1)
        i += 1

        if int(score_board) == 9:
            print("\n\n PLAYER {} ARE WINNER!!".format(which_player))
            break
    return score_board


def ships_sinked(ship_4, ship_3, ship_2):
    if len(ship_4) == 0:
        print("\n AIRCRAFT CARRIER SINKED \n")
        ship_4.append("Sinked")
    if len(ship_3) == 0:
        print("\n DESTROYER SINKED \n")
        ship_3.append("Sinked")
    if len(ship_2) == 0:
        print("\n SUBMARINE SINKED \n")
        ship_2.append("Sinked")


def two_players():

    board_drawing(player_1_board_position)
    setting_position_pl_1()
    board_drawing(player_1_board_position)

    time.sleep(2)
    os.system("clear")

    board_drawing(player_2_board_position)
    setting_position_pl_2()
    board_drawing(player_2_board_position)

    time.sleep(2)
    os.system("clear")

    score_player_1 = 0
    score_player_2 = 0

    while True:

        score_player_1 = players_shooting("1", player_2_board, score_player_1, ships_4_position_player_2,
                                          ship_3_position_player_2, ship_2_position_player_2)

        if int(score_player_1) == 9:
            break

        score_player_2 = players_shooting("2", player_1_board, score_player_2, ships_4_position_player_1,
                                          ship_3_position_player_1, ship_2_position_player_1)

        if int(score_player_2) == 9:
            break


def play_against_ai():

    board_drawing(player_1_board_position)
    setting_position_pl_1()
    board_drawing(player_1_board_position)

    time.sleep(2)
    os.system("clear")

    setting_position_ai()

    score_player_1 = 0
    score_ai = 0

    while True:
        score_player_1 = players_shooting("1", ai_board, score_player_1, ships_4_ai_position,
                                          ship_3_ai_position, ship_2_ai_position)

        if int(score_player_1) == 9:
            break

        ai_shoot_list = []
        j = 0
        print("(AI)BOARD WHEN AI SHOOT EARLIER")
        board_drawing(player_1_board)
        time.sleep(3)
        previous_hit = 0
        while int(j) < 3:
            try:
                if previous_hit == 1:
                    previous_shoot = int(ai_shoot_list[j-1])
                    while True:
                        try:
                            ai_shoot = random.choice([previous_shoot+1, previous_shoot+6, previous_shoot-1, previous_shoot-6])
                            ai_random_shooting.remove(ai_shoot)
                        except ValueError:
                            continue
                        break
                elif previous_hit == 0:
                    ai_shoot = random.choice(ai_random_shooting)
                    ai_random_shooting.remove(ai_shoot)
            except UnboundLocalError:
                pass
            
            ai_shoot_list.append(ai_shoot)
            print("AI shooted at position {}".format(ai_shoot))
            hit = "X".center(6)
            miss = "0".center(6)
            if str(ai_shoot_list[j]) in ships_4_position_player_1:
                player_1_board[int(ai_shoot_list[j])-1] = f"{Fore.GREEN}{hit}{Style.RESET_ALL}"
                ships_4_position_player_1.remove(str(ai_shoot_list[j]))
                ships_sinked(ships_4_position_player_1, ship_3_position_player_1, ship_2_position_player_1)
                print("\n AI HIT! \n")
                score_ai = int(score_ai)+1
                previous_hit = 1
            elif str(ai_shoot_list[j]) in ship_3_position_player_1:
                player_1_board[int(ai_shoot_list[j])-1] = f"{Fore.GREEN}{hit}{Style.RESET_ALL}"
                ship_3_position_player_1.remove(str(ai_shoot_list[j]))
                ships_sinked(ships_4_position_player_1, ship_3_position_player_1, ship_2_position_player_1)
                print("\n AI HIT! \n")
                score_ai = int(score_ai)+1
                previous_hit = 1
            elif str(ai_shoot_list[j]) in ship_2_position_player_1:
                player_1_board[int(ai_shoot_list[j])-1] = f"{Fore.GREEN}{hit}{Style.RESET_ALL}"
                ship_2_position_player_1.remove(str(ai_shoot_list[j]))
                ships_sinked(ships_4_position_player_1, ship_3_position_player_1, ship_2_position_player_1)
                print("\n AI HIT! \n")
                score_ai = int(score_ai)+1
                previous_hit = 1
            else:
                player_1_board[int(ai_shoot_list[j])-1] = f"{Fore.RED}{miss}{Style.RESET_ALL}"
                print("\n AI MISSED \n")
                previous_hit = 0
            board_drawing(player_1_board)
            time.sleep(4)
            j = int(j)+1
            if int(score_ai) == 9:
                print("AI ARE WINNER!! \n")
                break
        if int(score_ai) == 9:
            break


def game_choose():
    while True:
        print("Would you like to play against AI or another Player?")
        options = ['1', '2']
        choose = input("Choose 1 for AI and 2 for Two Players: ")
        if choose not in options:
            print('Please input only 1 or 2')
            continue
        elif choose in options:
            break
    if choose == "1":
        play_against_ai()
    elif choose == "2":
        two_players()


def menu():
    while True:
        choose = input("""\n
───│─────────────────────────────────────
───│────────▄▄───▄▄───▄▄───▄▄───────│────
───▌────────▒▒───▒▒───▒▒───▒▒───────▌────
───▌──────▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄─────▌────
───▌────▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄───▋────
▀█████████████1 START GAME█████████████▄─
──▀████████████2 TUTORIAL█████████████▀──
─────▀██████████3 CREDITS███████████▀────
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒4 QUIT▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
\n
""")
        if choose == '1':
            game_choose()
        elif choose == '2':
            tutorial()
        elif choose == '3':
            credits_4()
        elif choose == '4':
            quit_game()
        else:
            print('Please select 1, 2, 3 or 4')


def back():
    choose_1 = input("Press ENTER for MENU\n")
    if choose_1 is True:
        menu()


def tutorial():
    print('''\n
        The game is played on four boards, two for each player,\n
        first player must place his ships on board coordinates.\n
        Place 4 coordinates next to eachother for "Aircraft Carrier",\n
        3 for "Destroyer" and 2 for "Submarine".\n
        Your coordinates should be placed from lowest to highest.\n
        You can set your ships horizonatally or vertically.\n
        After ships are placed by both players, shooting phase begins.\n
        First player shoots first and strikes 3 times, each HIT is marked as "X" and MISSED "O"\n
        Game ends when one of the players hits all enemy ships coordinates''')
    back()


def credits_4():
    print('''\n
    Game Designers:
    1. Dawid Pawulski\n
    2. Wojciech Adamowski\n
    3. Tomasz Sikorski\n
    4. Marek Śmiałowski\n''')
    back()


def quit_game():
    exit(0)


menu()
game_choose()
