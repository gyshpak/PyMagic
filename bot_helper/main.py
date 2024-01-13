from pathlib import Path
# import bot_helper.address_book as book
import address_book as book
import note_book as notebook
from tabulate import tabulate
from commands import *
import pickle
from termcolor import colored, cprint
from schema import help_table
from rich.table import Table
from rich.prompt import Prompt
from rich.console import Console
from datetime import date

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



def input_error(func):
    def inner(my_book, val):
        try:
            return_data = func(my_book, val)
        except IndexError:
            return_data = cprint("Give me name and phone please", 'red')
        except TypeError:
            return_data = cprint("Wrong command, try again", 'red')
        except KeyError:
            return_data = cprint("Wrong user, repeat please", 'red')
        except ValueError:
            return_data = cprint("Wrong number, repeat please", 'red')
        except KeyboardInterrupt:
            print("\nCommand input interrupted. Exiting...")
            exit()
        except book.WrongBirthday:
            return_data = cprint("Wrong birthday, repeat please", 'red')
        except book.ExistsPhone:
            return_data = cprint("Phone is exist", 'red')
        return return_data
    return inner


def handler_hello(my_book, _ = None):
    return cprint("How can I help you?", 'yellow')

def handler_add(my_book, list_):
    my_book.exists_phone(list_[1])
    try:
        record = my_book.find(list_[0].capitalize())
    except:
        if len(list_) == 3:
            record = book.Record(list_[0].capitalize(),list_[2])
        else:
            record = book.Record(list_[0].capitalize())
        record.add_phone(list_[1])
        my_book.add_record(record)
    else:
        record.add_phone(list_[1])
        my_book.add_record(record)
    return cprint("Command successfully complete", 'green')

def handler_change(my_book, list_):
    my_book.exists_phone(list_[2])
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        record.edit_phone(list_[1], list_[2])
    return cprint(f"Phone {list_[1]} from user {list_[0].capitalize()} successfully chandget to phone {list_[2]}", 'green')
    
# def handler_show_all(my_book, _ = None):
#     return my_book

# def handler_show_all(my_book, _=None):
#     table_data = []

#     headers = ["Name", "Phone", "Email", "Birthday"]
#     table_data.append(headers)

#     for record in my_book:
#         name = record.name.value
#         phones = ', '.join(p.value for p in record.phones)
#         email = ''
#         birthday = date.strftime(record.birthday.value, '%d.%m.%Y') if hasattr(record, "birthday") else ''
#         table_data.append([name, phones, email, birthday])

#     formatted_table = tabulate(table_data, headers="firstrow", tablefmt="pretty")

#     return cprint(formatted_table, 'blue')

def handler_show_all(my_book, _=None):
    rows = []

    for record in my_book:
        name = record.name.value
        phones = ', '.join(p.value for p in record.phones)
        email = ''
        birthday = date.strftime(record.birthday.value, '%d.%m.%Y') if hasattr(record, "birthday") else ''
        rows.append([name, phones, email, birthday])

    pretty_table(
        title='List of commands with format',
        header=['Name', 'Telephone', 'Email', 'Birthday'],
        rows=rows
    )

def handler_exit(my_book, _ = None):
    return "Good bye!"

# def handler_find(my_book, list_):
#     list_rec = my_book.finde_records(list_[0].capitalize())
#     if len(list_rec) != 0:
#         ret_book = book.AddressBook()
#         for rec_ in list_rec:
#             ret_book.add_record(rec_)
            
#             pretty_table( 
#                 title='List of commands with format', 
#                 header=['Contact name', 'param first'], 
#                 rows=ret_book
#             )
#         # return ret_book
#     else:
#         return cprint("Contact not found", 'red')


def handler_find(my_book, list_):
    rows = []
    
    list_rec = my_book.finde_records(list_[0].capitalize())
    if len(list_rec) != 0:
        ret_book = book.AddressBook()
        for rec_ in list_rec:
            ret_book.add_record(rec_)
            
            name = rec_.name.value
            phones = ', '.join(p.value for p in rec_.phones)
            rows.append([name, phones])
            
        pretty_table( 
            title='List of commands with format', 
            header=['Contact name', 'Phones'], 
            rows=rows
        )
    else:
        return cprint("Contact not found", 'red')

    
