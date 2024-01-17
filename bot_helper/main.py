import bot_helper.address_book as book
import bot_helper.note_book as notebook
import bot_helper.pretty as pretty
from bot_helper.clean import sorting_files
from bot_helper.commands import *
import os

# from . import address_book as book
# from . import note_book as notebook
# from . import pretty
# from .clean import sorting_files
# from .commands import *


# import address_book as book
# import note_book as notebook
# import pretty
# from clean import sorting_files
# from commands import *



def input_error(func):
    def inner(my_book, val):
        try:
            return_data = func(my_book, val)
        except IndexError:
            return_data = ("Give me name please", )   #and phone please", )
        except TypeError:
            return_data = ("Wrong command, try again", )
        except KeyError:
            return_data = ("Wrong user, repeat please", )
        except ValueError:
            return_data = ("Wrong number, repeat please", )
        except book.WrongBirthday:
            return_data = ("Wrong birthday, repeat please", )
        except book.ExistsPhone:
            return_data = ("Phone is exist", )
        except book.ExistsMemo:
            return_data = ("User already has a memo", )
        except book.WrongMemo:
            return_data = ("Not printable characters in Memo or record size excides.", )
        except book.ExistsAddress:
            return_data = ("User already has an address", )
        except book.WrongAddress:
            return_data = ("Not printable characters in Address or record size excides.", )
        except book.WrongEmail:
            return_data = ("Wrong e-mail, repeat please", )
        except book.ExistsEmail:
            return_data = ("User already has an e-mail", )
        return return_data
    return inner


def handler_hello(my_book, _ = None):
    return "How can I help you?"

def handler_add(my_book, list_):
    if list_[0] == "":
        raise IndexError
    my_book.exists_phone(list_[1])
    try:
        record = my_book.find(list_[0].capitalize())
    except:
        # if list_[2] != '':
        #     record = book.Record(list_[0].capitalize(),list_[2])
        # else:
        #     record = book.Record(list_[0].capitalize())
        record = book.Record(list_[0].capitalize())
    else:
        my_book.add_record(record)
    finally:
        if list_[1] != "":
            record.add_phone(list_[1])
        if list_[2] != "":
            record.add_birthday(list_[2])
        if list_[3] != "":
            record.add_email(list_[3])
        if list_[4] != "":
            record.add_address(list_[4])
        if list_[5] != "":
            record.add_memo(list_[5])
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
        email = record.emails.value
        record.delete_email()
        try:
            new_email = ' '.join(list_[1:])
            record.add_email(new_email)
            return f"For user {list_[0].capitalize()} e-mail successfully changed to:\n\t {new_email}"
        except:
            record.add_email(email)

