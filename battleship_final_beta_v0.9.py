import sys
import random
import os
import time
from colorama import Style, Fore

# time.sleep(6)
os.system("clear")

player_1_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                  21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
player_2_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                  21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

ai_board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

player_1_board_position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
player_2_board_position = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

ai_random_shooting = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                      21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]


def boards_drawing(board, number):
    i = number - 6
    while i < number:
        if len(str(board[i])) == 1:
            print(str(" {}".format(board[i])) + " | ", end=" ")
        else:
            print(str("{}".format(board[i])) + " | ", end=" ")

        i += 1
    print("\n")


def print_player_1_board_position():
    boards_drawing(player_1_board_position, 6)
    boards_drawing(player_1_board_position, 12)
    boards_drawing(player_1_board_position, 18)
    boards_drawing(player_1_board_position, 24)
    boards_drawing(player_1_board_position, 30)
    boards_drawing(player_1_board_position, 36)
    print("\n")


def print_player_1_board():
    boards_drawing(player_1_board, 6)
    boards_drawing(player_1_board, 12)
    boards_drawing(player_1_board, 18)
    boards_drawing(player_1_board, 24)
    boards_drawing(player_1_board, 30)
    boards_drawing(player_1_board, 36)
    print("\n")


def print_player_2_board():
    boards_drawing(player_2_board, 6)
    boards_drawing(player_2_board, 12)
    boards_drawing(player_2_board, 18)
    boards_drawing(player_2_board, 24)
    boards_drawing(player_2_board, 30)
    boards_drawing(player_2_board, 36)
    print("\n")


def print_player_2_board_position():
    boards_drawing(player_2_board_position, 6)
    boards_drawing(player_2_board_position, 12)
    boards_drawing(player_2_board_position, 18)
    boards_drawing(player_2_board_position, 24)
    boards_drawing(player_2_board_position, 30)
    boards_drawing(player_2_board_position, 36)
    print("\n")


def print_ai_board():
    boards_drawing(ai_board, 6)
    boards_drawing(ai_board, 12)
    boards_drawing(ai_board, 18)
    boards_drawing(ai_board, 24)
    boards_drawing(ai_board, 30)
    boards_drawing(ai_board, 36)
    print("\n")


def setting_position_pl_1():
    print("Player 1 please enter position of your ships")
    while True:
        try:
            global s4_position_player_1
            s4_position_player_1 = input("Set the position of your aircraft carrier: ")
            s4_position_player_1 = s4_position_player_1.split(" ")
            if len(s4_position_player_1) != 4:
                print("It must be 4 values")
                continue
            for n in s4_position_player_1:
                player_1_board_position[int(n)-1] = "+"
            break
        except ValueError:
            print("Please write only integers!")
            continue
        except IndexError:
            print("Number must be between 1 and 36")
            continue  # to delete

    while True:
        try:
            global s3_position_player_1
            s3_position_player_1 = input("Set the position of your destroyer : ")
            s3_position_player_1 = s3_position_player_1.split(" ")
            if len(s3_position_player_1) != 3:
                print("It must be 3 values")
                continue
            for n in s3_position_player_1:
                player_1_board_position[int(n)-1] = "+"

            break
        except ValueError:
            print("Please write only integers!")
            continue
        except IndexError:
            print("Number must be between 1 and 36")
            continue

    while True:
        try:
            global s2_position_player_1
            s2_position_player_1 = input("Set the position of your submarine : ")
            s2_position_player_1 = s2_position_player_1.split(" ")
            if len(s2_position_player_1) != 2:
                print("It must be 2 values")
                continue
            for n in s2_position_player_1:
                player_1_board_position[int(n)-1] = "+"
            break
        except ValueError:
            print("Please write only integers!")
            continue
        except IndexError:
            print("Number must be between 1 and 36")
            continue


