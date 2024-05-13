#Page 1

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    frame = tk.Frame(content_frame, padding="3 3 12 12", bg='white')  # Using tk.Frame
    frame.pack(fill='both', expand=True)
    
    label = ttk.Label(frame, text="This is Page 1")
    label.pack()

    return frame
