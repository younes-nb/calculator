class IntegralModel:
    def getValues(self, upperBound, lowerBound, phrase):
        try:
            upperSum = 0
            lowerSum = 0
            for element in phrase:
                degree = element[1] + 1
                coefficient = int(element[0]) / degree
                upperSum += coefficient * (upperBound ** degree)
                lowerSum += coefficient * (lowerBound ** degree)

            return str(upperSum - lowerSum)
        except(Exception):
            return "Error"
