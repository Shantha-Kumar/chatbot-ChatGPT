from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QTextEdit
import sys
from backend import ChatBot
import threading


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Davinci")
        self.setMinimumSize(700, 500)

        self.chatbot = ChatBot()

        # Chat Area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Input Field
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter Your Message...")
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message)

        # Send Button
        self.send = QPushButton("Send", self)
        self.send.setGeometry(500, 340, 80, 40)
        self.send.clicked.connect(self.send_message)

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me : {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333 ; background-color: #E9E9E9'> DaVinci : {response}</p>")


app = QApplication(sys.argv)
main_window = ChatBotWindow()
main_window.show()
sys.exit(app.exec())
