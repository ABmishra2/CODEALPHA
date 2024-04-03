print("Hi, This is my first project of internship with codealpha")
print("creating a hangman game using python")
import tkinter as tk
import random

class Hangman_Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.words = ["python", "hangman", "computer", "programming", "algorithm", "interface", "keyboard", "mouse", "monitor"]
        self.current_word = random.choice(self.words)
        self.guesses = []

        self.word_display = tk.StringVar()
        self.word_display.set("_ " * len(self.current_word))

        self.word_label = tk.Label(self.master, textvariable=self.word_display, font=("Arial", 18))
        self.word_label.pack()

        self.guess_label = tk.Label(self.master, text="Guess a letter:", font=("Arial", 12))
        self.guess_label.pack()

        self.guess_entry = tk.Entry(self.master, font=("Arial", 12))
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess, font=("Arial", 12))
        self.guess_button.pack()

        self.message_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.message_label.pack()

    def make_guess(self):
        guess = self.guess_entry.get().lower()
        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter.")
            return
        if guess in self.guesses:
            self.message_label.config(text="You already guessed that letter.")
            return

        self.guesses.append(guess)
        if guess in self.current_word:
            word_progress = ""
            for letter in self.current_word:
                if letter in self.guesses:
                    word_progress += letter + " "
                else:
                    word_progress += "_ "
            self.word_display.set(word_progress)
            if "_" not in word_progress:
                self.message_label.config(text="Congratulations! You guessed the word.")
        else:
            self.message_label.config(text="Incorrect guess. Try again.")

        self.guess_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    hangman = Hangman_Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()
