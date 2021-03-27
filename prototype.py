from manimlib import *

class TestScene(Scene):
  def construct(self):
    text = Text("""
wat betekend het voor

een 2de graads functie om 2 

nulpunten te hebben""")
    text.scale(1)
    
    self.play(Write(text, run_time=3))
    self.wait(3)
    self.play(FadeOut(text, run_time=2))

    axes = Axes((-3, 5), (-3, 4))
    axes.add_coordinate_labels()

    self.play(Write(axes, lag_ratio=0.01, run_time=1))
    
    polynomial_graph = axes.get_graph(
    lambda x: x**2-x-2,
    color=BLUE,
    )
    polynomial_label = axes.get_graph_label(polynomial_graph, Tex("(x - 2)(x + 1)", direction=LEFT))
    
    self.play(
    ShowCreation(polynomial_graph, run_time=4))
    self.play(FadeIn(polynomial_label, LEFT, run_time=1))
    
    
    dot = Dot(color=RED)
    dot.move_to(axes.i2gp(2, polynomial_graph))
    self.play(FadeIn(dot, scale=1))
    
    x_tracker = ValueTracker(2)
    f_always(
    dot.move_to,
    lambda: axes.i2gp(x_tracker.get_value(), polynomial_graph)
    )

    self.play(x_tracker.animate.set_value(-1), run_time=3)
    self.wait(2)
    self.play(x_tracker.animate.set_value(3), run_time=4)
    self.wait(3)