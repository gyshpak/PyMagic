# from pathlib import Path
# import bot_helper.address_book as book
import address_book as book
import note_book as notebook
import pickle
from commands import *
import pretty
from commands import *

def input_error(func):
    def inner(my_book, val):
        try:
            return_data = func(my_book, val)
        except IndexError:
            return_data = "Give me name and phone please"
        except TypeError:
            return_data = "Wrong command, try again"
        except KeyError:
            return_data = "Wrong user, repeat please"
        except ValueError:
            return_data = "Wrong number, repeat please"
        except book.WrongBirthday:
            return_data = "Wrong birthday, repeat please"
        except book.ExistsPhone:
            return_data = "Phone is exist"
        except book.ExistsNote:
            return_data = "User already has a note"
        except book.WrongNote:
            return_data = "Not printable characters in Note or record size excides."
        except book.ExistsAddress:
            return_data = "User already has an address"
        except book.WrongAddress:
            return_data = "Not printable characters in Address or record size excides."
        except book.WrongEmail:
            return_data = "Wrong e-mail, repeat please"
        except book.ExistsEmail:
            return_data = "User already has an e-mail"
        return return_data
    return inner


def handler_hello(my_book, _ = None):
    return "How can I help you?"

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
    return "Command successfully complete"

def handler_change(my_book, list_):
    my_book.exists_phone(list_[2])
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        record.edit_phone(list_[1], list_[2])
    return f"Phone {list_[1]} from user {list_[0].capitalize()} successfully chandget to phone {list_[2]}"


