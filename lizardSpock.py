""" ===================================================================

**Rock Paper Scissors Lizard Spock Program**

@author: Courtney Brown <cornedtea@proton.me>

"""

from tkinter import *
from tkinter import messagebox
from random import *
from time import *
import platform
user_system = platform.uname()


def main():
    """ Run GUI program."""
    program = RockPaperScissorsLizardSpock()
    program.root.mainloop()


class RockPaperScissorsLizardSpock:
    """
    GUI program that runs a rock paper scissors simulation.
    """
    CANVAS_BG_COLOR = '#a3afbf'  # bluish grey color
    INTERFACE_BG_COLOR = '#b1b6bd'  # grey-ish color

    class Movable:
        """ Create movable object for team Rock, Paper, Scissors, Lizard, or Spock."""
        def __init__(self, team_size: int, team: str = 'Rock' or 'Paper' or 'Scissors' or 'Lizard' or 'Spock'):
            self.name = team
            self.x_movement = choice([5, -5])
            self.y_movement = choice([5, -5])
            self.width = 0
            self.height = 0
            self.image = self.set_image(team_size)

        def get_type(self):
            """ Returns the type of the Movable object as a string."""
            return self.name

        def set_type(self, team: str, team_size):
            """ Changes the team and image for object"""
            self.name = team
            self.image = self.set_image(team_size)

        def set_image(self, team_size):
            """ Sets the image of the object based on the team name."""
            if self.name == 'Rock':
                image = PhotoImage(file='Images/rock.png')
                image = image.zoom(2)
                image = image.subsample(3 * team_size)
            elif self.name == 'Paper':
                image = PhotoImage(file='Images/paper.png')
                image = image.zoom(3)
                image = image.subsample(team_size)
            elif self.name == 'Scissors':
                image = PhotoImage(file='Images/scissors.png')
                image = image.zoom(2)
                image = image.subsample(3 * team_size)
            elif self.name == 'Lizard':
                image = PhotoImage(file='Images/lizard.png')
                image = image.zoom(3)
                image = image.subsample(2 * team_size)
            else:
                image = PhotoImage(file='Images/spock.png')
                image = image.zoom(3)
                image = image.subsample(8 * team_size)
            self.width = image.width()
            self.height = image.height()
            return image

        def place(self, canvas, width, height):
            """ Place Movable objects on canvas of given width and height. """
            start_x = randrange(self.width // 2 + 20, width - self.width // 2 - 20)
            start_y = randrange(self.height // 2 + 20, height - self.height // 2 - 20)
            object_ID = canvas.create_image(start_x, start_y, image=self.image)
            collided = self.overlap(canvas, object_ID)
            while collided:
                canvas.delete(object_ID)
                start_x = randrange(self.width // 2, width - self.width // 2)
                start_y = randrange(self.height // 2, height - self.height // 2)
                object_ID = canvas.create_image(start_x, start_y, image=self.image)
                collided = self.overlap(canvas, object_ID)
            return object_ID

        def overlap(self, canvas, object_ID):
            """ Detects object overlap on canvas. """
            zone = canvas.bbox(object_ID)
            near_object_IDs = canvas.find_overlapping(zone[0], zone[1], zone[2], zone[3])
            near_object_IDs = list(near_object_IDs)
            near_object_IDs.remove(object_ID)
            if len(near_object_IDs) != 0:
                overlap = True
            else:
                overlap = False
            return overlap

    def __init__(self):
        self.root = Tk()
        self.root.title = 'Rock Paper Scissors Lizard Spock'
        self.window_width, self.window_height = self.adjust_window()
        self.canvas_frame, self.interface_frame = self.create_frames()
        self.rock_objects = []
        self.paper_objects = []
        self.scissors_objects = []
        self.lizard_objects = []
        self.spock_objects = []
        self.rock_IDs = []
        self.paper_IDs = []
        self.scissors_IDs = []
        self.lizard_IDs = []
        self.spock_IDs = []
        self.objects = {}
        self.setup_button, self.start_button, self.guess_label, self.quit_button = self.create_widgets()
        self.is_running = False
        self.user_guess = StringVar()
        self.team_size = IntVar()
        self.winner = None
        self.set_callbacks()

    def adjust_window(self):
        """Create application window"""
        window_width = self.root.winfo_screenwidth() - 50
        window_height = self.root.winfo_screenheight() - 150
        screensize = str(window_width) + 'x' + str(window_height)
        self.root.geometry(screensize + '+0+5')
        if user_system.system == "Windows":
            self.root.resizable(FALSE, FALSE)
        return window_width, window_height

    def create_frames(self):
        """ Creates canvas and interface frames."""
        interface_frame = Frame(self.root, height=50, bg=RockPaperScissorsLizardSpock.INTERFACE_BG_COLOR)
        interface_frame.pack(fill='x')

        canvas_frame = Canvas(self.root, bg=RockPaperScissorsLizardSpock.CANVAS_BG_COLOR, bd=0)
        canvas_frame.pack(fill='both', expand=True)
        return canvas_frame, interface_frame

    def create_widgets(self):
        """ Create widgets in interface."""
        spacer = Label(self.interface_frame, text='', bg=RockPaperScissorsLizardSpock.INTERFACE_BG_COLOR)
        spacer.pack(side=LEFT, fill=Y, expand=True)
        setup_button = Button(self.interface_frame, text='Set up',
                              highlightbackground=RockPaperScissorsLizardSpock.INTERFACE_BG_COLOR)
        setup_button.pack(side=LEFT, padx=20, pady=10)
        start_button = Button(self.interface_frame, text='---',
                              highlightbackground=RockPaperScissorsLizardSpock.INTERFACE_BG_COLOR)
        start_button.pack(side=LEFT, padx=20, pady=10)
        guess_label = Label(self.interface_frame, text='No guess made.',
                            bg=RockPaperScissorsLizardSpock.INTERFACE_BG_COLOR, fg='black')
        guess_label.pack(side=LEFT, padx=20, pady=10)
        quit_button = Button(self.interface_frame, text='Quit',
                             highlightbackground=RockPaperScissorsLizardSpock.INTERFACE_BG_COLOR)
        quit_button.pack(side=LEFT, padx=20, pady=10)
        spacer = Label(self.interface_frame, text='', bg=RockPaperScissorsLizardSpock.INTERFACE_BG_COLOR)
        spacer.pack(side=LEFT, fill=Y, expand=True)
        return setup_button, start_button, guess_label, quit_button

    def create_teams(self):
        """ Creates teams of equal size, one each of rock, paper, scissors, lizard, and Spock."""
        rock_objects = []
        paper_objects = []
        scissors_objects = []
        lizard_objects = []
        spock_objects = []
        for i in range(self.team_size.get()):
            newRock = self.Movable(self.team_size.get(), 'Rock')
            rock_objects.append(newRock)
            newPaper = self.Movable(self.team_size.get(), 'Paper')
            paper_objects.append(newPaper)
            newScissors = self.Movable(self.team_size.get(), 'Scissors')
            scissors_objects.append(newScissors)
            newLizard = self.Movable(self.team_size.get(), 'Lizard')
            lizard_objects.append(newLizard)
            newSpock = self.Movable(self.team_size.get(), 'Spock')
            spock_objects.append(newSpock)
        return rock_objects, paper_objects, scissors_objects, lizard_objects, spock_objects

    def set_callbacks(self):
        """ Set commands for interface buttons."""
        self.setup_button['command'] = self.setup1
        self.start_button['command'] = self.start
        self.quit_button['command'] = self.quit

    def setTeamSize(self):
        """ Creates popup window to select size of team."""
        popup = Tk()
        self.team_size = IntVar(popup)
        self.team_size.set(0)
        explanation = Label(popup, text='Select the size of each team.', padx=5)
        explanation.grid(row=0, column=0, columnspan=3)
        slider = Scale(popup, orient=HORIZONTAL, from_=1, to=15, variable=self.team_size)
        slider.grid(row=1, column=0, columnspan=3)
        spacer = Label(popup, text='')
        spacer.grid(row=2, column=0)
        set_button = Button(popup, text="Done")
        set_button.grid(row=2, column=1)
        set_button['command'] = lambda: [self.setup2(), popup.destroy()]
        spacer = Label(popup, text='')
        spacer.grid(row=2, column=2)

    def guess(self):
        """ Provides window for user to guess which team will win."""
        popup = Tk()
        self.user_guess = StringVar(popup)
        self.user_guess.set('None')
        question = Label(popup, text='Who do you think will win?')
        question.grid(row=0, column=0, columnspan=5)
        radio_rock = Radiobutton(popup, text='Rock', variable=self.user_guess,
                                 value='Rock')
        radio_rock.grid(row=1, column=0, sticky=W)
        radio_paper = Radiobutton(popup, text='Paper', variable=self.user_guess,
                                  value='Paper')
        radio_paper.grid(row=1, column=1, sticky=W)
        radio_scissors = Radiobutton(popup, text='Scissors', variable=self.user_guess,
                                     value='Scissors')
        radio_scissors.grid(row=1, column=2, sticky=W)
        radio_lizard = Radiobutton(popup, text='Lizard', variable=self.user_guess,
                                   value='Lizard')
        radio_lizard.grid(row=1, column=3, sticky=W)
        radio_spock = Radiobutton(popup, text='Spock', variable=self.user_guess,
                                  value='Spock')
        radio_spock.grid(row=1, column=4, sticky=W)
        spacer = Label(popup)
        spacer.grid(row=2, column=0)
        spacer = Label(popup)
        spacer.grid(row=2, column=1)
        submit_button = Button(popup, text='Submit')
        submit_button.grid(row=2, column=2)
        submit_button['command'] = popup.destroy
        spacer = Label(popup)
        spacer.grid(row=2, column=3)
        spacer = Label(popup)
        spacer.grid(row=2, column=4)

    # def display_guess(self):
    #     """ Using this to test guess().
    #     To use, add `, command=display_guess` after the value section
    #     of each radiobutton in the function above."""
    #     self.guess_label['text'] = 'Your guess: {}'.format(self.user_guess.get())

    def populate(self):
        """ Places objects from teams onto canvas. The object lists keeps track of
        the canvas representations of the objects."""
        rock_IDs = []
        paper_IDs = []
        scissors_IDs = []
        lizard_IDs = []
        spock_IDs = []
        for obj in self.rock_objects:
            rock = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            rock_IDs.append(rock)
        for obj in self.paper_objects:
            paper = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            paper_IDs.append(paper)
        for obj in self.scissors_objects:
            scissors = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            scissors_IDs.append(scissors)
        for obj in self.lizard_objects:
            lizard = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            lizard_IDs.append(lizard)
        for obj in self.spock_objects:
            spock = obj.place(self.canvas_frame, self.window_width, self.window_height - 100)
            spock_IDs.append(spock)
        return rock_IDs, paper_IDs, scissors_IDs, lizard_IDs, spock_IDs

    def setup1(self):
        """ First half of simulation set-up."""
        self.objects = {}
        self.winner = None
        self.guess_label['text'] = 'Your guess: '
        self.canvas_frame.delete('all')
        self.setTeamSize()

    def setup2(self):
        """ Second half of simulation setup."""
        self.rock_objects, self.paper_objects, self.scissors_objects, self.lizard_objects, self.spock_objects \
            = self.create_teams()
        self.rock_IDs, self.paper_IDs, self.scissors_IDs, self.lizard_IDs, self.spock_IDs \
            = self.populate()
        for i in range(self.team_size.get()):
            self.objects[self.rock_objects[i]] = self.rock_IDs[i]
            self.objects[self.paper_objects[i]] = self.paper_IDs[i]
            self.objects[self.scissors_objects[i]] = self.scissors_IDs[i]
            self.objects[self.lizard_objects[i]] = self.lizard_IDs[i]
            self.objects[self.spock_objects[i]] = self.spock_IDs[i]
        self.guess()
        self.start_button['text'] = 'Start'
        self.setup_button['text'] = 'Reset'

    def start(self):
        """ Start or stop program. """
        if not self.is_running:
            self.is_running = True
            self.start_button['text'] = 'Stop'
            self.canvas_frame.after(100, self.animate())
        else:
            self.is_running = False
            self.start_button['text'] = 'Start'

    def quit(self):
        """ Gets confirmation to quit, and then closes window."""
        really_quit = messagebox.askyesno('Quit', 'Are you sure you want to quit?')
        if really_quit:
            self.root.destroy()

    def animate(self):
        """ Animate canvas objects. """
        while self.is_running:
            for team in [zip(self.rock_objects, self.rock_IDs), zip(self.paper_objects, self.paper_IDs),
                         zip(self.scissors_objects, self.scissors_IDs), zip(self.lizard_objects, self.lizard_IDs),
                         zip(self.spock_objects, self.spock_IDs)]:
                for obj, object_ID in team:
                    self.canvas_frame.move(object_ID, obj.x_movement, obj.y_movement)
                    obj_pos = self.canvas_frame.coords(object_ID)
                    xc, yc = obj_pos
                    if xc < abs(obj.width) / 2 or xc > self.window_width - abs(obj.width) / 2:
                        obj.x_movement = -obj.x_movement
                        self.canvas_frame.move(object_ID, obj.x_movement, obj.y_movement)
                    if yc < abs(obj.height) / 2 or yc > (self.window_height - 50) - abs(obj.height) / 2:
                        obj.y_movement = -obj.y_movement
                        self.canvas_frame.move(object_ID, obj.x_movement, obj.y_movement)
                    collided, colliders = self.detectCollision(object_ID)
                    if collided:
                        obj.x_movement = -obj.x_movement
                        obj.y_movement = -obj.y_movement
                        for collider in colliders:
                            self.collision(obj, collider)
            self.root.update()
            if user_system.system == "Windows":
                sleep(0.01)

    def detectCollision(self, object_ID):
        """ Detect collision of canvas objects and return list of collided objects."""
        zone = self.canvas_frame.bbox(object_ID)
        near_object_IDs = self.canvas_frame.find_overlapping(zone[0], zone[1], zone[2], zone[3])
        near_object_IDs = list(near_object_IDs)
        near_object_IDs.remove(object_ID)
        if len(near_object_IDs) != 0:
            collided = True
        else:
            collided = False
        return collided, near_object_IDs

    def collision(self, obj1, object_ID2):
        """ Determines team transfer on collision."""
        val_list = list(self.objects.values())
        key_list = list(self.objects.keys())
        position = val_list.index(object_ID2)
        obj2 = key_list[position]
        winner_team = self.determineWinner(obj1, obj2)
        self.canvas_frame.itemconfig(self.objects[obj1], image=obj1.image)
        self.canvas_frame.itemconfig(self.objects[obj2], image=obj2.image)
        self.root.update()
        if len(winner_team) == len(self.objects):
            self.is_running = False
            if winner_team == self.rock_objects:
                self.winner = 'Rock'
            elif winner_team == self.paper_objects:
                self.winner = 'Paper'
            elif winner_team == self.scissors_objects:
                self.winner = 'Scissors'
            elif winner_team == self.lizard_objects:
                self.winner = 'Lizard'
            elif winner_team == self.spock_objects:
                self.winner = 'Spock'
            self.endResult()

    def determineWinner(self, obj1, obj2):
        """ Takes colliding objects and determines winner"""
        losesAgainst = {'Rock': ['Scissors', 'Lizard'],
                        'Paper': ['Rock', 'Spock'],
                        'Scissors': ['Paper', 'Lizard'],
                        'Lizard': ['Paper', 'Spock'],
                        'Spock': ['Scissors', 'Spock']}
        winsAgainst = {'Rock': ['Paper', 'Spock'],
                       'Paper': ['Scissors', 'Lizard'],
                       'Scissors': ['Rock', 'Spock'],
                       'Lizard': ['Rock', 'Scissors'],
                       'Spock': ['Paper', 'Lizard']}
        if obj1.get_type() in losesAgainst[obj2.get_type()]:
            winner = obj2
            loser = obj1
        elif obj1.get_type() in winsAgainst[obj2.get_type()]:
            winner = obj1
            loser = obj2
        else:
            winner = None
            loser = None

        if winner in self.rock_objects:
            winner_team = self.rock_objects
            winner_IDs = self.rock_IDs
        elif winner in self.paper_objects:
            winner_team = self.paper_objects
            winner_IDs = self.paper_IDs
        elif winner in self.scissors_objects:
            winner_team = self.scissors_objects
            winner_IDs = self.scissors_IDs
        elif winner in self.lizard_objects:
            winner_team = self.lizard_objects
            winner_IDs = self.lizard_IDs
        elif winner in self.spock_objects:
            winner_team = self.spock_objects
            winner_IDs = self.spock_IDs
        else:
            winner_team = []
            winner_IDs = []

        if loser in self.rock_objects:
            loser_team = self.rock_objects
            loser_IDs = self.rock_IDs
        elif loser in self.paper_objects:
            loser_team = self.paper_objects
            loser_IDs = self.paper_IDs
        elif loser in self.scissors_objects:
            loser_team = self.scissors_objects
            loser_IDs = self.scissors_IDs
        elif loser in self.lizard_objects:
            loser_team = self.lizard_objects
            loser_IDs = self.lizard_IDs
        elif loser in self.spock_objects:
            loser_team = self.spock_objects
            loser_IDs = self.spock_IDs
        else:
            loser_team = []
            loser_IDs = []

        if winner:
            loser_team.remove(loser)
            loser_IDs.remove(self.objects[loser])
            winner_team.append(loser)
            winner_IDs.append(self.objects[loser])
            loser.set_type(winner.get_type(), self.team_size.get())

        return winner_team

    def endResult(self):
        """ Creates message box telling user if their guess was correct."""
        if self.user_guess.get() == self.winner:
            messagebox.showinfo('Result', 'Congratulations! You guessed {} and {} won.'
                                .format(self.user_guess.get(), self.winner))
        else:
            messagebox.showinfo('Result', 'You guessed {}, but {} won. Better luck next time!'
                                .format(self.user_guess.get(), self.winner))


if __name__ == '__main__':
    main()
