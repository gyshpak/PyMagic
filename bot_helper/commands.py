from prompt_toolkit import prompt
# from termcolor import colored, cprint
from prompt_toolkit.completion import WordCompleter
# from main import handler_help, handler_hello, handler_add, handler_change, handler_show_all, handler_exit, handler_find, handler_delete_phone, handler_delete_user, handler_next_birthday, handler_add_note, handler_change_note, handler_show_all_notes, handler_find_note, handler_delete_tag, handler_delete_note, mode_change
# import address_book as book
# from rich.table import Table
# from rich.prompt import Prompt
# from rich.console import Console

NAME_COMMANDS = [
    "help",
    "hello",
    "add",
    "change",
    "show-all",
    "goodbye",
    "close",
    "exit",
    "find",
    "delete-telephone",
    "delete-user",
    "next-birthday",
    "finde-birthday",
    "address-replace",
    "address-delete",
    "address-add",
    "email-replace",
    "email-delete",
    "email-add",
    "memo-add",
    "memo-delete",
    "memo-replace",
]

# 13 add, show, back, change, good bye, close, exit, find, next-birthday, delete-telephone, delete-user, help, hello

NAME_COMMANDS_NOTES = [
    "help",
    "hello",
    "goodbye",
    "close",
    "exit",
    "back",
    "add-note",
    "add-note-tag",
    "change-note",
    "show-all-notes",
    "find-note",
    "find-note-by-tag",
    "delete-note-tag",
    "delete-note",
    
]

# add, show, change, goodbye, find, back, delete (x2), next-birthday, add-note, change-note, show-all-notes, find-note, delete-note-tag, delete-note

# def pretty_table(title=None, title_style=None, header=[], header_style='bold blue', rows=[], row_style='bright_green'): 
         
#         table = Table() 
#         if title: 
#             table.title = title 
#             table.title_style = title_style 
#             table.title_justify = 'left' 
         
#         longest_row = max([len(row) for row in rows]) if rows else 0
#         if len(header) < longest_row: 
#             for i in range(longest_row - len(header)): 
#                 header.append(f'Column_{i}') 
         
#         for column in header: 
#             table.add_column(column, header_style=header_style) 
 
#         for row in rows: 
#             table.add_row(*row, style=row_style) 
         
#         table.show_lines = True 
 
#         Console().print(table)

# def print_result(result_1):
#     rows = []

#     for record in result_1:
#         if hasattr(record, 'name') and hasattr(record, 'phones') and hasattr(record, 'birthday'):
#             name = record.name.value()
#             phones = ', '.join(p.value for p in record.phones)
#             email = ''
#             birthday = date.strftime(record.birthday.value, '%d.%m.%Y') if hasattr(record, "birthday") else ''
#             rows.append([name, phones, email, birthday])
            
#     pretty_table(
#         title='List of commands with format',
#         header=['Name', 'Telephone', 'Address', 'Email', 'Birthday', 'Notes'],
#         rows=rows
#     )