def handler_delete_phone(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    record.remove_phone(list_[1])
    return cprint(f"Phone {list_[1]} of user {list_[0].capitalize()} successfully deleted", 'green')

def handler_delete_user(my_book, list_):
    my_book.delete(list_[0].capitalize())
    return cprint(f"User {list_[0].capitalize()} successfully deleted", 'green')

def handler_next_birthday(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    days = record.days_to_birthday()
    return cprint(f"Next birthday for user {list_[0].capitalize()} after {days} days", 'yellow')


def handler_help(my_book = None, _ = None):
    pretty_table( 
        title='List of commands with format', 
        header=['Command', 'Param first', 'Param second', 'Param third', 'Description'], 
        rows=help_table
    )

#Додавання нотатки
def handler_add_note(my_book, list_):
    my_book.exists_tag(list_[1])
    try:
        record = my_book.find(list_[0].capitalize())
    except:
        if len(list_) == 3:
            record = notebook.Record(list_[0].capitalize(),list_[2])
        else:
            record = notebook.Record(list_[0].capitalize())
        record.add_tag(list_[1])
        my_book.add_record(record)
    else:
        record.add_tag(list_[1])
        my_book.add_record(record)
    return cprint("Command successfully complete", 'green')

#Змінення тексту нотаток
# Not working
def handler_change_note(my_book, list_):
    print(list_[0].capitalize())
    record = my_book.find(list_[0].capitalize())
    print(record)
    if record is not None:
        record.edit_text(list_[1])
    return cprint(f"Text from note {list_[0].capitalize()} successfully changed", 'green')

#Показати всі нотатки
def handler_show_all_notes(my_book, _=None):

    rows = []

    for record in my_book:
        title = record.title() if callable(record.title) else record.title
        text = record.text.value if hasattr(record, 'text') else ''
        tags = ', '.join(tag.value for tag in record.tags) if hasattr(record, 'tags') else ''
        rows.append([title, text, tags])

    pretty_table(
        title='List of commands with format',
        header=['Title', 'Text', 'Tags'],
        rows=rows
    )

#Пошук нотаток
# Not working
def handler_find_note(my_book, list_):
    list_rec = my_book.find_records(list_[0].capitalize())
    if len(list_rec) != 0:
        ret_book = notebook.NoteBook()
        for rec_ in list_rec:
            ret_book.add_record(rec_)
        return ret_book
    else:
        return cprint("Note not found", 'red')

#Видалення тегу
# Not working
def handler_delete_tag(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    record.remove_tag(list_[1])
    return cprint(f"Tag {list_[1]} of note {list_[0].capitalize()} successfully deleted", 'green')

#Видалення нотатки
def handler_delete_note(my_book, list_):
    print(list_[0].capitalize())
    my_book.delete(list_[0].capitalize())
    return f"Note {list_[0].capitalize()} successfully deleted"

#Вибір режиму (телефонна книга або нотатки)
def mode_change(my_book = None, _ = None):
    try: 
        mode = input("Please choose mode\n 1. Address book\n 2. Notes\n ")
    except KeyboardInterrupt:
        exit()
    return mode

    
@input_error
def parser_command(my_book, command):
    list_command = command.split(" ")
    command_name = list_command[0]
    if command_name in NAME_COMMANDS:
        any_command = NAME_COMMANDS[command_name]
        ret_result = any_command(my_book, list_command[1:])
        return ret_result

    if command_name in NAME_COMMANDS_NOTES:
        any_command = NAME_COMMANDS_NOTES[command_name]
        ret_result = any_command(my_book, list_command[1:])
        return ret_result

    compound_command = command_name + "-" + list_command[1] if len(list_command) > 1 else None
    if compound_command in NAME_COMMANDS:
        any_command = NAME_COMMANDS[compound_command]
        ret_result = any_command(my_book, list_command[2:])
        return ret_result

    if compound_command in NAME_COMMANDS_NOTES:
        any_command = NAME_COMMANDS_NOTES[compound_command]
        ret_result = any_command(my_book, list_command[2:])
        return ret_result

    return cprint(f"Unrecognized command: {command_name}", 'red')


def main():
    print(handler_help())
    file_name_phones_p = "bot_helper\\book_pickle.bin"
    
    # file_name_j = "bot_helper\\book_json.json"
    # file_name_j = Path("E:\pyton_proj\Go-IT\\bot_helper\\bot_helper\\book_json.json")
    
    my_book_phones_p = book.AddressBook()
    
    # my_book_j = book.AddressBook()
    my_book_phones = my_book_phones_p.load_from_file_pickle(file_name_phones_p)

    file_name_notes_p = "bot_helper\\notes_book_pickle.bin"
    my_book_notes_p = notebook.NoteBook()
    try:
        my_book_notes = my_book_notes_p.load_from_file_pickle(file_name_notes_p)
    except (EOFError, pickle.UnpicklingError):
        print("Error loading data from pickle file. Check file format and data consistency.")
        my_book_notes = notebook.NoteBook() 
    
    while True:
        #Вибір режиму (телефонна книга або нотатки)
        mode = mode_change()
        if (mode == "1"):
            # command = input("please enter command ").lower()
            user_input = get_command_suggestions("", mode)
            ret_rezault = parser_command(my_book_phones, user_input)
            if ret_rezault:
                print(ret_rezault)
                if ret_rezault == "Good bye!":
                    my_book_phones.save_to_file_pickle(file_name_phones_p)
                    my_book_notes.save_to_file_pickle(file_name_notes_p)
                    # my_book.save_to_file_json(file_name_j)
                    exit()
        elif (mode == "2"):
            user_input = get_command_suggestions("", mode)
            ret_rezault = parser_command(my_book_notes, user_input)
            if ret_rezault:
                print(ret_rezault)
                if ret_rezault == "Good bye!":
                    my_book_phones.save_to_file_pickle(file_name_phones_p)
                    my_book_notes.save_to_file_pickle(file_name_notes_p)
                    exit()
        else:
            cprint("Wrong command!", 'red')
            mode = mode_change()
        
if __name__ == "__main__":
    main()