def setting_position_pl_2():
    print("Player 2 please enter position of your ships")
    while True:
        try:
            global s4_position_player_2
            s4_position_player_2 = input("Set the position of your aircraft carrier: ")
            s4_position_player_2 = s4_position_player_2.split(" ")
            if len(s4_position_player_2) != 4:
                print("It must be 4 values")
                continue
            for n in s4_position_player_2:
                player_2_board_position[int(n)-1] = "+"
            break
        except ValueError:
            print("Please write only integers!")
            continue
        except IndexError:
            print("Number must be between 1 and 36")
            continue

    while True:
        try:
            global s3_position_player_2
            s3_position_player_2 = input("Set the position of your destroyer : ")
            s3_position_player_2 = s3_position_player_2.split(" ")
            if len(s3_position_player_2) != 3:
                print("It must be 3 values")
                continue
            for n in s3_position_player_2:
                player_2_board_position[int(n)-1] = "+"
            break
        except ValueError:
            print("Please write only integers!")
            continue
        except IndexError:
            print("Number must be between 1 and 36")
            continue

    while True:
        try:
            global s2_position_player_2
            s2_position_player_2 = input("Set the position of your submarine : ")
            s2_position_player_2 = s2_position_player_2.split(" ")
            if len(s2_position_player_2) != 2:
                print("It must be 2 values")
                continue
            for n in s2_position_player_2:
                player_2_board_position[int(n)-1] = "+"
            break
        except ValueError:
            print("Please write only integers!")
            continue
        except IndexError:
            print("Number must be between 1 and 36")
            continue


def setting_position_ai():

    position_s4_list = [1, 2, 3, 7, 8, 9, 13, 14, 15, 19, 20, 21, 25, 26, 27, 31, 32, 33]

    position_s3_list = [1, 2, 3, 4, 7, 8, 9, 10, 13, 14, 15, 16, 19, 20, 21, 22, 25, 26, 27,
                        28, 31, 32, 33, 34]

    position_s2_list = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22,
                        23, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35]

    random_num = random.choice(position_s4_list)
    s4_first_position = ai_random_shooting[random_num-1]
    global s4_ai_position
    s4_ai_position = [s4_first_position, s4_first_position+1, s4_first_position+2,
                      s4_first_position+3]

    for n in s4_ai_position:
        if n in position_s3_list:
            position_s3_list.remove(n)
        if n in position_s2_list:
            position_s2_list.remove(n)

    random_num = random.choice(position_s3_list)
    s3_first_position = ai_random_shooting[random_num-1]
    global s3_ai_position
    s3_ai_position = [s3_first_position, s3_first_position+1, s3_first_position+2]

    for n in s3_ai_position:
        if n in position_s2_list:
            position_s2_list.remove(n)

    random_num = random.choice(position_s2_list)
    s2_first_position = ai_random_shooting[random_num-1]
    global s2_ai_position
    s2_ai_position = [s2_first_position, s2_first_position+1]

    print("Computer picked position for his ships")


# warunek po pierwszej podanej wartości - malejący albo rosnący ciąg arytmetyczny (4, 3 i 2 wyrazowy) z różnicą 1 albo 6


def two_players():

    print_player_1_board_position()

    setting_position_pl_1()

    print_player_1_board_position()

    time.sleep(2)
    os.system("clear")

    print_player_2_board_position()

    setting_position_pl_2()

    print_player_2_board_position()

    time.sleep(2)
    os.system("clear")

    score_player_1 = 0
    score_player_2 = 0
    l = 0

    while l < 1:
        player_1_shoot = []
        i = 0
        print("(PLAYER 1)BOARD WHEN YOU SHOOT EARLIER")
        print_player_2_board()
        while int(i) < 3:
            while True:
                try:
                    player_1_input = input("(PLAYER 1)Where you shoot: ")
                    int(player_1_input)
                    if int(player_1_input) in range(1, 37):
                        player_1_shoot.append(player_1_input)
                        break
                    else:
                        print("Number must be between 1 and 36")
                        continue
                except ValueError:
                    print("Please write only integers!")
                    continue
                # except IndexError:
                #     print("Number must be between 1 and 36")
                #     continue

            if player_1_shoot[i] in s4_position_player_2 or player_1_shoot[i] in s3_position_player_2 \
               or player_1_shoot[i] in s2_position_player_2:
                player_2_board[int(player_1_shoot[i])-1] = f"{Fore.GREEN}X{Style.RESET_ALL}"
                print("\n\n YOU HIT!")
                score_player_1 = int(score_player_1)+1
            else:
                player_2_board[int(player_1_shoot[i])-1] = f"{Fore.RED}0{Style.RESET_ALL}"
                print("\n\n YOU MISSED")
            print_player_2_board()
            time.sleep(1)
            i = int(i)+1

            if int(score_player_1) == 9:
                print("\n\n PLAYER 1 ARE WINNER!!")
                break
        if int(score_player_1) == 9:
            break

        player_2_shoot = []
        j = 0
        print("(PLAYER 2)BOARD WHEN YOU SHOOT EARLIER")
        print_player_1_board()
        while int(j) < 3:
            while True:
                try:
                    player_2_input = input("(PLAYER 2)Where you shoot: ")
                    int(player_2_input)
                    if int(player_2_input) in range(1, 37):
                        player_2_shoot.append(player_2_input)
                        break
                    else:
                        print("Number must be between 1 and 36")
                        continue
                except ValueError:
                    print("Please write only integers!")
                    continue
                # except IndexError:
                #     print("Number must be between 1 and 36")
                #     continue

            if player_2_shoot[j] in s4_position_player_1 or player_2_shoot[j] in s3_position_player_1 \
               or player_2_shoot[j] in s2_position_player_1:
                player_1_board[int(player_2_shoot[j])-1] = f"{Fore.GREEN}X{Style.RESET_ALL}"
                print("YOU HIT!")
                score_player_2 = int(score_player_2)+1
            else:
                player_1_board[int(player_2_shoot[j])-1] = f"{Fore.RED}0{Style.RESET_ALL}"
                print("YOU MISSED")
            print_player_1_board()
            time.sleep(1)
            j = int(j)+1

            if int(score_player_2) == 9:
                print("PLAYER 2 ARE WINNER!!")
                break
        if int(score_player_2) == 9:
            break