def handler_add_email(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        new_email = ' '.join(list_[1:])
        record.add_email(new_email)
        return f"To user {list_[0].capitalize()} successfully added e-mail:\n\t {new_email}"

def handler_delete_email(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        record.delete_email()
        return f"From user {list_[0].capitalize()} successfully deleted e-mail."


def handler_replace_email(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        email = record.email.value
        record.delete_email()
        try:
            new_email = ' '.join(list_[1:])
            record.add_email(new_email)
            return f"For user {list_[0].capitalize()} e-mail successfully changed to:\n\t {new_email}"
        except:
            record.add_email(email)

def handler_add_note(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        new_note = ' '.join(list_[1:])
        record.add_note(new_note)
        return f"To user {list_[0].capitalize()} successfully added note:\n\t {new_note}"

def handler_delete_note(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        record.delete_note()
        return f"From user {list_[0].capitalize()} successfully deleted note."

def handler_replace_note(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        note = record.notes.value
        record.delete_note()
        try:
            new_note = ' '.join(list_[1:])
            record.add_note(new_note)
            return f"For user {list_[0].capitalize()} note successfully changed to:\n\t {new_note}"
        except:
            record.add_note(note)

def handler_add_addr(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        new_addr = ' '.join(list_[1:])
        record.add_address(new_addr)
        return f"To user {list_[0].capitalize()} successfully added address:\n\t {new_addr}"

def handler_delete_addr(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        record.delete_address()
        return f"From user {list_[0].capitalize()} successfully deleted address."

def handler_replace_addr(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        addr = record.address.value
        record.delete_address()
        try:
            new_addr = ' '.join(list_[1:])
            record.add_address(new_addr)
            return f"For user {list_[0].capitalize()} address successfully changed to:\n\t {new_addr}"
        except:
            record.add_address(addr)

def handler_show_all(my_book, _ = None):
    return my_book

def handler_exit(my_book, _ = None):
    return "Good bye!"

def handler_find(my_book, list_):
    list_rec = my_book.find_records(list_[0].capitalize())
    # list_rec = my_book.finde_records(list_[0].capitalize())
    if len(list_rec) != 0:
        ret_book = book.AddressBook()
        ret_book.qua_for_iter = my_book.qua_for_iter
        for rec_ in list_rec:
            ret_book.add_record(rec_)
        return ret_book
    else:
        return "Contact not found"
    
def handler_delete_phone(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    record.remove_phone(list_[1])
    return f"Phone {list_[1]} of user {list_[0].capitalize()} successfully deleted"

def handler_delete_user(my_book, list_):
    print(list_[0].capitalize())
    my_book.delete(list_[0].capitalize())
    return f"User {list_[0].capitalize()} successfully deleted"

def handler_next_birthday(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    days = record.days_to_birthday()
    return f"Next birthday for user {list_[0].capitalize()} after {days} days"

#Coded by Illia

#Додавання нотатки
# Not working
def handler_add_note(my_book, list_):
    #my_book.exists_tag(list_[2])
    try:
        record = my_book.find(list_[0].capitalize())
    except:
        record = notebook.Record(list_[0].capitalize(),list_[1])

    record.add_tag(list_[2])
    my_book.add_record(record)
    return "Command successfully complete"

#Змінення тексту нотаток
def handler_change_note(my_book, list_):
    print(list_[0].capitalize())
    record = my_book.find(list_[0].capitalize())
    print(record)
    if record is not None:
        record.edit_text(list_[1])
    return f"Text from note {list_[0].capitalize()} successfully changed"

#Пошук нотаток
def handler_find_note(my_book, list_):
    list_rec = my_book.find_records(list_[0].capitalize())
    if len(list_rec) != 0:
        ret_book = notebook.NoteBook()
        for rec_ in list_rec:
            ret_book.add_record(rec_)
        return ret_book
    else:
        return "Note not found"
    
#Пошук нотаток за тегом
def handler_find_note_by_tag(my_book, list_):
    list_rec = my_book.find_records(list_[0].lower())
    if len(list_rec) != 0:
        ret_book = notebook.NoteBook()
        for rec_ in list_rec:
            ret_book.add_record(rec_)
        return ret_book
    else:
        return "Note not found"

#Видалення тегу
def handler_delete_tag(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    record.remove_tag(list_[1].lower())
    return f"Tag {list_[1]} of note {list_[0].capitalize()} successfully deleted"

#Додавання тегу
def handler_add_tag(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    record.add_tag(list_[1])
    return f"Tag {list_[1]} of note {list_[0].capitalize()} successfully added"

#Видалення нотатки
def handler_delete_note(my_book, list_):
    print(list_[0].capitalize())
    my_book.delete(list_[0].capitalize())
    return f"Note {list_[0].capitalize()} successfully deleted"

#Показати всі нотатки
def handler_show_all_notes(my_book, _=None):
    return my_book

#Вибір режиму (телефонна книга або нотатки)
def mode_change(my_book = None, _ = None):
    i = True
    while i:
        mode = input("Please choose mode\n 1. Address book\n 2. Notes\n ")
        if(mode == "1"):
            return mode
        if(mode == "2"):
            return mode
        else:
            print("Wrong number!")


def handler_help(my_book = None, _ = None):
    help_list = [
        ['help', 'for help'],
        ['hello', 'for hello'],
        ['add <name> <phone> [birthday]',
        'for add user, if user is exist will be added\n'
        'variation format for telefon number:\n'
        '+38(055)111-22-33\n'
        '38(055)111-22-34\n'
        '8(055)111-22-35\n'
        '(055)111-22-36\n'
        '055111-22-37\n'
        'and all variant without "-"'],
        ['change <name> <from_phone> <to_phone>', 'for chandge phone'],
        ['show all', 'for show all records'],
        ['find <some_letters> | find <some_nombers>', 'for find record by name or phone'],
        ['delete phone <user> <phone>', 'for delete phone from user'],
        ['delete user <user>', 'for delete user from address book'],
        ['email add <name> <email_text>', 'to add e-mail to user'],
        ['email delete <name>', 'to delete e-mail from user'],
        ['email replace <name> <new_email>', 'to replace existing e-mail with new text'],
        ['good bye | close | exit', 'for exit'],
        ['note add <name> <note_text>',
            'to add note to user (max.240 printable characters)'],
        ['note delete <name>', 'to delete note from user'],
        ['note replace <name> <note_text>', 'to replace existing note at user with new text'],
        ['address add <name> <address_text>', 'to add address to user (max.100 printable characters)'],
        ['address delete <name>', 'to delete address from user'],
        ['address replace <name> <new_address>', 'to replace existing address at user with new text']
    ]

    pretty.table(
        title='List of commands with format',
        header=['Command', 'Description'],
        rows=help_list
    )

NAME_COMMANDS = {

    "help": handler_help,
    "hello": handler_hello,
    "add": handler_add,
    "change": handler_change,
    "showall": handler_show_all,
    "goodbye": handler_exit,
    "close": handler_exit,
    "exit": handler_exit,
    "find": handler_find,
    "deletephone": handler_delete_phone,
    "deleteuser": handler_delete_user,
    "nextbirthday": handler_next_birthday,

    "add-note": handler_add_note,
    "change-note": handler_change_note,
    "show-all-notes": handler_show_all_notes,
    "find-note": handler_find_note,
    "find-note-by-tag": handler_find_note_by_tag,
    "delete-note-tag": handler_delete_tag,
    "add-note-tag":handler_add_tag,
    "delete-note": handler_delete_note,

    "emailadd": handler_add_email,
    "emaildelete": handler_delete_email,
    "emailreplace": handler_replace_email,
    "noteadd": handler_add_note,
    "notedelete": handler_delete_note,
    "notereplace": handler_replace_note,
    "addressadd": handler_add_addr,
    "addressdelete": handler_delete_addr,
    "addressreplace": handler_replace_addr

}


def defs_commands(comm):
    return NAME_COMMANDS[comm]


@input_error
def parser_command(my_book, command):
    list_command = command.split(" ")
    # list_command = command
    if list_command[0] in NAME_COMMANDS:
        any_command = defs_commands(list_command[0])
        ret_rezault = any_command(my_book, list_command[1:])
        return ret_rezault
    elif len(list_command) > 1 and list_command[0]+list_command[1] in NAME_COMMANDS:
        any_command = defs_commands(list_command[0]+list_command[1])
        ret_rezault = any_command(my_book, list_command[2:])
        return ret_rezault
    else:
        any_command = defs_commands()
        return ret_rezault


def main():
    handler_help()
    file_name_phones_p = "bot_helper\\book_pickle.bin"
    # file_name_j = "bot_helper\\book_json.json"
    # file_name_j = Path("E:\pyton_proj\Go-IT\\bot_helper\\bot_helper\\book_json.json")
    my_book_phones_p = book.AddressBook()
    # my_book_j = book.AddressBook()
    my_book_phones = my_book_phones_p.load_from_file_pickle(file_name_phones_p)
    # my_book = my_book_j.load_from_file_json(file_name_j)

    #Файл для Notes
    file_name_notes_p = "bot_helper\\notes_book_pickle.bin"
    my_book_notes_p = notebook.NoteBook()
    my_book_notes = my_book_notes_p.load_from_file_pickle(file_name_notes_p)
    
    while True:

        #Вибір режиму (телефонна книга або нотатки)
        mode = mode_change()
        command = input("please enter command ").lower()
        if (mode == "1"):
            command = get_command_suggestions("mode")
            ret_rezault = parser_command(my_book_phones, command)
        elif (mode == "2"):
            command = get_command_suggestions("mode")
            ret_rezault = parser_command(my_book_notes, command)

        
        ret_rezault = parser_command(my_book, command)

        if ret_rezault:
            # print_result(ret_rezault)
            pretty.parser(ret_rezault)
            # ret_result = get_user_info()
                
                
            if ret_rezault == "Good bye!":
                my_book_phones.save_to_file_pickle(file_name_phones_p)
                my_book_notes.save_to_file_pickle(file_name_notes_p)
                # my_book.save_to_file_json(file_name_j)
                exit()

        
if __name__ == "__main__":
    main()