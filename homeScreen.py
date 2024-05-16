#homeScreen.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame, load_page):
    # Create a background frame
    frame = tk.Frame(content_frame, bg='white')
    frame.pack(fill='both', expand=True)

    # Use a container frame inside to manage padding
    container = tk.Frame(frame, bg='white', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    # Add a welcome message
    welcome_label = ttk.Label(container, text="Welcome to Quantix", font=("Arial", 24), background='white')
    welcome_label.pack(pady=20)

    # Add a portfolio summary
    portfolio_label = ttk.Label(container, text="Portfolio Value: $100,000", font=("Arial", 16), background='white')
    portfolio_label.pack(pady=10)

    # Add market news
    news_label = ttk.Label(container, text="Market News: All stocks are up today!", font=("Arial", 16), background='white')
    news_label.pack(pady=10)

    # Add more widgets as needed
    details_button = ttk.Button(container, text="View Portfolio Details", command=lambda: load_page(content_frame, 2))
    details_button.pack(pady=10)
