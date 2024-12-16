# Flashcard Application

This is a Python-based Flashcard Application designed to help users learn French vocabulary. The app presents a random French word on a card and flips it after 3 seconds to show its English translation. Users can mark whether they know the word or not, and the app saves progress to ensure the user can resume learning from where they left off.

## Features
1. Random Flashcards: Displays a random French word on the front side of the card.
2. Card Flipping: Automatically flips the card after 3 seconds to reveal the English translation.
3. Progress Tracking: Words marked as "known" are removed from the pool of cards, and progress is saved to a local file.
4. Intuitive User Interface: Buttons for marking words as "known" or "unknown."

## Requirements
- Python 3.x
- Pandas library
- Tkinter library (comes pre-installed with Python)
- CSV file containing French-English word pairs
- Image files for the flashcards and buttons

## How It Works
1. On startup, the app loads the words from `words_to_learn` (if available) or from `french_words.csv`.
2. A French word is displayed on the card.
3. After 3 seconds, the card flips to show the English translation.
4. Users can:
- Press the "right" button (✅) if they know the word. This removes the word from the list and saves progress.
- Press the "wrong" button (❌) to keep the word in the learning pool.
5. Progress is saved to `words_to_learn` whenever a word is marked as "known."

## Customization
You can customize the application by:
- Modifying the word data in `french_words.csv`.
- Replacing the card and button images.

## License
This project is open-source and free to use for educational purposes.


