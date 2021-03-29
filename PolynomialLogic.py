from manimlib import *
import numpy as np


class polynomial(Scene):
  def construct(self):
    text = Text("""
wat betekend het voor

een 2de graads functie om 2 

nulpunten te hebben""")
    text.scale(1)
    
    # self.play(Write(text, run_time=3))
    # self.wait(3)
    # self.play(FadeOut(text, run_time=2))

    axes = Axes((self.y_min, self.y_max), (self.x_min, self.x_max))
    axes.add_coordinate_labels()

    self.play(Write(axes, lag_ratio=0.01, run_time=1))
    
    polynomial_graph = axes.get_graph(
    lambda x: x**2 - x - 2,
    color=BLUE
    )
    polynomial_label = axes.get_graph_label(polynomial_graph, Tex("(x - 2)(x + 1)", direction=LEFT))
    
    self.play(
    ShowCreation(polynomial_graph, run_time=2))
    self.play(FadeIn(polynomial_label, LEFT, run_time=0.5))




    # self.play(FadeOut(dot, run_time=0.2))
    # self.play(FadeOut(polynomial_label, run_time=0.2))
    # self.play(FadeOut(polynomial_graph, run_time=0.2))
    # self.play(FadeOut(axes, run_time=0.2))
    # self.wait()

    Rectange = Square(side_length= 0.5)
    Rectange.set_fill(BLUE_E, 1)

    Rectange.shift(np.array((-4, 2., 0.)))
    self.add(Rectange)
    
    
    braceU = always_redraw(Brace, Rectange, UP)
    textU, numberU = labelU = VGroup(
    Text("(x - 2) = "),
    DecimalNumber(
        0,
        show_ellipsis=True,
        num_decimal_places=2,
        include_sign=True,
        )
    )
    numberU.scale(0.5)
    braceU.scale(0.5)
    labelU.scale(0.5)

    always(labelU.next_to, braceU, UP)
    f_always(numberU.set_value, Rectange.get_width)
    labelU.arrange(RIGHT)


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


    self.add(braceU, labelU, braceR, labelR)
    self.wait()
    
    
    dot = Dot(color=RED)
    dot.move_to(axes.i2gp(2, polynomial_graph))
    self.play(FadeIn(dot, scale=1))
    
    x_tracker = ValueTracker(2)
    f_always(
    dot.move_to,
    lambda: axes.i2gp(x_tracker.get_value(), polynomial_graph)
    )
    scale_factor = [-PI/2, 5/2, 0]
    scale_factor1 = [-(2/PI), -2/5, 0]
    self.play(
    Rectange.animate.scale(scale_factor),
    run_time=1,
    )
    self.wait()
    self.play(
    Rectange.animate.scale(scale_factor1),
    run_time=1,
    )
    # self.play(
    #             frame.animate.scale(scale_factor),
    #             zoomed_display.animate.scale(scale_factor),
    #             FadeOut(zoomed_camera_text),
    #             FadeOut(frame_text)
    #         )
        


    self.play(x_tracker.animate.set_value(-1), run_time=1.5)
    self.wait(1)
    self.play(x_tracker.animate.set_value(3), run_time=2)
    self.wait(1)
    # self.wait(1)
    # self.play(ReplacementTransform(labelU, labelU , run_time=2))
    # self.play(ReplacementTransform(labelR, labelR , run_time=2))

    #self.close()
    
class SecondPoly(polynomial):
    CONFIG = {
    "y_min": -3,
    "y_max": 5,
    "x_min": -3,
    "x_max": 4
    } 