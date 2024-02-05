import random
from collections import  defaultdict

import matplotlib.pyplot as plt
from rich.console import Console

from draw_table import draw_table


def task7() -> None:
    console = Console()
    
    nums = 1_000_000
    
    counts = defaultdict(int)
    
    for _ in range(nums):
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        counts[first_dice + second_dice] += 1
    
    probabilities = {key: count / nums for key, count in counts.items()}
    
    console.print(draw_table(probabilities, 'Probabilities table'))

    plt.bar(probabilities.keys(), probabilities.values())
    plt.show()

if __name__ == "__main__":
    task7()