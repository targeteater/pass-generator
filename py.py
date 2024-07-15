import tkinter as tk
from tkinter import ttk
import random
import string

def generated_pass():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
    label.config(text=password)

root = tk.Tk()
root.title("Cool Password Generator")
root.geometry("400x200")
root.resizable(True, False)

style = ttk.Style()
style.theme_create("cool_theme", parent="clam", settings={
    "TButton": {
        "configure": {"background": "#4CAF50", "foreground": "white"},
        "map": {"background": [("active", "#45A049")]}
    },
    "TLabel": {
        "configure": {"foreground": "#4CAF50"}
    },
    "TEntry": {
        "configure": {"foreground": "#4CAF50"}
    }
})
style.theme_use("cool_theme")

buttaon = ttk.Button(root, text="epic generator by target")
buttaon.pack(padx=20, pady=10)

label = ttk.Label(root, text="pass")
label.pack(pady=10)

input_label = ttk.Label(root, text="What is this password for?")
input_label.pack(pady=10)

input_entry = ttk.Entry(root)
input_entry.pack(pady=5)

def save_password():
    password = label.cget("text")
    purpose = input_entry.get()
    with open("pass1.txt", "a") as file:
        file.write(f"\n\nPassword: {password}\nPurpose: {purpose}")

save_button = ttk.Button(root, text="Save", command=save_password)
save_button.pack(side="left", padx=10, pady=10)
copy_button = ttk.Button(root, text="Copy", command=lambda: root.clipboard_append(label.cget("text")))
copy_button.pack(side="left", padx=10, pady=10)
button = ttk.Button(root, text="Generate Password", command=generated_pass)
button.pack(side="left", padx=10, pady=10)

root.mainloop()
