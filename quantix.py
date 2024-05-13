import tkinter as tk
from tkinter import ttk

def load_page(page):
    #Placeholder to load different pages.
    print(f'Loading page {page}')

def main():
    #Main application window.
    root = tk.Tk()
    root.title("Quantix - analytical platform")
    root.configure(bg='#1a1a1a')

    #dimensions for the window 70% of the screen size, center, position.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.7)
    height = int(screen_height * 0.7)
    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2) 
    root.geometry(f'{width}x{height}+{x_offset}+{y_offset}')

    #Navigation bar setup
    navbar = ttk.Frame(root)
    navbar.pack(side="top", fill="x")

    #Start Tkinetr event loop.
    root.mainloop()

if __name__ == "__main__":
    main()