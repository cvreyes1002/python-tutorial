import tkinter as tk

def button_clicked(name):
    print(f"Clicked: {name}")

root = tk.Tk()

# Pass a string ID using lambda
tk.Button(root, text="Button A", command=lambda: button_clicked("A")).pack()
tk.Button(root, text="Button B", command=lambda: button_clicked("B")).pack()

root.mainloop()