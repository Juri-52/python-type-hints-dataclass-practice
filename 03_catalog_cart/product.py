# Productをdataclassにし、READMEのフィールドを定義してください。
from dataclasses import dataclass

@dataclass
class Product:
    product_id:int
    name:str
    price:int = 0

    def get_info(self) -> str:
        return f"{self.product_id}. {self.name} - {self.price}円"