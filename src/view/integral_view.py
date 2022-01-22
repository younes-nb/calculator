from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QComboBox


class IntegralView(QWidget):
    def __init__(self):
        super(IntegralView, self).__init__()
        self.geometry = self.setGeometry(150, 150, 500, 450)
        self.setWindowTitle("Integral")
        self.setStyleSheet(""" 
            background-color: #323232; 
            font-size: 15px;   
        """)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.upper_input = QLineEdit()
        self.upper_input.setPlaceholderText("Upper Bound")
        self.upper_input.setStyleSheet("""    
            margin: 30px 30px 0 0; 
            color: lightgray; 
            padding: 3px; 
            border-bottom: 1px solid #F29C1F;  
            border-radius: 5px;   
            font-size: 18px; 
        """)

        upper_container = QHBoxLayout()
        upper_container.addWidget(self.upper_input)
        upper_container.addStretch(1)

        self.lower_input = QLineEdit()
        self.lower_input.setPlaceholderText("Lower Bound")
        self.lower_input.setStyleSheet("""  
            margin: 100px 30px 0 0;; 
            color: lightgray; 
            padding: 3px; 
            border-bottom: 1px solid #F29C1F;  
            border-radius: 5px;   
            font-size: 18px;
        """)

        lower_container = QHBoxLayout()
        lower_container.addWidget(self.lower_input)
        lower_container.addStretch(1)

        bound_col = QVBoxLayout()
        bound_col.addLayout(upper_container)
        bound_col.addLayout(lower_container)
        integral_label = QLabel("\u222b")
        integral_label.setStyleSheet(""" 
            font-size: 170px;   
            color: lightgray;
        """)
        integral_row = QHBoxLayout()
        integral_row.addWidget(integral_label)
        integral_row.addLayout(bound_col)
        integral_row.setAlignment(Qt.AlignmentFlag.AlignTop)

        degree_label = QLabel("Select polynomial's degree :")
        degree_label.setFixedSize(320, 30)
        degree_label.setStyleSheet("""  
            font-size: 17px; 
            color: #F29C1F; 
            margin-left: 95px;
        """)

        self.degree_input = QComboBox()
        self.degree_input.setFixedSize(70, 30)
        self.degree_input.setStyleSheet("""
            color: #F29C1F;
            background-color: #4B4B4B; 
            padding :5px;  
            font-size :17px;
        """)
        for num in range(10):
            self.degree_input.addItem(str(num))

        degree_row = QHBoxLayout()
        degree_row.addWidget(degree_label)
        degree_row.addWidget(self.degree_input)
        degree_row.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        integral_inputs = QHBoxLayout()
        self.phrases = []
        for num in range(10):
            phrase = QHBoxLayout()

            divider = QLabel("+")
            divider.setFixedSize(10, 30)
            divider.setStyleSheet(""" 
                color: lightgray; 
                font-size : 16px 
            """)
            divider.hide()
            coefficient_input = QLineEdit()
            coefficient_input.setFixedSize(40, 30)
            coefficient_input.setStyleSheet(""" 
                background-color: #4B4B4B; 
                color: #F29C1F; 
                padding: 5px;  
                font-size: 16px; 
                border: 1px solid transparent; 
                border-radius: 5px;
            """)
            coefficient_input.hide()
            variable = QLabel("x^{0}".format(str(num)))
            variable.setFixedSize(30, 30)
            variable.setStyleSheet("""  
                    color: lightgray; 
                    font-size : 16px 
                """)
            variable.hide()

            phrase.addWidget(divider)
            phrase.addWidget(coefficient_input)
            phrase.addWidget(variable)
            phrase_widgets = (divider, coefficient_input, variable)
            self.phrases.append(phrase_widgets)
            integral_inputs.addLayout(phrase)
        integral_inputs.addStretch(1)

        self.calculate_btn = QPushButton("Calculate")
        self.calculate_btn.setFixedSize(150, 50)
        self.calculate_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.calculate_btn.setStyleSheet("""   
            QPushButton:hover{  
                background-color: #F29C1F; 
                color: #4B4B4B;
            }  
            QPushButton{  
                background-color: #4B4B4B; 
                color: #F29C1F; 
                font-size: 20px;  
                border-radius: 5px; 
                border: 1px solid #4B4B4B; 
                margin: 5px;  
                padding: 3px;
            } 
        """)
        calculate_btn_container = QHBoxLayout()
        calculate_btn_container.addWidget(self.calculate_btn)
        calculate_btn_container.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.result_label = QLabel()
        self.result_label.setStyleSheet("""  
            color: #F29C1F; 
            font-size: 30px;
        """)
        self.result_label.hide()

        result_container = QHBoxLayout()
        result_container.addWidget(self.result_label)
        result_container.setAlignment(Qt.AlignmentFlag.AlignCenter)

        main_col = QVBoxLayout()
        main_col.addLayout(integral_row)
        main_col.addLayout(degree_row)
        main_col.addLayout(integral_inputs)
        main_col.addLayout(calculate_btn_container)
        main_col.addLayout(result_container)
        self.layout.addLayout(main_col)
