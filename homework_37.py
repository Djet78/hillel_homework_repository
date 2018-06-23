# ------------------------ Task 37 -------------------------


class Magazine:

    def __init__(self):
        self.cash_box = 0
        self.expenses = 0

    def make_sale(self, salesman, item, quantity, storage):
        """
        Implement sale

        Count selling price and adds to 'Magazine.cash_box' and 'Salesman.personal_sales'
        Count purchase price and adds to 'Magazine.expenses'
        Subtracts 'quantity' from 'Storage.goods'
        :param salesman: takes seller
        :param item: takes Item object
        :param quantity: quantity of selling items
        """
        try:
            selling_price_total = item.sell_price * quantity
            buying_price_total = item.purchase_price * quantity
            self.cash_box += selling_price_total
            self.expenses += buying_price_total
            storage.goods[item.name] -= quantity
            salesman.total_sales += selling_price_total
        except KeyError:
            raise KeyError("Wrong 'seller id' or 'item'")

    def show_income(self):
        print(self.cash_box - self.expenses)

    def show_cash_box(self):
        print(self.cash_box)

    def show_expenses(self):
        print(self.expenses)

    def clear_cash_box(self):
        self.cash_box = 0

    def clear_expenses(self):
        self.expenses = 0

    def write_off(self, item, quantity, storage):
        """
        Subtract quantity of items in 'Storage.goods' (For spoiled items)

        :param item: Takes Item object
        :param quantity: quantity of spoiled items
        """
        if item.name in Storage.goods:
            storage.goods[item.name] -= quantity
            self.expenses += item.purchase_price * quantity
        else:
            raise KeyError("Wrong item: %s" % item.name)


# ----------------------------------------------------------------


class Salesman:

    LAST_ID = 1

    def __init__(self, name):
        self.name = name
        self.id = Item.LAST_ID
        Salesman.LAST_ID += 1
        self.total_sales = 0

    def show_sales(self):
        print(self.total_sales)

    def clear_sales(self):
        self.total_sales = 0

# ----------------------------------------------------------------


class Item:

    items = dict()
    LAST_ID = 1

    def __init__(self, name, purchase_price, sell_price):
        self.name = name
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.id = Item.LAST_ID
        Item.LAST_ID += 1
        self.items[self.name] = self.id

    def show_item(self):
        """
        Shows all item data (name, purchase price, sell price, item id)
        """
        print("Item name: ", self.name,
              "\nPurchase price: ", self.purchase_price,
              "\nSell price: ", self.sell_price,
              "\nItem id: ", self.id)

# ----------------------------------------------------------------


class Storage:

    goods = dict()

    def add_item(self, item, quantity):
        """
        Saves item.name and quantity to 'Storage.goods'

        :param item: Takes Item object
        :param quantity: quantity of coming items
        """
        self.goods[item.name] = self.goods.get(item.name, 0) + quantity

    def withdraw_item(self, item, quantity):
        """
        Subtract quantity of item in 'Storage.goods' (When item was sold)

        :param item: Takes Item object
        :param quantity: quantity of consuming items
        """
        if item.name in self.goods:
            self.goods[item.name] -= quantity
        else:
            raise KeyError("Wrong item: %s" % item.name)

    def item_balance(self, item=None):
        if item is None:
            print(self.goods)
        else:
            print(item.name, self.goods[item.name])

# ----------------------------------------------------------------


# --------------------------- Sandbox ----------------------------


seller_r2d2 = Salesman("r2d2")
seller_2 = Salesman("Petya")
seller_r2d2.show_sales()

cabbage = Item("cabbage", 10, 15)
carrot = Item("carrot", 4, 8)
rabbit_breast = Item("rabbit_breast", 80, 110)

storage = Storage()

storage.add_item(cabbage, 50)
storage.add_item(carrot, 130)
storage.add_item(rabbit_breast, 20)
storage.item_balance(item=carrot)

storage.withdraw_item(carrot, 20)
storage.item_balance()

storage.item_balance()

magazine = Magazine()
magazine.write_off(carrot, 20, storage)
magazine.show_income()

magazine.make_sale(seller_r2d2, carrot, 18, storage)
seller_r2d2.show_sales()
magazine.show_income()

seller_r2d2.show_sales()
seller_2.show_sales()
storage.item_balance()
storage.add_item(carrot, 17)
storage.item_balance()

carrot.show_item()

seller_r2d2.clear_sales()
seller_r2d2.show_sales()

magazine.show_expenses()
magazine.show_cash_box()

magazine.clear_expenses()
magazine.clear_cash_box()

magazine.show_expenses()
magazine.show_cash_box()

magazine.write_off(carrot, 20, storage)
storage.item_balance()
carrot.show_item()