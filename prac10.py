# Product class
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def reduce_stock(self, quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
        else:
            print(f"Error: Not enough stock for {self.name}.")

    def increase_stock(self, quantity):
        self.stock_quantity += quantity

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price} (Stock: {self.stock_quantity})"


# Customer class
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cart = ShoppingCart(self)

    def view_cart(self):
        self.cart.view_items()

    def __str__(self):
        return f"Customer: {self.name} (ID: {self.customer_id}) - Email: {self.email}"


# ShoppingCart class
class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = {}  # Dictionary to store items and their quantities
    
    def add_item(self, product, quantity):
        if product.stock_quantity >= quantity:
            if product.product_id in self.items:
                self.items[product.product_id]['quantity'] += quantity
            else:
                self.items[product.product_id] = {'product': product, 'quantity': quantity}
            product.reduce_stock(quantity)
            print(f"Added {quantity} x {product.name} to the cart.")
        else:
            print(f"Error: Not enough stock for {product.name}.")
    
    def remove_item(self, product, quantity):
        if product.product_id in self.items:
            if self.items[product.product_id]['quantity'] >= quantity:
                self.items[product.product_id]['quantity'] -= quantity
                product.increase_stock(quantity)
                print(f"Removed {quantity} x {product.name} from the cart.")
            else:
                print(f"Error: You don't have enough quantity of {product.name} in the cart.")
        else:
            print(f"Error: {product.name} is not in the cart.")
    
    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item['product'].price * item['quantity']
        return total

    def checkout(self):
        total_cost = self.calculate_total()
        if total_cost > 0:
            print(f"Total cost: ${total_cost:.2f}")
            print("Order processed successfully!")
            self.items.clear()  # Clear the cart after checkout
        else:
            print("Error: Your cart is empty!")

    def view_items(self):
        if not self.items:
            print("Your cart is empty!")
        else:
            for item in self.items.values():
                product = item['product']
                quantity = item['quantity']
                print(f"{product.name} - ${product.price} x {quantity} = ${product.price * quantity:.2f}")


# Example usage
if __name__ == "__main__":
    # Create some products
    p1 = Product(1, "Laptop", 1000, 5)
    p2 = Product(2, "Smartphone", 500, 10)
    p3 = Product(3, "Headphones", 150, 15)

    # Create a customer
    customer = Customer(101, "John Doe", "johndoe@example.com")

    # Add items to the shopping cart
    customer.cart.add_item(p1, 2)
    customer.cart.add_item(p2, 3)

    # View items in the cart
    customer.view_cart()

    # Checkout the cart
    customer.cart.checkout()

    # Try adding more items (testing stock limits)
    customer.cart.add_item(p1, 4)  # This should fail because only 3 are left in stock
    customer.view_cart()

    # Adding more products after checking out
    customer.cart.add_item(p3, 2)
    customer.view_cart()
    customer.cart.checkout()  # Final checkout
