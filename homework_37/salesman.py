class Salesman:

    LAST_ID = 1

    def __init__(self, name):
        self.name = name
        self.id = self.LAST_ID
        Salesman.LAST_ID += 1
        self._total_sales = 0

    def show_sales(self):
        print(self._total_sales)

    def clear_sales(self):
        self._total_sales = 0

    def show_info(self):
        print("Name: ", self.name, "ID: ", self.id)
