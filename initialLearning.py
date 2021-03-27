from manimlib import *

class TestScene(Scene):
  def construct(self):
    text = Text("I literally h8 u.")
    text.scale(2)

    self.play(Write(text))
    self.wait()
    self.exit()

class TestScene2(Scene):
  def construct(self):
    text = Text_Mobject("I literally $$3 u.")
    text.scale(2)

    self.play(Write(text))
    self.wait()

class TestScene3(Scene):
  def construct(self):
    bruh = SVGMobject("./thonk.svg")
    bruh.scale(2)

    self.play(Write(bruh))
    self.wait()
