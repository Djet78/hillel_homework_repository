class Storage:

    def __init__(self):
        self._goods = dict()

    def add_item(self, item, quantity):
        """
        Saves item.name and quantity to 'Storage.goods'

        :param item: Takes Item object
        :param quantity: quantity of coming items
        """
        self._goods[item.name] = self._goods.get(item.name, 0) + quantity

    def withdraw_item(self, item, quantity):
        """
        Subtract quantity of item in 'Storage.goods' (When item was sold)

        :param item: Takes Item object
        :param quantity: quantity of consuming items
        """
        if item.name in self._goods:
            self._goods[item.name] -= quantity
        else:
            raise KeyError("Wrong item: %s" % item.name)

    def item_balance(self, item=None):
        if item is None:
            print(self._goods)
        else:
            print(item.name, self._goods[item.name])
