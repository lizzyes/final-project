import tkinter as tk
from tkinter import PhotoImage


class VisualNovel:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Novel")
        self.root.geometry("1080x670")

        # Initial scene setup
        self.scene = 0  # Start with the first scene
        self.dialogues = [
            "Chris has invited you to see a movie with some friends.",
            "You think about whether you should accept the invitation or not."
        ]

        # Background image (ensure the file path is valid)
        self.background_image = PhotoImage(file=r"/Users/Boo/Downloads/finalsweek.png")

        # Set up the canvas for background and character images
        self.canvas = tk.Canvas(self.root, width=1080, height=670)
        self.canvas.pack()

        # Add the background image to the canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        # Create a text ID for canvas text
        self.text_id = self.canvas.create_text(
            540, 520,  # Center the text at the bottom
            text="", font=("Helvetica", 16), fill="white", width=800, anchor="center"
        )

        # Set up the button for advancing the dialogue
        self.advance_button = tk.Button(self.root, text="Next", font=("Helvetica", 14), command=self.advance_dialogue)
        self.advance_button.place(x=500, y=600)  # Centered at the bottom

        # Set the first dialogue
        self.update_dialogue()

    def update_dialogue(self):
        """Update the dialogue box and button based on the current scene."""
        if self.scene < len(self.dialogues):
            dialogue = self.dialogues[self.scene]
            self.canvas.itemconfig(self.text_id, text=dialogue)

            # Add choices at scene 1
            if self.scene == 1:
                self.add_choices()
        else:
            self.end_game()

    def add_choices(self):
        """Add choices to the story at scene 1."""
        self.advance_button.place_forget()  # Hide the Next button while making a choice

        # Choice 1 Button
        self.choice_button1 = tk.Button(
            self.root, text="Tell Chris you can’t go", font=("Helvetica", 14), command=self.choice2
        )
        self.choice_button1.place(x=360, y=600)  # Left-aligned

        # Choice 2 Button
        self.choice_button2 = tk.Button(
            self.root, text="Tell Chris you will meet him there", font=("Helvetica", 14), command=self.choice1
        )
        self.choice_button2.place(x=640, y=600)  # Right-aligned

    def choice1(self):
        """Choice 1: Tell Chris you can’t go."""
        description = (
            "You and your roommate accept the invitation to go see the movie. "
            "You end up having a great time all together. It's been a hot minute since you got the chance to spend time with Chris "
            "and couldn’t be happier in that moment. It’s pretty late by the time you both return to the dorms, "
            "when you and your roommate realize how much work you still have to do on your group project. "
            "You both agree that tomorrow will be dedicated to working on the group project. Once you finish showering, "
            "you crawl into bed for the night."
        )
        self.dialogues = [description]  # Replace dialogues with the choice description
        self.scene = 0  # Reset the scene for the new description
        self.remove_choices()
        self.update_dialogue()

    def choice2(self):
        """Choice 2: Tell Chris you will meet him there."""
        description = (
            "The next morning you wake up bright and early. Despite how much you want to lay back down and fall back asleep, "
            "you get out of bed and start getting ready for the day. You had three classes that day with long gaps in between each. "
            "Once you're ready you head out to your first class. Your first class felt so slow that you almost fell asleep many times. "
            "You managed to stay awake and finally the class ended. You decide to stay on campus and find a cozy spot to work on some "
            "classwork that you couldn’t work on yesterday. Suddenly one of Chris’s friends recognizes you and says hi. They sit down next to you and "
            "start trying to have small talk with you, and you struggle to multitask between talking to the person and trying to get work done."
        )
        self.dialogues = [description]  # Replace dialogues with the choice description
        self.scene = 0  # Reset the scene for the new description
        self.remove_choices()
        self.update_dialogue()

    def remove_choices(self):
        """Remove choice buttons after making a decision."""
        self.choice_button1.destroy()
        self.choice_button2.destroy()
        self.advance_button.place(x=500, y=600)  # Show the Next button again

    def advance_dialogue(self):
        """Advance the story to the next scene."""
        self.scene += 1
        self.update_dialogue()

    def end_game(self):
        """End the game."""
        self.canvas.itemconfig(self.text_id, text="Thank you for playing!")
        self.advance_button.destroy()


# Create the root window
root = tk.Tk()

# Create an instance of the VisualNovel class
game = VisualNovel(root)

# Start the Tkinter event loop
root.mainloop()
