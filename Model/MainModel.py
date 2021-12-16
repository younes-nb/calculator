import math


class MainModel:
    def inputValuesAnalysis(self, inputText=str):
        result = ''
        try:
            for char in inputText:
                if char == '!':
                    number = ''
                    for i in range(inputText.index(char), -1, -1):
                        if inputText[i] not in [str(num) for num in range(10)]:
                            continue
                        number += inputText[i]
                    number = number[::-1]
                    inputText = inputText.replace("{}!".format(number), "math.factorial({})".format(number))

            inputText = inputText.replace("\u00f7", "/")
            inputText = inputText.replace("\u00d7", "*")
            inputText = inputText.replace("\u2212", "-")
            inputText = inputText.replace('^', '**')
            inputText = inputText.replace("sin", "math.sin")
            inputText = inputText.replace("cos", "math.cos")
            inputText = inputText.replace("tan", "math.tan")
            inputText = inputText.replace("cot", "math.cot")
            inputText = inputText.replace("log\u2082", "math.log2")
            inputText = inputText.replace("log\u2081\u2080", "math.log10")
            inputText = inputText.replace("\u03c0", "math.pi", )
            inputText = inputText.replace("e", "math.e")
            result = eval(inputText)
            if (result == ''):
                return "Error"
            return str(result)

        except(Exception):
            return "Error"