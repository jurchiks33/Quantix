#Page 1

import tkinter as tk
from tkinter import ttk

def create_page(root):
    frame = ttk.Frame(root, padding="3 3 12 12")
    frame.pack(fill='both', expand=True)  # Use pack for better control
    frame.configure(background='white')  # Set background to white
    
    label = ttk.Label(frame, text="This is Page 1", background='white')
    label.pack()

    return frame