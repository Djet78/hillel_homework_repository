# ------------------------ Task 37 -------------------------


class Magazine:

    expenses = 0

    def __init__(self):
        self.cash_box = 0

    def make_sale(self, salesman_id, item, quantity):
        """
        Implement sale

        Count selling price and adds to 'Magazine.cash_box' and 'Salesman.personal_sales'
        Count purchase price and adds to 'Magazine.expenses'
        Subtracts 'quantity' from 'Storage.goods'
        :param salesman_id: takes sellers id
        :param item: takes Item object
        :param quantity: quantity of selling items
        """
        try:
            selling_price_total = Item.item_prices[item.name][Item.SELL_PRICE] * quantity
            buying_price_total = Item.item_prices[item.name][Item.PURCHASE_PRICE] * quantity
            self.cash_box += selling_price_total
            self.expenses += buying_price_total
            storage.consumption(item, quantity)
            Salesman.personal_sales[salesman_id] += Salesman.personal_sales.get(salesman_id, 0) + selling_price_total
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


# ----------------------------------------------------------------


class Salesman:

    personal_sales = dict()

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.personal_sales[self.id] = 0

    def show_sales(self):
        print(self.personal_sales[self.id])

    def clear_sales(self):
        self.personal_sales[self.id] = 0

# ----------------------------------------------------------------


class Item:

    item_prices = dict()
    PURCHASE_PRICE = 0
    SELL_PRICE = 1

    def __init__(self, name, purchase_price, sell_price, item_id):
        self.name = name
        self.item_id = item_id
        self.item_prices[self.name] = [purchase_price, sell_price, item_id]

    def show_item(self):
        """
        Shows all item data (name, purchase price, sell price, item id)
        """
        print("Item name: ", self.name,
              "\nPurchase price: ", self.item_prices[self.name][self.PURCHASE_PRICE],
              "\nSell price: ", self.item_prices[self.name][self.SELL_PRICE],
              "\nItem id: ", self.item_id)

# ----------------------------------------------------------------


class Storage:

    goods = dict()

    def coming(self, item, quantity):
        """
        Saves item.name and quantity to 'Storage.goods'

        :param item: Takes Item object
        :param quantity: quantity of coming items
        """
        self.goods[item.name] = self.goods.get(item.name, 0) + quantity

    def consumption(self, item, quantity):
        """
        Subtract quantity of item in 'Storage.goods' (When item was sold)

        :param item: Takes Item object
        :param quantity: quantity of consuming items
        """
        if item.name in self.goods:
            self.goods[item.name] -= quantity
        else:
            raise KeyError("Wrong item")

    def write_off(self, item, quantity):
        """
        Subtract quantity of item in 'Storage.goods' (For spoiled items)

        :param item: Takes Item object
        :param quantity: quantity of spoiled items
        """
        if item.name in self.goods:
            self.goods[item.name] -= quantity
            Magazine.expenses += Item.item_prices[item.name][Item.PURCHASE_PRICE] * quantity
        else:
            raise KeyError("Wrong item")

    def show_remnants(self):
        print(self.goods)

# ----------------------------------------------------------------


# --------------------------- Sandbox ----------------------------


seller_r2d2 = Salesman("r2d2", 1)
seller_2 = Salesman("Petya", 2)
seller_r2d2.show_sales()

cabbage = Item("cabbage", 10, 15, 1)
carrot = Item("carrot", 4, 8, 2)
rabbit_breast = Item("rabbit_breast", 80, 110, 3)

storage = Storage()

storage.coming(cabbage, 50)
storage.coming(carrot, 130)
storage.coming(rabbit_breast, 20)
storage.show_remnants()

storage.consumption(carrot, 20)
storage.show_remnants()

storage.write_off(carrot, 10)
storage.write_off(cabbage, 3)
storage.show_remnants()

magazine = Magazine()

magazine.show_income()

magazine.make_sale(1, carrot, 17)
magazine.show_income()

seller_r2d2.show_sales()
seller_2.show_sales()
storage.show_remnants()
storage.coming(carrot, 17)
storage.show_remnants()

carrot.show_item()

seller_r2d2.clear_sales()
seller_r2d2.show_sales()

magazine.show_expenses()
magazine.show_cash_box()

magazine.clear_expenses()
magazine.clear_cash_box()

magazine.show_expenses()
magazine.show_cash_box()

print(seller_2.personal_sales)
