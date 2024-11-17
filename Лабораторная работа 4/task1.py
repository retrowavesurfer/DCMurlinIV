import json

def task() -> float:
    with open('input.json', 'r') as f:
        numbers = json.load(f)
    summa = 0.0
    for num in numbers:
        summa += num['score'] * num['weight']
    return round(summa, 3)
print(task())
