import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("三目並べ")
        self.turn = "〇"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.buttons = [[tk.Button(root, text="", font=("Arial", 24), width=5, height=2, command=lambda r=row, c=col: self.make_move(r, c)) 
                        for col in range(3)] for row in range(3)]
        
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.turn
            self.buttons[row][col].config(text=self.turn)

            if self.check_winner():
                return

            self.turn = "×" if self.turn == "〇" else "〇"

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                self.show_result(f"{row[0]} の勝ち!")
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                self.show_result(f"{self.board[0][col]} の勝ち!")
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "" or self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.show_result(f"{self.board[1][1]} の勝ち!")
            return True

        
        if all(all(cell != "" for cell in row) for row in self.board):
            self.show_result("引き分け!")
            return True

        return False

    def show_result(self, message):
        for row in self.buttons:
            for btn in row:
                btn.config(state="disabled")
        label = tk.Label(self.root, text=message, font=("Arial", 20))
        label.grid(row=3, column=0, columnspan=3)

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()