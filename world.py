try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    import Tkinter as tk
    from Tkinter import ttk


class World:

    def __init__(self):
        self.parent = tk.Tk()
        self.parent['padx'] = 5
        self.parent['pady'] = 5
        self.parent.title("Q-Learning")
        self.barriers = [tk.IntVar() for i in range(64)]
        self.failing = [tk.IntVar() for i in range(64)]

        ## Gridworld LabelFrame
        self.world_frame = ttk.LabelFrame(master=self.parent, text="Gridworld")
        self.world_frame.grid(row=0, column=0, rowspan=100, sticky=tk.E + tk.N + tk.W, ipadx=5)

        # Tk Canvas for our little robot :)
        self.world = tk.Canvas(master=self.world_frame, width=480, height=480)
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

        # Setting up walls (pop-up window)
        self.barrier_button = ttk.Button(master=self.environment_frame, text="Open Barrier Editor",
                                         command=self.barrier_edit)
        self.barrier_button.grid(row=0, column=1, sticky=tk.E + tk.W)

        # Setting up walls (label)
        self.barrier_label = ttk.Label(master=self.environment_frame, text="Set Barriers:")
        self.barrier_label.grid(row=0, column=0, sticky=tk.E)

        # Setting up failing points (pop-up window)
        self.failing_button = ttk.Button(master=self.environment_frame, text="Open Negative Reward Editor",
                                         command=self.failing_edit)
        self.failing_button.grid(row=1, column=1)

        # Setting up failing points (label)
        self.failing_label = ttk.Label(master=self.environment_frame, text="Set Negative Rewards:")
        self.failing_label.grid(row=1, column=0, sticky=tk.E)

        # Setting up succeeding points (pop-up window)
        self.good_button = ttk.Button(master=self.environment_frame, text="Open Positive Reward Editor",
                                       command=self.succeeding_edit)
        self.good_button.grid(row=2, column=1, sticky=tk.E + tk.W)

        # Setting up succeeding points (label)
        self.good_label = ttk.Label(master=self.environment_frame, text="Set Positive Rewards:")
        self.good_label.grid(row=2, column=0, sticky=tk.E)

        ## Simulation Settings LabelFrame
        self.simulation_frame = ttk.LabelFrame(master=self.parent, text="Simulation Settings")
        self.simulation_frame.grid(row=2, column=1, sticky=tk.S + tk.W + tk.E, padx=5, ipady=5)

    def barrier_edit(self):
        temp = [0 for i in range(64)]
        test = tk.Toplevel(self.parent)

        barrier_frame = ttk.LabelFrame(master=test, text="Barrier Editor")
        barrier_frame.pack(padx=5, pady=5)

        for i in range(64):
            temp[i] = ttk.Checkbutton(master=barrier_frame, variable=self.barriers[i])
            temp[i].grid(row=1 + (i % 8), column=1 + (i // 8))

    def failing_edit(self):
        for i in self.barriers:
            print(i.get())

    def succeeding_edit(self):
        pass

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






