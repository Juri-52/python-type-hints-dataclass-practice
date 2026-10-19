# 必要なインポートと型ヒントを追加してください。
from product import Product

class Catalog:
    def __init__(self, products:list[Product]) -> None:
        self.products = products

    def find_product(self, product_id:int) -> Product | None:
        for item in self.products:
            if item.product_id == product_id:
                return item
        return None