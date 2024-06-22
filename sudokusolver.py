import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import time

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.style = ttk.Style("cosmo")  
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()
    
    def create_grid(self):
        frame = ttk.Frame(self.root)
        frame.pack(pady=(50, 0))  
        for row in range(9):
            for col in range(9):
                cell = ttk.Entry(frame, style="dark", width=3, justify="center", font=("Arial", 14))
                cell.grid(row=row, column=col, padx=1, pady=1)
                self.cells[row][col] = cell
    
    def create_buttons(self):
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        solve_button = ttk.Button(button_frame, text="Solve", command=self.solve_sudoku, bootstyle=SUCCESS)
        solve_button.grid(row=0, column=0, padx=10)

        reset_button = ttk.Button(button_frame, text="Reset", command=self.reset_board, bootstyle=WARNING)
        reset_button.grid(row=0, column=1, padx=10)
    
    def get_board(self):
        board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                val = self.cells[row][col].get()
                current_row.append(int(val) if val else 0)
            board.append(current_row)
        return board
    
    def set_board(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] != 0:
                    self.cells[row][col].delete(0, ttk.END)
                    self.cells[row][col].insert(0, str(board[row][col]))
                else:
                    self.cells[row][col].delete(0, ttk.END)

    def solve_sudoku(self):
        board = self.get_board()
        if not self.is_valid_sudoku(board):
            messagebox.showerror("Error", "The initial Sudoku board is invalid.")
            return
        if self.solve(board):
            self.set_board(board)
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku.")
    
    def is_valid_sudoku(self, board):
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != 0:
                    board[i][j] = 0
                    if not self.is_valid(board, num, (i, j)):
                        return False
                    board[i][j] = num
        return True

    def solve(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                self.update_single_cell(row, col, num)
                if self.solve(board):
                    return True
                board[row][col] = 0
                self.update_single_cell(row, col, 0)
        return False

    def find_empty(self, board):
        min_count, min_pos = 10, None
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    count = self.count_possible_values(board, (i, j))
                    if count < min_count:
                        min_count = count
                        min_pos = (i, j)
        return min_pos
    
    def count_possible_values(self, board, pos):
        row, col = pos
        possible_values = 0
        for num in range(1, 10):
            if self.is_valid(board, num, pos):
                possible_values += 1
        return possible_values
    
    def is_valid(self, board, num, pos):
        row, col = pos
        for i in range(9):
            if board[row][i] == num and col != i:
                return False
        for i in range(9):
            if board[i][col] == num and row != i:
                return False
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False
        return True
    
    def update_single_cell(self, row, col, value):
        self.cells[row][col].delete(0, ttk.END)
        if value != 0:
            self.cells[row][col].insert(0, str(value))
        self.root.update_idletasks()
        time.sleep(0.05)

    def reset_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, ttk.END)

if __name__ == "__main__":
    root = ttk.Window(themename="morph", resizable=(False, False), title="Sudoku Solver", size=(500, 500))
    app = SudokuGUI(root)
    root.mainloop()
