import random

def roll():
    min_score = 1
    max_score = 6
    roll = random.randint(min_score, max_score)

    return roll

while True:
    players = input("Wprowadź ilość graczy od 2 - 4: ")

    if players.isdigit():
        players = int(players)

        if 2 <= players <= 4:
            break
        else:
            print("Musisz wybrać od 2 - 4 graczy!")

    else:
        print("Wprowadzono błędną wartość. Spróbuj ponownie!")


max_score = 50
players_score = [0 for _ in range(players)]

while max_score > max(players_score):
    for players_idx in range(players):
        print(f"\nGracz o numerze {players_idx + 1} rozpoczął swoją turę!")
        print(f"Twój ogólny wynik wynosi: {players_score[players_idx]}\n")
        current_score = 0
        while True:
            should_roll = input("Czy chcesz losować? (t/n)\n")
            if should_roll != 't':
                break
            value = roll()
            if value == 1:
                print('Wylosowałeś 1! Koniec Twojwj tury!')
                current_score = 0
                break
            else:
                current_score += value
                print(f'Wylosowałeś: {value}!')

            print(f'Twój aktualny wynik podczas tej tury wynosi: {current_score}.')

        players_score[players_idx] += current_score
        print(f'Twój ogólny wynik wynosi: {players_score[players_idx]}')

max_score = max(players_score)
winning_idx = players_score.index(max_score)
print(f"Zwycięzcą gry jest {winning_idx + 1}! Gratulacje!")

