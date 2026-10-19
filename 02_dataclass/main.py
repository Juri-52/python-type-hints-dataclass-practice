# Productをインポートし、READMEの比較と表示を確認してください。
from product import Product

def main():
    notebook1 = Product(1,"ノート",200)
    notebook2 = Product(1,"ノート",200)
    sample = Product(11,"試供品")

    print(notebook1.get_info())
    print(notebook1)
    print(sample.price)
    print(notebook1 == notebook2) # 数値が同一なのでTrue
    print(notebook1 is notebook2) # インスタンスが異なるのでFalse

if __name__ == "__main__":
    main()