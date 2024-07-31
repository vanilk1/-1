from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

window_main = QWidget()
window_main_layout = QVBoxLayout()

#виджети вікна
menu_pbtn = QPushButton("Setings")
rest_pbtn = QPushButton("freetime")
give_answer_pbtn  = QPushButton ("відповісти")

rest_sbox = QSpinBox()
rest_sbox.setValue(30)

ans1_rbtn = QRadioButton("1")
ans2_rbtn = QRadioButton("2")
ans3_rbtn = QRadioButton("3")
ans4_rbtn = QRadioButton("4")

question_lbl = QLabel("Qestion")
minuts_lbl = QLabel(" хвилина ")
result_lbl = QLabel("Правильна відпвідь")

answers_gbox = QGroupBox()
result_gbox = QGroupBox()

#ЛОЯУТ ВІКНА
header_layout = QHBoxLayout()

answers_gbox_Layout = QVBoxLayout()
result_gbox_layout = QVBoxLayout()

answer_buttons_row1_layout = QHBoxLayout()
answer_buttons_row2_layout = QHBoxLayout()

header_layout.addWidget(menu_pbtn)
header_layout.addWidget(rest_pbtn)
header_layout.addWidget(rest_sbox)
header_layout.addWidget(minuts_lbl)
window_main_layout.addLayout(header_layout)

window_main_layout.addWidget(question_lbl)

answer_buttons_row1_layout.addWidget(ans1_rbtn)
answer_buttons_row1_layout.addWidget(ans2_rbtn)

answer_buttons_row2_layout.addWidget(ans3_rbtn)
answer_buttons_row2_layout.addWidget(ans4_rbtn)

answers_gbox_Layout.addLayout(answer_buttons_row1_layout)
answers_gbox_Layout.addLayout(answer_buttons_row2_layout)
answers_gbox.setLayout(answers_gbox_Layout)
window_main_layout.addWidget(answers_gbox)

result_gbox_layout.addWidget(result_lbl)
result_gbox.setLayout(result_gbox_layout)
window_main_layout.addWidget(result_gbox)

window_main_layout.addWidget(give_answer_pbtn)

window_main.setLayout(window_main_layout)