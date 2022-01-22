from src.view.integral_view import IntegralView
from src.model.integral_model import get_values


class IntegralController(IntegralView):
    def __init__(self):
        super(IntegralController, self).__init__()
        self.current_phrases = None
        self.integral_view = IntegralView()
        self.integral_view.hide()

        self.integral_view.degree_input.currentTextChanged.connect(self.show_phrases)
        self.integral_view.calculate_btn.clicked.connect(self.init_btn)

    def show_phrases(self):
        self.current_phrases = []
        count = self.integral_view.degree_input.currentIndex() + 1

        for phrase in range(count):
            self.current_phrases.append(['', phrase])
            for widget in range(3):
                self.integral_view.phrases[phrase][widget].show()

        for phrase in range(count, 10):
            for widget in range(3):
                self.integral_view.phrases[phrase][widget].hide()

    def init_btn(self):
        try:
            for index in range(self.current_phrases.__len__()):
                self.current_phrases[index][0] = int(self.integral_view.phrases[index][1].text())

            self.integral_view.result_label.setText(
                get_values(int(self.integral_view.upper_input.text()),
                           int(self.integral_view.lower_input.text()),
                           self.current_phrases))
        except Exception:
            self.integral_view.result_label.setText("Error")
        finally:
            self.integral_view.result_label.show()
