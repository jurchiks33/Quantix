#tasks.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    #Create background frame.
    frame = tk.Frame(content_frame, bg='midnight blue')
    frame.pack(fill='both', expand=True)

    #Use container frame to manage padding
    container = tk.Frame(frame, bg='midnight blue', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    #place label inside container.
    label = ttk.Label(container, text="This is Page 8", background='midnight blue')
    label.pack()

    return frame