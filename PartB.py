#Ready For Marking
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class AIPlayer(Player):
    def __init__(self, name, color):
        super().__init__(name, color)

    def make_move(self, game):
        piece = "B" if self.color == "Black" else "R"
        direction = 1 if piece == "B" else -1

        for row in range(8):
            for col in range(8):
                if game.board[row][col] == piece:
                    for change in [-1, 1]:
                        new_row = row + direction
                        new_col = col + change

                        if game.move_piece(row, col, new_row, new_col):
                            print(f"{self.name} moved a piece!")
                            return

        print("No available moves.")

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

    def move_piece(self, row, col, new_row, new_col):
        if not (self.is_valid_position(row, col) and
                self.is_valid_position(new_row, new_col)):
            return False

        piece = self.board[row][col]

        if piece not in ["R", "B"]:
            return False

        if self.board[new_row][new_col] != ".":
            return False

        direction = -1 if piece == "R" else 1

        if new_row - row != direction or abs(new_col - col) != 1:
            return False

        self.board[new_row][new_col] = piece
        self.board[row][col] = "."

        return True

#Testing the game
player1 = Player("Alice", "Red")
player2 = AIPlayer("Computer", "Black")

game = Checkers()

print("Player 1:", player1.name, "-", player1.color)
print("Player 2:", player2.name, "-", player2.color)

print("Board Size:", Checkers.get_board_size())
print("Valid Position (3, 4):", Checkers.is_valid_position(3, 4))
print("Valid Position (9, 2):", Checkers.is_valid_position(9, 2))

print("\nInitial Board:")
game.display_board()

print("\nPlayer 1 Move:")
print("Move Successful:", game.move_piece(5, 0, 4, 1))
game.display_board()

print("\nInvalid Move:")
print("Move Successful:", game.move_piece(5, 2, 3, 2))

print("\nAI Player Move:")
player2.make_move(game)
game.display_board()
