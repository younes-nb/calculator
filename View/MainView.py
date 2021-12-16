from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QTextEdit, \
    QPushButton, QLayout
from PyQt6.QtGui import QIcon, QCursor, QRegularExpressionValidator
from PyQt6 import QtCore
from PyQt6.QtCore import Qt, QRegularExpression


class MainView(QWidget):

    def __init__(self):
        super().__init__()

        self.geometry = self.setGeometry(100, 100, 500, 450)
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("./icons/icon.png"))
        self.setStyleSheet(""" 
            background-color: #323232; 
            font-size: 15px;   
        """)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.mainInput = QLineEdit()
        self.mainInput.setText("0")

        pattern = "[0-9]+"
        reg = QRegularExpression(pattern)
        reg_validator = QRegularExpressionValidator(reg)
        self.mainInput.setValidator(reg_validator)

        self.mainInput.setStyleSheet(""" 
            color: lightgray; 
            padding: 25px 25px 10px 25px; 
            border-bottom: 1px solid #F29C1F;  
            border-radius: 5px;   
            margin-bottom:20px; 
            font-size:25px; 
        """)

        self.layout.addWidget(self.mainInput)

        self.col_2 = QGridLayout()
        self.buttons = {'sin(x)': (0, 0),
                        'MS': (0, 1),
                        'MR': (0, 2),
                        'MC': (0, 3),
                        'CE': (0, 4),
                        '\u232b': (0, 5),
                        'cos(x)': (1, 0),
                        '\u222b': (1, 1),
                        '(': (1, 2),
                        '.': (1, 3),
                        ')': (1, 4),
                        '%': (1, 5),
                        'tan(x)': (2, 0),
                        'x!': (2, 1),
                        '7': (2, 2),
                        '8': (2, 3),
                        '9': (2, 4),
                        '\u00f7': (2, 5),
                        'cot(x)': (3, 0),
                        'x\u02b8': (3, 1),
                        '4': (3, 2),
                        '5': (3, 3),
                        '6': (3, 4),
                        '\u00d7': (3, 5),
                        '\u03c0': (4, 0),
                        'log\u2082(x)': (4, 1),
                        '1': (4, 2),
                        '2': (4, 3),
                        '3': (4, 4),
                        '\u2212': (4, 5),
                        'e': (5, 0),
                        'log\u2081\u2080(x)': (5, 1),
                        '0': (5, 2),
                        '=': (5, 4),
                        '+': (5, 5)
                        }
        for btnText, btnPos in self.buttons.items():
            self.buttons[btnText] = QPushButton(btnText)
            self.buttons[btnText].setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            if btnText == '=':
                self.buttons[btnText].setStyleSheet("""   
                    QPushButton:hover{  
                        background-color: #F29C1F; 
                        color: #4B4B4B;
                    }  
                    QPushButton{  
                        background-color: #4B4B4B; 
                        color: #F29C1F; 
                        font-size: 30px;  
                        border-radius: 3px; 
                        border:1px solid #4B4B4B; 
                        margin: 5px; 
                        height: 50px
                    } 
                """)
                self.col_2.addWidget(self.buttons[btnText], btnPos[0], btnPos[1])
            elif btnText == '0':
                self.buttons[btnText].setStyleSheet("""  
                    QPushButton:hover{  
                        background-color: #F29C1F; 
                        color: #4B4B4B;
                    }    
                    QPushButton{  
                        background-color: #4B4B4B; 
                        color: white; 
                        font-size: 25px;  
                        border-radius: 3px; 
                        border:1px solid #4B4B4B; 
                        margin: 5px; 
                        height: 50px;
                    }
                """)
                self.col_2.addWidget(self.buttons[btnText], btnPos[0], btnPos[1], 1, 2)

            elif btnText in ("sin(x)", "cos(x)", "tan(x)", "cot(x)", "log\u2082(x)", "log\u2081\u2080(x)"):
                self.buttons[btnText].setStyleSheet("""  
                    QPushButton:hover{  
                        background-color: #F29C1F; 
                        color: #4B4B4B;
                    }    
                    QPushButton{  
                        background-color: #3F3F3F; 
                        color: white; 
                        font-size: 18px;  
                        border-radius: 3px; 
                        border:1px solid #3F3F3F; 
                        margin: 5px; 
                        height: 50px;
                    }
                """)
                self.col_2.addWidget(self.buttons[btnText], btnPos[0], btnPos[1])
            elif btnText in [str(num) for num in range(10)]:
                self.buttons[btnText].setStyleSheet("""  
                    QPushButton:hover{  
                        background-color: #F29C1F; 
                        color: #4B4B4B;
                    }    
                    QPushButton{  
                        background-color: #4B4B4B; 
                        color: white; 
                        font-size: 23px;  
                        border-radius: 3px; 
                        border:1px solid #4B4B4B; 
                        margin: 5px; 
                        height: 50px;
                    }
                """)
                self.col_2.addWidget(self.buttons[btnText], btnPos[0], btnPos[1])
            else:
                self.buttons[btnText].setStyleSheet("""  
                    QPushButton:hover{  
                        background-color: #F29C1F; 
                        color: #4B4B4B;
                    }    
                    QPushButton{  
                        background-color: #3F3F3F; 
                        color: white; 
                        font-size: 23px;  
                        border-radius: 3px; 
                        border:1px solid #3F3F3F; 
                        margin: 5px; 
                        height: 50px;
                    }
                """)
                self.col_2.addWidget(self.buttons[btnText], btnPos[0], btnPos[1])
        self.layout.addLayout(self.col_2)
