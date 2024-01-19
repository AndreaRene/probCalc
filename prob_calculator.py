import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)
        
    def draw(self, draw_num):
        drawn = []
        on_draw = (random.sample(self.contents, min(draw_num, len(self.contents))))
        for ball in on_draw:
            drawn.append(ball)
            self.contents.remove(ball)
        return drawn
        
       

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    matches = 0
    original = copy.deepcopy(hat.contents)
    expected = Counter(expected_balls)

    for _ in range(num_experiments):
        hat.contents = copy.deepcopy(original)
        drawn_balls = hat.draw(num_balls_drawn)
        drawn_counter = Counter(drawn_balls)
        if all(drawn_counter[ball] >= count for ball, count in expected.items()):
            matches += 1
    print(matches)
    probability =  matches / num_experiments
    print(probability)
    return probability