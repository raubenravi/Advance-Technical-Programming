
import tkinter
from typing import Callable

import numpy as np
import seaborn as sns
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure






def servo(angle : int):
    #source: https://gist.github.com/Fonger/4f415822bb593c15c2a41fc29335f2e0
    dutyCycle =  ((0.025 + (0.12 - 0.025) * (angle / 180.0)) * 0x7fff)
    print("duty cycle is : ", dutyCycle)


