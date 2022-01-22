def input_values_analysis(input_text: str):
    result = ''
    try:
        for char in input_text:
            if char == '!':
                number = ''
                for i in range(input_text.index(char), -1, -1):
                    if input_text[i] not in [str(num) for num in range(10)]:
                        continue
                    number += input_text[i]
                number = number[::-1]
                input_text = input_text.replace("{}!".format(number), "math.factorial({})".format(number))

        input_text = input_text.replace("\u00f7", "/")
        input_text = input_text.replace("\u00d7", "*")
        input_text = input_text.replace("\u2212", "-")
        input_text = input_text.replace('^', '**')
        input_text = input_text.replace("sin", "math.sin")
        input_text = input_text.replace("cos", "math.cos")
        input_text = input_text.replace("tan", "math.tan")
        input_text = input_text.replace("cot", "math.cot")
        input_text = input_text.replace("log\u2082", "math.log2")
        input_text = input_text.replace("log\u2081\u2080", "math.log10")
        input_text = input_text.replace("\u03c0", "math.pi", )
        input_text = input_text.replace("e", "math.e")
        result = eval(input_text)
        if result == '':
            return "Error"
        return str(result)

    except Exception:
        return "Error"
