from functools import partial
from View.MainView import MainView
from Model.MainModel import MainModel
from Controller.IntegralController import IntegralController


class MainController(MainView):
    def __init__(self):
        super().__init__()
        self.view = MainView()
        self.model = MainModel()
        self.integralController = IntegralController()
        self.initBtn()
        self.memory = ''

    def initBtn(self):
        for btnText, btn in self.view.buttons.items():
            btnText = btnText.replace('x)', '')
            btnText = btnText.replace('x', '')
            match (btnText):
                case 'MS':
                    btn.clicked.connect(self.memorySave)
                case 'MR':
                    btn.clicked.connect(self.memoryReset)
                case 'MC':
                    btn.clicked.connect(self.memoryCall)
                case 'CE':
                    btn.clicked.connect(self.clearInput)
                case '\u232b':
                    btn.clicked.connect(self.delInput)
                case '\u222b':
                    btn.clicked.connect(self.integral)
                case '\u02b8':
                    btn.clicked.connect(partial(self.writeToInput, '^'))
                case '=':
                    btn.clicked.connect(self.showResult)
                case _:
                    btn.clicked.connect(partial(self.writeToInput, btnText))

    def writeToInput(self, btnText):
        if self.view.mainInput.text() == '0' and btnText in [str(num) for num in range(10)]:
            self.view.mainInput.setText(btnText)
        else:
            self.view.mainInput.setText(self.view.mainInput.text() + btnText)
        self.view.mainInput.setFocus()

    def clearInput(self):
        self.view.mainInput.setText("0")
        self.view.mainInput.setFocus()

    def delInput(self):
        if self.view.mainInput.text().__len__() == 1:
            self.view.mainInput.setText('0')
        else:
            self.view.mainInput.backspace()
        self.view.mainInput.setFocus()

    def showResult(self):
        result = self.model.inputValuesAnalysis(self.view.mainInput.text())
        self.view.mainInput.setText(result)

    def absoluteValue(self):
        result = self.model.absoluteValue(self.view.mainInput.text())
        self.view.mainInput.setText(result)

    def memorySave(self):
        if self.view.mainInput.text() != '':
            self.memory = self.view.mainInput.text()

    def memoryReset(self):
        self.memory = ''

    def memoryCall(self):
        if (self.memory != ''):
            self.view.mainInput.setText(self.memory)

    def integral(self):
        self.integralController.integralView.show()
