"""6.009 Spring 2019 Lab 9 -- 6.009 Zoo"""

from math import ceil  # ONLY import allowed in this lab

# NO CUSTOM IMPORTS ALLOWED!

class Constants:
    """
    A collection of game-specific constants.

    You can experiment with tweaking these constants, but
    remember to revert the changes when running the test suite!
    """
    # width and height of keepers
    KEEPER_WIDTH = 31
    KEEPER_HEIGHT = 31

    # width and height of animals
    ANIMAL_WIDTH = 31
    ANIMAL_HEIGHT = 31

    # width and height of food
    FOOD_WIDTH = 11
    FOOD_HEIGHT = 11

    # width and height of rocks
    ROCK_WIDTH = 51
    ROCK_HEIGHT = 51

    # thickness of the path
    PATH_THICKNESS = 31

    # some other characters
    DEMON_WIDTH = 51
    DEMON_HEIGHT = 51
    DEMON_RADIUS = 75  # Only animals this close are affected.
    DEMON_MULTIPLIER = 2  # Animal speeds multiplied by this factor
    DEMON_PRICE = 100

    VHS_WIDTH = 31
    VHS_HEIGHT = 31
    VHS_RADIUS = 75
    VHS_MULTIPLIER = .5
    VHS_PRICE = 20

    CRAZY_NAP_LENGTH = 20

    TRAINEE_THRESHOLD = 20  # How many food hits must the trainee score,
    # before becoming a speedy zookeeper?

    TEXTURES = {
        'rock': '1f5ff',
        'animal': '1f418',
        'SpeedyZookeeper': '1f472',
        'ThriftyZookeeper': '1f46e',
        'OverreachingZookeeper': '1f477',
        'food': '1f34e',
        'Demon': '1f479',
        'VHS': '1f4fc',
        'TraineeZookeeper': '1f476',
        'CrazyZookeeper': '1f61c',
        'SleepingZookeeper': '1f634'
    }

    KEEPER_INFO = {'SpeedyZookeeper':
                       {'price': 250,
                        'range': 50,
                        'throw_speed_mag': 20},
                   'ThriftyZookeeper':
                       {'price': 100,
                        'range': 100,
                        'throw_speed_mag': 15},
                   'OverreachingZookeeper':
                       {'price': 150,
                        'range': 150,
                        'throw_speed_mag': 5},
                   'TraineeZookeeper':
                       {'price': 50,
                        'range': 100,
                        'throw_speed_mag': 5},
                   'CrazyZookeeper':
                       {'price': 100,
                        'range': 1000,
                        'throw_speed_mag': 50}
                   }

# New spec for timestep(self, mouse):
# (0. Do not take any action if the player is already defeated.)
# 1. Compute the new speed of animals based on the presence of nearby VHS cassettes or demons.
# 2. Compute any changes in formation locations and remove any off-board formations.
# 3. Handle any food-animal collisions, and remove the fed animals and the eaten food.
# 4. Upgrade trainee zookeeper if needed.
# 5. Throw new food if possible.
# 6. Spawn a new animal from the path's start if needed.
# 7. Handle mouse input, which is the integer tuple coordinate of a player's click, the string label of a particular
#   zookeeper type, or None.
# 8. Redeem one dollar per animal fed this timestep.
# 9. Check for the losing condition.

################################################################################
##  Copy and paste your code from lab8 below EXCEPT for the Constants class.  ##
##  The Constants class above contains the changes needed for the lab.        ##
################################################################################

### lab8 code here ###

if __name__ == '__main__':
    pass