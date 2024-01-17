# Import the random module to generate random numbers
import random

# Create a class called GameLogic to encapsulate game logic functions
class GameLogic:
    # Define a static method calculate_score that takes a dice_roll as input
    @staticmethod
    def calculate_score(dice_roll):
        # Check if all six dice values are present in the roll (1 through 6)
        if set(dice_roll) == set(range(1, 7)):
            return 1500
        # Check if all six dice are the same value (three pairs)
        if len(dice_roll) == 6 and all(dice_roll.count(value) == 2 for value in set(dice_roll)):
            return 1500

        # Initialize a variable to store the score
        score = 0
        # Create a dictionary 'counts' to store the count of each dice value
        counts = {x: dice_roll.count(x) for x in set(dice_roll)}

        # Iterate through the dice values and their counts
        for num, count in counts.items():
            # If a value appears at least three times
            if count >= 3:
                # Check if it's the value 1
                if num == 1:
                    # Add 1000 points to the score
                    score += 1000
                else:
                    # Add points based on the value (e.g., 2 => 200 points)
                    score += num * 100
                # If the value appears four times, add additional points
                if count == 4:
                    score += 1000 if num == 1 else num * 100
                # If the value appears five times, add more additional points
                elif count == 5:
                    score += 2000 if num == 1 else num * 200
                # If the value appears six times, add even more additional points
                elif count == 6:
                    score += 3000 if num == 1 else num * 300
            # If the value is 1 or 5 and appears less than three times
            elif num == 1 or num == 5:
                # Add points based on the value (1 => 100 points, 5 => 50 points) multiplied by its count
                score += (100 if num == 1 else 50) * count
        # Return the final score
        return score
    
    # Define a static method roll_dice that takes the number of dice to roll as input
    @staticmethod
    def roll_dice(num_dice):
        # Check if the number of dice is within the valid range (1 to 6)
        if not 1 <= num_dice <= 6:
            # Raise a ValueError if the input is not within the valid range
            raise ValueError("Number of dice must be between 1 and 6")
        # Generate a tuple of random dice values based on the input number of dice
        return tuple(random.randint(1, 6) for _ in range(num_dice))