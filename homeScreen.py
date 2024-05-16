#Page 1

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    # Create a bckground frame
    frame = tk.Frame(content_frame, bg='white') 
    frame.pack(fill='both', expand=True) 

    # Use a container frame inside to manage padding
    container = tk.Frame(frame, bg='white', padx=12, pady=12)  
    container.pack(expand=True, fill='both')

    # Place a label inside the container
    label = ttk.Label(container, text="This is Page 1", background='white')
    label.pack()

    return frame

