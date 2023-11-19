import random


def get_user():
    while True:
        user_choice = input("Введите камень, ножницы или бумагу! ").lower()
        if user_choice in ["камень", "ножницы", "бумага"]:
            return user_choice
        else:
            print("Некоректный ввод данных, введите камень, ножницы или бумагу! ")


def get_computer():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)


def winner(user, computer):
    if user == computer:
        return "Ничья! "
    elif (
            (user == "камень" and computer == "ножницы") or
            (user == "ножницы" and computer == "бумага") or
            (user == "бумага" and computer == "камень")
    ):
        return "Вы победили"
    else:
        return "Вы проиграли"


def play_game():
    user_wins = 0
    computer_wins = 0
    while user_wins < 3 and computer_wins < 3:
        user = get_user()
        computer = get_computer()
        print(f"Вы выбрали {user}, компьютер выбрал {computer}")
        result = winner(user, computer)
        print(result)
        if result == "Вы победили":
            user_wins += 1
        elif result == "Вы проиграли":
            computer_wins += 1
        print(f"Счет: Вы {user_wins}: {computer_wins} Компьютер\n")
    if user_wins == 3:
        print("Вы выйграли! ")
    else:
        print("Вы проиграли! ")


if __name__ == "__main__":
    play_game()