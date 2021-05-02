import numpy as np
import argparse

use_minor = True
use_seventh = True
use_positions = True # TODO allow to change in arguments


# We define a generic class for sampling stuff
class WeightedDistributions:
    """A list of objects with weigths"""
    def __init__(self,objects,weights=None):
        self.objects = objects
        
        if weights is None:
            self.weights = np.ones(len(self.objects))
        elif isinstance(weights,list) or isinstance(weights,np.ndarray):
            assert len(weights) == len(self.objects)
            self.weights = np.array(weights)
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
    parser = argparse.ArgumentParser()
    parser.add_argument("num_chords", help="the number of chords to generate", type=int)
    args = parser.parse_args()
    num_chords = args.num_chords

    print("Welcome to the random chord generator!\n"
         f"You requested {num_chords} chords to play...\n"
          "Well, here you go:\n")

    # Print chords
    for i in range(num_chords):
        print(''.join(mod.draw() for mod in all_modifiers))
