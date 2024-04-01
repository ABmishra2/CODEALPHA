print("Hi, This is my first project of internship with codealpha")
print("creating a hangman game using python")
import random
import tkinter as tk


root = tk.Tk()
root.title("Hangman")


canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

words = ["Python","DataScience","ML","AI","JAVA","DSA","C"]

secret_word = random.choice(words)


incorrect_guesses = 0


def create_hangman():

  canvas.create_line(100, 100, 100, 200)
  canvas.create_line(100, 100, 200, 100)

  canvas.create_oval(100, 100, 120, 120)


  canvas.create_line(110, 120, 110, 150)
  canvas.create_line(110, 130, 100, 140)
  
  canvas.create_line(110, 130, 120, 140)
  canvas.create_line(110, 150, 100, 160)
  canvas.create_line(110, 150, 120, 160)


def check_guess(guess):
  global incorrect_guesses

  if guess in secret_word:
   
    pass
  else:
   
    incorrect_guesses += 1

    


def start_game():

  canvas.delete("all")


  create_hangman()


  word_label = tk.Label(root, text=secret_word)
  word_label.pack()

  guess_entry = tk.Entry(root)
  guess_entry.pack()

  guess_button = tk.Button(root, text="Guess", command=lambda: check_guess(guess_entry.get()))
  guess_button.pack()


start_game()


root.mainloop()