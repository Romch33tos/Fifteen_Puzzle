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
    
  def setup_menu(self):
    menubar = tk.Menu(self.root)
    game_menu = tk.Menu(menubar, tearoff=0)
    game_menu.add_command(label="Новая игра", command=self.restart_game)
    menubar.add_cascade(label="Игра", menu=game_menu)
    self.root.config(menu=menubar)
    
if __name__ == "__main__":
  ctk.set_appearance_mode("system")
  ctk.set_default_color_theme("blue")
  root = ctk.CTk()
  game = FifteenPuzzle(root)
  root.mainloop()
