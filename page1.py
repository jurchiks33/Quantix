# page1.py

import tkinter as tk
from tkinter import ttk

def create_page(root):
    frame = ttk.Frame(root, padding="3 3 12 12")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    label = ttk.Label(frame, text="This is Page 1")
    label.grid(column=0, row=0, sticky=(tk.W, tk.E))

    return frame