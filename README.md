# 🎮 Number Guessing Game

A simple interactive Python game where the computer thinks of a random number and you try to guess it!

## 📝 Description

This is my first Python project as a B.Tech IT student. The game generates a random number between 1 and 10, and the player has to guess it. After each guess, the game provides hints ("Too high!" or "Too low!") to help the player find the correct number.

**Version 2.0** - Now with play again feature!

## ✨ Features

- Random number generation
- Interactive user input
- Hints after each guess (too high/too low)
- Attempt counter to track your performance
- **Play again option** - Play multiple games without restarting!
- **Smart input handling** - Accepts "yes", "YES", "Yes", "y" for playing again
- Simple and clean interface with decorative banners

## 🚀 How to Play

1. Run the program
2. The computer will think of a number between 1 and 10
3. Enter your guess
4. Follow the hints (Too high/Too low)
5. Keep guessing until you find the correct number!
6. The game will tell you how many attempts it took

## 💻 Requirements

- Python 3.x
- No external libraries needed (uses built-in `random` module)

## 📦 Installation

1. Make sure you have Python installed on your computer
2. Download the `game.py` file
3. Open terminal/command prompt
4. Navigate to the folder containing the file
5. Run: `python game.py`

## 🎯 Example Gameplay

```
==================================================
   WELCOME TO NUMBER GUESSING GAME!!
==================================================

I'm thinking of a number between 1 to 10

Enter your guess: 5
Too High! Try Again

Enter your guess: 3
Too Low! Try Again

Enter your guess: 4

🎉 Congratulations! You Win! 🎉
You guessed the number in 3 attempts!

Do you want to play again? (yes/no): yes

==================================================
   STARTING NEW GAME!
==================================================

I'm thinking of a number between 1 to 10

Enter your guess: 7
Too Low! Try Again

Enter your guess: 9

🎉 Congratulations! You Win! 🎉
You guessed the number in 2 attempts!

Do you want to play again? (yes/no): no

Thanks for playing! Goodbye! 👋
```

## 📚 What I Learned

While building this project, I learned:
- Using the `random` module in Python
- Working with nested `while` loops (outer and inner loops)
- Using conditional statements (`if/elif/else`)
- Getting user input with `input()`
- Type conversion with `int()`
- String methods like `.lower()` for case-insensitive input
- Counting and tracking variables
- Writing clean, commented code
- Understanding program flow and loop control with `break`

## 🔮 Future Improvements

Ideas for making this game better:
- [x] Play again option ✅ **Added in v2.0!**
- [ ] Add difficulty levels (Easy: 1-10, Medium: 1-50, Hard: 1-100)
- [ ] Limit the number of attempts
- [ ] Add a scoring system
- [ ] Show how close the guess is (very close, close, far)
- [ ] Keep a high score record

## 👨‍💻 Author

**vaishnavilad726-ops**
- GitHub: [@vaishnavilad726-ops](https://github.com/vaishnavilad726-ops)
- B.Tech IT Student
- Learning Python and building projects!

## 📄 License

This project is open source and available for anyone to learn from and modify.

## 🙏 Acknowledgments

- Thanks to my learning journey in Python
- Inspired by classic number guessing games

---

⭐ If you found this helpful, please star this repository!
