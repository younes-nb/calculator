from View.IntegralView import IntegralView
from Model.IntegralModel import IntegralModel


class IntegralController(IntegralView):
    def __init__(self):
        super().__init__()
        self.integralView = IntegralView()
        self.integralModel = IntegralModel()
        self.integralView.hide()

        self.integralView.degreeinput.currentTextChanged.connect(self.showPhrases)
        self.integralView.calculateBtn.clicked.connect(self.initBtn)

    def showPhrases(self):
        self.currentPhrases = []
        count = self.integralView.degreeinput.currentIndex() + 1

        for phrase in range(count):
            self.currentPhrases.append(['', phrase])
            for widget in range(3):
                self.integralView.phrases[phrase][widget].show()

        for phrase in range(count, 10):
            for widget in range(3):
                self.integralView.phrases[phrase][widget].hide()

    def initBtn(self):
        try:
            for index in range(self.currentPhrases.__len__()):
                self.currentPhrases[index][0] = int(self.integralView.phrases[index][1].text())

            self.integralView.resultLabel.setText(
                self.integralModel.getValues(int(self.integralView.upperInput.text()),
                                             int(self.integralView.lowerInput.text()),
                                             self.currentPhrases))
        except(Exception):
            self.integralView.resultLabel.setText("Error")
        finally:
            self.integralView.resultLabel.show()
