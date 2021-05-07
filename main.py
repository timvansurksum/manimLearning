from manimlib import *    
import numpy as np

# import pyautogui
# pos = pyautogui.position()

# x = [pos]
# i = 0


# while pos[0] < 1900:
#     pos = pyautogui.position()
#     print("x = " + str(pos[0]) + " y = " + str(pos[1]))
#     x.append(pos)
# print(x)




class polynomial3(Scene):

    def construct(self):
        def function(x): lambda x: x**2 - x - 2
        x = ValueTracker(2).get_value()

        y = x**2 - x -2
        print(x)
        print(y)
        