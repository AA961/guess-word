import requests
import random


def get_random_word(length):
    url = f"https://random-word-api.herokuapp.com/word?number=1&length={
        length}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data[0]
    else:
        print(f"Error fetching random word from the API. Status code: {
              response.status_code}")
        return None


def reset_game():
    again = input("Game Over, Wanna Play Again? Enter Yes: ").lower()
    if again == "yes":
        play_game()


def initialize_game():
    correct_ans = ""
    digit = input(
        "How many letters Word you wanna Guess?: ")

    correct_ans = get_random_word(digit)
    if not correct_ans:
        print("Failed to fetch a word. Exiting.")
        exit()

    hint = random.randint(0, len(correct_ans)-1)
    progress = ["_"] * len(correct_ans)
    progress[hint] = correct_ans[hint]
    print(progress)
    #print(correct_ans)
    return correct_ans, progress


def play_game():
    Tries = 5
    correct_ans, progress = initialize_game()

    while "_" in progress and Tries > 0:
        ans = input("Enter The Word: ").lower()
        if ans in correct_ans:
            for i in range(len(correct_ans)):
                if ans == correct_ans[i]:
                    progress[i] = ans
            print(progress)

            if correct_ans.count(ans) > 1:
                        continue
        else:
            print("Incorrect Guess: Try Again,", progress)
            Tries -= 1
            print("Tries Left:", Tries, "\n")

    if "_" not in progress:
        print("Congrats you won!")
        reset_game()
    else:
        print("You Used all of your tries & you lost. Correct ans was:", correct_ans)
        reset_game()
play_game()
