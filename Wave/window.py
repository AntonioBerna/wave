from tkinter import *
from tkinter.messagebox import showerror
from wave import Wave


class Window:
    def __init__(self, master):
        self.features = {}
        self.signal = 0
        self.amplitude_ = 7.0
        self.angle_ = 0.0
        self.frequency_ = 0.5

        self.master = master
        self.master.title("Wave Signal - by Clever Code")
        self.master.geometry("400x200")
        self.master.resizable(False, False)

        self.frame_up = Frame(self.master)
        self.frame_up.pack()

        self.title = Label(self.frame_up, text="Wave Signal", font="Arial 18 normal")
        self.title.grid(row=0, column=0, columnspan=2, sticky="WE", padx=5, pady=5)

        self.amplitude = Label(self.frame_up, text="Amplitude", font="Arial 14 normal")
        self.amplitude.grid(row=1, column=0, sticky="WE", padx=5, pady=5)
        self.amplitude_value = Entry(self.frame_up, justify="center")
        self.amplitude_value.focus_set()
        self.amplitude_value.insert(0, self.amplitude_)
        self.amplitude_value.grid(row=1, column=1, sticky="WE", padx=5, pady=5)

        self.angle = Label(self.frame_up, text="Angle", font="Arial 14 normal")
        self.angle.grid(row=2, column=0, sticky="WE", padx=5, pady=5)
        self.angle_value = Entry(self.frame_up, justify="center")
        self.angle_value.insert(0, self.angle_)
        self.angle_value.grid(row=2, column=1, sticky="WE", padx=5, pady=5)

        self.frequency = Label(self.frame_up, text="Frequency", font="Arial 14 normal")
        self.frequency.grid(row=3, column=0, sticky="WE", padx=5, pady=5)
        self.frequency_value = Entry(self.frame_up, justify="center")
        self.frequency_value.insert(0, self.frequency_)
        self.frequency_value.grid(row=3, column=1, sticky="WE", padx=5, pady=5)

        self.frame_down = Frame(self.master)
        self.frame_down.pack()

        self.plot_button = Button(self.frame_down, text="Plot Signal Wave", font="Arial 14 normal", command=self.plot)
        self.plot_button.grid(row=0, column=0, sticky="WE", padx=5, pady=5)

        self.clear_button = Button(self.frame_down, text="Clear All", font="Arial 14 normal", command=self.clear)
        self.clear_button.grid(row=0, column=1, sticky="WE", padx=5, pady=5)

    def plot(self):
        if self.amplitude_value.get() != "" and self.angle_value.get() != "" and self.frequency_value.get() != "":
            if float(self.frequency_value.get()) >= 0.0:
                self.features = {
                    "amplitude": float(self.amplitude_value.get()),
                    "angle": float(self.angle_value.get()),
                    "frequency": float(self.frequency_value.get())
                }
                print(f"Ampiezza: {self.features['amplitude']}\nAngolo: {self.features['angle']}\nFrequenza: {self.features['frequency']}")
                self.signal = Wave(self.features['amplitude'], self.features['angle'], self.features['frequency'])
                self.signal.update_values()
            else:
                showerror("Wave Signal - by Clever Code", "Frequency Cannot Be Negative")
        else:
            showerror("Wave Signal - by Clever Code", "Invalid Input")

    def clear(self):
        self.amplitude_value.delete(0, END)
        self.angle_value.delete(0, END)
        self.frequency_value.delete(0, END)