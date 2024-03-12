import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QCheckBox, QLabel, QHBoxLayout, QGridLayout, QPushButton, QMenu, QAction, QComboBox, QFileDialog
from PyQt5.QtCore import QUrl
from factuality import Factuality
from PyQt5.QtGui import QDesktopServices
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ChatInterface(QMainWindow):
    # Votre code précédent ici...

    def open_pdf_guide(self):
        # Chemin relatif du fichier PDF
        file_path = "Guide_ReadFact.pdf"

        # Récupérer le chemin absolu du fichier PDF
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, file_path)

        # Ouvrir le fichier PDF avec l'application par défaut
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))


import requests

# Thème Clair
BACKGROUND_COLOR = "#FFFFFF"
TEXT_COLOR = "#000000"
BUTTON_COLOR = "#4CAF50"
BUTTON_HOVER_COLOR = "#45a049"
BUTTON_TEXT_COLOR = "#FFFFFF"
CHECKBOX_COLOR = "#4CAF50"

API_URL = "https://api-inference.huggingface.co/models/valurank/en_readability"
headers = {"Authorization": "Bearer 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"}

class LanguageInterface:
    def __init__(self, chat_interface):
        self.chat_interface = chat_interface
        self.language_options = {"English", "French", "Spanish", "German", "Italian"}  # Exemple de langues disponibles
        self.language_combobox = QComboBox()
        self.language_combobox.addItems(self.language_options)
        self.language_combobox.currentTextChanged.connect(self.change_language)

    def change_language(self, language):
        print(f"Changer la langue en: {language}")
        # Mettre en place la logique pour changer la langue de l'interface utilisateur
        if language == "English":
            self.translate_to_english()
        elif language == "French":
            self.translate_to_french()
        elif language == "Spanish":
            self.translate_to_spanish()
        elif language == "German":
            self.translate_to_german()
        elif language == "Italian":
            self.translate_to_italian()

    def translate_to_english(self):
        # Traduire les textes en anglais
        self.chat_interface.label_phrase.setText("Your sentence")
        self.chat_interface.label_history.setText("History")
        self.chat_interface.send_button.setText("Send")
        self.chat_interface.quit_button.setText("Quit")
        self.chat_interface.function1_checkbox.setText("Function 1")
        self.chat_interface.function2_checkbox.setText("Function 2")

    def translate_to_french(self):
        # Traduire les textes en français
        self.chat_interface.label_phrase.setText("Votre phrase")
        self.chat_interface.label_history.setText("Historique")
        self.chat_interface.send_button.setText("Envoyer")
        self.chat_interface.quit_button.setText("Quitter")
        self.chat_interface.function1_checkbox.setText("Fonction 1")
        self.chat_interface.function2_checkbox.setText("Fonction 2")

    def translate_to_spanish(self):
        # Traduire les textes en espagnol
        self.chat_interface.label_phrase.setText("Tu frase")
        self.chat_interface.label_history.setText("Historial")
        self.chat_interface.send_button.setText("Enviar")
        self.chat_interface.quit_button.setText("Salir")
        self.chat_interface.function1_checkbox.setText("Función 1")
        self.chat_interface.function2_checkbox.setText("Función 2")

    def translate_to_german(self):
        # Traduire les textes en allemand
        self.chat_interface.label_phrase.setText("Ihr Satz")
        self.chat_interface.label_history.setText("Geschichte")
        self.chat_interface.send_button.setText("Senden")
        self.chat_interface.quit_button.setText("Beenden")
        self.chat_interface.function1_checkbox.setText("Funktion 1")
        self.chat_interface.function2_checkbox.setText("Funktion 2")

    def translate_to_italian(self):
        # Traduire les textes en italien
        self.chat_interface.label_phrase.setText("La tua frase")
        self.chat_interface.label_history.setText("Storia")
        self.chat_interface.send_button.setText("Inviare")
        self.chat_interface.quit_button.setText("Uscita")
        self.chat_interface.function1_checkbox.setText("Funzione 1")
        self.chat_interface.function2_checkbox.setText("Funzione 2")

class ChatInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatBot")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.setStyleSheet(f"background-color: {BACKGROUND_COLOR}; color: {TEXT_COLOR};")

        layout = QGridLayout()
        
        # Zone de saisie des messages
        self.entry_field = QTextEdit()
        self.label_phrase = QLabel("Votre phrase")
        layout.addWidget(self.label_phrase, 0, 0)
        layout.addWidget(self.entry_field, 1, 0)

        # Cases à cocher pour les fonctions
        self.function1_checkbox = QCheckBox("Factuality")
        self.function1_checkbox.setStyleSheet(f"QCheckBox {{ color: {TEXT_COLOR}; }}")  # Appliquer uniquement la couleur du texte
        self.function2_checkbox = QCheckBox("Readability")
        self.function2_checkbox.setStyleSheet(f"QCheckBox {{ color: {TEXT_COLOR}; }}")  # Appliquer uniquement la couleur du texte

        self.checkbox_layout = QVBoxLayout()
        self.checkbox_layout.addWidget(self.function1_checkbox)
        self.checkbox_layout.addWidget(self.function2_checkbox)
        self.checkbox_layout.setSpacing(0)  # Définir l'espacement entre les cases à cocher à 0

        layout.addLayout(self.checkbox_layout, 1, 1)

        # Console de sortie
        self.message_display = QTextEdit()
        self.message_display.setReadOnly(True)
        self.label_history = QLabel("Historique")
        layout.addWidget(self.label_history, 0, 2)
        layout.addWidget(self.message_display, 1, 2)

        # Boutons Send et Quit
        button_layout = QHBoxLayout()
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setStyleSheet(f"background-color: {BUTTON_COLOR}; color: {BUTTON_TEXT_COLOR};")
        button_layout.addWidget(self.send_button)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)
        self.quit_button.setStyleSheet(f"background-color: {BUTTON_COLOR}; color: {BUTTON_TEXT_COLOR};")
        button_layout.addWidget(self.quit_button)
        
        layout.addLayout(button_layout, 2, 0)

        self.central_widget.setLayout(layout)

        # Création de la barre de menus
        self.create_menu()

        # Initialiser l'interface de langue
        self.language_interface = LanguageInterface(self)

    def create_menu(self):
        # Création de la barre de menus
        menubar = self.menuBar()

        # Menu Fichier
        file_menu = menubar.addMenu('Fichier')

        # Action Enregistrer Historique
        save_history_action = QAction('Enregistrer Historique', self)
        save_history_action.triggered.connect(self.save_history)
        file_menu.addAction(save_history_action)

        # Menu Langue
        self.menu_language = menubar.addMenu('Langue')
        self.language_options = {"English", "French", "Spanish", "German", "Italian"}  # Langues disponibles
        for language in self.language_options:
            language_action = QAction(language, self)
            language_action.triggered.connect(lambda _, lang=language: self.language_interface.change_language(lang))
            self.menu_language.addAction(language_action)

        # Menu Aide
        help_menu = menubar.addMenu('Aide')

        # Action Aide PDF
        help_pdf_action = QAction('Guide d\'utilisation (PDF)', self)
        help_pdf_action.triggered.connect(self.open_pdf_guide)
        help_menu.addAction(help_pdf_action)
    
    def save_history(self):
        # Demander à l'utilisateur de spécifier le nom et le chemin du fichier PDF
        file_path, _ = QFileDialog.getSaveFileName(self, "Enregistrer Historique", "", "Fichiers PDF (*.pdf)")

        if file_path:
            # Enregistrer l'historique dans un fichier PDF
            with open(file_path, "wb") as f:
                c = canvas.Canvas(f, pagesize=letter)
                #c.drawString(100, 750, "Historique du ChatBot:")
                text = self.message_display.toPlainText()
                y = 730
                for line in text.split('\n'):
                    y -= 15
                    c.drawString(100, y, line)
                c.showPage()
                c.save()

            # Ouvrir le fichier PDF avec l'application par défaut
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))
    def send_message(self):
        # Envoyer le message et afficher la réponse dans la console
        message = self.entry_field.toPlainText()
        self.display_message(message)
        
        # Calcul de la factualité du texte
        factuality_calculator = Factuality(message)
        factuality_result = factuality_calculator.calcul()

        selected_function = None
        if self.function1_checkbox.isChecked():
            self.display_message("Factuality")
            selected_function = 1
        elif self.function2_checkbox.isChecked():
            self.display_message("Function 2 checked")
            selected_function = 2
        else:
            self.display_message("No function selected")

        if selected_function == 1:
            response = factuality_calculator.toString()
        elif selected_function == 2:
            response = function2(message)
        else:
            response = "No function selected"

        self.display_message(response)
        self.entry_field.clear()

    def display_message(self, message):
        # Afficher un message dans la console de sortie
        self.message_display.append(message)

    def open_pdf_guide(self):
        # Chemin relatif du fichier PDF
        file_path = "Guide_ReadFact.pdf"

        # Lancer l'application par défaut pour ouvrir le fichier PDF
        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

def main():
    # Lancer l'application
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Utiliser le style Fusion pour une apparence plus moderne
    chat_interface = ChatInterface()
    chat_interface.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()