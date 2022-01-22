def get_values(upper_bound, lower_bound, phrase):
    try:
        upper_sum = 0
        lower_sum = 0
        for element in phrase:
            degree = element[1] + 1
            coefficient = int(element[0]) / degree
            upper_sum += coefficient * (upper_bound ** degree)
            lower_sum += coefficient * (lower_bound ** degree)

        return str(upper_sum - lower_sum)
    except Exception:
        return "Error"
