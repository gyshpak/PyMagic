import address_book as book
from rich.console import Console
from rich.table import Table
# from rich.prompt import Prompt


def pretty_table(title=None, title_style=None, header=[], header_style='bold blue', rows=[], row_style='bright_green'):

    table = Table()
    if title:
        table.title = title
        table.title_style = title_style
        table.title_justify = 'left'

    longest_row = max([len(row) for row in rows])
    if len(header) < longest_row:
        for i in range(longest_row - len(header)):
            header.append(f'Column_{i}')

    for column in header:
        table.add_column(column, header_style=header_style)

    for row in rows:
        table.add_row(*row, style=row_style)

    table.show_lines = True

    Console().print(table)
