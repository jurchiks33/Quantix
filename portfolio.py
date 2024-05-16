# portfolio.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    # Create a bckground frame
    frame = tk.Frame(content_frame, bg='green') 
    frame.pack(fill='both', expand=True) 

    # Use a container frame inside to manage padding
    container = tk.Frame(frame, bg='green', padx=12, pady=12)  
    container.pack(expand=True, fill='both')

    # Place a label inside the container
    label = ttk.Label(container, text="This is Page 2", background='green')
    label.pack()

    return frame
