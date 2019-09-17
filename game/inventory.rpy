init -1 python:
    class Item(object):
        def __init__(self, item, amount=0):
            self.item = item
            self.amount = amount
    class Container(object):
        def __init__(self):
            self.inventory = []
        def has_item(self, item, amount=1):
            if item in [i.item for i in self.inventory]:
                if self.inventory[[i.item for i in self.inventory].index(item)].amount >= amount:
                    return(self.inventory[[i.item for i in self.inventory].index(item)].amount)
                else:
                    return(False)
        def find_item(self, item):
            return(self.inventory[[i.item for i in self.inventory].index(item)])
        def add_item(self, item, amount=1):
            self.inventory.append(Item(item, amount))
        def remove_item(self, item, amount=1):
            if self.has_item(item):
                self.find_item(item).amount -= amount
            if self.find_item(item).amount <= 0:
                self.inventory.pop(self.inventory.index(self.find_item(item)))

default workbag = Container()
default purse = Container()
default person = Container()
