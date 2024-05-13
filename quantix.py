import tkinter as tk

def main():
    #Main application window.
    root = tk.Tk()
    root.title("Quantix - analytical platform")

    #Background color.
    root.configure(bg='#1a1a1a')

    #Calculate dimensions for the window to be 70% of the screen size.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.7)
    height = int(screen_height * 0.7)

    #Center the window on the screen.
    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2) 

    #Set the initial position and the size of the window.
    root.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
    

    #Start Tkinetr event loop.

if __name__ == "__main__":
    main()