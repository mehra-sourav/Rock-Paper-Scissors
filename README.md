## Rock, Papers and Scissors

A rock, paper, scissors game in which the user plays against the CPU by giving hand gestures as inputs. These inputs are feeded into trained ML models for classification into any of the three categories:rock, paper or scissors. Meanwhile the CPU randomly generates its own move;either rock,paper or scissors. The move of the CPU is evaluated against the user's input.

The rules for evaluation are as follow:
*	Rock beats Scissors
*	Scissors beat Paper
*	Paper beats Rock
*	If gestures of both sides are same, it's a draw

Following the rules above, the moves of the CPU and the player are evaluated. The winning side's counter increases as they win along with a win message. In case of a draw, a draw message is displayed. The scores and the input are displayed in a GUI made through PyQt. Also, a live image feed is shown on the GUI to help the user know if their gesture is coming in the camera's frame.

Following are some pictures of the project.

![image](https://user-images.githubusercontent.com/36883648/51465774-9c847a00-1d8e-11e9-8c4c-d34bc621bed7.png "Initial Preview")

![image](https://user-images.githubusercontent.com/36883648/51465830-bd4ccf80-1d8e-11e9-917d-5e9959b2b2d1.png "CPU Wins")

![image](https://user-images.githubusercontent.com/36883648/51465669-5deebf80-1d8e-11e9-8df8-eddb7c1db9df.png "Player Wins")
