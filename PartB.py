class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Checkers:
    board_size = 8 

    def __init__(self):
        self.board = [["." for _ in range(8)] for _ in range(8)]
        self.current_player = "Red"

        # Set up pieces
        for row in range(8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    if row < 3:
                        self.board[row][col] = "B"
                    elif row > 4:
                        self.board[row][col] = "R"

    @classmethod
    def get_board_size(cls):
        return cls.board_size

    # Static method
    @staticmethod
    def is_valid_position(row, col):
        return 0 <= row < 8 and 0 <= col < 8

    # Instance method
    def display_board(self):
        print("  0 1 2 3 4 5 6 7")
        for i, row in enumerate(self.board):
            print(i, " ".join(row))

#Testing the game
player1 = Player("Alice", "Red")
player2 = Player("Bob", "Black")

game = Checkers()

print("Player 1:", player1.name, "-", player1.color)
print("Player 2:", player2.name, "-", player2.color)

print("Board Size:", Checkers.get_board_size())
print("Valid Position (3, 4):", Checkers.is_valid_position(3, 4))
print("Valid Position (9, 2):", Checkers.is_valid_position(9, 2))

print("\nInitial Board:")
game.display_board()
