import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Pow, sin, diff
from IPython.display import display, Math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')


class Indefinite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()
