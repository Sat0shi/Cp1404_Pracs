class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return"{:>20} ({}), worth $ {:10,.2f} {}".format(self.name, self.year, self.cost, self.is_vintage())

    def get_age(self):
        return 2019 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return '(Vintage)'
        else:
            return ''
        