# Integral Calculator 

A desktop application that returns the anti-derivative [and/or derivative] in LaTex—then plots the graph—of definite or indefinite inputs. Written in Python using Tkinter, Matplotlib, and Sympy. 

## How to install and run
1. Install python 3.6+ from the official website.
2. Download/clone the repository then unzip the files.
3. Find the folder containing main.py.
4. Run from the terminal `python/python3 main.py` or use your IDE.

## Features
* Utilizes Sympy for symbolic calculations.
* Output is displayed in LaTex by using Tkinter's canvas and Matplotlib.
* Graphing of functions by using Symplot.
* Derivatives as an added bonus.

## Known issues:
* terrible menu gui due to the gridding.
* definite integral's lower and upper bound entries are oddly placed
* intervals for indefinite integrals and derivatives can be weird, hence, charts can be weird. (this is due to symplot's automatic interval assignment)

### MENU
![menu](https://i.ibb.co/J2c62pd/1.png)
### Indefinite Integrals
![indefinite](https://i.ibb.co/RYfyMxp/calc.png)
### Definite Integrals
![definite](https://i.ibb.co/VMj8Bfy/2.png)
### Derivatives
![derivative](https://i.ibb.co/fMLdkym/3.png)

