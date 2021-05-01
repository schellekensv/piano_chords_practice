import numpy as np

use_minor = True
use_seventh = True
use_positions = True # TODO allow to change in arguments


# We define a generic class for sampling stuff
class WeightedDistributions:
    # A list of objects with weigths
    def __init__(self,objects,weights=None):
        self.objects = objects
        self.n = len(objects) # Number of objects
        if weights is None:
            self.weights = np.ones(self.n)
        elif isinstance(weights,list):
            assert len(weights) == self.n
            self.weights = np.array(weights)
        elif isinstance(weights,np.ndarray):
            assert weights.size == self.n
            self.weights = weights
        else:
            raise ValueError("weights is of unknown type")
        # Normalize to probability distribution
        self.weights /= self.weights.sum()

    def draw(self):
        return np.random.choice(self.objects,p=self.weights)


# List the base chords here
base_chords_names = [ 'C','Db', 'D','Eb', 'E', 'F','F#', 'G','Ab', 'A','Bb', 'B']
base_chords_probs = [ 3.0, 1.0, 3.0, 1.0, 3.0, 3.0, 1.0, 3.0, 1.0, 3.0, 2.0, 2.0]
base_chords = WeightedDistributions(base_chords_names,base_chords_probs)
all_modifiers = [base_chords]

# There are several modifications that can be applied to those base chords
# Minor
minor_names = ['' , 'm']
minor_probs = [0.7, 0.3]
minor = WeightedDistributions(minor_names,minor_probs)
if use_minor:
    all_modifiers += [minor]

# 7th
seventh_names = ['' , '7']
seventh_probs = [0.9, 0.1]
seventh = WeightedDistributions(seventh_names,seventh_probs)
if use_seventh:
    all_modifiers += [seventh]

# Several positions, for piano only
positions_names = [' (root)',' (mid.)',' (backw.)']
positions_probs = [      0.5,     0.25,       0.25]
positions = WeightedDistributions(positions_names,positions_probs)
if use_positions:
    all_modifiers += [positions]

if __name__ == "__main__":
    print("Welcome to the random chord generator!")

    # Get user input
    num_chords = None
    while not(num_chords):
        num_chords_raw = input("How many chords do you want to play? ")
        try:
            num_chords = int(num_chords_raw)
        except:
            print("Please enter a valid number.")
            num_chords = None

    # Print chords
    for i in range(num_chords):
        expression = ''
        for mod in all_modifiers:
            expression += mod.draw()
        print(expression)
