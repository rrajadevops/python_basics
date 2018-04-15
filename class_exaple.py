class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    def add_items(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)
    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total
    def stock_price_alternet(self):
        return sum([item['price'] for item in self.items])


    def franchise(cls, store):
        return Store(store.name + " - Franchise")

    @staticmethod
    def store_details(store):
        return '{}, total stock price: {}'.format(store.name, int(store.stock_price()))

mynam = Store("Raja")
mynam.add_items("Rice", 100)
mynam.add_items("Doll", 200)
print (mynam.stock_price())
print (mynam.stock_price_alternet())
