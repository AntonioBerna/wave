import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np


class Wave:
	def __init__(self, amplitude, angle, frequency):
		self.figure, self.ax = plt.subplots()
		plt.subplots_adjust(left=0.1, bottom=0.30)
		self.ax.grid(True, which="both")
		self.figure.canvas.set_window_title("Wave Signal - by Clever Code")

		self.amplitude = amplitude
		self.max_amplitude = 10.0
		self.angle = angle
		self.max_angle = 360.0
		self.frequency = frequency
		self.min_frequency, self.max_frequency = 0.0, 5.0

		self.__adjust_values()

		self.t = np.arange(-self.max_frequency, self.max_frequency, 0.001)
		self.signal = self.amplitude * np.sin((2 * np.pi * self.frequency * self.t) + self.angle)  # Equazione Del Segnale Generico
		self.y, = plt.plot(self.t, self.signal)  # Plot Segnale

		self.ax.set_ylim(-self.max_amplitude, self.max_amplitude)
		self.ax.set_xlim(-self.max_frequency, self.max_frequency)

		self.ax_amplitude = plt.axes([0.25, 0.20, 0.65, 0.03])
		self.ax_angle = plt.axes([0.25, 0.15, 0.65, 0.03])
		self.ax_frequency = plt.axes([0.25, 0.10, 0.65, 0.03])
		self.ax_reset = plt.axes([0.8, 0.025, 0.1, 0.04])

		self.s_amplitude = Slider(self.ax_amplitude, "Amplitude", -self.max_amplitude, self.max_amplitude, valinit=self.amplitude, valstep=1.0)
		self.s_angle = Slider(self.ax_angle, "Angle", -self.max_angle, self.max_angle, valinit=self.angle, valstep=1.0)
		self.s_frequency = Slider(self.ax_frequency, "Frequency", self.min_frequency, self.max_frequency, valinit=self.frequency, valstep=0.1)
		self.button_reset = Button(self.ax_reset, "Reset")

	def __update(self, val):
		self.y.set_ydata(self.s_amplitude.val * np.sin((2 * np.pi * self.s_frequency.val * self.t) + self.s_angle.val))
		self.figure.canvas.draw_idle()

	def __reset(self, event):
		self.s_amplitude.reset()
		self.s_angle.reset()
		self.s_frequency.reset()

	def __adjust_values(self):
		if self.amplitude > self.max_amplitude:
			self.max_amplitude = self.amplitude
		if self.angle > self.max_angle:
			self.max_angle = self.angle
		if self.frequency > self.max_frequency:
			self.max_frequency = self.frequency

	def update_values(self):
		self.s_amplitude.on_changed(self.__update)
		self.s_angle.on_changed(self.__update)
		self.s_frequency.on_changed(self.__update)
		self.button_reset.on_clicked(self.__reset)
		plt.show()