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

if __name__ == "__main__":
  ctk.set_appearance_mode("system")
  ctk.set_default_color_theme("blue")
  root = ctk.CTk()
  game = FifteenPuzzle(root)
  root.mainloop()
