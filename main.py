import sys
from PyQt5.QtWidgets import QApplication
from timer_widget import PomodoroWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Pomodoro APP")  # Pencere başlığını ayarlar

    pomodoro_widget = PomodoroWidget()
    pomodoro_widget.show()
    sys.exit(app.exec_())