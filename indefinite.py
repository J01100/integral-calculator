import matplotlib
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Pow, sin, diff
import tkinter as tk
from IPython.display import display, Math
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use('TkAgg')

# DEFINITE, INDEFINITE, DIFFERNTIAL
# for page frames
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

def test(expr):
    return sp.latex(sp.integrate(expr))

def graph(event=None):
    i = entry.get()
    tmptext = test(i)

    # tmptext = "$"+ sp.latex(sp.sympify(i)) + "\ dx" + "=" + "$"
    # tmptext = "$"+ tmptext + "$"
    tmptext = "$\int$" + "$" + sp.latex(sp.sympify(i)) + "\ dx" + "=" +tmptext+ "+c" + "$"

    ax.clear()
    if len(tmptext) >= 120 and len(tmptext) <= 122:
        fs = 12
    elif len(tmptext) > 122 and len(tmptext) <= 140:
        fs = 11
        print(len(tmptext))
    else:
        fs = 16
    ax.text(0.05, .4, tmptext, fontsize=fs)
    canvas.draw()

root = tk.Tk()
root.title("Indefinite Integrals")
root.resizable(False, False)

mainframe = tk.Frame(root)
mainframe.pack()


entry = tk.Entry(mainframe, width=30)
entry.pack()

button = tk.Button(mainframe, text="Integrate", command=graph).pack()

label = tk.Label(mainframe)
label.pack()

fig = matplotlib.figure.Figure(figsize=(10, 1), dpi=100)
ax = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=label)
canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
canvas._tkcanvas.pack(side="top", fill="both", expand=True)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

try:
    graph()
except:
    pass

# root.bind("<Return>", graph)
root.mainloop()