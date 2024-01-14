from rich.console import Console
from rich.table import Table
# from rich.prompt import Prompt


def table(title=None, title_style=None, header=[], header_style='bold blue', rows=[], row_style='bright_green'):

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


def parser(book):
    # print(type(book))
    records = []
    rec_per_page = book.qua_for_iter
    
    def value_getter(key):
        value = record.__dict__.get(key)
        if isinstance(value, list):
            value = ' '.join([repr(i) for i in value]) if len(value) else '*'
        elif value:
            value = repr(value)
        else:
            value = '*'
        return value
    
    for record in book.data.values():
        row = [
            value_getter('name'),
            value_getter('phones'),
            value_getter('e_mails'),
            value_getter('birthday'),
            value_getter('address'),
            value_getter('notes')
               ]
        records.append(row)

    header = ['Name', 'Phones', 'E-mails',
              'Birthday', 'Address', 'Notes']
    title = '...'
    page = []
    for row in enumerate(records, start=1):
        if row[0]%rec_per_page:
            page.append(row[1])
        elif (row[0] == len(records)) and (page != []):
            page.append(row[1])  
            table(title=title, header=header, rows=page)
            page.clear()
        else:
            page.append(row[1])
            table(title=title, header=header, rows=page)    
            page.clear()
            
    # print(rows)
    
    # for row in rows:
    #     table(title, header, row)
    #     if input("Next page (y)?") == 'y':
    #         continue
    #     else:
    #         break

    # pages = str(book).split(' \n')
    # print(pages)


    # def validator(object: str, pattern: str):
    #     index = object.find(pattern)
    #     if index != -1:
    #         found = object[index:]
    #         found = found.split(':')[1]
    #         rest = object[:index]
    #     else:
    #         found = '*'
    #         rest = object
    #     return rest, found

    # for page in pages:
    #     lines = page.split('; ')
    #     rows = []
    #     for line in lines:
    #         text = line
    #         text, address = validator(text, 'address:')
    #         text, note = validator(text, 'notes:')
    #         text, birthday = validator(text, 'birthday:')
    #         text, phones = validator(text, 'phones:')
    #         text, name = validator(text, 'Contact name:')

    #         rows.append([name, phones, birthday, address, note])

