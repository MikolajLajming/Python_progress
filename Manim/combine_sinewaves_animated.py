from manim import *
from random import choice, uniform

ITERATIONS = 12


class TestSine(Scene):

    def __init__(self):
        super(TestSine, self).__init__()
        self.amplitudes = []
        self.frequencies = []
        self.phases = []
        self.colors = [WHITE, BLUE_A, BLUE_B, BLUE_C, BLUE_D, BLUE_E, PURE_BLUE, TEAL_A, TEAL_B,
                       TEAL_C, TEAL_D, TEAL_E, GREEN_A, GREEN_B, GREEN_C, GREEN_D, GREEN_E, PURE_GREEN,
                       YELLOW_A, YELLOW_B, YELLOW_D, YELLOW_E, GOLD_A, GOLD_B, GOLD_C, GOLD_D, GOLD_E,
                       RED_A, RED_B, RED_C, RED_D, RED_E, PURE_RED, MAROON_A, MAROON_B, MAROON_C, MAROON_D,
                       MAROON_E, PURPLE_A, PURPLE_B, PURPLE_C, PURPLE_D, PURPLE_E, PINK, LIGHT_PINK,
                       ORANGE, LIGHT_BROWN]

    def construct(self):

        ax = Axes(y_range=(-2, 2), x_range=(0, 20), y_length=4, x_length=10)
        group = VGroup()

        for i in range(0, ITERATIONS):
            # harmonic_amplitude = round((uniform(1, 2) - (i / 20)), 2)
            harmonic_amplitude = round((2 - (i / 12)), 2)
            self.amplitudes.append(harmonic_amplitude)
            harmonic_frequency = i + 1
            self.frequencies.append(harmonic_frequency)
            # harmonic_phase = uniform(0.0, 1.0)
            harmonic_phase = 0
            self.phases.append(harmonic_phase)
            harmonic_curve = ax.plot(
                self.generate_curve(harmonic_amplitude, harmonic_frequency, harmonic_phase)
            )
            if i != 0:
                harmonic_curve.color = choice(self.colors)
                harmonic_curve.stroke_width = 0.5
            else:
                harmonic_curve.color = BLUE
                harmonic_curve.stroke_width = 0.8
            group.add(harmonic_curve)
        curve_final = ax.plot(lambda x: self.combine_curves(x))
        curve_final.set_color(YELLOW)
        # self.add(curve_final)
        self.play(Create(ax))
        # self.play(Create(group[0]), Create(group[1]), Create(group[2]), Create(group[3]), Create(group[4]), Create(group[5]), Create(group[6]), Create(group[7]), Create(group[8]), Create(group[9]), Create(group[10]), Create(group[11]), run_time=3)
        self.play(Create(group), run_time=5)
        self.play(ReplacementTransform(group, curve_final), run_time=2)
        self.play(FadeOut(ax))

    def generate_curve(self, ampl, freq, ph):
        return lambda x: self.math_function(ampl=ampl, freq=freq, ph=ph, x=x)

    def math_function(self, ampl, freq, ph, x):
        return ampl * (1.0 / freq) * np.sin(freq * (x - ph))

    def combine_curves(self, x):
        cc = 0
        for n in range(0, ITERATIONS):
            cc += self.amplitudes[n] * (1.0 / self.frequencies[n]) * np.sin(self.frequencies[n] * (x - self.phases[n]))
        return cc

# class testSquare(Scene):
#     def construct(self):
#         square = Square(color=RED, fill_opacity=0.5)
#         self.play(DrawBorderThenFill(square, run_time=4))
