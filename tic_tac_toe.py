class TicTacToe:
    def __init__(self):
        """Initialize the game board and current player."""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        
    def display_board(self):
        """Display the current state of the board."""
        print("\n" + "=" * 17)
        for i, row in enumerate(self.board):
            print(f"  {row[0]} | {row[1]} | {row[2]} ")
            if i < 2:
                print("  " + "-" * 11)
        print("=" * 17)
        print("\nPosition guide:")
        print("  1 | 2 | 3 ")
        print("  " + "-" * 11)
        print("  4 | 5 | 6 ")
        print("  " + "-" * 11)
        print("  7 | 8 | 9 ")
        print()
        
    def is_valid_move(self, position):
        """Check if the move is valid."""
        row = (position - 1) // 3
        col = (position - 1) % 3
        return 1 <= position <= 9 and self.board[row][col] == ' '
    
    def make_move(self, position):
        """Make a move on the board."""
        row = (position - 1) // 3
        col = (position - 1) % 3
        self.board[row][col] = self.current_player
        
    def check_winner(self):
        """Check if there's a winner."""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        return None
    
    def check_draw(self):
        """Check if the game is a draw."""
        for row in self.board:
            if ' ' in row:
                return False
        return True
    
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play(self):
        """Main game loop."""
        print("\n" + "=" * 40)
        print("  Welcome to Tic-Tac-Toe!")
        print("=" * 40)
        print("\nPlayers take turns. Enter a position (1-9) to make your move.")
        print("Player X goes first!\n")
        
        while not self.game_over:
            self.display_board()
            
            # Get player input
            try:
                position = int(input(f"Player {self.current_player}, enter position (1-9): "))
                
                if not self.is_valid_move(position):
                    print("Invalid move! That position is already taken or out of range. Try again.")
                    continue
                
                # Make the move
                self.make_move(position)
                
                # Check for winner
                winner = self.check_winner()
                if winner:
                    self.game_over = True
                    self.winner = winner
                    self.display_board()
                    print(f"\n🎉 Congratulations! Player {winner} wins! 🎉")
                    break
                
                # Check for draw
                if self.check_draw():
                    self.game_over = True
                    self.display_board()
                    print("\n🤝 It's a draw! Good game!")
                    break
                
                # Switch player
                self.switch_player()
                
            except ValueError:
                print("Invalid input! Please enter a number between 1 and 9.")
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
        
        # Ask if players want to play again
        if not self.game_over:
            return
        
        try:
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again in ['yes', 'y']:
                return True
            else:
                print("\nThanks for playing! Goodbye!")
                return False
        except:
            return False


def main():
    """Main function to run the game."""
    while True:
        game = TicTacToe()
        play_again = game.play()
        if not play_again:
            break


if __name__ == "__main__":
    main()

