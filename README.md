# Battleship
 The battleship board game. Please enjoy, it was a nightmare to code.

This is a Battleship game.

How to run:
-
$ bash run.sh

Instructions
-

Here is a video explaining how to play it: https://www.youtube.com/watch?v=4gHJlYLomrs

First, the computer will ask for you to place your ships by getting the coordinates and direction. If you give it an invalid input, the will keep prompting you to give it something valid.

After you set all the ships, you and the computer will take turns firing at each other's ships. Same as before, if you give it an invalid firing location, the computer will keep prompting you to give it something valid.

This will repeat until one of you wins.

How can an input be invalid?
-
When the computer asks for a row, you give it something other than [A, B, C, D, E, F, G, H, I, J]. If you type in a lowercase version of one of these valid responses, the computer will convert it and move on.
     
     Enter a row: RE%^UDYFTUGOfguh9y7gy8oubhij  ===> INVALID
     Enter a row: 78 ===> INVALID
     Enter a row: Z ===> INVALID
     Enter a row: a ===> VALID
     Enter a row: A ===> VALID

When the computer asks for a column, you give it something other than [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
     
     Enter a column: RE%^UDYFTUGOfguh9y7gy8oubhij ===> INVALID
     Enter a column: one ===> INVALID
     Enter a column: 11 ===> INVALID
     Enter a column: 5 ===> VALID

When the computer asks for a direction you give it something other than [N, S, E, W]. Like the row, if you type in a lowercase version of one of these valid responses, the computer will make it uppercase and move on.
    
     Enter a direction: A ===> INVALID
     Enter a direction: north ===> INVALID
     Enter a direction: 2 ===> INVALID
     Enter a direction: w ===> VALID
     Enter a direction: E ===> VALID

When you want to place a ship that will go off the board. 

    Picture this: cell A1 is at the top left of the entire board. If you attempt to go north, the computer will say "OFF BOARD!" since you can't go any further upwards and ask you to re-enter a position and direction.

When you want to place a ship that will overlap with another ship. (Yes, even submarines follow this rule.)

    You want to place a cruiser (5 cells long) on A1 facing east. Then, you want to place a battleship (4 cells long) at A3 facing south. This will not work because the first ship takes up the [A1, A2, A3, A4, A5] cells and the second ship takes up the [A3, B3, C3, D3] cells. Since both ships take up "A3", this will cause an overlap. The computer will ask you to re-enter position and direction.