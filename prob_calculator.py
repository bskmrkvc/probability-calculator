import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        
        self.contents = [k for k, v in kwargs.items() for i in range(v)]

    def draw(self, balls):
        
        if balls > len(self.contents):
            return self.contents

        balls_drawn = random.sample(self.contents, k=balls)

        for ball in balls_drawn:
            self.contents.remove(ball)

        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    successes = 0
    expected_balls = [k for k, v in expected_balls.items() for i in range(v)]

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls = []

        for ball in expected_balls:
            if ball in balls_drawn:
                balls_drawn.remove(ball)
                balls.append(ball)
    
        if sorted(expected_balls) == sorted(balls):
            successes += 1

    return successes / num_experiments
