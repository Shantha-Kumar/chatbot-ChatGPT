from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QTextEdit
import sys
from backend import ChatBot


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goku")
        self.setMinimumSize(700, 500)

        # Chat Area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Input Field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        # Send Button
        self.send = QPushButton("Send", self)
        self.send.setGeometry(500, 340, 80, 40)


chatbot = ChatBot()

app = QApplication(sys.argv)
main_window = ChatBotWindow()
main_window.show()
sys.exit(app.exec())
