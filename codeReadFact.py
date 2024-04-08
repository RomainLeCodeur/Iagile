import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from openpyxl import *
import factuality 
from PyQt5.QtGui import QDesktopServices
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import re
import fitz

class ChatInterface(QMainWindow):

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
        self.setWindowTitle("ReadFact")
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
        
        # Action Charger Phrases depuis Excel
        load_phrases_action = QAction('Charger Phrases depuis Excel', self)
        load_phrases_action.triggered.connect(self.load_phrases_from_excel)
        file_menu.addAction(load_phrases_action)

        # Action Charger Phrases depuis Excel
        load_phrases_action = QAction('Charger Phrases depuis Pdf', self)
        load_phrases_action.triggered.connect(self.load_text_from_pdf)
        file_menu.addAction(load_phrases_action)
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

    def load_phrases_from_excel(self):
        # Demander à l'utilisateur de sélectionner le fichier Excel
        file_path, _ = QFileDialog.getOpenFileName(self, "Charger Phrases depuis Excel", "", "Fichiers Excel (*.xlsx)")

        if file_path:
            # Demander à l'utilisateur de spécifier les lignes et les colonnes
            rows_input, ok_rows = QInputDialog.getText(self, "Lignes", "Numéros de lignes (séparés par des virgules ou intervalle 'début;fin') : ", QLineEdit.Normal, "")
            columns_input, ok_columns = QInputDialog.getText(self, "Colonnes", "Lettres des colonnes (séparées par des virgules ou intervalle 'début;fin') : ", QLineEdit.Normal, "")
            
            if ok_rows and ok_columns:
                # Traitement des lignes et des colonnes spécifiées par l'utilisateur
                rows = self.process_rows_input(rows_input)
                columns = self.process_columns_input(columns_input)

                # Charger les phrases à partir du fichier Excel avec les lignes et colonnes spécifiées
                phrases = self.load_phrases(file_path, rows=rows, columns=columns)
                for phrase in phrases:
                    self.entry_field.append(phrase)

    def process_columns_input(self, columns_input):
        columns = []

        # Diviser les entrées par virgule
        inputs = columns_input.split(',')

        for item in inputs:
            if ';' in item:
                # Si l'entrée contient un point-virgule, traiter comme un intervalle
                start, end = item.split(';')
                columns.extend(self.get_column_range(start, end))
            else:
                # Sinon, traiter comme une lettre de colonne unique
                columns.append(item.strip())

        return columns

    def get_column_range(self, start, end):
        # Fonction pour générer une plage de lettres de colonne entre start et end inclusivement
        start_index = ord(start.upper()) - 65
        end_index = ord(end.upper()) - 65
        return [chr(i + 65) for i in range(start_index, end_index + 1)]

    def process_rows_input(self, rows_input):
        rows = []
        # Diviser les entrées par virgule
        inputs = rows_input.split(',')

        for item in inputs:
            if ';' in item:
                # Si l'entrée contient un point-virgule, traiter comme un intervalle
                start, end = item.split(';')
                rows.extend(range(int(start), int(end) + 1))
            else:
                # Sinon, traiter comme un numéro de ligne unique
                rows.append(int(item))
        return rows                

    def load_text_from_pdf(self):
        # Demander à l'utilisateur de sélectionner le fichier PDF
        file_path, _ = QFileDialog.getOpenFileName(self, "Charger Texte depuis PDF", "", "Fichiers PDF (*.pdf)")

        if file_path:
            try:
                # Ouvrir le fichier PDF
                document = fitz.open(file_path)

                # Parcourir chaque page du PDF et extraire le texte
                text = ""
                for page in document:
                    text += page.get_text()

                # Ajouter le texte à la zone de saisie des messages
                self.entry_field.append(text)

                # Fermer le document PDF
                document.close()
            except Exception as e:
                # Gérer les erreurs lors de l'ouverture ou de l'extraction du texte du fichier PDF
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la lecture du fichier PDF : {e}")
    def load_phrases(self, file_path, rows=None, columns=None):
        phrases = []

        # Lire le fichier Excel et extraire les phrases
        try:
            workbook = load_workbook(file_path, read_only=True)
            sheet = workbook.active

            if rows and columns:
                # Si des lignes et des colonnes sont spécifiées, ajoutez uniquement les cellules correspondantes
                for row in rows:
                    for column in columns:
                        cell_value = sheet[f"{column}{row}"].value
                        if cell_value:
                            phrases.append(str(cell_value))
            elif rows:
                # Si seulement des lignes sont spécifiées, ajoutez toutes les cellules de ces lignes
                for row in rows:
                    for cell in sheet[row]:
                        if cell.value:
                            phrases.append(str(cell.value))
            elif columns:
                # Si seulement des colonnes sont spécifiées, ajoutez toutes les cellules de ces colonnes
                for column in columns:
                    for cell in sheet[column]:
                        if cell.value:
                            phrases.append(str(cell.value))
            else:
                # Par défaut, ajoutez toutes les cellules non vides de la feuille de calcul
                for row in sheet.iter_rows(values_only=True):
                    for cell_value in row:
                        if cell_value:
                            phrases.append(str(cell_value))

            workbook.close()
        except Exception as e:
            # Gérer les erreurs de lecture du fichier Excel
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la lecture du fichier Excel : {e}")

        return phrases

    def save_history(self):
        # Demander à l'utilisateur de spécifier le nom et le chemin du fichier Excel
        file_path, _ = QFileDialog.getSaveFileName(self, "Enregistrer Historique", "", "Fichiers Excel (*.xlsx)")

        if file_path:
            # Créer un nouveau classeur Excel
            wb = Workbook()
            ws = wb.active

            # Ajouter des en-têtes
            ws['A1'] = 'Phrase'
            ws['B1'] = 'Choix du modèle'
            ws['C1'] = 'Score'

            # Ajouter l'historique dans la feuille de calcul
            messages = self.message_display.toPlainText().split('\n')
            row_index = 2  # Commencer à la ligne suivante après l'en-tête
            for message in messages:
                # Récupérer la phrase, le choix du modèle et le score de chaque message
                phrase, model_choice, score = self.parse_message(message)

                # Écrire les données dans le classeur Excel
                ws.cell(row=row_index, column=1, value=phrase)
                ws.cell(row=row_index, column=2, value=model_choice)
                ws.cell(row=row_index, column=3, value=score)
                row_index += 1

            # Enregistrer le classeur Excel
            wb.save(file_path)

            # Ouvrir le fichier Excel avec l'application par défaut
            QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

    def parse_message(self, message):
        # Séparer le message en phrase, choix du modèle et score
        parts = message.split(': ')
        phrase = parts[0]
        if len(parts) > 1:
            model_choice, score = parts[1].split(' - ')
            return phrase, model_choice, score
        else:
            return phrase, '', ''
        
    def send_message(self):
        # Envoyer le message et afficher la réponse dans la console
        message = self.entry_field.toPlainText()
        self.display_message(message)

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
            response = factuality.scoreFact(message)
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