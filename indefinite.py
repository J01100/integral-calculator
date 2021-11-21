import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Pow, sin, diff
from IPython.display import display, Math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import main

matplotlib.use('TkAgg')


def _integrate(expr):
    return sp.latex(sp.integrate(expr))


class Indefinite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("Menu"))
        button.pack()

        def _graph(self, event=None):
            i = entry.get()
            to_latex = _integrate(i)
            to_latex = "$\int$" + "$" + sp.latex(sp.sympify(i)) + "\ dx" + "=" + to_latex + "+c" + "$"
            ax.clear()

            if 120 <= len(to_latex) <= 122:
                fs = 12
            elif 122 < len(to_latex) <= 140:
                fs = 11
                print(len(to_latex))
            else:
                fs = 16

            ax.text(0.05, .4, to_latex, fontsize=fs)
            canvas.draw()

        mainframe = tk.Frame(main.app.container)
        mainframe.pack()

        entry = tk.Entry(mainframe, width=30)
        entry.pack()

        button = tk.Button(mainframe, text="Integrate", command=_graph).pack()

        label = tk.Label(mainframe)
        label.pack()

        fig = matplotlib.figure.Figure(figsize=(10, 1), dpi=100)
        ax = fig.add_subplot(111)

        canvas = FigureCanvasTkAgg(fig, master=label)
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        canvas.tkcanvas.pack(side="top", fill="both", expand=True)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        try:
            _graph()
        except TypeError or Exception:
            pass

        main.Main.app.bind("<Return>", _graph)
        main.Main.app.mainloop()
