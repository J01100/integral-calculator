# Integral Calculator 

A desktop application that returns the anti-derivative [and/or derivative] in LaTex—then plots the graph—of definite or indefinite inputs. Written in Python using Tkinter, Matplotlib, and Sympy. 

## How to install and run
1. Install Python 3.6+ from the official website.
2. Install the dependencies: Sumpy, Tkinter, and Matplotlib by running `pip install <dependency_name>` from the terminal.
3. Download/clone the repository then unzip the files.
4. Find the folder containing main.py.
5. Run from the terminal `python/python3 main.py` or use your IDE.

## Features
* Utilizes Sympy for symbolic calculations.
* Output is displayed in LaTex by using Tkinter's canvas and Matplotlib.
* Graphing of functions by using Symplot.
* Derivatives as an added bonus.

## Known issues:
* Terrible menu gui due to the gridding.
* Definite integral's lower and upper bound entries are oddly placed.
* Intervals for indefinite integrals and derivatives can be weird, hence, charts can be weird. (this is due to symplot's automatic interval assignment).

## Possible updates:
* Refine the GUI.
* Code refactoring for readability and reusability.

### MENU
![menu](https://i.ibb.co/J2c62pd/1.png)
### Indefinite Integrals
![indefinite](https://i.ibb.co/RYfyMxp/calc.png)
### Definite Integrals
![definite](https://i.ibb.co/VMj8Bfy/2.png)
### Derivatives
![derivative](https://i.ibb.co/fMLdkym/3.png)

