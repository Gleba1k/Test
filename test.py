from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QGroupBox, QPushButton, QRadioButton, QMessageBox)

program = QApplication([])

window =QWidget()
window.resize(600, 500)
window.setStyleSheet("background-color: rgb(77, 85, 197)")

text = QLabel("Хто такий сігма?")

button_next_question = QPushButton("Далі")

box_for_buttons = QGroupBox("Варіанти Відповідей")

radio_button1 = QRadioButton("Степан")
radio_button2 = QRadioButton("Глеб")
radio_button3 = QRadioButton("Вадим")
radio_button4 = QRadioButton("Оля")

button_next_question = QPushButton("Наступне питання")

vertical_line_button_1 = QVBoxLayout()
vertical_line_button_1.addWidget(radio_button1)
vertical_line_button_1.addWidget(radio_button2)

vertical_line_button_2 = QVBoxLayout()
vertical_line_button_2.addWidget(radio_button3)
vertical_line_button_2.addWidget(radio_button4)

horizontal_button_line = QHBoxLayout()
horizontal_button_line.addLayout(vertical_line_button_1)
horizontal_button_line.addLayout(vertical_line_button_2)

horizontal_button_line1 = QVBoxLayout()
horizontal_button_line.addLayout(vertical_line_button_1)


box_for_buttons.setLayout(horizontal_button_line)

vertical_line = QVBoxLayout()
vertical_line.addWidget(text, alignment=Qt.AlignCenter)
vertical_line.addWidget(box_for_buttons)
vertical_line.addWidget(button_next_question)



window.setLayout(vertical_line)




questions_and_answers = [
    {"question": "1/8 .Сама вилика скеля землі",
    "answer": ["Абоба", "Алімп","Еверест", "Говерла"],
    "correct": 2
    },

    {"question": "2/8 .Сама висока скеля України",
    "answer": ["Логіка","Говерла","еверест", "Алімп" ],
    "correct": 1
    },
    {"question": "3/8 .Який звір найсамий безпечний?",
    "answer": ["МКоролівська кобра","Медведь Гризлі","Панда", "Собака" ],
    "correct": 2
    },
    {"question": "4/8 .Коли люди почали думать що собака найкращій друг чоловіка?",
    "answer": ["2024","1821","1999", "1790" ],
    "correct": 1
    },
    {"question": "5/8 .Найбезпечніщі країни, хто з них є Безпечною країною на віки",
    "answer": ["Ісландія","Данія","Ірландія", "Нова Зеландія" ],
    "correct": 0
    },
    {"question": "6/8 .Найсучасніша Країна це?",
    "answer": ["Південна Корея ","США","Швейцарія ", "Японія" ],
    "correct": 0
    },
    {"question": "7/8 .Саме виличезне дерево у світі? його прозвище Генерал Шерман ",
    "answer": ["Гіперіон","Баобаб","Геліос", "Дерево" ],
    "correct": 0
    },
    {"question": "8/8 .звідки вода появилась у сахарі? у 2025 році",
    "answer": ["Далина смерті","сахара","Маріанська западина", "Україна" ],
    "correct": 0
    },
    
]
current_question = 0 
correct_answer = 0
answer_checked = False

def load_questions(index):
    global current_question, answer_checked
    answer_checked = False
    current_question = index
    question = questions_and_answers[index]
    text.setText(question["question"])
    radio_button1.setText(question["answer"][0])
    radio_button2.setText(question["answer"][1])
    radio_button3.setText(question["answer"][2])
    radio_button4.setText(question["answer"][3])

def go_to_the_next_question():
    global current_question
    if current_question < len(questions_and_answers) - 1:
        load_questions(current_question + 1)
    else:
        show_result_of_test()


def show_result(is_correct):
    global correct_answer
    final_msg = QMessageBox()
    final_msg.setStyleSheet("background-color: rgb(77, 133, 212)")
    if is_correct:
        final_msg.setText("Правильно!\nВірна відповідь")
        correct_answer += 1
    else:
        final_msg.setText("Невірно!\nНа жаль це не правильна відповідь")    
    final_msg.exec()

def check_answer(index):
    global answer_checked
    if not answer_checked:
        correct_answers = questions_and_answers[current_question]["correct"]
        show_result(index == correct_answers)
        answer_checked = True

def on_button_clicked():
    if radio_button1.isChecked():
        check_answer(0)
    elif radio_button2.isChecked():
        check_answer(1)
    elif radio_button3.isChecked():
        check_answer(2)
    elif radio_button4.isChecked():
        check_answer(3)



def show_result_of_test():
    end = QMessageBox()
    all_questions = len(questions_and_answers)
    end.setText(f"Ви відповіли правильно на {correct_answer} з {all_questions} питань.")
    end.exec()
    program.quit()




load_questions(current_question)

button_next_question.clicked.connect(go_to_the_next_question)


radio_button1.clicked.connect(on_button_clicked)
radio_button2.clicked.connect(on_button_clicked)
radio_button3.clicked.connect(on_button_clicked)
radio_button4.clicked.connect(on_button_clicked)





window.show()
program.exec()
