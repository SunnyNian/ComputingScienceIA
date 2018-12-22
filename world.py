import tkinter as tk
from tkinter import ttk


class World:

    def __init__(self):
        self.parent = tk.Tk()
        self.parent['padx'] = 5
        self.parent['pady'] = 5
        self.parent.title("Q-Learning")

        ## Gridworld LabelFrame
        self.world_frame = ttk.LabelFrame(master=self.parent, text="Gridworld")
        self.world_frame.grid(row=0, column=0, rowspan=100, sticky=tk.E + tk.N + tk.W, ipadx=5)

        # Tk Canvas for our little robot :)
        self.world = tk.Canvas(master=self.world_frame, width=420, height=420)
        self.world.pack(padx=5, pady=5)

        ## Variable LabelFrame
        self.variable_frame = ttk.LabelFrame(master=self.parent, text="Q-Learning Variables")
        self.variable_frame.grid(row=0, column=1, padx=5, sticky=tk.E + tk.N + tk.W)

        # Learning Rate (alpha)
        self.alpha_label = ttk.Label(master=self.variable_frame, text="Learning Rate (α):")
        self.alpha_label.grid(row=0, column=0, sticky=tk.E)

        self.alpha_scale = tk.Scale(master=self.variable_frame, width=6, from_=0, to=1, length=160, tickinterval=1,
                                    resolution=0.01, orient=tk.HORIZONTAL, command=self.update_alpha)
        self.alpha_scale.grid(row=0, column=1)

        self.alpha_box = ttk.Entry(master=self.variable_frame, width=6)
        self.alpha_box.grid(row=0, column=2)

        self.alpha_button = ttk.Button(master=self.variable_frame, width=5, text="Set α", command=self.set_alpha)
        self.alpha_button.grid(row=0, column=3)

        # Discount Factor (gamma)
        self.gamma_label = ttk.Label(master=self.variable_frame, text="Discount Factor (γ):")
        self.gamma_label.grid(row=1, column=0, sticky=tk.E)

        self.gamma_scale = tk.Scale(master=self.variable_frame, width=6, from_=0, to=1, length=160, tickinterval=1,
                                    resolution=0.01, orient=tk.HORIZONTAL, command=self.update_gamma)
        self.gamma_scale.grid(row=1, column=1)

        self.gamma_box = ttk.Entry(master=self.variable_frame, width=6)
        self.gamma_box.grid(row=1, column=2)

        self.gamma_button = ttk.Button(master=self.variable_frame, width=5, text="Set γ", command=self.set_gamma)
        self.gamma_button.grid(row=1, column=3)

        ## Environment LabelFrame
        self.environment_frame = ttk.LabelFrame(master=self.parent, text="Environment")
        self.environment_frame.grid(row=1, column=1, sticky=tk.N + tk.E + tk.W, padx=5, ipady=5)

        # test
        self.environment_box = ttk.Combobox(master=self.environment_frame)
        self.environment_box.grid(row=0, column=0, padx=5)

        ## Simulation Settings LabelFrame
        self.simulation_frame = ttk.LabelFrame(master=self.parent, text="Simulation Settings")
        self.simulation_frame.grid(row=2, column=1, sticky=tk.S + tk.W + tk.E, padx=5, ipady=5, ipadx=5)

        #test
        self.barrier_label = ttk.Label(master=self.simulation_frame, text="Set Barriers")
        self.simulation_box.grid(row=0, column=0, padx=5)

    def update_gamma(self, gamma):
        self.gamma_box.delete(0, "end")
        self.gamma_box.insert(0, gamma)

    def set_gamma(self):
        try:
            gamma = float(self.gamma_box.get())
            if gamma >= 1.00:
                self.gamma_scale.set(1.00)
                self.gamma_box.delete(0, "end")
                self.gamma_box.insert(0, 1.00)
            elif gamma <= 0.00:
                self.gamma_scale.set(0.00)
                self.gamma_box.delete(0, "end")
                self.gamma_box.insert(0, 0.00)
            else:
                self.gamma_box.delete(0, "end")
                self.gamma_box.insert(0, gamma)
                self.gamma_scale.set(gamma)

        except ValueError:
            self.gamma_box.delete(0, "end")
            self.gamma_box.insert(0, 0.00)

    def update_alpha(self, alpha):
        self.alpha_box.delete(0, "end")
        self.alpha_box.insert(0, alpha)

    def set_alpha(self):
        try:
            alpha = float(self.alpha_box.get())
            if alpha >= 1.00:
                self.alpha_scale.set(1.00)
                self.alpha_box.delete(0, "end")
                self.alpha_box.insert(0, 1.00)
            elif alpha <= 0.00:
                self.alpha_scale.set(0.00)
                self.alpha_box.delete(0, "end")
                self.alpha_box.insert(0, 0.00)
            else:
                self.alpha_box.delete(0, "end")
                self.alpha_box.insert(0, alpha)
                self.alpha_scale.set(alpha)

        except ValueError:
            self.alpha_box.delete(0, "end")
            self.alpha_box.insert(0, 0.00)

    def console_error(self):
        pass


a = World()

tk.mainloop()






