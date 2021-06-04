import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **kwargs):
        # when class is initialised, create a list of all balls based on kwargs
        # so if blue = 3, contents would have three elements called "blue"
        self.contents = []
        for i in kwargs:
            for j in range(kwargs[i]):
                self.contents.append(i)
        
        #print(self.contents)

    # removes specified number of balls from contents list at random
    # returns removed balls as a list
    def draw(self, num_balls_drawn):

        self.num_balls_drawn = num_balls_drawn
        x = []

        try:
            for i in range(num_balls_drawn):
                x.append(random.choice(self.contents))
                self.contents.remove(x[i])
        except IndexError:
            self.contents.append(x)

        return x



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for i in range(num_experiments):
        exp_balls_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        draw = hat_copy.draw(num_balls_drawn)
        
        # if expected balls are drawn, remove them from exp_balls_copy
        for j in draw:
            if j in exp_balls_copy:
                exp_balls_copy[j] -= 1

        # if exp_balls_copy is zero or less, add one to m
        # m is the number or times the expected balls were drawn
        if(all(x <= 0 for x in exp_balls_copy.values())):
            #print(exp_balls_copy.values())
            m += 1

    return (m / num_experiments)
        
