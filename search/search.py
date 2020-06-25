# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    from util import Stack
    path_to_node = []
    problem_start_state = problem.getStartState()
    start_node = [problem_start_state, path_to_node]   #path_to_node : a list with actions required to reach each node, starting from the start_node
    frontier = Stack()
    frontier.push(start_node)
    explored = set()

    while True:
        if frontier.isEmpty():
            return []                              # return failure = a empty list

        parent = frontier.pop()

        if problem.isGoalState(parent[0]):          #if goal state has reached
            return parent[1]                        #return solution , parent[1] = the path_to_node list

        if parent[0] not in explored :              # parent[0] = parent's state
            explored.add(parent[0])
            children = problem.getSuccessors(parent[0]) # children = list of triples (successor, action, stepCost) /we dont need stepCost at this case
            for child in children:                      #for each successor
                child_state = child[0]
                child_action = child[1]

                if (child_state not in explored):
                    path_to_child = list(parent[1])     #creating a copy of a path_to_node list reaching up to the previous node
                    path_to_child.append(child_action)  #adding to the list mentioned above, the action required to reach the child from the parent
                    child = [child_state, path_to_child]
                    frontier.push(child)


def breadthFirstSearch(problem):  # it is exactly the same code as dfs above, apart from the fact that the frontier is a queue this time
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    from util import Queue
    path_to_node = []
    problem_start_state = problem.getStartState()
    start_node = [problem_start_state, path_to_node]
    frontier = Queue()
    frontier.push(start_node)
    explored = set()

    while True :
        if frontier.isEmpty():
            return []

        parent = frontier.pop()

        if problem.isGoalState(parent[0]):
            return parent[1]

        if parent[0] not in explored:
            explored.add(parent[0])
            children = problem.getSuccessors(parent[0])
            for child in children :
                child_state = child[0]
                child_action = child[1]

                if (child_state not in explored):
                    path_to_child = list(parent[1])
                    path_to_child.append(child_action)
                    child = [child_state, path_to_child]
                    frontier.push(child)





def uniformCostSearch(problem):    # almost the same code as above with some little difference
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    from util import PriorityQueue
    path_to_node = []
    path_cost = 0                         #total cost from beginning to each node
    problem_start_state = problem.getStartState()
    start_node = [problem_start_state, path_to_node, path_cost]  #include path_cost too
    frontier = PriorityQueue()
    frontier.push(start_node, path_cost)  #pushing both node and path cost which will be used as a key for sorting at the priority queue
    explored = set()

    while True :
        if frontier.isEmpty() :
            return []

        parent = frontier.pop()

        if problem.isGoalState(parent[0]):
            return parent[1]

        if parent[0] not in explored:
            explored.add(parent[0])
            children = problem.getSuccessors(parent[0])
            for child in children :
                child_state = child[0]
                child_action = child[1]
                child_cost = child[2]

                if child_state not in explored :
                    total_cost = parent[2] + child_cost  # parent[2] = total cost from the beginning to the parent node
                    path_to_child = list(parent[1])
                    path_to_child.append(child_action)
                    child = [child_state, path_to_child, total_cost]
                    frontier.update(child, total_cost)



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):  # it is almost the same code as ucs above but with some minor differences again
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    from util import PriorityQueue
    path_to_node = []
    path_cost = 0
    problem_start_state = problem.getStartState()
    start_node = [problem_start_state, path_to_node]  # no need to store the path_cost at the node this time
    frontier = PriorityQueue()
    frontier.push(start_node, path_cost)
    explored = set()

    while True:
        if frontier.isEmpty():
            return []

        parent = frontier.pop()

        if problem.isGoalState(parent[0]):
            return parent[1]

        if parent[0] not in explored:
            explored.add(parent[0])
            children = problem.getSuccessors(parent[0])
            for child in children:
                child_state = child[0]
                child_action = child[1]

                if child_state not in explored:
                    path_to_child = list(parent[1])
                    path_to_child.append(child_action)
                    heuristic_cost = heuristic(child_state, problem)
                    cost_of_actions = problem.getCostOfActions(path_to_child)  #using getCostOfActions to calculate the cost of actions from beginnig to this node
                    total_cost = heuristic_cost + cost_of_actions
                    child = [child_state, path_to_child]
                    frontier.update(child, total_cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
