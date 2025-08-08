from tkinter import Tk
from main_window import TodoApp
from db import database



if __name__ == "__main__":
    database.init_db()
    root = Tk()
    app = TodoApp(root)
    root.mainloop()