from functools import partial
from src.view.main_view import MainView
from src.model.main_model import input_values_analysis
from src.controller.integral_controller import IntegralController


class MainController(MainView):
    def __init__(self):
        super(MainController, self).__init__()
        self.view = MainView()
        self.integral_controller = IntegralController()
        self.init_btn()
        self.memory = ''

    def init_btn(self):
        for btn_text, btn in self.view.buttons.items():
            btn_text = btn_text.replace('x)', '')
            btn_text = btn_text.replace('x', '')
            match btn_text:
                case 'MS':
                    btn.clicked.connect(self.memory_save)
                case 'MR':
                    btn.clicked.connect(self.memory_reset)
                case 'MC':
                    btn.clicked.connect(self.memory_call)
                case 'CE':
                    btn.clicked.connect(self.clear_input)
                case '\u232b':
                    btn.clicked.connect(self.del_input)
                case '\u222b':
                    btn.clicked.connect(self.integral)
                case '\u02b8':
                    btn.clicked.connect(partial(self.write_to_input, '^'))
                case '=':
                    btn.clicked.connect(self.show_result)
                case _:
                    btn.clicked.connect(partial(self.write_to_input, btn_text))

    def write_to_input(self, btn_text):
        if self.view.main_input.text() == '0' and btn_text in [str(num) for num in range(10)]:
            self.view.main_input.setText(btn_text)
        else:
            self.view.main_input.setText(self.view.main_input.text() + btn_text)
        self.view.main_input.setFocus()

    def clear_input(self):
        self.view.main_input.setText("0")
        self.view.main_input.setFocus()

    def del_input(self):
        if self.view.main_input.text().__len__() == 1:
            self.view.main_input.setText('0')
        else:
            self.view.main_input.backspace()
        self.view.main_input.setFocus()

    def show_result(self):
        result = input_values_analysis(self.view.main_input.text())
        self.view.main_input.setText(result)

    def memory_save(self):
        if self.view.main_input.text() != '':
            self.memory = self.view.main_input.text()

    def memory_reset(self):
        self.memory = ''

    def memory_call(self):
        if self.memory != '':
            self.view.main_input.setText(self.memory)

    def integral(self):
        self.integral_controller.integral_view.show()