def handler_add_memo(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        new_memo = ' '.join(list_[1:])
        record.add_memo(new_memo)
        return f"To user {list_[0].capitalize()} successfully added memo:\n\t {new_memo}"

def handler_delete_memo(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        record.delete_memo()
        return f"From user {list_[0].capitalize()} successfully deleted memo."

def handler_replace_memo(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    if record is not None:
        if record.memos is not None:
            memo = record.memos.value
            record.delete_memo()
            try:
                new_memo = ' '.join(list_[1:])
                record.add_memo(new_memo)
                return f"For user {list_[0].capitalize()} memo successfully changed to:\n\t {new_memo}"
            except:
                record.add_memo(memo)
        else:
            return handler_add_memo(my_book, list_)

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
        if record.address is not None:
            addr = record.address.value
            record.delete_address()
            try:
                new_addr = ' '.join(list_[1:])
                record.add_address(new_addr)
                return f"For user {list_[0].capitalize()} address successfully changed to:\n\t {new_addr}"
            except:
                record.add_address(addr)
        else:
            return handler_add_addr(my_book, list_)

def handler_show_all(my_book, _ = None):
    return my_book

def handler_exit(my_book, _ = None):
    return "Good bye!"

def handler_find(my_book, list_):
    list_rec = my_book.find_records(list_[0].capitalize())
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
    my_book.delete(list_[0].capitalize())
    return f"User {list_[0].capitalize()} successfully deleted"

def handler_next_birthday(my_book, list_):
    record = my_book.find(list_[0].capitalize())
    days = record.days_to_birthday()
    return f"Next birthday for user {list_[0].capitalize()} after {days} days"

#Coded by Illia

#Додавання нотатки
def handler_add_note(my_book, list_):
    try:
        record = my_book.find(list_[0].capitalize())
    except:
        record = notebook.Record(list_[0].capitalize(),list_[1])

    record.add_tag(list_[2])
    my_book.add_record(record)
    return "Command successfully complete"

#Змінення тексту нотаток
def handler_change_note(my_book, list_):
    record = my_book.find(list_[0].capitalize())
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
    list_rec = my_book.find_records_by_tag(list_[0].lower())
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
    my_book.delete(list_[0].capitalize())
    return f"Note {list_[0].capitalize()} successfully deleted"

#Показати всі нотатки
def handler_show_all_notes(my_book, _=None):
    return my_book

#Вибір режиму (телефонна книга або нотатки)
def mode_change(my_book = None, _ = None):
    i = True
    while i:
        mode = input("Please choose mode\n 1. Address book\n 2. Notes\n 3. Sort folder\n")
        if mode == "1" or mode == "2" or mode == "3":
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
        ['memo-add <name> <note_text>',
            'to add note to user (max.240 printable characters)'],
        ['memo-delete <name>', 'to delete note from user'],
        ['memo-replace <name> <note_text>', 'to replace existing note at user with new text'],
        ['address-add <name> <address_text>', 'to add address to user (max.100 printable characters)'],
        ['address-delete <name>', 'to delete address from user'],
        ['address-replace <name> <new_address>', 'to replace existing address at user with new text'],
        ['add-note <title> <text> [tag]',' to add note'],
        ['change-note <title> <new_text>',' to change text in note by title'],
        ['show-all-notes',' to show all notes'],
        ['find-note <some_text>',' to find notes by <some_text> in title of note'],
        ['find-note-by-tag <some_text>',' to find notes by <some_text> in tags of note'],
        ['delete-note-tag <title> <tag>',' to delete tag <tag> in note <title>'],
        ['add-note-tag <title> <tag>',' to add tag <tag> in note <title>'],
        ['delete-note <title>',' to delete note by <title>']
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
    "show-all": handler_show_all,
    "goodbye": handler_exit,
    "close": handler_exit,
    "exit": handler_exit,
    "find": handler_find,
    "delete-telephone": handler_delete_phone,
    "delete-user": handler_delete_user,
    "next-birthday": handler_next_birthday,
    "sort-folder" : sorting_files,

    "add-note": handler_add_note,
    "change-note": handler_change_note,
    "show-all-notes": handler_show_all_notes,
    "find-note": handler_find_note,
    "find-note-by-tag": handler_find_note_by_tag,
    "delete-note-tag": handler_delete_tag,
    "add-note-tag":handler_add_tag,
    "delete-note": handler_delete_note,
    "email-add": handler_add_email,
    "email-delete": handler_delete_email,
    "email-replace": handler_replace_email,
    
    "memo-add": handler_add_memo,
    "memo-delete": handler_delete_memo,
    "memo-replace": handler_replace_memo,
    "address-add": handler_add_addr,
    "address-delete": handler_delete_addr,
    "address-replace": handler_replace_addr

}


def defs_commands(comm):
    return NAME_COMMANDS[comm]


@input_error
def parser_command(my_book, command):
    list_command = command
    if list_command[0] in NAME_COMMANDS:
        any_command = defs_commands(list_command[0])
        ret_rezault = any_command(my_book, list_command[1:])
        return ret_rezault
    else:
        any_command = defs_commands()
        return ret_rezault


current_path = os.path.abspath(os.getcwd())
file_name_phones_p = os.path.join(current_path, 'bot_helper', 'book_pickle.bin')
file_name_notes_p = os.path.join(current_path, 'bot_helper', 'notes_book_pickle.bin')



def main():
    # handler_help()
    # file_name_phones_p = "E:\\GitHub\\PyMagic\\bot_helper\\book_pickle.bin"
    # file_name_phones_p = "bot_helper\\book_pickle.bin"
    if os.path.exists(file_name_phones_p):
        my_book_phones_p = book.AddressBook()
        my_book_phones = my_book_phones_p.load_from_file_pickle(file_name_phones_p)
    else:
        my_book_phones = book.AddressBook()

    # file_name_notes_p = "E:\\GitHub\\PyMagic\\bot_helper\\notes_book_pickle.bin"
    # file_name_notes_p = "bot_helper\\notes_book_pickle.bin"
    if os.path.exists(file_name_notes_p):
        my_book_notes_p = notebook.NoteBook()
        my_book_notes = my_book_notes_p.load_from_file_pickle(file_name_notes_p)
    else:
        my_book_notes = notebook.NoteBook()
    
    while True:
        # #Вибір режиму (телефонна книга або нотатки)
        mode = mode_change()
        if mode == "1":
            command = get_command_suggestions("", mode)
            ret_rezault = parser_command(my_book_phones, command)
        elif mode == "2":
            command = get_command_suggestions("", mode)
            ret_rezault = parser_command(my_book_notes, command)
        elif mode == "3":
            command = ["sort-folder"]
            command.append(input("Please enter path for folder for sorting "))
            ret_rezault = parser_command(my_book_notes, command)
        if ret_rezault:
            pretty.parser(ret_rezault, mode)
            if ret_rezault == "Good bye!":
                my_book_phones.save_to_file_pickle(file_name_phones_p)
                my_book_notes.save_to_file_pickle(file_name_notes_p)
                exit()
        
if __name__ == "__main__":
    main()