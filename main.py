from PyQt6.QtCore import*
from PyQt6.QtWidgets import *

from app import app
from main_window import window_main

window = QWidget()
window_layout = QVBoxLayout()

window_layout.addWidget (window_main)
window.setLayout(window_layout)
window.show()
app.exec ()
