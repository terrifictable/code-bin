class Percentage:
    def __init__(self):
        pass

    def percentage(self, g, pw):
        return (pw/g) * 100

    def percentage_val(self, g, p):
        return (g/10) * (p/10)

    def val_calc(self, p, pw):
        return (pw*100) / p


calc = Percentage()
base = 600
percentage = 30
fraction = 180

print(str(calc.percentage(base, fraction)) + "%")
print(calc.percentage_val(base, percentage))
print(calc.val_calc(percentage, fraction))
