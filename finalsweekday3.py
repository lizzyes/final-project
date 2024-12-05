import tkinter as tk

class FinalsWeekApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Finals Week")
        self.root.geometry("500x300")

        # Pages
        self.pages = {
            "main": "Chris invites you to an event. What do you say?",
            "cant_go": "You told Chris you can’t go. He’s disappointed but understands you need to study.",
            "will_meet": "You told Chris you will meet him there. He’s excited to see you! BUT you did not study and prep for your final."
        }
        self.current_page = "main"

        # Page display
        self.page_label = tk.Label(
            self.root, text=self.pages[self.current_page], wraplength=450, font=("Arial", 14), justify="center"
        )
        self.page_label.pack(pady=20)

        # Button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)

        # Buttons
        self.cant_go_button = tk.Button(self.button_frame, text="Tell Chris you can’t go", command=self.go_to_cant_go)
        self.cant_go_button.grid(row=0, column=0, padx=10)

        self.will_meet_button = tk.Button(self.button_frame, text="Tell Chris you will meet him there", command=self.go_to_will_meet)
        self.will_meet_button.grid(row=0, column=1, padx=10)

        self.back_button = tk.Button(self.root, text="Go Back", command=self.go_back, state="disabled")
        self.back_button.pack(pady=10)

    # Navigation functions
    def go_to_cant_go(self):
        """Navigate to the 'can't go' page."""
        self.current_page = "cant_go"
        self.update_page()

    def go_to_will_meet(self):
        """Navigate to the 'will meet' page."""
        self.current_page = "will_meet"
        self.update_page()

    def go_back(self):
        """Navigate back to the main page."""
        self.current_page = "main"
        self.update_page()

    def update_page(self):
        """Update the page content and adjust button states."""
        self.page_label.config(text=self.pages[self.current_page])
        if self.current_page == "main":
            self.back_button.config(state="disabled")
        else:
            self.back_button.config(state="normal")

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    app = FinalsWeekApp(root)
    root.mainloop()
