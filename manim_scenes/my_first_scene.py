from manim import *


class MyScene(Scene):
    def construct(self):
        title = Text("Hello, Manim!", font_size=72)
        circle = Circle(radius=1.5, color=BLUE)
        square = Square(side_length=1.5, color=GREEN).next_to(circle, RIGHT, buff=1)

        # Animate shapes and text
        self.play(Create(circle))
        self.play(FadeIn(square, shift=UP))
        self.play(Write(title))
        self.play(circle.animate.shift(LEFT * 1.5), square.animate.shift(RIGHT * 1.5))
        self.play(title.animate.scale(0.7).to_edge(UP))
        self.wait(1)
