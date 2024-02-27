# Battleship Game

This is a battleship game, in which a player can play against a computer to try to hit each other battleships on a board.

## Features

### The game has these features implemented:

+ The Player-Board

-The player gets a board with a grid pattern on which they can position their battleships on.

-The board has 8 columns that are labeled with the letters A to H.
The program can translate those letters into the numbers from 0 to 7.

-The rows of the board are also 8 in number and are labeled with the numbers from 1 to 8.
Because the numbers in the program start with 0, it can translate the row numbers to the numberrange from 0 to 7.

+ The Computer-Board

- The computer gets a board on which the battleships get randomly positioned on.
To not cause any errors or bugs, the program can check for both the player and the computer, if a ship fits in a choosen space, and if it overlaps with other ships on the board.

+ The Positioning Of The Ships

-The player and the computer get 5 ships to distribute on their boards.

-The ships have different sizes.
1 ship covers 2 grid spaces
2 ships cover 3 grid spaces
1 ship covers 4 grid spaces
1 ship covers 5 grid spaces

-For each of those ships, the player gets asked for their input for the positioning of the battleships on the board.
1 input asks if the current ship should be placed vertically or horizontally (V or H)
1 input asks in what column the ship should be placed in (A to H)
To prevent from errors due to inputting lower case letters, the program can automatically uppercase any letters that are being entered
1 input asks for the row number in which the ship should get placed in (1 to 8)

-If the player enters invalid inputs, the program notifys them and gives them another try to enter the correct inputs.

+ The Guess-Boards

-The player and the computer get empty boards on which they can take turns to guess where on the board the oponents ships are placed

-For the player input, the player gets asked as to in which row and column they guess the computers ships in.

-Both the computer and the player get 17 turns, to guess the positions of the ships.

-if the player manages to hit more ships then the computer, they get a "You Win!" message, otherwise they will get a message notifying them, that they lost the game.

## Testing

+ Tested the python code mutiple times with an official validator.
+ Bugs found:

-2 while-loops had medium severety issues:
They were both single iterations, so the while was changed into an if-statement

Bug fixed!

## Validator Testing

+ Python

No errors were found when passing through the official [Snky - Validator](https://snyk.io/code-checker/python/)

## Unfixed Bugs

none

## Deployment

+ used Github and Gitpod to make changes and test locally.
+ pushed each change with GitHub
+ added to each commit a short describtion about what was changed or added before it being pushed