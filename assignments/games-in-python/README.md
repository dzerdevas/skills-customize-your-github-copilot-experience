# 📘 Assignment: Games in Python - Hangman

## 🎯 Objective

In this assignment, you will build a text-based Hangman game in Python. You will practice using loops, conditionals, strings, and user input to create game logic.

## 📝 Tasks

### 🛠️	Create the Game Setup

#### Description
Set up the basic game data, including a list of possible words, a randomly selected secret word, and variables to track guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Include a predefined list of at least 5 possible words.
- Randomly select one word at the start of each game.
- Create a data structure to store guessed letters.
- Start the player with a fixed number of incorrect guesses (for example, 6).


### 🛠️	Implement the Gameplay Loop

#### Description
Build the main loop where the player guesses letters, sees word progress, and wins or loses based on their guesses.

#### Requirements
Completed program should:

- Ask the player for one letter guess each turn.
- Display the current word progress using underscores for unknown letters (example: h _ n g m a n).
- Decrease remaining attempts only when a guessed letter is not in the word.
- End the game with a win message when the full word is guessed.
- End the game with a lose message when attempts reach zero and reveal the word.
