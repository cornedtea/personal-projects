"""
@author: Courtney Brown <cornedtea@proton.me>
"""

from tkinter import *


def main():
    DrawBraille().root.mainloop()


def add_numbers(bd):
    """ Add the digits 1-9 to the Braille dictionary bd"""
    bd['1'] = [1, 0, 0, 0, 0, 0]
    bd['2'] = [1, 1, 0, 0, 0, 0]
    bd['3'] = [1, 0, 0, 1, 0, 0]
    bd['4'] = [1, 0, 0, 1, 1, 0]
    bd['5'] = [1, 0, 0, 0, 1, 0]
    bd['6'] = [1, 1, 0, 1, 0, 0]
    bd['7'] = [1, 1, 0, 1, 1, 0]
    bd['8'] = [1, 1, 0, 0, 1, 0]
    bd['9'] = [0, 1, 0, 1, 0, 0]
    bd['0'] = [0, 1, 0, 1, 1, 0]


def add_letters(bd):
    """ Add the letters a-z to the Braille dictionary, bd."""
    bd['a'] = [1, 0, 0, 0, 0, 0]
    bd['b'] = [1, 1, 0, 0, 0, 0]
    bd['c'] = [1, 0, 0, 1, 0, 0]
    bd['d'] = [1, 0, 0, 1, 1, 0]
    bd['e'] = [1, 0, 0, 0, 1, 0]
    bd['f'] = [1, 1, 0, 1, 0, 0]
    bd['g'] = [1, 1, 0, 1, 1, 0]
    bd['h'] = [1, 1, 0, 0, 1, 0]
    bd['i'] = [0, 1, 0, 1, 0, 0]
    bd['j'] = [0, 1, 0, 1, 1, 0]

    bd['k'] = [1, 0, 1, 0, 0, 0]
    bd['l'] = [1, 1, 1, 0, 0, 0]
    bd['m'] = [1, 0, 1, 1, 0, 0]
    bd['n'] = [1, 0, 1, 1, 1, 0]
    bd['o'] = [1, 0, 1, 0, 1, 0]
    bd['p'] = [1, 1, 1, 1, 0, 0]
    bd['q'] = [1, 1, 1, 1, 1, 0]
    bd['r'] = [1, 1, 1, 0, 1, 0]
    bd['s'] = [0, 1, 1, 1, 0, 0]
    bd['t'] = [0, 1, 1, 1, 1, 0]

    bd['u'] = [1, 0, 1, 0, 0, 1]
    bd['v'] = [1, 1, 1, 0, 0, 1]
    bd['x'] = [1, 0, 1, 1, 0, 1]
    bd['y'] = [1, 0, 1, 1, 1, 1]
    bd['z'] = [1, 0, 1, 0, 1, 1]

    bd['w'] = [0, 1, 0, 1, 1, 1]


def grade2(bd):
    """Upgrade a grade 1 Braille dictionary, bd, to grade 2."""
    bd['but'] = [1, 1, 0, 0, 0, 0]
    bd['can'] = [1, 0, 0, 1, 0, 0]
    bd['do'] = [1, 0, 0, 1, 1, 0]
    bd['every'] = [1, 0, 0, 0, 1, 0]
    bd['from'] = [1, 1, 0, 1, 0, 0]
    bd['go'] = [1, 1, 0, 1, 1, 0]
    bd['have'] = [1, 1, 0, 0, 1, 0]
    bd['just'] = [0, 1, 0, 1, 1, 0]

    bd['knowledge'] = [1, 0, 1, 0, 0, 0]
    bd['like'] = [1, 1, 1, 0, 0, 0]
    bd['more'] = [1, 0, 1, 1, 0, 0]
    bd['not'] = [1, 0, 1, 1, 1, 0]
    bd['people'] = [1, 1, 1, 1, 0, 0]
    bd['quite'] = [1, 1, 1, 1, 1, 0]
    bd['rather'] = [1, 1, 1, 0, 1, 0]
    bd['so'] = [0, 1, 1, 1, 0, 0]
    bd['that'] = [0, 1, 1, 1, 1, 0]

    bd['us'] = [1, 0, 1, 0, 0, 1]
    bd['very'] = [1, 1, 1, 0, 0, 1]
    bd['it'] = [1, 0, 1, 1, 0, 1]
    bd['you'] = [1, 0, 1, 1, 1, 1]
    bd['as'] = [1, 0, 1, 0, 1, 1]

    bd['will'] = [0, 1, 0, 1, 1, 1]


