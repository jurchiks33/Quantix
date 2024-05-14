# quantix.py

import tkinter as tk
from tkinter import ttk

# Import page modules
import page1
import page2
import page3
import page4
import page5
import page6
import page7
import page8
import page9
import page10

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
    elif page == 3:
        page3.create_page(content_frame)
    elif page == 4:
        page4.create_page(content_frame)
    elif page == 5:
        page5.create_page(content_frame)
    elif page == 6:
        page6.create_page(content_frame)
    elif page == 7:
        page7.create_page(content_frame)
    elif page == 8:
        page8.create_page(content_frame)
    elif page == 9:
        page9.create_page(content_frame)
    elif page == 10:
        page10.create_page(content_frame)
    # Add more pages here.

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

    # Page names
    page_names = [
        "Dashboard", 
        "Analytics", 
        "Reports", 
        "Settings", 
        "Profile", 
        "Notifications", 
        "Messages", 
        "Tasks", 
        "Calendar", 
        "Help"
    ]

    # Buttons for the pages
    for i, name in enumerate(page_names, start=1):
        button = ttk.Button(navbar, text=name, command=lambda i=i: load_page(content_frame, i))
        button.pack(side="left")

    # Load Page 1 as a default page.
    load_page(content_frame, 1)

    root.mainloop()

if __name__ == "__main__":
    main()

