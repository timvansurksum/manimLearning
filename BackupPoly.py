class polynomial1(Scene):
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
    # dotR = Dot(color=RED)
    # dotL = Dot(color=YELLOW)
    # dotC = Dot(color=GREEN)
    # dotU = Dot(color=PINK)
    # dotD = Dot(color=BLUE)
    # dotR.move_to(np.array((1,0,0)))
    # dotL.move_to(np.array((-1,0,0)))   
    # dotC.move_to(np.array((0,0,0)))
    # dotU.move_to(np.array((0,1,0)))
    # dotD.move_to(np.array((0,-1,0)))
    # self.add(dotR, dotL, dotC, dotU, dotD)


    self.play(Write(axes, lag_ratio=0.01, run_time=1))

    polynomial_graph = axes.get_graph(
    lambda x: x**2 - x - 2,
    color=BLUE
    )
    polynomial_label = axes.get_graph_label(polynomial_graph, Tex("(x - 2)(x + 1)"), direction=LEFT)
    
    self.play(
    ShowCreation(polynomial_graph, run_time=2))
    self.play(FadeIn(polynomial_label, LEFT, run_time=0.5))


    Rectange = Square(side_length= 0.5)
    Rectange.set_fill(BLUE_E, 1)

    Rectange.shift(np.array((-4, 2., 0.)))
    self.add(Rectange)
    
    
    braceD = always_redraw(Brace, Rectange, UP)
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
    braceD.scale(0.5)
    labelU.scale(0.5)

    always(labelU.next_to, braceD, UP)
    f_always(numberU.set_value, Rectange.get_width)
    labelU.arrange(RIGHT)


    braceR = always_redraw(Brace, Rectange, RIGHT)
    textR, numberR = labelR = VGroup(
    Text("(x + 1) = "),
    DecimalNumber(
        0,
        show_ellipsis=True,
        num_decimal_places=4,
        include_sign=True,
    )
    )

    numberR.scale(0.5)
    braceR.scale(0.5)
    labelR.scale(0.5)
    
    labelR.arrange(RIGHT)
    always(labelR.next_to, braceR, RIGHT)
    f_always(numberR.set_value, Rectange.get_height)


    self.add(braceD, labelU, braceR, labelR)
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
    

class SecondPoly1(polynomial1):
    CONFIG = {
    "y_min": -3,
    "y_max": 5,
    "x_min": -3,
    "x_max": 4
    } 

    
class polynomial2(Scene):
  def construct(self):
    text = Text("""

    wat betekend het voor

    een 2de graads functie om 2 

    nulpunten te hebben""")
    text.scale(1)
    
    #self.play(Write(text, run_time=3))
    # self.wait(3)
    # self.play(FadeOut(text, run_time=2))
    # dotR = Dot(color=RED)
    # dotL = Dot(color=YELLOW)
    # dotC = Dot(color=GREEN)
    # dotU = Dot(color=PINK)
    # dotD = Dot(color=BLUE)
    # dotR.move_to(np.array((1,0,0)))
    # dotL.move_to(np.array((-1,0,0)))   
    # dotC.move_to(np.array((0,0,0)))
    # dotU.move_to(np.array((0,1,0)))
    # dotD.move_to(np.array((0,-1,0)))
    # self.add(dotR, dotL, dotC, dotU, dotD)

    axes = Axes((self.y_min, self.y_max), (self.x_min, self.x_max))
    axes.add_coordinate_labels(

    )
    axes.shift(np.array((-2, -1, 0)))
    axes.scale(0.75)
    self.play(Write(axes, lag_ratio=0.01, run_time=1))
    
    #y = (x-2)(x+1)
    text = Tex("(x - 2)(x + 1) = y", fill_color=BLUE)
    text.shift(np.array((-3.5, 3, 0.)))
    self.play(Write(text, run_time=1))
    
    
    
    polynomial_graph = axes.get_graph(
    lambda x: x**2 - x - 2,
    color=BLUE
    )

    #polynomial_label = axes.get_graph_label(polynomial_graph, label=Tex("(x - 2)(x + 1)", direction=RIGHT))
    
    self.play(
    ShowCreation(polynomial_graph, run_time=2))
    Rectange = Square(side_length= 0.5)
    Rectange.set_fill(BLUE_E, 1)
    
    self.add(Rectange)
    Rectange.shift(np.array((2, 1, 0.)))
    
    
    
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
    

class SecondPoly2(polynomial2):
    CONFIG = {
    "y_min": -3,
    "y_max": 5,
    "x_min": -3,
    "x_max": 4,

    } 