def play_against_ai():

    print_player_1_board_position()

    setting_position_pl_1()

    print_player_1_board_position()

    time.sleep(2)
    os.system("clear")

    setting_position_ai()

    score_player_1 = 0
    score_ai = 0
    l = 0
    while l < 1:
        player_1_shoot = []
        i = 0
        print("(PLAYER 1)BOARD WHEN YOU SHOOT EARLIER")
        print_ai_board()
        while int(i) < 3:
            while True:
                try:
                    player_1_input = input("(PLAYER 1)Where you shoot: ")
                    int(player_1_input)
                    if int(player_1_input) in range(1, 37):
                        player_1_shoot.append(player_1_input)
                        break
                    else:
                        print("Number must be between 1 and 36")
                        continue
                except ValueError:
                    print("Please write only integers!")
                    continue

            if int(player_1_shoot[i]) in s4_ai_position or int(player_1_shoot[i]) in s3_ai_position \
               or int(player_1_shoot[i]) in s2_ai_position:
                ai_board[int(player_1_shoot[i])-1] = f"{Fore.GREEN} X{Style.RESET_ALL}"
                print("\n\n YOU HIT! \n")
                score_player_1 = int(score_player_1)+1
            else:
                ai_board[int(player_1_shoot[i])-1] = f"{Fore.RED} 0{Style.RESET_ALL}"
                print("\n\n YOU MISSED \n")
            print_ai_board()
            time.sleep(1)
            i = int(i)+1

            if int(score_player_1) == 9:
                print("PLAYER 1 ARE WINNER!!")
                break

        if int(score_player_1) == 9:
            break

        ai_shoot_list = []
        j = 0
        print("(AI)BOARD WHEN AI SHOOT EARLIER")
        print_player_1_board()
        time.sleep(3)
        while int(j) < 3:
            ai_shoot = random.choice(ai_random_shooting)
            ai_random_shooting.remove(ai_shoot)
            ai_shoot_list.append(ai_shoot)
            print("AI shooted at position {}".format(ai_shoot))

            if str(ai_shoot_list[j]) in s4_position_player_1 or str(ai_shoot_list[j]) in s3_position_player_1 \
               or str(ai_shoot_list[j]) in s2_position_player_1:
                player_1_board[int(ai_shoot_list[j])-1] = f"{Fore.GREEN} X{Style.RESET_ALL}"
                print("\n AI HIT! \n")
                score_ai = int(score_ai)+1
            else:
                player_1_board[int(ai_shoot_list[j])-1] = f"{Fore.RED} 0{Style.RESET_ALL}"
                print("\n AI MISSED \n")
            print_player_1_board()
            time.sleep(4)
            j = int(j)+1

            if int(score_ai) == 9:
                print("AI ARE WINNER!!")
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


game_choose()
