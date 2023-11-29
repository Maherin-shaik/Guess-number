# Guess-number
Guess the number Game
<br>
The Number Guessing Game is a simple and interactive Python program where the player attempts to guess a randomly selected number within a specified range. In this case, the range is set between 1 and 100. Here's an overview of how the game works:

Initialization:
The game starts by generating a random number between 1 and 100 using the random.randint function.
The player is welcomed to the game, and the objective is explained: to guess the randomly selected number.

Game Loop:
The game enters a loop that continues until the player guesses and upto 3 chances.
In each iteration of the loop, the player is prompted to enter their guess.
The program checks if the guess is correct. If it is, the game congratulates the player, displays the number of attempts, and exits the loop.
If the guess is incorrect, the program provides feedback on whether the guess was too high or too low, and the player is prompted to try again.
Input Validation:
The program includes error handling to ensure that the player enters a valid number. If the input is not a valid integer, the player is informed of the error and prompted to enter a valid guess.

End of Game:
Once the player correctly guesses the number, the game congratulates them or if chances are over then,the it will display your chances are over and it will display final random number.
