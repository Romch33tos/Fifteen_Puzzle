import tkinter as tk
from random import shuffle
from tkinter import messagebox as mb
import customtkinter as ctk

class FifteenPuzzle:
  def __init__(self, root):
    self.root = root
    self.root.title("15")
    self.root.resizable(width=False, height=False)
    self.grid_size = 4
    self.tiles = list(range(1, self.grid_size * self.grid_size)) + [None]
    
    self.setup_menu()
    self.setup_ui()
    
  def setup_menu(self):
    menubar = tk.Menu(self.root)
    game_menu = tk.Menu(menubar, tearoff=0)
    game_menu.add_command(label="Новая игра", command=self.restart_game)
    menubar.add_cascade(label="Игра", menu=game_menu)
    self.root.config(menu=menubar)

  def setup_ui(self):
    self.tile_buttons = []
    for row in range(self.grid_size):
      button_row = []
      for col in range(self.grid_size):
        button = ctk.CTkButton(
          self.root,
          text="",
          text_color="white",
          width=50,
          height=50,
          command=lambda r=row, c=col: self.handle_move(r, c),
          corner_radius=8,
          font=("Arial", 14, "bold"),
        )
        button.grid(row=row, column=col, padx=2, pady=2)
        button_row.append(button)
      self.tile_buttons.append(button_row)
    self.update_ui()

def update_ui(self):
  for row in range(self.grid_size):
    for col in range(self.grid_size):
      index = row * self.grid_size + col
      if self.tiles[index] is None:
        self.tile_buttons[row][col].configure(text="", state="disabled")
      else:
        self.tile_buttons[row][col].configure(text=str(self.tiles[index]), state="normal")

def handle_move(self, row, col):
  empty_index = self.tiles.index(None)
  empty_row, empty_col = divmod(empty_index, self.grid_size)

  if (abs(empty_row - row) == 1 and empty_col == col) or (abs(empty_col - col) == 1 and empty_row == row):
    self.tiles[empty_index], self.tiles[row * self.grid_size + col] = self.tiles[row * self.grid_size + col], self.tiles[empty_index]
    self.update_ui()
    if self.check_win():
      self.show_win_message()

if __name__ == "__main__":
  ctk.set_appearance_mode("system")
  ctk.set_default_color_theme("blue")
  root = ctk.CTk()
  game = FifteenPuzzle(root)
  root.mainloop()
