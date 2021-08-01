import random
import math
import sys


# In this case an exponential temperature update is used,
# for greater performance as shown at: https://pdfs.semanticscholar.org/e893/4a942f06ee91940ab57732953ec6a24b3f00.pdf
# k: decides the size of the "stride" of the curve
# alpha: defines the shape of the temperature decay
# limit: number of iterations
def exp_schedule(k=4, alpha=0.001, limit=20000):
    return lambda t: (k * math.exp(-alpha * t) if t < limit else 0)


def simulated_annealing(problem, schedule=exp_schedule()):
    current = problem.initial()
    current_h = problem.heuristic(current)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0 or problem.goal_test(current):
            return current
        neighbour = problem.randomNearState(current)
        if not neighbour:
            return current
        # NOTE: problem.heuristic (state) returns -h

        new_h = problem.heuristic(neighbour)
        delta_e = new_h - current_h
        
# Decision making based on energy variation and probability
        if delta_e > 0 or math.exp(delta_e / T) > random.uniform(0.0, 1.0):
            current = neighbour
            current_h = new_h
