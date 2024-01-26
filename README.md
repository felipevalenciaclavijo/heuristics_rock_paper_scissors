# Heuristics Machine for Rock Paper Scissors

First, let's define what is a heuristic:

> "A heuristic, or heuristic technique, is any approach to problem solving or self-discovery that employs a practical method that is not guaranteed to be optimal, perfect, or rational, but is nevertheless sufficient for reaching an immediate, short-term goal or approximation." ([Wikipedia](https://en.wikipedia.org/wiki/Heuristic))

This project tests the use of a common heuristic for playing and winning in the popular game Rock, Paper, Scissors. In which the machine uses the previous round's output to then choose for the next round.

I created 6 different scenarios and did some simulations to test the different outcomes:

You can also watch a video about it [here](https://youtu.be/Ndine82s4k0).

### Scenario 1: Random vs Random

After simulating 1000 games where both the machine and the user made random selections, we found that eventually, the results would follow a normal distribution, so there were always around 300-350 wins, losses, and ties.

### Scenario 2: Random vs User

No matter how much a player tries to find a strategy because the machine is making random decisions, after many games we ended up with a similar result as in scenario 1, with a normal distribution. 

### Scenario 3: Random vs User Bias

After simulating 1000 games, where the machine made random decisions and the user always used the heuristic biases we programmed. We found that eventually, the results would follow a normal distribution, so there were always around 300-350 wins, losses, and ties.

### Scenario 4: Heuristic vs Random

After simulating 1000 games, the machine made the heuristic decisions and the other made random selections. We found that eventually, the results will follow a normal distribution, like in previous simulations, so there were always around 300-350 wins, losses, and ties.

At this point, we discovered that every time any of the two players or both played randomly the result was always the same, a normal distribution of the points after many games.

### Scenario 5: Heuristic vs User Bias (SUCCESS)

After simulating 1000 games, the machine made the heuristic decisions and the user followed the biases of the heuristic decisions, we found that almost all the times the machine won, and we ended up with the machine winning around 99.9% of the times. The reason for not having a 100% is that the first decision made by the machine is random and from there, it starts to use the output of the previous round.

### Scenario 6: Heuristic vs User (PARTIAL SUCCESS)

After testing with several real users we noticed that the machine was capable of initially winning several rounds, but then the humans understood the heuristic technique of the machine and started to implement a counter strategy. Therefore, we can conclude that a heuristic is sufficient for reaching an immediate, short-term goal, but it does not work in the long term.

## Contact

For questions or comments, please send them to:

Felipe Valencia, BYU-Idaho.

fevacla@byui.edu