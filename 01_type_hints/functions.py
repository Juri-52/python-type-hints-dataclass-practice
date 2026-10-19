# 引数と戻り値に型を追加し、各関数を完成させてください。

def calculate_total(price:int, quantity:int) -> int:
    total = price * quantity
    return total

def make_label(name:str, price:int) -> str:
    return f"{name}:{price}円"

def sum_prices(prices:list[int]) -> int:
    sum = 0
    for item in prices:
        sum += item
    return sum