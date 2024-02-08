from rich.table import Table

def draw_table(data: dict, title: str) -> Table:
    table = Table(title=title, style="blue", show_lines=True)

    table.add_column("Dice", justify="center", style="green",max_width=20, no_wrap=True)
    table.add_column("Probability, %", style="yellow", justify="center", max_width=20, no_wrap=False)

    for dice, prob in data.items():
        table.add_row(f'{dice}', f'{(prob * 100):.2f}')
    return table

