class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.inocome = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


x = Position('Egor', 'Badich', 'Teamlead', 300000, 200000)
print(x.get_full_name())
print(x.position)
print(x.get_total_income())