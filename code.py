import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QCheckBox, QLabel, QHBoxLayout, QGridLayout

import requests

API_URL = "https://api-inference.huggingface.co/models/valurank/en_readability"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

def function(phrase):
    output = query({"inputs": phrase})
    for i in range(1):  # Utilisez plutôt len(output) si vous voulez parcourir tous les éléments
        label = output[0][i]['label']
        score = output[0][i]['score']
        # Affiche le résultat dans l'interface utilisateur
    return str(score)

def function2(phrase):
    # Implémentez la logique de votre deuxième fonction ici
    return "Résultat de la fonction 2"

class ChatInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QGridLayout()
        
        self.entry_field = QTextEdit()
        layout.addWidget(QLabel("Votre phrase"), 0, 0)
        layout.addWidget(self.entry_field, 0, 0)

        self.function1_checkbox = QCheckBox("Function 1")
        self.function2_checkbox = QCheckBox("Function 2")

        self.checkbox_layout = QVBoxLayout()
        self.checkbox_layout.addWidget(self.function1_checkbox)
        self.checkbox_layout.addWidget(self.function2_checkbox)
        self.checkbox_layout.setSpacing(0)  # Définir l'espacement à 0

        layout.addLayout(self.checkbox_layout, 0, 1)

        self.message_display = QTextEdit()
        self.message_display.setReadOnly(True)
        layout.addWidget(QLabel("Historique"), 0, 2)
        layout.addWidget(self.message_display, 0, 2)

        button_layout = QHBoxLayout()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        button_layout.addWidget(self.send_button)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)
        button_layout.addWidget(self.quit_button)
        
        layout.addLayout(button_layout, 1, 0)

        self.central_widget.setLayout(layout)

    def send_message(self):
        message = self.entry_field.toPlainText()
        self.display_message("Votre phrase: " + message)
        
        selected_function = None
        if self.function1_checkbox.isChecked():
            selected_function = 1
        elif self.function2_checkbox.isChecked():
            selected_function = 2

        if selected_function == 1:
            response = function(message)
        elif selected_function == 2:
            response = function2(message)
        else:
            response = "Aucune fonction sélectionnée"

        self.display_message("ChatBot: " + response)
        self.entry_field.clear()

    def display_message(self, message):
        self.message_display.append(message)

def main():
    app = QApplication(sys.argv)
    chat_interface = ChatInterface()
    chat_interface.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
