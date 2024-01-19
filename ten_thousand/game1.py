from ten_thousand.game_logic import GameLogic

class TenThousandGame:
    def __init__(self):
        self.total_score = 0
        self.current_round = 0
        self.zilch = False

    def play(self):
        print("Welcome to Ten Thousand")
        if input("(y)es to play or (n)o to decline\n> ").lower() != 'y':
            print("OK. Maybe another time")
            return

        while True:
            self.current_round += 1
            print(f"Starting round {self.current_round}")
            if self.play_round() == 'quit':
                break
            if self.zilch:
                self.zilch = False
                continue

            if input("Play another round? (y/n): ").lower() != 'y':
                break

        print(f"Thanks for playing. You earned {self.total_score} points")

    def play_round(self):
        num_dice = 6
        unbanked_points = 0
        self.zilch = False

        while num_dice > 0:
            roll = GameLogic.roll_dice(num_dice)
            print(f"Rolling {num_dice} dice...")
            print("*** " + " ".join(map(str, roll)) + " ***")

            keeper_dice = self.get_valid_keepers(roll)
            if keeper_dice == 'quit':
                return 'quit'

            score = GameLogic.calculate_score(keeper_dice)
            if score == 0:
                print("****************************************")
                print("**        Zilch!!! Round over         **")
                print("****************************************")
                self.zilch = True
                return

            unbanked_points += score
            num_dice -= len(keeper_dice)

            if num_dice == 0 and GameLogic.calculate_score(roll) > 0:
                print("Hot dice! Rolling 6 dice again.")
                num_dice = 6

            print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")
            next_action = input("(r)oll again, (b)ank your points or (q)uit:\n> ").lower()

            if next_action == 'b':
                self.total_score += unbanked_points
                print(f"You banked {unbanked_points} points in round {self.current_round}")
                print(f"Total score is {self.total_score} points")
                break
            elif next_action == 'q':
                return 'quit'

    def get_valid_keepers(self, roll):
        while True:
            keeper_input = input("Enter dice to keep, or (q)uit:\n> ")
            if keeper_input.lower() == 'q':
                return 'quit'

            try:
                keeper_dice = tuple(map(int, keeper_input.split()))
                if GameLogic.validate_keepers(roll, keeper_dice):
                    return keeper_dice
                else:
                    print("Cheater!!! Or possibly made a typo...")
                    print("*** " + " ".join(map(str, roll)) + " ***")
            except ValueError:
                print("Invalid input. Please enter the dice values again.")

if __name__ == "__main__":
    game = TenThousandGame()
    game.play()
