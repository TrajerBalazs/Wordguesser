import random

# 1. Szólista
WORDS = ["alma", "banan", "szilva", "korte", "eper", "dinnye", "narancs"]

def select_random_word():
    """Véletlenszerűen kiválaszt egy szót a WORDS listából."""
    return random.choice(WORDS)

def display_current_state(word, guessed_letters):
    """Megjeleníti a jelenlegi állapotot, a kitalált és a hiányzó betűket."""
    return "".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    # 2. Véletlenszerű szó kiválasztása
    word_to_guess = select_random_word()
    guessed_letters = set()
    attempts_left = 6  # Maximális próbálkozások száma

    print("Üdvözöl a Szókitaláló játék!")
    print("Találd ki a szót betűnként. Maximum 6 hibás próbálkozásod lehet.")

    while attempts_left > 0:
        print(f"\nSzó: {display_current_state(word_to_guess, guessed_letters)}")
        print(f"Próbálkozások száma: {attempts_left}")
        guess = input("Adj meg egy betűt: ").lower()

        # Betűellenőrzés
        if guess in guessed_letters:
            print("Ezt a betűt már próbáltad!")
        elif guess in word_to_guess:
            print("Talált!")
            guessed_letters.add(guess)
            # Győzelem ellenőrzése
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"Gratulálok! Kitaláltad a szót: {word_to_guess}")
                break
        else:
            print("Rossz tipp!")
            guessed_letters.add(guess)
            attempts_left -= 1

        # Vereség ellenőrzése
        if attempts_left == 0:
            print(f"Sajnos vesztettél! A szó: {word_to_guess}")

# 5. Játék indítása
play_game()
