#quantix.py

import tkinter as tk
from tkinter import ttk

# Import page modules
import page1
import page2

def clear_frame(frame):
    # Destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()

def load_page(content_frame, page):
    # Clear existing content
    clear_frame(content_frame)
    
    # Load the respective page
    if page == 1:
        page1.create_page(content_frame)
    elif page == 2:
        page2.create_page(content_frame)
    #below coming more pages later

def main():
    root = tk.Tk()
    root.title("Quantix - Analytical Platform")
    root.configure(bg='#1a1a1a')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.7)
    height = int(screen_height * 0.7)
    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2)
    root.geometry(f'{width}x{height}+{x_offset}+{y_offset}')

    # Navigation bar setup
    navbar = ttk.Frame(root)
    navbar.pack(side="top", fill="x")

    # Content frame
    content_frame = tk.Frame(root, bg='#1a1a1a')  # using tk.Frame to allow background setting
    content_frame.pack(fill='both', expand=True)

    # Buttons for the pages
    pages = 7
    for i in range(1, pages + 1):
        button = ttk.Button(navbar, text=f"Page {i}", command=lambda i=i: load_page(content_frame, i))
        button.pack(side="left")

    root.mainloop()

if __name__ == "__main__":
    main()
