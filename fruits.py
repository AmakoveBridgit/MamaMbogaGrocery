class Fruit:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def add_fruits(self):
            return f"I want to order {self.name}"
    
    def remove_fruits(self):
        return f"I am removing {self.name}"
    
    def categorize_fruits(self):
         return f"categorize {self.name}"
    
fruit1=Fruit("Apple",50,20)
fruit2=Fruit("Mangoes",60,20)
fruit3=Fruit("Pineaples",100,30)
fruit4=Fruit("Bananas",50,60)
fruit5=Fruit("Berries",50,20)
fruit6=Fruit("Oranges",50,20)
fruit7=Fruit("WaterMelon",50,20)

print(fruit1.add_fruits())
print(fruit3.remove_fruits())
print(fruit5.categorize_fruits())



