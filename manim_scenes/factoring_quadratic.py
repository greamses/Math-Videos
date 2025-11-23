from manim import *


class FactoringQuadratic(Scene):
    """Explain three essential factoring methods for x^2 + 4x + 4:
    1) Inspection (recognize a perfect square)
    2) Completing the square
    3) Using the quadratic formula / discriminant
    """

    def construct(self):
        expr = MathTex("x^2 + 4x + 4", font_size=96)
        expr.to_edge(UP)
        self.play(Write(expr))
        self.wait(0.6)

        # Method 1: Inspection / Perfect square
        m1_title = MathTex(r"\text{Method 1: Inspection (Perfect square)}", font_size=36)
        m1_equation = MathTex(r"(x+2)^2", font_size=72)
        m1_group = VGroup(m1_title, m1_equation).arrange(DOWN, center=False, aligned_edge=LEFT)
        m1_group.to_edge(LEFT).shift(DOWN * 0.5)

        self.play(FadeIn(m1_title, shift=RIGHT))
        self.wait(0.3)
        # transform the original into the factored form (matching tex makes this smooth)
        self.play(TransformMatchingTex(expr, MathTex("(x+2)^2", font_size=96)))
        self.play(Write(m1_equation))
        self.wait(1.2)

        # Reset expression on top for next method
        expr = MathTex("x^2 + 4x + 4", font_size=72)
        expr.to_edge(UP)
        self.play(Transform(m1_equation, expr), FadeOut(m1_title))
        self.wait(0.5)

        # Method 2: Completing the square (show steps)
        m2_title = MathTex(r"\text{Method 2: Completing the square}", font_size=36)
        # We'll show step-by-step aligned equations
        step1 = MathTex(r"x^2 + 4x + 4", font_size=48)
        step2 = MathTex(r"= x^2 + 4x + 4", font_size=48)
        step3 = MathTex(r"= (x^2 + 4x + 4)", font_size=48)
        step4 = MathTex(r"= (x+2)^2", font_size=64)

        m2_group = VGroup(m2_title, step1, step2, step3, step4).arrange(DOWN, center=False, aligned_edge=LEFT)
        m2_group.to_edge(LEFT).shift(DOWN * 0.5)

        self.play(FadeIn(m2_title, shift=RIGHT))
        self.wait(0.3)
        self.play(Write(step1))
        self.wait(0.5)

        # Show the completing-the-square idea: b/2 = 2 -> (b/2)^2 = 4
        hint = MathTex(r"\text{take }\frac{b}{2}=\frac{4}{2}=2 \Rightarrow 2^2=4", font_size=36)
        hint.next_to(step1, RIGHT, buff=1)
        self.play(Write(hint))
        self.wait(0.8)

        self.play(TransformMatchingTex(step1, step4))
        self.wait(1.0)
        self.play(FadeOut(m2_title, hint))

        # Restore top expression for Method 3
        expr = MathTex("x^2 + 4x + 4", font_size=72)
        expr.to_edge(UP)
        self.play(Transform(step4, expr))
        self.wait(0.5)

        # Method 3: Quadratic formula / discriminant
        m3_title = MathTex(r"\text{Method 3: Quadratic formula / Discriminant}", font_size=34)
        disc = MathTex(r"\Delta = b^2 - 4ac = 4^2 - 4\cdot 1 \cdot 4 = 16 - 16 = 0", font_size=40)
        roots = MathTex(r"x = \frac{-b \pm \sqrt{\Delta}}{2a} = \frac{-4}{2} = -2", font_size=48)
        fact = MathTex(r"\Rightarrow x^2 + 4x + 4 = (x+2)^2", font_size=56)

        m3 = VGroup(m3_title, disc, roots, fact).arrange(DOWN, center=False, aligned_edge=LEFT)
        m3.to_edge(LEFT).shift(DOWN * 0.5)

        self.play(FadeIn(m3_title, shift=RIGHT))
        self.wait(0.3)
        self.play(Write(disc))
        self.wait(0.6)
        self.play(Write(roots))
        self.wait(0.6)
        self.play(Write(fact))
        self.wait(1.2)

        # Final summary in the center
        summary = VGroup(
            MathTex(r"\textbf{All three methods agree:}", font_size=36),
            MathTex(r"x^2 + 4x + 4 = (x+2)^2", font_size=72),
        ).arrange(DOWN)
        summary.move_to(ORIGIN)
        self.play(FadeOut(m3), Transform(expr, summary[1]), Write(summary[0]))
        self.wait(2)
