# Tic-Tac-Toe-using-Markov-Decision-Process
It is an example &amp; Application, how Markov Chain works ! 

# What Is A Markov Chain?

Andrey Markov first introduced Markov chains in the year 1906. He explained Markov chains as:
A stochastic process containing random variables, transitioning from one state to another depending on certain assumptions and definite probabilistic rules.
These random variables transition from one to state to the other, based on an important mathematical property called Markov Property.

# Tic-tac-toe
Tic-tac-toe is the game given by the incidence structure, consisting of nine points, three horizontal lines, three vertical lines, and two diagonal lines, each line consisting of at least three points.


When considering only the state of the board, and after taking into account board symmetries (i.e. rotations and reflections), there are only 138 terminal board positions. A combinatorics study of the game shows that when "X" makes the first move every time,

1) 91 distinct positions are won by (X)
2) 44 distinct positions are won by (O)
3) 3 distinct positions are drawn

![image](https://user-images.githubusercontent.com/63719445/125157489-e5ac2c80-e188-11eb-9de3-45b0cab42ed4.png)

Our goal is to make an interface like Right side. For this purpose, in python, we have a pre-installed library called tkinter, which is used to create such graphics. 
python’s Tkinter module, which is very easy to implement. Also, we will use fundamental concepts of python like lists, if condition and functions.

![image](https://user-images.githubusercontent.com/63719445/125157553-518e9500-e189-11eb-99ff-da8791de2c98.png)


In this given program, the agent will check the state of action and predict whether there will be chance of machine winning by using the given build-in data/logic
By using this set of operation program we are also checking the state of action and predict whether there will be chance of Defence, if there is no chance of winning for machine.

The code under the i =f statement is making the machine to pick any of the empty boxes and will write O in it.
The code under the else statement making the machine to play tactically so that the player will make his/her nature of next move as defense not attack.
the above two condition will execute if there is no option for machine winning opportunity and defense move opportunity for machine.

When none of the logics is work, then it is a Tried Match
‘O’ → Black
‘X’  → Red
Configuring Rest button at the end 
Root.mainloop() is a loop which continuously monitor each and every moment in the Current state.

![image](https://user-images.githubusercontent.com/63719445/125157627-c06bee00-e189-11eb-8e81-93427721b6f0.png)


We deisged the program for easy mode, if you want to change any another mode, you can!
I am always open for the any improvement.! we will discuss..,! 
