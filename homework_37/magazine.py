class Magazine:

    def __init__(self):
        self._cash_box = 0
        self._expenses = 0

    def make_sale(self, salesman, item, quantity, storage):
        """
        Implement sale

        Count selling price and adds to 'Magazine.cash_box' and 'Salesman.personal_sales'
        Count purchase price and adds to 'Magazine.expenses'
        Subtracts 'quantity' from 'Storage.goods'
        :param storage: takes given storage obj.
        :param salesman: takes seller obj.
        :param item: takes Item obj.
        :param quantity: quantity of selling items
        """
        try:
            selling_price_total = item.sell_price * quantity
            buying_price_total = item.purchase_price * quantity
            self._cash_box += selling_price_total
            self._expenses += buying_price_total
            storage._goods[item.name] -= quantity
            salesman._total_sales += selling_price_total
        except KeyError:
            raise KeyError("Wrong 'seller id' or 'item'")

    def show_income(self):
        print(self._cash_box - self._expenses)

    def show_cash_box(self):
        print(self._cash_box)

    def show_expenses(self):
        print(self._expenses)

    def clear_cash_box(self):
        self._cash_box = 0

    def clear_expenses(self):
        self._expenses = 0

    def write_off(self, item, quantity, storage):
        """
        Subtract quantity of items in 'Storage.goods' (For spoiled items)

        :param item: Takes Item object
        :param quantity: quantity of spoiled items
        :param storage: takes given storage obj.
        """
        if item.name in storage._goods:
            storage._goods[item.name] -= quantity
            self._expenses += item.purchase_price * quantity
        else:
            raise KeyError("Wrong item: %s" % item.name)
