from ten_thousand.game_logic import GameLogic

class TenThousandGame:
    def __init__(self):
        self.total_score = 0
        self.current_round = 0

    def play(self):
        print("Welcome to Ten Thousand")
        if input("(y)es to play or (n)o to decline\n> ").lower() != 'y':
            print("OK. Maybe another time")
            return

        while True:
            self.current_round += 1
            print(f"Starting round {self.current_round}")
            self.play_round()

            if input("Play another round? (y/n): ").lower() != 'y':
                break

        print(f"Thanks for playing. You earned {self.total_score} points")

    def play_round(self):
        num_dice = 6
        unbanked_points = 0

        while num_dice > 0:
            roll = GameLogic.roll_dice(num_dice)
            print(f"Rolling {num_dice} dice...")
            print("*** " + " ".join(map(str, roll)) + " ***")

            keeper_dice = input("Enter dice to keep, or (q)uit:\n> ")
            if keeper_dice.lower() == 'q':
                break

            keeper_dice = tuple(map(int, keeper_dice))
            unbanked_points += GameLogic.calculate_score(keeper_dice)
            num_dice -= len(keeper_dice)

            print(f"You have {unbanked_points} unbanked points and {num_dice} dice remaining")
            next_action = input("(r)oll again, (b)ank your points or (q)uit:\n> ").lower()
            
            if next_action == 'b':
                self.total_score += unbanked_points
                print(f"You banked {unbanked_points} points in round {self.current_round}")
                print(f"Total score is {self.total_score} points")
                break
            elif next_action == 'q':
                break

if __name__ == "__main__":
    game = TenThousandGame()
    game.play()
