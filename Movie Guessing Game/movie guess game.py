# https://www.youtube.com/watch?v=mbImkkJFxBs
from movies import movies
import random
import string

def get_movie(movies):
    movie = random.choice(movies)  
    while '-' in movie or ' ' in movie:
        movie = random.choice(movie)

    return movie.upper()

def guess():
    movie = get_movie(movies)
    movie_letters = set(movie)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 9

    while len(movie_letters) > 0 and lives > 0:

        print(f"\nYou have {lives} lives left and have used these letters:", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in movie]
        print("Current word", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in movie_letters:
                movie_letters.remove(user_letter)
            else:
                lives -= 1
        elif user_letter in used_letters:
            print("You have already guessed the letter. Try another.")
        else:
            print("Invalid character. Try again.")

    if lives == 0:
        print(f"\nOops, you're out of lives. The movie was {movie}!")
    else:
        print(f"\nBravo! You won. It's {movie}")
        print("You're a Movie Geek!")

if __name__ == "__main__":
    guess()