# page2.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    frame = tk.Frame(content_frame, padding="3 3 12 12", bg='white')  # Using tk.Frame
    frame.pack(fill='both', expand=True)
    
    label = ttk.Label(frame, text="This is Page 2")
    label.pack()

    return frame
