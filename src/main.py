from xml_handler import load_data, save_data
from category import Category
from product import Product

def add_category(categories, name):
    for category in categories:
        if category.name == name:
            print(f"Category '{name}' already exists. Skipping addition.")
            return category
    category = Category(name)
    categories.append(category)
    return category

def add_product_to_category(category, name, price, quantity):
    for product in category.products:
        if product.name == name:
            print(f"Product '{name}' already exists in category '{category.name}'. Skipping addition.")
            return product
    product = Product(name, price, quantity)
    category.add_product(product)
    return product

def edit_product(product, name=None, price=None, quantity=None):
    if name:
        product.name = name
    if price:
        product.price = price
    if quantity:
        product.quantity = quantity

if __name__ == "__main__":
    print("Loading data from XML...")
    categories = load_data('data/store.xml')

    print("\nCurrent categories and products:")
    for category in categories:
        print(f"Category: {category.name} (ID: {category.id})")
        for product in category.products:
            print(f"  Product: {product.name} (ID: {product.id}, Price: {product.price}, Quantity: {product.quantity})")

    # Check if the "Fruits" category already exists before adding
    print("\nAdding new category 'Fruits' if it doesn't exist...")
    new_category = add_category(categories, 'Fruits')

    # Check if the products already exist in the "Fruits" category before adding
    print("Adding products to 'Fruits' category if they don't exist...")
    add_product_to_category(new_category, 'Apple', '1.20', '50')
    add_product_to_category(new_category, 'Banana', '0.80', '100')

    # Editing the product "Apple" in the "Fruits" category if it exists
    print("\nEditing 'Apple' product before:")
    for product in new_category.products:
        if product.name == 'Apple':
            print(f"  Product: {product.name} (ID: {product.id}, Price: {product.price}, Quantity: {product.quantity})")
            edit_product(product, price='1.30', quantity='60')
            print("  After editing:")
            print(f"  Product: {product.name} (ID: {product.id}, Price: {product.price}, Quantity: {product.quantity})")

    print("\nUpdated categories and products:")
    for category in categories:
        print(f"Category: {category.name} (ID: {category.id})")
        for product in category.products:
            print(f"  Product: {product.name} (ID: {product.id}, Price: {product.price}, Quantity: {product.quantity})")

    print("\nSaving data to XML...")
    save_data('data/store.xml', categories)

    print("Operation completed.")