def create_braille_dictionary():
    """Creates and returns a Braille dictionary"""
    braille_dictionary = {" ": [0, 0, 0, 0, 0, 0]}
    add_numbers(braille_dictionary)
    add_letters(braille_dictionary)
    grade2(braille_dictionary)
    return braille_dictionary


class DrawBraille:
    def __init__(self):
        self.root = Tk()
        self.root.title("Braille Text Interface")
        self.window_width = self.root.winfo_screenwidth() - 50
        self.window_height = self.root.winfo_screenheight() - 100
        self.screensize = str(self.window_width) + 'x' + str(self.window_height)
        self.root.geometry(self.screensize + '+0+5')
        self.canvas = Canvas(self.root, bg="#F7E1C8")
        self.canvas.pack(expand=True, fill="both")
        self.text = Label(self.canvas, text="Begin typing (all lowercase, no punctuation, space to display word)",
                          bg="#F7E1C8")
        self.text.place(x=0, y=2)
        self.word_display = Label(self.canvas, text="", bg="#F7E1C8")
        self.word_display.place(x=400, y=2)
        self.last_5_words = []
        self.root.bind("<Key>", self.addLetter)
        self.bd = create_braille_dictionary()
        self.word = ""
        self.char_tracker = 0
        self.line_tracker = 0

    def addLetter(self, event):
        key = event.keysym
        if self.char_tracker > 40:
            self.line_tracker += 1
            self.char_tracker = 0
        if key == "space":
            self.draw_braille()
            self.update_display()
            self.word = ""
        elif key == "BackSpace":
            self.word = self.word[:-1]
        elif key == "Return":
            self.line_tracker += 1
            self.char_tracker = 0
            self.draw_braille()
            self.update_display()
            self.word = ""
        else:
            self.word += key

    def draw_character(self, character: str, start_x, start_y):
        """ Draw a single Braille character"""
        diameter = 10
        x00 = start_x + 1
        y00 = start_y + 1
        for i in range(6):
            if i // 3 < 1:
                x0 = x00
                y0 = y00 + i * (2 + diameter)
            else:
                x0 = x00 + 2 + diameter
                y0 = start_y + 1 + (i - 3) * (2 + diameter)
            x1 = x0 + diameter
            y1 = y0 + diameter
            if self.bd[character][i] == 0:
                fill_color = "#F7E1C8"
            else:
                fill_color = "black"
            circle = self.canvas.create_oval(x0, y0, x1, y1, fill=fill_color)
        self.char_tracker += 1

    def draw_braille(self):
        """ Draw Braille characters"""
        self.word = self.word.lower()
        if self.word in self.bd:
            self.draw_character(self.word, self.char_tracker * 24 + 20, self.line_tracker * 36 + 50)
        else:
            for letter in self.word:
                self.draw_character(letter, self.char_tracker * 24 + 20, self.line_tracker * 36 + 50)

        self.draw_character(" ", self.char_tracker * 24 + 20, self.line_tracker * 36 + 50)

    def update_display(self):
        self.last_5_words = self.last_5_words[1:]
        self.last_5_words.append(self.word)
        self.word_display['text'] = "Last word: "
        for word in self.last_5_words:
            self.word_display['text'] = self.word_display['text'] + word + " "


if __name__ == "__main__":
    main()
