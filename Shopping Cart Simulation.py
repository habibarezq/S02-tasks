#Shopping cart Simulation
class ShoppingCart:
    def __init__(self):
        
        self.cart={}  #dictionary {key:value} pairs
        
    def add_item(self,name,price,quantity):
        
        if name in self.cart:
            self.cart[name]['quantity']+=quantity
        else:
            self.cart[name]={'price':price,'quantity': quantity}   
            
    def display_cart(self):
        if not self.cart:
            print("Your Shopping Cart is Empty!!")
        else:
            print(f"{'Name':<15}{'Price':<10}{'Quantity':<10}")
        
        for key,value in self.cart.items():
            
            print(f"{key:<15}{value['price']:<10.2f}{value['quantity']:<10}")
    def rem_item(self,name):
        if(self.cart.get(name)):
            self.cart.pop(name)
            print(f"{name} deleted!!")
        else:
            print(f"{name} doesn't exist and Can't be deleted")
    def calc_total(self):
        total=0
        for key,value in self.cart.items():
            total+=(value['price'] * value['quantity'])
        return total
#end of class

cart=ShoppingCart()
cart.add_item("Apple",36.05,2)
cart.add_item("Apple",36.05,1)
cart.add_item("Orange",20,1)
cart.add_item("Pineapple",24,1)
cart.rem_item("Apple")
cart.add_item("Pineapple",24,1)
cart.display_cart()
print(f"Your Total : {cart.calc_total():.2f} $")
