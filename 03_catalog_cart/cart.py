# 必要なインポートと型ヒントを追加してください。
from product import Product

class Cart:
    def __init__(self) -> None:
        self.items:list[Product] = []

    def add_product(self, product:Product) -> None:
        self.items.append(product)

    def get_total(self) -> int:
        total = 0
        for item in self.items:
            total += item.price
        return total