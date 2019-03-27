class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        new_store = cls(store.name + " - franchise")
        return new_store
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'
        return ("{}, total stock price: {}".format(store.name, store.stock_price()))

store = Store("test")
store.add_item("keyboard", 160)
print(Store.franchise(store))
print(Store.store_details(store))