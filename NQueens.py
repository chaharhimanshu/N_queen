from random import choice
from collections import Counter
from random import randrange


#Generic class of search problems
class SearchProblem:
    #Starts the search (receives the initial parameters)
    def __init__(self, initial=None):
        pass

    # Sets the initial state
    def initial(self):
        pass

    # Objective test
    def goal_test(self, state):
        pass
# Heuristic, used for maximization or minimization problems
    def heuristic(self, state):
        pass


# Returns the states accessible from the current state
    def nearStates(self, state):
        pass

    # Returns a random choice among the nearby states
    def randomNearState(self, state):
        return choice(self.nearStates(state))


# Implementation of the model of the n-queens problem, overriding the SearchProblem class
class NQueensSearch(SearchProblem):
   # State model
    #
    # State: ([line_queens],
    # (a, b, c),
    #        (H)
    #
    # Where:
    # a: saves queens column value
    # b: guard l-c of queens
    # c: guard l + c of queens
    # h: value of the state heuristic
    # The check is for each queen on the board, where it is tested
    # if there is another queen already visited with the same values ​​as a, b, c.
    # if it exists, it is not an objective state
    def __init__(self, N):
        self.N = N

    
# Initial state:
    # Returns the initial state from the size
    def initial(self):
        return list(randrange(self.N) for i in range(self.N))


# Objective test:
    # Tests if any row / column / diagonal is populated by more than one queen
    def goal_test(self, state):
        a, b, c = (set() for i in range(3))
        for row, col in enumerate(state):
            if col in a or row - col in b or row + col in c:
                return False
            a.add(col)
            b.add(row - col)
            c.add(row + col)
        return True

   # Heuristics: h
    # Number of pairs of queens attacking each other
    def heuristic(self, state):
       # defines a, b, c as counters
        a, b, c = [Counter() for i in range(3)]
       
# count how many queens the values ​​have (a, b, c)
        # so that you get for example how many queens have the value of a = 1
        for row, col in enumerate(state):
            a[col] += 1
            b[row - col] += 1
            c[row + col] += 1
        h = 0 # start collisions with 0
        # scans the counting structures (a, b, c) just increasing the collision value
        # case for some value of (a / b / c)> 1 since cnt is done [key] -1
        # divides to remove double counts
        for count in [a, b, c]:
            for key in count:
                h += count[key] * (count[key] - 1) / 2
        return -h

    # Children or neighboring states: children []
    # Returns all states accessible from the current one by moving parts by column
    def nearStates(self, state):
        near_states = []
        # For each state [column] it checks if the neighboring columns are empty
        for row in range(self.N):
            for col in range(self.N):
               # If different:
                # then the current iteration col is available to move around
                # since state [] stores the value of the columns where the queens are

                if col != state[row]:
                    aux = list(state)
                    aux[row] = col  
                # Change column to empty
                    near_states.append(list(aux))  #And includes in the list of nearStates

        return near_states
