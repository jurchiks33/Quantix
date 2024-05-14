#page4.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    #Background frame
    frame = tk.Frame(content_frame, bg='blanched almond')
    frame.pack(fill='both', expand=True)

    #Container frame for padding
    container = tk.Frame(frame, bg='blanched almond', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    #Place label inside container.
    label = ttk.Label(container, text="This is a page 4", background='blanched almond')
    label.pack()

    return frame