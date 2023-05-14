import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for x, y in kwargs.items():
            self.contents.extend([x]*y)

    def draw(self, balls):
        balls_drafted = []
        if balls > len(self.contents):
            return self.contents
        for i in range(balls):
            ball_pick = random.choice(self.contents)
            balls_drafted.append(ball_pick)
            self.contents.pop(self.contents.index(ball_pick))
        return balls_drafted


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    sucess = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draws = hat_copy.draw(num_balls_drawn)
        expect = []
        for x, y in expected_balls.items():
            expect.extend([x] * y)

        for i in expect:
            if i in draws:
                draws.remove(i)
            else:
                break
        else:
            sucess += 1

    return sucess / num_experiments

