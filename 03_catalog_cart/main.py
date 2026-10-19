# READMEの順番で、カタログの作成・検索・カートへの追加を確認してください。
from cart import *
from catalog import *
from sample_data import *

def main():
    catalog = []
    products = PRODUCTS
    for item in products:
        product = Product(item["product_id"],item["name"],item["price"])
        catalog.append(product)
    catalog = Catalog(catalog)
    print(f"商品数：{len(catalog.products)}")
    cart = Cart()
    product1 = Catalog.find_product(catalog,1)
    if product1 is not None:
        print(product1.get_info())
        cart.add_product(product1)
        cart.add_product(product1)
    product2 = Catalog.find_product(catalog,2)
    if product2 is not None:
        cart.add_product(product2)
    print(f"カート：{len(cart.items)}点")
    print(f"合計：{cart.get_total()}円")
    product999 = Catalog.find_product(catalog,999)
    if product999 is None:
        print("商品が見つかりません")
    print(f"合計：{cart.get_total()}円")
    new_cart = Cart()
    print(f"新しいカート：{new_cart.get_total()}円")

if __name__ == "__main__":
    main()
