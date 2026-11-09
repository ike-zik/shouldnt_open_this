import tkinter as tk
import random

# Settings
MAX_WINDOWS = 250
WINDOW_WIDTH = 250
WINDOW_HEIGHT = 120
SPAWN_DELAY = 10

windows = []

root = tk.Tk()
root.title("hehehehe")
root.geometry("350x150")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


def spawn_window():
    if len(windows) >= MAX_WINDOWS:
        return

    x = random.randint(0, screen_width - WINDOW_WIDTH)
    y = random.randint(0, screen_height - WINDOW_HEIGHT)

    window = tk.Toplevel(root)
    window.title("NO ESCAPE >:)")
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

    tk.Label(
        window,
        text="---good luck---",
        font=("Arial", 12, "bold")
    ).pack(expand=True)
    tk.Label(
            window,
            text="think about it next time when you say something weird",
            font=("Arial", 6, "bold")
        ).pack(expand=True)

    tk.Label(
        window,
        text="esc to close",
        font=("Arial", 3, "bold")
    ).pack(expand=True)

    windows.append(window)

    window.bind("<Escape>", close_all)

    root.after(SPAWN_DELAY, spawn_window)


def close_all(event=None):
    for window in windows:
        if window.winfo_exists():
            window.destroy()

    windows.clear()
    root.destroy()


root.bind_all("<Escape>", close_all)

# Automatically start spawning
root.after(1000, spawn_window)

root.mainloop()