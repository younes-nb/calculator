import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout, QLabel, QTextEdit, \
    QPushButton, QLayout, QComboBox
from PyQt6.QtGui import QIcon, QCursor, QRegularExpressionValidator
from PyQt6 import QtCore
from PyQt6.QtCore import Qt


class IntegralView(QWidget):
    def __init__(self):
        super().__init__()
        self.geometry = self.setGeometry(150, 150, 500, 450)

        self.setWindowTitle("Integral")
        self.setWindowIcon(QIcon("./icons/intagral-icon.png"))
        self.setStyleSheet(""" 
                    background-color: #323232; 
                    font-size: 15px;   
                """)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.upperInput = QLineEdit()
        self.upperInput.setPlaceholderText("Upper Bound")
        self.upperInput.setStyleSheet("""    
            margin: 30px 30px 0 0; 
            color: lightgray; 
            padding: 3px; 
            border-bottom: 1px solid #F29C1F;  
            border-radius: 5px;   
            font-size:18px; 
        """)

        upperContainer = QHBoxLayout()
        upperContainer.addWidget(self.upperInput)
        upperContainer.addStretch(1)

        self.lowerInput = QLineEdit()
        self.lowerInput.setPlaceholderText("Lower Bound")
        self.lowerInput.setStyleSheet("""  
                margin: 100px 30px 0 0;; 
                color: lightgray; 
                padding: 3px; 
                border-bottom: 1px solid #F29C1F;  
                border-radius: 5px;   
                font-size:18px;
            """)

        lowerContainer = QHBoxLayout()
        lowerContainer.addWidget(self.lowerInput)
        lowerContainer.addStretch(1)

        boundCol = QVBoxLayout()
        boundCol.addLayout(upperContainer)
        boundCol.addLayout(lowerContainer)
        integralLable = QLabel("\u222b")
        integralLable.setStyleSheet(""" 
                font-size:170px;   
                color : lightgray;
            """)
        integralRow = QHBoxLayout()
        integralRow.addWidget(integralLable)
        integralRow.addLayout(boundCol)
        integralRow.setAlignment(Qt.AlignmentFlag.AlignTop)

        degreeLable = QLabel("Select polynomial's degree :")
        degreeLable.setFixedSize(320, 30)
        degreeLable.setStyleSheet("""  
            font-size :17px; 
            color: #F29C1F; 
            margin-left:95px;
        """)

        self.degreeinput = QComboBox()
        self.degreeinput.setFixedSize(70, 30)
        self.degreeinput.setStyleSheet("""
            color: #F29C1F;
            background-color: #4B4B4B; 
            padding :5px;  
            font-size :17px;
        """)
        for num in range(10):
            self.degreeinput.addItem(str(num))

        degreeRow = QHBoxLayout()
        degreeRow.addWidget(degreeLable)
        degreeRow.addWidget(self.degreeinput)
        degreeRow.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        integralInputs = QHBoxLayout()
        self.phrases = []
        for num in range(10):
            phrase = QHBoxLayout()

            divider = QLabel("+")
            divider.setFixedSize(10, 30)
            divider.setStyleSheet(""" 
                color:lightgray; 
                font-size : 16px 
            """)
            divider.hide()
            coefficientInput = QLineEdit()
            coefficientInput.setFixedSize(40, 30)
            coefficientInput.setStyleSheet(""" 
                    background-color: #4B4B4B; 
                    color: #F29C1F; 
                    padding: 5px;  
                    font-size: 16px; 
                    border: 1px solid transparent; 
                    border-radius: 5px;
                """)
            coefficientInput.hide()
            variable = QLabel("x^{0}".format(str(num)))
            variable.setFixedSize(30, 30)
            variable.setStyleSheet("""  
                    color:lightgray; 
                    font-size : 16px 
                """)
            variable.hide()

            phrase.addWidget(divider)
            phrase.addWidget(coefficientInput)
            phrase.addWidget(variable)
            phraseWidgets = (divider, coefficientInput, variable)
            self.phrases.append(phraseWidgets)
            integralInputs.addLayout(phrase)
        integralInputs.addStretch(1)

        self.calculateBtn = QPushButton("Calculate")
        self.calculateBtn.setFixedSize(150, 50)
        self.calculateBtn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.calculateBtn.setStyleSheet("""   
                    QPushButton:hover{  
                        background-color: #F29C1F; 
                        color: #4B4B4B;
                    }  
                    QPushButton{  
                        background-color: #4B4B4B; 
                        color: #F29C1F; 
                        font-size: 20px;  
                        border-radius: 5px; 
                        border:1px solid #4B4B4B; 
                        margin: 5px;  
                        padding: 3px;
                    } 
                """)
        calculateBtnContainer = QHBoxLayout()
        calculateBtnContainer.addWidget(self.calculateBtn)
        calculateBtnContainer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.resultLabel = QLabel()
        self.resultLabel.setStyleSheet("""  
            color: #F29C1F; 
            font-size: 30px;
        """)
        self.resultLabel.hide()

        resultContainer = QHBoxLayout()
        resultContainer.addWidget(self.resultLabel)
        resultContainer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        mainCol = QVBoxLayout()
        mainCol.addLayout(integralRow)
        mainCol.addLayout(degreeRow)
        mainCol.addLayout(integralInputs)
        mainCol.addLayout(calculateBtnContainer)
        mainCol.addLayout(resultContainer)
        self.layout.addLayout(mainCol)
