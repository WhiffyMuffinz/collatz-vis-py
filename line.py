from pyglet.gl import glBegin, glEnd, glColor3f, glVertex2f, GL_LINE_LOOP, GL_LINE_STRIP


class line:
    def __init__(self, input, colour):

        self.input = input
        self.colour = colour
        self.arr = []

        # parse string input for ints with error checking. if there is an error, ignore input
        try:
            for i in self.input.split(", "):
                self.arr.append(int(i))

        except ValueError:
            self.arr = []
            print("There was a non-int in the input string for {}".format(self))

    def __repr__(self):
        return "list with size {} and colour {}".format(len(self.input), self.colour)

    def get_max_value(self):
        out = self.arr[0]
        for i in self.arr:
            if i > out:
                out = i
        return out
    
    def draw(self, wind, debug = False):
        glColor3f(self.colour[0], self.colour[1], self.colour[2])

        max_val = self.get_max_value()
        length = len(self.arr)
        
        j = 0
        glBegin(GL_LINE_STRIP)
        for i in self.arr:
            glVertex2f(wind.width*(j/length), wind.height*(i/max_val))

            if debug:
                print("{},{}".format(wind.width*(j/length), wind.height*(i/max_val)))

            j+= 1
        glEnd()

        