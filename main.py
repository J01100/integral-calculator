import tkinter as tk
from tkinter import font as tkfont
import matplotlib
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Pow, sin, diff
from IPython.display import display, Math
import sympy.plotting.plot as symplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

matplotlib.use('TkAgg')


class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Arial', size=14, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.grid(row=1, column=1)
        self.frames = {}
        for F in (Menu, Indefinite, Definite, Differential):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Menu", font=controller.title_font).pack()

        button1 = tk.Button(self, text="Indefinite Integrals",
                            command=lambda: controller.show_frame("Indefinite"))
        button2 = tk.Button(self, text="Definite Integrals",
                            command=lambda: controller.show_frame("Definite"))
        button3 = tk.Button(self, text="Differentials",
                            command=lambda: controller.show_frame("Differential"))
        button1.pack()
        button2.pack()
        button3.pack()


class Differential(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Derivatives", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("Menu"))

        def derive(expr):
            return sp.latex(sp.diff(expr))

        def graph(event=None):
            i = entry.get()
            tmptext = derive(i)

            tmptext = "$ \\frac{dy}{dx}" + sp.latex(sp.sympify(i)) + "=" + tmptext + "$"

            ax.clear()
            if 120 <= len(tmptext) <= 122:
                fs = 12
            elif 122 < len(tmptext) <= 140:
                fs = 11
                print(len(tmptext))
            else:
                fs = 16

            ax.text(0.05, .4, tmptext, fontsize=fs)
            canvas.draw()

            symplot(sp.diff(i))
            # symplot(i)

        entry = tk.Entry(self, width=70)
        entry.pack()

        tk.Button(self, text="Differentiate", command=graph).pack()

        label = tk.Label(self)
        label.pack()

        fig = matplotlib.figure.Figure(figsize=(10, 1), dpi=80)
        ax = fig.add_subplot(111)

        canvas = FigureCanvasTkAgg(fig, master=label)
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        canvas._tkcanvas.pack(side="top", fill="both", expand=True)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        back_button.pack()

        try:
            graph()
        except:
            pass


class Indefinite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Indefinite Integrals", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("Menu"))

        def integrate(expr):
            return sp.latex(sp.integrate(expr))

        def graph(event=None):
            i = entry.get()
            tmptext = integrate(i)

            tmptext = "$\int$" + "$" + sp.latex(sp.sympify(i)) + "\ dx" + "=" + tmptext + "+c" + "$"

            ax.clear()
            if 120 <= len(tmptext) <= 122:
                fs = 12
            elif 122 < len(tmptext) <= 140:
                fs = 11
                print(len(tmptext))
            else:
                fs = 16

            ax.text(0.05, .4, tmptext, fontsize=fs)
            canvas.draw()

            symplot(sp.integrate(i))
            # symplot(i)

        entry = tk.Entry(self, width=70)
        entry.pack()

        tk.Button(self, text="Integrate", command=graph).pack()

        label = tk.Label(self)
        label.pack()

        fig = matplotlib.figure.Figure(figsize=(10, 1), dpi=80)
        ax = fig.add_subplot(111)

        canvas = FigureCanvasTkAgg(fig, master=label)
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
        canvas._tkcanvas.pack(side="top", fill="both", expand=True)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        back_button.pack()

        try:
            graph()
        except:
            pass



class Definite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Definite Integrals", font=controller.title_font)
        label.grid(row=1, column=1, columnspan=6)
        back_button = tk.Button(self, text="Back",
                                command=lambda: controller.show_frame("Menu"))

        def integrate(expr, up, low):
            x = sp.symbols('x')
            return sp.latex(sp.integrate(expr, (x, low, up)))

        def graph(event=None):
            i = entry.get()
            l = lower.get()
            u = upper.get()
            tmptext = integrate(i, u, l)

            tmptext = "$\int_{%s}^{%s}$" % (l, u) + "$" + sp.latex(sp.sympify(i)) + "\ dx" + "=" + tmptext + "$"

            ax.clear()
            if 120 <= len(tmptext) <= 122:
                fs = 12
            elif 122 < len(tmptext) <= 140:
                fs = 11
                print(len(tmptext))
            else:
                fs = 16

            ax.text(0.05, .4, tmptext, fontsize=fs)
            canvas.draw()

            x = sp.symbols('x')
            symplot(i, (x, int(l), int(u)))


        upper = tk.StringVar()
        tk.Entry(self, textvariable=upper, width=3).grid(row=2, column=2, sticky='w')
        tk.Label(self, text="upper").grid(row=2, column=1, sticky='e')

        lower = tk.StringVar()
        tk.Entry(self, textvariable=lower, width=3).grid(row=3, column=2, sticky='w')
        tk.Label(self, text="lower").grid(row=3, column=1, sticky='e')

        entry = tk.StringVar()
        tk.Entry(self, textvariable=entry, width=50).grid(row=3, column=3)

        tk.Button(self, text="Integrate", command=graph).grid(row=3, column=4, sticky='w')

        label = tk.Label(self)
        label.grid(row=6, column=1, columnspan=6)

        fig = matplotlib.figure.Figure(figsize=(10, 1), dpi=80)
        ax = fig.add_subplot(111)

        canvas = FigureCanvasTkAgg(fig, master=label)
        canvas.get_tk_widget().grid(row=7, column=1, columnspan=6)
        canvas._tkcanvas.grid(row=8, column=1, columnspan=6)

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        back_button.grid(row=9, column=2)

        try:
            graph()
        except:
            pass


app = Main()


def main():
    app.title("Advanced Calculus")
    app.resizable(False, False)
    app.mainloop()


if __name__ == "__main__":
    main()