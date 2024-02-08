from greedy_algorithm import greedy_algorithm
from dynamic_programming import dynamic_programming

def task6() -> None:
    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
    }
    
    budget = 100
    
    greedy_res = greedy_algorithm(items, budget)
    
    dynamic_res = dynamic_programming(items, budget)
    
    print('\nGreedy algorithm:')
    for key, value in greedy_res.items():
        print(f'{key} =  {value}')
    
    print('\nDynamic programming:')
    for key, value in dynamic_res.items():
        print(f'{key} =  {value}')
    

if __name__ == "__main__":
    task6()