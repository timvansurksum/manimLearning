# -*- coding: utf-8 -*-
from manimlib import *

class TestScene(Scene):
  def construct(self):
    axes = Axes((3, 50), (0.2, 1))
    axes.add_coordinate_labels()
    
    self.play(Write(axes, lag_ratio=0.01, run_time=2))
    
    
    polynomial_graph = axes.get_graph(
    lambda x: 1-((30-1)/30)**x,
    color=BLUE,
    )
    polynomial_label = axes.get_graph_label(polynomial_graph, Tex("1-((30-1)/30)^x", direction=LEFT))
    
    self.play(
    ShowCreation(polynomial_graph, run_time=2))
    self.play(FadeIn(polynomial_label, LEFT, run_time=1))
