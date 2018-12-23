import tkinter as tk
from tkinter import ttk

parent = tk.Tk()
barriers = [0 for i in range(49)]

temp = [0 for i in range(49)]

test_a = ttk.Label(master=parent, text="States in Environment")
test_a.grid(row=0, column=0)

for i in range(49):
    temp[i] = tk.Checkbutton(master=parent, variable=barriers[i])
    temp[i].grid(row=i % 7, column=i // 7)

tk.mainloop()