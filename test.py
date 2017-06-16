import tkinter as tk
import tkinter.filedialog as tkf
import os
import time

file = tkf.askopenfilename(initialdir="C\\Voktrainer")
directory = os.path.split(file)[0]
print(directory)