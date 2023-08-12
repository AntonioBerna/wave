from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QDesktopWidget, QSplashScreen
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtGui import QPixmap
import numpy as np
import time
import sys

class SplashScreen(QSplashScreen):
    WIDTH = 700

    def __init__(self):
        img_path = "imgs/app/splash.jpg"
        super().__init__(QPixmap(img_path).scaledToWidth(self.WIDTH))
        self.setMask(self.pixmap().mask())

class PlotApp(QMainWindow):
    WIDTH = HEIGHT = 700

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plot App")
        self.setGeometry(0, 0, self.WIDTH, self.HEIGHT)
        self.center_on_screen()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.amplitude_label = QLabel("Amplitude:")
        self.amplitude_input = QLineEdit()
        self.amplitude_input.setText("1.0")
        self.layout.addWidget(self.amplitude_label)
        self.layout.addWidget(self.amplitude_input)

        self.frequency_label = QLabel("Frequency:")
        self.frequency_input = QLineEdit()
        self.frequency_input.setText("1.0")
        self.layout.addWidget(self.frequency_label)
        self.layout.addWidget(self.frequency_input)

        self.phase_label = QLabel("Phase:")
        self.phase_input = QLineEdit()
        self.phase_input.setText("0.0")
        self.layout.addWidget(self.phase_label)
        self.layout.addWidget(self.phase_input)

        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot)
        self.layout.addWidget(self.plot_button)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
    
    def center_on_screen(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def plot(self):
        amplitude_text = self.amplitude_input.text()
        frequency_text = self.frequency_input.text()
        phase_text = self.phase_input.text()

        if not amplitude_text or not frequency_text or not phase_text:
            self.show_popup("Error", "All fields must be filled in.")
            return

        try:
            amplitude = float(amplitude_text)
            frequency = float(frequency_text)
            phase = float(phase_text)
        except ValueError:
            self.show_popup("Error", "Enter valid numerical values.")
            return

        x = np.linspace(0, 2 * np.pi, 1000)
        y = amplitude * np.sin(frequency * x + phase)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("Time")
        ax.set_ylabel("Amplitude")
        ax.set_title("Sinusoidal Signal")
        self.canvas.draw()

    def show_popup(self, title, message):
        popup = QMessageBox(self)
        popup.setWindowTitle(title)
        popup.setText(message)
        popup.setIcon(QMessageBox.Warning)
        popup.exec_()

def main():
    app = QApplication(sys.argv)

    splash = SplashScreen()
    splash.show()

    app.processEvents()
    time.sleep(1.5)
    app.processEvents()
    
    window = PlotApp()
    window.show()
    splash.finish(window)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
