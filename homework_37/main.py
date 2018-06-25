from magazine import Magazine
from storage import Storage
from item import Item
from salesman import Salesman

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
seller_r2d2.show_info()
s1 = Storage()
s1.add_item(Item('iPhone', 1000, 1200), 10)
s1.item_balance()

s2 = Storage()
s2.item_balance()

seller_r2d2.show_sales()
