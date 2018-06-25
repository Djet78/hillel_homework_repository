class Item:

    __LAST_ID = 1

    def __init__(self, name, purchase_price, sell_price):
        self.name = name
        self.purchase_price = purchase_price
        self.sell_price = sell_price
        self.id = Item.__LAST_ID
        Item.__LAST_ID += 1

    def show_item(self):
        """
        Shows all item data (name, purchase price, sell price, item id)
        """
        print("Item name: ", self.name,
              "\nPurchase price: ", self.purchase_price,
              "\nSell price: ", self.sell_price,
              "\nItem id: ", self.id)
