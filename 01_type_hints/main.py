# functions.pyの関数をインポートし、READMEの4つの結果を表示してください。
from functions import *

def main():
    print(calculate_total(200,3))
    print(make_label("ノート",200))
    print(sum_prices([200,150,100]))
    print(sum_prices([]))

if __name__ == "__main__":
    main()
