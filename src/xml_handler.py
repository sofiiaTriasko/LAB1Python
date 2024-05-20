import xml.etree.ElementTree as ET
from xmlschema import XMLSchema
from category import Category
from product import Product

def validate_xml(xml_file, xsd_file):
    schema = XMLSchema(xsd_file)
    if not schema.is_valid(xml_file):
        print("XML file is not valid against the provided XSD")
        raise ValueError("Invalid XML file")
    print("XML file is valid against the provided XSD")

def load_data(filename):
    validate_xml(filename, 'data/store.xsd')
    tree = ET.parse(filename)
    root = tree.getroot()
    categories = []
    for cat_elem in root.findall('category'):
        category = Category(cat_elem.get('name'))
        category.id = cat_elem.get('id')
        for prod_elem in cat_elem.findall('product'):
            product = Product(
                prod_elem.get('name'),
                prod_elem.get('price'),
                prod_elem.get('quantity')
            )
            product.id = prod_elem.get('id')
            category.add_product(product)
        categories.append(category)
    return categories

def save_data(filename, categories):
    root = ET.Element('store')
    for category in categories:
        cat_elem = ET.SubElement(root, 'category', id=category.id, name=category.name)
        for product in category.products:
            ET.SubElement(cat_elem, 'product', id=product.id, name=product.name, price=product.price, quantity=product.quantity)

    tree = ET.ElementTree(root)
    tree.write(filename)
    validate_xml(filename, 'data/store.xsd')
