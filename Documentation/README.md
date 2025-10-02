# Tres & Wordy: CLI Game Collection

## Overview

This is a simple command-line interface (CLI) application written in **Python**, featuring two games:

- **Tres**: The primary game, inspired by Uno, with a unique and strategic punishment mechanic.
- **Wordy**: An optional word guessing game that puts a twist on the classic Wordle formula.

---

## Tres

Tres is a card game where players compete to be the first to play all their cards by matching either colors or numbers. The game draws inspiration from Uno, but introduces a new mechanic: when a player reaches exactly three cards, a punishment round is triggered. This replaces Uno's "call Uno" rule.

### Punishment Mechanic

When a player has exactly 3 cards, they can initiate a punishment round:

1. **Choose a Number**: The player selects a number between 1 and 100.
2. **Secret Number**: The game randomly generates a secret number between 1 and 100.
    - If the player's number is **higher** than the secret number, the player must punish themselves.
    - If the player's number is **lower** than the secret number, the player can punish all other players.
    - If the player matches the **exact** secret number, the punishment effect is doubled (2x multiplier).
3. **Punishment Amount**: The game randomly generates a number between 1 and 5; this is the number of cards to be drawn as punishment.
    - If the player guessed the exact secret number, this amount is doubled.
    - The punishment (drawing cards) is applied either to the punisher (if higher), or to all other players (if lower or exact).

This mechanic adds suspense and strategic depth to the game whenever a player reaches three cards.

---

## Wordy

Wordy is a word-guessing game inspired by Wordle, but with several twists:

- Words are randomly selected from a predefined list and can be of any length.
- Players have a limited number of attempts to guess the word.
- After each guess, feedback is provided:
      - The number of letters in the correct position.
      - The number of correct letters in the wrong position.
      - If your guess has the wrong number of letters, the game will tell you, but it will not reveal the actual word length.

---

## How to Play

1. Make sure you have Python installed.
2. Run the CLI application.
3. Choose to play either Tres or Wordy.
4. Follow the on-screen instructions to play, make guesses, and interact with the punishment mechanic (Tres) or word feedback (Wordy).

---

## Legal Disclaimer

- The name "Tres" is not currently trademarked for card games and is used here to avoid conflicts with existing trademarks such as "Uno" and "Dos."
- This project is an original creation inspired by Uno and Wordle, but does not copy or reuse proprietary designs, artwork, or mechanics from trademarked products.

---

## License

This project is open source and free to use. See the LICENSE file for details.
