import tkinter as tk
from tkinter import messagebox as mb

header_font = ("Arial", 18)
default_font = ("Arial", 16)

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(self.root, text="Your Message", font=(header_font))
        self.label.pack(padx=10, pady=10)
        self.textbox = tk.Text(self.root, height=5, font=(default_font) )
        self.textbox.pack(padx=10, pady=10)
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Message Box", font=(default_font), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        self.button = tk.Button(self.root, text="Click me", command=self.show_message)
        self.button.pack(padx=10, pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def show_message(self):
        check = self.check_state.get()
        message = self.textbox.get("1.0", tk.END)
        if check == 0:
            print(message)
        else:
          mb.showinfo("Message", message)

    def on_closing(self):
        if mb.askyesno("Quit", "Do you want to quit?"):
            self.root.destroy()
        
        

MyGUI()

