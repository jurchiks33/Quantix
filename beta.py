#page7.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    #Create background frame.
    frame = tk.Frame(content_frame, bg='dark slate gray')
    frame.pack(fill='both', expand=True)

    #Use container frame to manage padding
    container = tk.Frame(frame, bg='dark slate gray', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    #place label inside container.
    label = ttk.Label(container, text="This is Page 7", background='dark slate gray')
    label.pack()

    return frame