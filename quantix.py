import tkinter as tk

def main():
    #Main application window.
    root = tk.TK()
    root.title("Quantix - analytical platform")

    #Background color.
    root.configure(bg='1a1a1a')

    #Calculate dimensions for the window to be 70% of the screen size.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.7)
    height = int(screen_height * 0.7)
        