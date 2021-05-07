from manimlib import *
import numpy as np
import pyautogui

class polynomial3(Scene):

  def construct(self):

    def add_dots():
        dotR = Dot(color=RED)
        dotL = Dot(color=YELLOW)
        dotC = Dot(color=GREEN)
        dotU = Dot(color=PINK)
        dotD = Dot(color=BLUE)
        dotR.move_to(np.array((1,0,0)))
        dotL.move_to(np.array((-1,0,0)))   
        dotC.move_to(np.array((0,0,0)))
        dotU.move_to(np.array((0,1,0)))
        dotD.move_to(np.array((0,-1,0)))
        self.add(dotR, dotL, dotC, dotU, dotD)
    add_dots()


    def add_axis():
        axes = Axes((self.y_min, self.y_max), (self.x_min, self.x_max))
        axes.add_coordinate_labels(

        )
        dotk = Dot(color=BLUE)
        dotk.move_to(np.array((-2, -1, 0)))
        self.add(dotk)
        axes.shift(np.array((-2, -1, 0)))
        axes.scale(0.75)
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        return axes, dotk
    axes, dotk = add_axis()


    def add_graphs():
        polynomial_graph = axes.get_graph(
        lambda x: x**2 - x - 2,
        color=BLUE
        )

        self.play(ShowCreation(polynomial_graph, run_time=1))
        return polynomial_graph
    polynomial_graph = add_graphs()


    def add_dot():
        dot1 = Dot(color=ORANGE)
        dot1.move_to(axes.i2gp(2, polynomial_graph))
        self.play(FadeIn(dot1, scale=1))

        return dot1
    dot1 = add_dot()


    
    def add_label():
        polynomial_label = Tex("(x - 2)(x + 1)", fill_color=GREEN).add_updater(lambda m: m.next_to(dot1, UP))
        self.play(Write(polynomial_label, run_time=0.5))
        return polynomial_label
    polynomial_label = add_label()
    
    def add_rectange(location=np.array((2, 1, 0.))):
        Rectange = Square(side_length= 0.5)
        Rectange.set_fill(BLUE_E, 1)
        self.add(Rectange)
        Rectange.shift(location)    

        braceD = always_redraw(Brace, Rectange, DOWN)
        textD, numberD = labelD = VGroup(
        Text("(x - 2) = "),
        DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=2,
            include_sign=True,
            )
        )
        numberD.scale(0.5)
        braceD.scale(0.5)
        labelD.scale(0.5)

        always(labelD.next_to, braceD, DOWN)
        f_always(numberD.set_value, Rectange.get_width)
        labelD.arrange(RIGHT)


        braceR = always_redraw(Brace, Rectange, RIGHT)
        textR, numberR = labelR = VGroup(
        Text("(x + 1) = "),
        DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=2,
            include_sign=True,
        )
        )

        numberR.scale(0.5)
        braceR.scale(0.5)
        labelR.scale(0.5)

        labelR.arrange(RIGHT)
        always(labelR.next_to, braceR, RIGHT)
        f_always(numberR.set_value, Rectange.get_height)
        self.add(braceD, labelD, braceR, labelR)
        return Rectange, braceD, textD, numberD, braceR, textR, numberR, labelR, labelD
    Rectange, braceD, textD, numberD, braceR, textR, numberR, labelR, labelD = add_rectange() 



    self.wait()


    x_tracker = ValueTracker(2)
    f_always(
    dot1.move_to,
    lambda: axes.i2gp(x_tracker.get_value(), polynomial_graph)
    )
    scale_factor = [-PI/2, 5/2, 0]
    x = x_tracker.get_value()
    y = x**2 - x - 2
    scale_factor1 = [x, y, 0]
    f_always(Rectange.scale(scale_factor1))

    self.play(x_tracker.animate.set_value(-1), run_time=1.5)
    self.wait(1)
    self.play(x_tracker.animate.set_value(3), run_time=2)
    self.wait(1)
    


class SecondPoly3(polynomial3):
    CONFIG = {
    "y_min": -3,
    "y_max": 5,
    "x_min": -3,
    "x_max": 4
    } 