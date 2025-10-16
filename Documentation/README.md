# Tres & Wordy: CLI Game Collection

## Overview

This is a simple command-line interface (CLI) application written in **Python**, featuring two games:

- **Tres**: The primary game, inspired by Uno, with a unique and strategic punishment mechanic.
- **Wordy**: An optional word guessing game that puts a twist on the classic Wordle formula.

---

## Tres

Tres is a card game where players compete to be the first to play all their cards by matching either colors or numbers. The game draws inspiration from Uno, but introduces a new mechanic: when a player reaches exactly three cards, a punishment round is triggered. This replaces Uno's "call Uno" rule.

### Tres Basic Rules

    - Match cards by either color or number.
    - Be the first to play all your cards to win.
    - Skip Card: Play a skip card to skip the next player's turn.
    - Wild Card: Play a wild card to change the current color to any color of your choice.
    - +2 Card: Play a +2 card to force the next player to draw two cards.
    - +4 Card: Play a +4 card to force the next player to draw four cards. 
    Also change the current color to a color of your choice.
    - Reverse Card: Play a reverse card to change the order of play.
    - You may stack +2 and +4 cards, has to be with the same type of card.
    - When you have exactly 3 cards, the punishment mechanic activates.

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

### Wordy Basic Rules

    - Words are randomly selected from a predefined list and can be of any length.
    - Choose your difficulty level: Easy has 4 letters, Medium has 6 letters, and Hard has 8 letters.
    - You have a limited number of attempts to guess the word (You only get 6 of them!).
    - Be strategic with your guesses to find the secret word in as few attempts as possible.
    - Any English word is allowed, including proper nouns. 
    - No special characters.

### Feedback System

    After each guess, you'll receive feedback:
    
        - The number of letters in the correct position.
        - The number of correct letters but in the wrong position.

### Strategy Tips

    - Start with common letters and vowels.
    - Use the feedback to eliminate impossible letters.
    - Pay attention to letter positions to narrow down possibilities.

Good luck guessing the secret word!""")

## Development Environment

This project includes an automated setup system for codespace environments:

### Auto-Sync Script (`auto_sync.py`)

When your codespace opens, the auto-sync script automatically:

1. **Ubuntu Version Upgrades**: Checks for and offers to install new Ubuntu releases (like LTS upgrades)
2. **System Updates**: Checks for and installs Ubuntu package updates and security patches
3. **Repository Sync**: Updates your codespace with the latest code from GitHub (including extension configs)
4. **VS Code Extension Sync**: Installs missing extensions and updates all extensions to latest versions
5. **Branch Management**: Automatically switches to the Testing branch for development work
6. **User-Friendly Interface**: Provides VS Code-style dialogs for all interactions

### Extension Management System

The codespace includes an advanced extension management system:

#### **Automatic Extension Sync**

- **Extension Tracking**: All installed extensions are automatically tracked in `.vscode/extensions.txt`
- **Cross-Codespace Sync**: Extensions sync across different codespaces automatically
- **Smart Installation**: Missing extensions are detected and installed on startup
- **Auto-Updates**: All extensions are updated to their latest versions

#### **How It Works**

1. **Install Extensions Normally**: Just install any extension through VS Code's extension marketplace
2. **Automatic Tracking**: The system automatically adds new extensions to the tracking file
3. **Push Changes**: When you push changes to GitHub, the extensions list is included
4. **New Codespace Sync**: Opening a new codespace automatically installs all tracked extensions

#### **Extension File Format**

Extensions are organized by category in `.vscode/extensions.txt`:

### Python Development

ms-python.python
ms-python.vscode-pylance

## Git and Version Control  

eamodio.gitlens
github.copilot

The script runs automatically on codespace startup and can also be triggered manually through the VS Code Tasks menu.

### Manual Sync Options

- **Auto Update Codespace on Startup**: Runs automatically when codespace opens
- **Manual Codespace Update**: Run the sync script manually anytime
- **Sync VS Code Extensions**: Manually sync extensions across codespaces
- **Push Changes to GitHub**: Use `git_sync.py` to push your changes back to GitHub

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
