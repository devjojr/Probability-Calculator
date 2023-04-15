import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, num_balls in kwargs.items():
            for _ in range(num_balls):
                self.contents.append(color)

    def draw(self, num_balls):
        seen_balls = []
        if len(self.contents) < num_balls:
            return self.contents
        else:
            for _ in range(num_balls):
                get_ball = random.randint(0, len(self.contents)-1)
                ball = self.contents.pop(get_ball)
                seen_balls.append(ball)
            return seen_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_matches = 0

    for _ in range(num_experiments):
        copy_of_hat = copy.deepcopy(hat)

        selected_balls = copy_of_hat.draw(num_balls_drawn)
        match = True

        for color, num_balls in expected_balls.items():
            if selected_balls.count(color) < num_balls:
                match = False
                break

        if match:
            num_matches += 1

    result = num_matches / num_experiments

    return result
