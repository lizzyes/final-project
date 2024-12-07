import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
class VisualNovel:
    def __init__(self, root):
        self.root = root
        self.root.title("Finals Week Visual Novel")
        self.root.geometry("800x600")
        
    
        self.scene = 0
        self.dialogues = [
            "You decide to not text Chris until tomorrow ",
            "and finish up the work for your project. ",
            "Before you know it it is midnight ",
            "but your project is completely finished! ",
            "You give a big yawn and go to shower.",
            "Once done in the shower you get in bed",
            "and are able to fall asleep with the peace of mind knowing",
            "that you were able to finish the final!",

            "Today is your due day for the project! ",
            "You and your roommate wake up bright and ",
            "early and completely finish the final Project!",
            "You text Chris and tell him all about how you finished your project",
            "and would love to spend time with him now that finals are all over!",
            "He responds With so much excitement for you and all your hard work!",
            "He suggests going to a fair he saw a poster for and you happily agree!",
            "You and your roommate celebrate with some yummy breakfast and head to class.",
            "Once you both get to class you both give your presentation and get a 100%!",
            "You break out your phone and tell Chris the good news!",
            "Next"
        ]
        
        # Background images
        self.background_image=PhotoImage(file=r"C:\Users\dylan\Downloads\F9852533-DE91-456B-9197-C2B335D719D3.png")
        
        # Set up the canvas for background and character images
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()

        # Add the background image to the canvas
        self.background = self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        # Set up the text box for displaying dialogue
        self.dialogue_box = tk.Label(self.root, text="", font=("Helvetica", 12), bg="white", anchor="w", justify="left", width=70, height=4)
        self.dialogue_box.place(x=50, y=300)
        
        # Set up the button for advancing the dialogue
        self.advance_button = tk.Button(self.root, text="Next", font=("Helvetica", 14), command=self.advance_dialogue)
        self.advance_button.place(x=350, y=550)

        # Set the first dialogue
        self.update_dialogue()

    def update_dialogue(self):
        """Update the dialogue box and button based on the current scene."""
        if self.scene < len(self.dialogues):
            dialogue = self.dialogues[self.scene]
            self.dialogue_box.config(text=dialogue)

            if self.scene == 5:
                self.add_choices()

        else:
            self.end_game()

    def add_choices(self):
        """Add choices to the story at scene 2."""
        self.choice_button1 = tk.Button(self.root, text="Next", font=("Helvetica", 14), command=self.choice1)
        self.choice_button1.place(x=200, y=450)
        
        self.choice_button2 = tk.Button(self.root, text="Next", font=("Helvetica", 14), command=self.choice2)
        self.choice_button2.place(x=400, y=450)

    def choice1(self):
        """Choice 1: Next."""
        self.scene = 10
        self.remove_choices()
        self.update_dialogue()

    def choice2(self):
        """Choice 2: Next."""
        self.scene = 8
        self.remove_choices()
        self.update_dialogue()

    def remove_choices(self):
        """Remove choice buttons after making a decision."""
        self.scene = 6
        self.choice_button1.destroy()
        self.choice_button2.destroy()
