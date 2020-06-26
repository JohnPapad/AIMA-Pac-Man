# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.
      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.
        getAction chooses among the best options according to the evaluation function.
        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.
        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.
        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.
        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        if currentGameState.isWin(): #victory
            return 999999

        if currentGameState.isLose(): #failure
            return -999999

        if newPos == currentGameState.getPacmanPosition() : #pacman remained stationary
            return -999999

        food_list = newFood.asList()

        if len(food_list) ==0:  #if no food left
            return 999999        #victory

        total_food_dist = 0
        for food_point in food_list:  #sum all manhattan distances between pacman and every food point (at the new game state)
            f_d = manhattanDistance(food_point, newPos)
            total_food_dist += f_d

        new_ghost_pos = successorGameState.getGhostPositions() #get ghost's positions at the new game state
        for ghost in new_ghost_pos: #calculate every manhatan distance between pacman and every ghost (at the new game state)
            ghost_pacman_dist  = manhattanDistance(ghost, newPos)
            if ghost_pacman_dist == 0: # if pacman runs into a ghost
                return -999999          #defeat

        return 2000/total_food_dist + 20000/len(food_list)


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.
      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.
      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.
      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.
          Here are some method calls that might be useful when implementing minimax.
          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1
          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action
          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"

        def max_value(state, depth):
            if (state.isWin() is True) or (state.isLose() is True) or (depth == self.depth):  # terminal test
                return self.evaluationFunction(state)

            v = -999999
            pac_acts = state.getLegalActions(0)     #get all pacman's legal actions at this game state (pacman's id is 0 )
            for action in pac_acts:                  #for every pacman's legal action
                next_game_state = state.generateSuccessor(0, action) # get pacman's next game state based on the particular action at a certain depth
                temp_value = min_value(next_game_state, depth, 1) #get the max of min_values of ghosts(starting with ghost #1) at a certain depth
                if temp_value > v:
                    v = temp_value
            return v

        def min_value(state, depth, agent_id):
            if (state.isWin() is True) or (state.isLose() is True): #terminal test
                return self.evaluationFunction(state)

            v = 999999
            agent_legal_actions = state.getLegalActions(agent_id) #get ghost's legal actions
            for action in agent_legal_actions: #for every ghost's legal action
                next_game_state = state.generateSuccessor(agent_id, action)# get ghost's next game state based on the particular action
                if agent_id == gameState.getNumAgents()-1:      #if it is the last ghost
                    v = min(v, max_value(next_game_state, depth +1 )) #finished with every ghost at this depth so start over with next pacman's move (increased depth)
                else :
                    v = min(v, min_value(next_game_state, depth, agent_id +1)) #continue with min_value for next ghost at the same depth
            return v


        pac_acts = gameState.getLegalActions(0) #get all pacman's legal actions at this game state (pacman's id is 0)
        max_val = -999999
        best_act = Directions.STOP  # it is always a legal action
        for action in pac_acts : #for every pacman's legal action
            next_game_state = gameState.generateSuccessor(0, action) # get pacman's next game state based on the particular action
            temp_value = min_value(next_game_state, 0, 1) #first agent is pacman (which is a max player) so get the maximum of min_values of ghosts(starting with ghost #1 at depth=0)
            if (temp_value > max_val):
                max_val = temp_value
                best_act = action

        return best_act

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):  # code is similar as above (but this time alpha beta variables are included)
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        def max_value(state, a, b, depth):
            if (state.isWin() is True) or (state.isLose() is True) or (depth == self.depth):
                return self.evaluationFunction(state)

            v = -999999
            pac_acts = state.getLegalActions(0)
            for action in pac_acts:
                next_game_state = state.generateSuccessor(0, action)
                v = max(v, min_value(next_game_state, a, b, depth, 1))
                if v > b:
                    return v
                a = max(a, v)
            return v


        def min_value(state, a, b, depth, agent_id):
            if (state.isWin() is True) or (state.isLose() is True):
                return self.evaluationFunction(state)

            v = 999999
            agent_legal_actions = state.getLegalActions(agent_id)
            for action in agent_legal_actions:
                next_game_state = state.generateSuccessor(agent_id, action)
                if agent_id == gameState.getNumAgents()-1:
                    v = min(v, max_value(next_game_state, a, b, depth +1))
                else:
                    v = min(v, min_value(next_game_state, a, b, depth, agent_id+1))
                if v < a:
                    return v
                b = min(b, v)
            return v


        pac_acts = gameState.getLegalActions(0)
        max_val, a, b = -999999, -999999, 999999
        best_act = Directions.STOP
        for action in pac_acts:
            next_game_state = gameState.generateSuccessor(0, action)
            temp_value = min_value(next_game_state, a, b, 0, 1)
            if temp_value > max_val:
                max_val = temp_value
                best_act = action
            if max_val > b:
                return best_act
            a = max(a, max_val)

        return best_act


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):  #again code is similar as the one in minmax but with some differences (in the expect_value function and in main body)
        """
          Returns the expectimax action using self.depth and self.evaluationFunction
          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"

        def max_value(state, depth):  #exactly the same as minmax
            if (state.isWin() is True )or (state.isLose() is True) or (depth == self.depth) :
                return self.evaluationFunction(state)

            v = -999999
            pac_acts = state.getLegalActions(0);
            for action in pac_acts:
                next_game_state = state.generateSuccessor(0, action)
                v = max(v, expect_value(next_game_state, depth, 1))
            return v

        def expect_value(state, depth, agent_id):
            if (state.isWin() is True )or (state.isLose() is True ):
                return self.evaluationFunction(state)

            v = 0
            agent_legal_actions = state.getLegalActions(agent_id)
            total_acts = len(agent_legal_actions)
            for action in agent_legal_actions:
                next_game_state = state.generateSuccessor(agent_id, action)
                if agent_id == gameState.getNumAgents()-1:
                    v += (max_value(next_game_state, depth +1)) / total_acts    #sum the averages
                else:
                    v += (expect_value(next_game_state, depth, agent_id +1)) / total_acts #sum the averages
            return v


        pac_acts = gameState.getLegalActions(0)
        max_val = -999999
        best_act = Directions.STOP
        for action in pac_acts:
            next_game_state = gameState.generateSuccessor(0, action)
            temp_val = expect_value(next_game_state, 0, 1)
            if (temp_val > max_val) or( (temp_val == max_val) and (random.random() > 0.5)):   #select randomly between best actions
                max_val = temp_val
                best_act = action
        return best_act

def betterEvaluationFunction(currentGameState):  #it is basically the same function as the one in question 1 but adjusted to current game state
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).
      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    if currentGameState.isWin():  #victory
        return 999999

    if currentGameState.isLose():  #defeat
        return -999999

    curr_food =  currentGameState.getFood()
    curr_food_list = curr_food.asList()
    pac_pos = currentGameState.getPacmanPosition()

    if len(curr_food_list) == 0:  # if no food left
        return 999999     # victory

    total_food_dist = 0
    for food_point in curr_food_list:  # sum all manhattan distances between pacman and every food point (at the new game state)
        f_d = manhattanDistance(food_point, pac_pos)
        total_food_dist += f_d

    ghost_pos = currentGameState.getGhostPositions()  # get ghost's positions at the current game state
    for ghost in ghost_pos:  # calculate every manhatan distance between pacman and every ghost (at the current game state)
        ghost_pacman_dist = manhattanDistance(ghost, pac_pos)
        if ghost_pacman_dist == 0:  # if pacman runs into a ghost
            return -999999           #defeat


    return 900 / total_food_dist + 150000 / len(curr_food_list)   #average score 1001.0



# Abbreviation
better = betterEvaluationFunction

