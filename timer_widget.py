from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

class PomodoroWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.work_duration = 25 * 60  # Varsayılan çalışma süresi (saniye cinsinden)
        self.break_duration = 5 * 60  # Varsayılan ara süresi (saniye cinsinden)
        self.pomodoro_count = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Başlık etiketi için bir yazı tipi tanımlıyoruz
        title_font = QFont()
        title_font.setPointSize(32)  # Başlık yazı boyutunu 16 olarak ayarlayabilirsiniz

        title_label = QLabel("POMODORO APP")
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)  # Metni ortalamak için
        layout.addWidget(title_label)

        
        # Büyük boyutta bir yazı tipi tanımlıyoruz
        font = QFont()
        font.setPointSize(24)  # Yazı boyutunu 24 olarak ayarlayabilirsiniz

        self.timer_label = QLabel("25:00")
        self.timer_label.setFont(font)  # Tanımladığımız yazı tipini kullanıyoruz
        layout.addWidget(self.timer_label)

        self.start_button = QPushButton("Başla")
        self.start_button.clicked.connect(self.start_pomodoro)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Durdur")
        self.stop_button.clicked.connect(self.stop_pomodoro)
        layout.addWidget(self.stop_button)

        self.resume_button = QPushButton("Devam Et")
        self.resume_button.clicked.connect(self.resume_pomodoro)
        layout.addWidget(self.resume_button)

        self.finish_button = QPushButton("Bitir")
        self.finish_button.clicked.connect(self.finish_pomodoro)
        layout.addWidget(self.finish_button)

        self.work_input = QLineEdit()
        self.work_input.setPlaceholderText("Çalışma Süresi (dakika)")
        layout.addWidget(self.work_input)

        self.break_input = QLineEdit()
        self.break_input.setPlaceholderText("Ara Süresi (dakika)")
        layout.addWidget(self.break_input)

        self.score_label = QLabel("Toplam Pomodoro Sayısı: 0")
        self.score_label.setFont(font)  # Tanımladığımız yazı tipini kullanıyoruz
        layout.addWidget(self.score_label)

        self.setLayout(layout)
        self.update_button_state()

    def update_button_state(self):
        self.start_button.setEnabled(not self.timer.isActive())
        self.stop_button.setEnabled(self.timer.isActive())
        self.resume_button.setEnabled(False)
        self.finish_button.setEnabled(self.timer.isActive())

    def start_pomodoro(self):
        work_minutes = int(self.work_input.text())
        break_minutes = int(self.break_input.text())

        self.work_duration = work_minutes * 60
        self.break_duration = break_minutes * 60
        self.remaining_time = self.work_duration

        self.timer_label.setText(f"Kalan Zaman: {work_minutes:02d}:00 - Ara: {break_minutes:02d}:00")

        self.timer.start(1000)
        self.update_button_state()

    def stop_pomodoro(self):
        self.timer.stop()
        self.update_button_state()
        self.resume_button.setEnabled(True)

    def resume_pomodoro(self):
        self.timer.start(1000)
        self.update_button_state()
        self.resume_button.setEnabled(False)

    def finish_pomodoro(self):
        self.timer.stop()
        self.update_button_state()
        self.resume_button.setEnabled(False)
        self.start_button.setEnabled(True)
        self.finish_button.setEnabled(False)
        self.pomodoro_count += 1
        self.score_label.setText(f"Toplam Pomodoro Sayısı: {self.pomodoro_count}")

    def update_timer(self):
        if self.remaining_time > 0:
            self.remaining_time -= 1
            minutes = self.remaining_time // 60
            seconds = self.remaining_time % 60
            self.timer_label.setText(f"Kalan Zaman: {minutes:02d}:{seconds:02d}")
        else:
            self.timer.stop()
            self.pomodoro_count += 1
            self.score_label.setText(f"Toplam Pomodoro Sayısı: {self.pomodoro_count}")
            self.update_button_state()

    def update_display(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        self.timer_label.setText(f"{minutes:02}:{seconds:02}")
