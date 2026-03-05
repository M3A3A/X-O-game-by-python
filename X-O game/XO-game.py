
class player:
    def __init__(self):
        self.name = ""
        self.symbol = ""

    def choose_name(self):
        while True:
            name = input("Enter Your Name (Letters Only) : ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid Name, Please Use Letters Only")

    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, Please Enter Your Symbol (Single Letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid Symbol, Please Enter A Single Letter Only")


class menu:
    def display_main_menu(self):
        print("\nWelcome To The Game")
        print("[1] Start The Game")
        print("[2] Quit")
        return input("Enter Your Choice: ")

    def end_game(self):
        print("\n[1] Begin A New Game")
        print("[2] Quit")
        return input("Enter Your Choice: ")


class board:
    def __init__(self):
        self.board = [str(i) for i in range(1, 10)]

    def display_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 9)

    def update_board(self, choice, symbol):
        try:
            c = int(choice)
            if 1 <= c <= 9 and self.board[c - 1].isdigit():
                self.board[c - 1] = symbol
                return True
        except:
            pass
        return False

    def check_win(self):
        # مصفوفة احتمالات الفوز (8 احتمالات)
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # أفقي
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # عمودي
            [0, 4, 8], [2, 4, 6]  # قطري
        ]
        for combo in win_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        # إذا لم يعد هناك أرقام في اللوحة ولم يفز أحد، فهذا تعادل
        return all(not cell.isdigit() for cell in self.board)

    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class game:
    def __init__(self):
        self.players = [player(), player()]
        self.board = board()
        self.menu = menu()
        self.current_player_index = 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for i, p in enumerate(self.players):
            print(f"\nPlayer {i + 1} Setup:")
            p.choose_name()
            p.choose_symbol()

    def play_game(self):
        while True:
            self.board.display_board()
            p = self.players[self.current_player_index]
            print(f"\n{p.name}'s turn ({p.symbol})")

            move = input("Choose a position (1-9): ")
            if self.board.update_board(move, p.symbol):
                # فحص الفوز بعد كل حركة
                if self.board.check_win():
                    self.board.display_board()
                    print(f"\nCongratulations! {p.name} Wins! 🎉")
                    break
                # فحص التعادل
                if self.board.check_draw():
                    self.board.display_board()
                    print("\nIt's a Draw! 🤝")
                    break

                # تبديل اللاعب
                self.current_player_index = 1 - self.current_player_index
            else:
                print("Invalid move, try again.")

        # خيارات نهاية اللعبة
        if self.menu.end_game() == "1":
            self.board.reset_board()
            self.play_game()
        else:
            self.quit_game()

    def quit_game(self):
        print("Goodbye!")


# بدء التشغيل
if __name__ == "__main__":
    new_game = game()
    new_game.start_game()