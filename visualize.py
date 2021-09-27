from pyglet.gl import Config
import pyglet
import random
from os import path

from line import line

FILE_PATH = r""

DEBUG = False


def get_window_config():
    disp = pyglet.canvas.get_display()
    screen = disp.get_default_screen()

    template = Config(double_buffer=True, samples=4, sample_buffers=1)
    try:
        config = screen.get_best_config(template)
    except pyglet.window.NoSuchConfigException:
        template = Config()
        config = screen.get_best_config(template)
    return config


def make_window():
    config = get_window_config()
    window = pyglet.window.Window(
        width=1280,
        height=720,
        config=config,
        caption="visualization of the collatz conjecture",
    )
    return window


def make_list(path = FILE_PATH):
    file = open(path, "r")
    full_text = file.read()

    split_text = full_text.split("\n")

    out = []

    for l in split_text:
        out.append(line(l, (random.random(), random.random(), random.random())))

    out.pop()
    return out 




def run():
    wind = make_window()

    line_list = make_list(FILE_PATH)

    def update(_):
        for l in line_list:
            l.draw(wind, DEBUG)
            

    pyglet.clock.schedule_interval(update, 0.0001)

    pyglet.app.run()


if __name__ == "__main__":
    run()