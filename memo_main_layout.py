from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QTableWidget, QListView, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel, QSpinBox)
from memo_app import app
from memo_edit_layout import layout_form
from memo_card_layout import layout_card


app.setStyleSheet("""
    QWidget {
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
        stop:0 #e0e0ff, stop:1 #b0b0ff);
    }
""")


def choose_theme():
    if app.property("theme") == "light":
        app.setStyleSheet("""
            QWidget {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 #2c2c2c, stop:1 #1a1a1a);
                color: white;
            }
            QPushButton {
                background-color: #444;
                color: white;
            }
        """)
        app.setProperty("theme", "dark")
    else:
        app.setStyleSheet("""
            QWidget {
                background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                stop:0 #e0e0ff, stop:1 #b0b0ff);
                color: black;
            }
            QPushButton {
                background-color: #f0f0f0;
                color: black;
            }
        """)
        app.setProperty("theme", "light")


list_questions = QListView()
wdgt_edit = QWidget()
wdgt_edit.setLayout(layout_form)
btn_add = QPushButton('Next question ')
btn_delete = QPushButton('Delete question ')
btn_start = QPushButton('Start')
btn_theme_toggle = QPushButton('White/Dark Theme')
btn_theme_toggle.clicked.connect(choose_theme)

main_col1 = QVBoxLayout()
main_col1.addWidget(list_questions)
main_col1.addWidget(btn_add)

main_col2 = QVBoxLayout()
main_col2.addWidget(wdgt_edit)
main_col2.addWidget(btn_delete)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)
main_line2.addWidget(btn_theme_toggle)

layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)

# Встановлення стандартної теми як світлої
app.setProperty("theme", "light")