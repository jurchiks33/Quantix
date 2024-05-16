#financialCalendar.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    #Background frame
    frame = tk.Frame(content_frame, bg='light sky blue')
    frame.pack(fill='both', expand=True)

    #Container frame for padding
    container = tk.Frame(frame, bg='light sky blue', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    #Place label inside container.
    label = ttk.Label(container, text="This is a page 9", background='light sky blue')
    label.pack()

    return frame