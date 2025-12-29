import tkinter as tk
from datetime import datetime

def log_key(event):
    key = event.keysym
    time = datetime.now().strftime("%H:%M:%S")
    log_entry = f"{time} - {key}\n"

    text_area.insert(tk.END, log_entry)

    with open("keystroke_log.txt", "a") as file:
        file.write(log_entry)

# Create main window
root = tk.Tk()
root.title("Keystroke Logging Demonstration")
root.geometry("500x400")

label = tk.Label(root, text="Type inside this window (Demo Only)", font=("Arial", 12))
label.pack(pady=10)

text_area = tk.Text(root, height=15, width=55)
text_area.pack(pady=10)

info = tk.Label(
    root,
    text="Note: Keystrokes are recorded only within this window\nwith user consent.",
    fg="red"
)
info.pack()

# Bind keypress event
root.bind("<KeyPress>", log_key)

root.mainloop()
