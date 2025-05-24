import random
import tkinter as tk
from tkinter import ttk
import time

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x400")
        self.root.configure(bg="#9ABDF0")  # Dark background theme

        # Initialize game variables
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        # Create GUI components
        self.setup_ui()

    def setup_ui(self):
        self.frame = tk.Frame(self.root, bg="#222831", padx=20, pady=20)
        self.frame.pack(expand=True)

        self.title_label = tk.Label(self.frame, text="🎯 Guess a number between 1 and 100", font=("Arial", 14), fg="#EEEEEE", bg="#222831")
        self.title_label.pack(pady=10)

        self.entry = tk.Entry(self.frame, font=("Arial", 14))
        self.entry.pack()

        self.submit_btn = tk.Button(self.frame, text="Submit Guess", font=("Arial", 14), command=self.check_guess, bg="#00ADB5", fg="white")
        self.submit_btn.pack(pady=10)

        self.feedback_label = tk.Label(self.frame, text="", font=("Arial", 12), fg="#FF2E63", bg="#222831")
        self.feedback_label.pack()

        self.progress = ttk.Progressbar(self.frame, maximum=5, mode="determinate", length=200)
        self.progress.pack(pady=5)

    def animate_feedback(self, message, color):
        """Animates feedback text with color transition"""
        for _ in range(3):  # Flash effect
            self.feedback_label.config(text=message, fg=color)
            self.root.update()
            time.sleep(0.2)
            self.feedback_label.config(text="", fg="#222831")
            self.root.update()
            time.sleep(0.2)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            self.progress.step(1)  # Progress indicator

            if guess < 1 or guess > 100:
                self.animate_feedback("❌ Out of range! Pick 1-100.", "#FF2E63")
                self.entry.delete(0, tk.END)
                return

            if guess < self.number_to_guess:
                self.animate_feedback("⬆ Too low! Try again.", "#F8B400")
            elif guess > self.number_to_guess:
                self.animate_feedback("⬇ Too high! Try again.", "#F8B400")
            else:
                self.animate_feedback(f"🎉 Correct! You guessed it in {self.attempts} tries!", "#00FF00")
                self.submit_btn.config(state=tk.DISABLED)

                # Background color transition effect
                for _ in range(5):
                    self.frame.config(bg="#00FF00")
                    self.root.update()
                    time.sleep(0.2)
                    self.frame.config(bg="#222831")
                    self.root.update()
                    time.sleep(0.2)

            # Clear input field after each attempt
            self.entry.delete(0, tk.END)

        except ValueError:
            self.animate_feedback("⚠ Invalid input! Enter a number.", "#FF2E63")
            self.entry.delete(0, tk.END)  # Clears invalid input

if __name__ == "__main__":
    root = tk.Tk()
    NumberGuessingGame(root)
    root.mainloop()
