import random


def get_and_validate_user_input():
    while True:
        user_choice = input("Введите камень, ножницы или бумагу:\n").lower()
        if user_choice in ["камень", "ножницы", "бумага"]:
            return user_choice
        else:
            print("Некорректный ввод данных, введите камень, ножницы или бумагу! ")


def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья! "
    elif (
            (user_choice == "камень" and computer_choice == "ножницы") or
            (user_choice == "ножницы" and computer_choice == "бумага") or
            (user_choice == "бумага" and computer_choice == "камень")
    ):
        return "Вы победили"
    else:
        return "Вы проиграли"


def play_game():
    user_wins = 0
    computer_wins = 0
    while user_wins < 3 and computer_wins < 3:
        user = get_and_validate_user_input()
        computer = get_computer_choice()
        print(f"Вы выбрали {user}, компьютер выбрал {computer}")
        result = get_winner(user, computer)
        print(result)
        if result == "Вы победили":
            user_wins += 1
        elif result == "Вы проиграли":
            computer_wins += 1
        print(f"Счет: Вы {user_wins}: {computer_wins} Компьютер\n")
    if user_wins == 3:
        print("Вы выиграли! ")
    else:
        print("Вы проиграли! ")


if __name__ == "__main__":
    play_game()