def get_command_suggestions(prefix, mode):
    try:
        if mode == "1":
            command_list = NAME_COMMANDS
        elif mode == "2": 
            command_list = NAME_COMMANDS_NOTES
        else:
            print('COMMANDS.PY')
            
        suggestions = [cmd for cmd in command_list if prefix.lower() in cmd.lower()]
        formatted_suggestions = "\n".join(f"{' ' * 60}| {cmd} |" for cmd in suggestions)
        
        user_input = prompt(f"Please enter your command: ", completer=WordCompleter(suggestions, ignore_case=True))
        
        if user_input == "add":
            command = user_input
            name = input("User name: ")
            number = input("Enter phone number: ")
            birthday = input("Enter birthday: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            notes = input("Enter notes: ")
            user_input_list = [command, name, number, birthday, email, address, notes]
            # print(user_input_list)
            return user_input_list
        elif user_input == "add-note":
            command = user_input
            titleNote = input("Note for title: ")
            textNote = input("Write some text: ")
            tagNote = input("Write some tag: ")
            user_input_list = [command, titleNote, textNote, tagNote]
            # print(user_input_list)
            return user_input_list
        elif user_input == "add-note-tag":
            command = user_input
            title = input("Note for title: ")
            tag = input("Write some text: ")
            user_input_list = [command, title, tag]
            # print(user_input_list)
            return user_input_list
        elif user_input == "show-all":
            command = user_input
            user_input_list = [command]
            return user_input_list
        elif user_input == "show-all-notes":
            command = user_input
            user_input_list = [command]
            return user_input_list
        elif user_input == "back":
            command = user_input
            user_input_list = [command]
            return user_input_list
        elif user_input == "change":
            command = user_input
            name = input("User name: ")
            old_phone_number = input("Old phone number: ")
            new_phone_number = input("New phone number: ")
            user_input_list = [command, name, old_phone_number, new_phone_number]
            # print(user_input_list)
            return user_input_list
        elif user_input == "change-note":
            command = user_input
            titleOld = input("Title of note: ")
            titleNew = input("New title of note: ")
            user_input_list = [command, titleOld, titleNew]
            # print(user_input_list)
            return user_input_list
        elif user_input == "goodbye" or user_input == "close" or user_input == "exit":
            return [user_input]
        elif user_input == "find":
            command = user_input
            letter = input("Give me a letter: ")
            user_input_list = [command, letter]
            return user_input_list
        elif user_input == "find-note":
            command = user_input
            letter = input("Give me a letter: ")
            user_input_list = [command, letter]
            return user_input_list
        elif user_input == "find-note-by-tag":
            command = user_input
            letterTag = input("Give me a letter of tag: ")
            user_input_list = [command, letterTag]
            return user_input_list
        elif user_input == "find-note-by-tag":
            command = user_input
            letterTag = input("Give me a letter of tag: ")
            user_input_list = [command, letterTag]
            return user_input_list
        elif user_input == "next-birthday":
            command = user_input
            nextBirthday = input("Give me Name: ")
            user_input_list = [command, nextBirthday]
            return user_input_list
        elif user_input == "finde-birthday":
            command = user_input
            findebirthday = input("Give me quantity days: ")
            user_input_list = [command, findebirthday]
            return user_input_list
        elif user_input == "delete-telephone":
            command = user_input
            nameUser = input("Give me a user name: ")
            phoneNumber = input("Give me a phone number: ")
            user_input_list = [command, nameUser, phoneNumber]
            return user_input_list
        elif user_input == "delete-note-tag":
            command = user_input
            nameOfNote = input("Give me a title of note: ")
            nameOfTag = input("Give me a tag of note: ")
            user_input_list = [command, nameOfNote, nameOfTag]
            return user_input_list
        elif user_input == "delete-user":
            command = user_input
            userName = input("Give me a user name: ")
            user_input_list = [command, userName]
            return user_input_list
        elif user_input == "delete-note":
            command = user_input
            nameOfNote = input("Give me a name of note: ")
            user_input_list = [command, nameOfNote]
            return user_input_list
        elif user_input == "help":
            command = user_input
            user_input_list = [command]
            return user_input_list
        elif user_input == "hello":
            command = user_input
            user_input_list = [command]
            return user_input_list
        elif user_input == "email-add":
            command = user_input
            nameOfEmail = input("Write name of email: ")
            textOfEmail = input("Write text for email: ")
            user_input_list = [command, nameOfEmail, textOfEmail]
            return user_input_list
        elif user_input == "email-delete":
            command = user_input
            deleteEmail = input("Write name of email for delete: ")
            user_input_list = [command, deleteEmail]
            return user_input_list
        elif user_input == "email-replace":
            command = user_input
            nameReplaceEmail = input("Write name of email: ")
            newNameForEmail = input("Write new name of email: ")
            user_input_list = [command, nameReplaceEmail, newNameForEmail]
            return user_input_list
        elif user_input == "memo-add":
            command = user_input
            nameOfNote = input("Write name of memo: ")
            textOfNote = input("Write text for memo: ")
            user_input_list = [command, nameOfNote, textOfNote]
            return user_input_list
        elif user_input == "memo-delete":
            command = user_input
            deleteNote = input("Write name of memo for delete: ")
            user_input_list = [command, deleteNote]
            return user_input_list
        elif user_input == "memo-replace":
            command = user_input
            nameReplaceNote = input("Write name of memo: ")
            textForNote = input("Write new text for memo: ")
            user_input_list = [command, nameReplaceNote, textForNote]
            return user_input_list
        elif user_input == "address-add":
            command = user_input
            nameOfAddress = input("Write name of address: ")
            textForAddress = input("Write an address: ")
            user_input_list = [command, nameOfAddress, textForAddress]
            return user_input_list
        elif user_input == "address-delete":
            command = user_input
            deleteAddress = input("Write name of address for delete: ")
            user_input_list = [command, deleteAddress]
            return user_input_list
        elif user_input == "address-replace":
            command = user_input
            nameReplaceAddress = input("Write name of address: ")
            textForAddress = input("Write new address: ")
            user_input_list = [command, nameReplaceAddress, textForAddress]
            return user_input_list
        
        return user_input.lower()
    except KeyboardInterrupt:
        print("\nCommand input interrupted. Exiting...")
        exit()