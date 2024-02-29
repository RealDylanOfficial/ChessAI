# ChessAI
Seperate repository for just the chess AI for the robot arm project: extracted from https://github.com/RealDylanOfficial/ArmProjectChessAI. It is a minimax algorithm with alpha-beta pruning.

To run it, just use the following command:  
python ai_test.py <agent_type> <search_depth>  
where agent type must be one of the following: random, human, AI  
Note: testing the AI against another AI instance does not currently work. Test it against random or human.

Using the regular python interpreter will be very slow so it is recommended that you run it with pypy. pypy is a different python interpreter with greater optimisation. Download it here: https://www.pypy.org/download.html

Running the program with pypy will look something like this:  
.\pypy3.10-v7.3.14-win64\pypy.exe ai_test.py random 6

The text may not display properly with the windows version of pypy so you may need to use the linux version. To run the linux version on windows use wsl.
