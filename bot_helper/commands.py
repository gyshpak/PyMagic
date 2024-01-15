from prompt_toolkit import prompt
from termcolor import colored, cprint
from prompt_toolkit.completion import WordCompleter
# from main import handler_help, handler_hello, handler_add, handler_change, handler_show_all, handler_exit, handler_find, handler_delete_phone, handler_delete_user, handler_next_birthday, handler_add_note, handler_change_note, handler_show_all_notes, handler_find_note, handler_delete_tag, handler_delete_note, mode_change
import address_book as book
from rich.table import Table
from rich.prompt import Prompt
from rich.console import Console

# NAME_COMMANDS = {
#     "help": handler_help,
#     "hello": handler_hello,
#     "add": handler_add,
#     "change": handler_change,
#     "show-all": handler_show_all,
#     "goodbye": handler_exit,
#     "close": handler_exit,
#     "exit": handler_exit,
#     "find": handler_find,
#     "delete-telephone": handler_delete_phone,
#     "delete-user": handler_delete_user,
#     "next-birthday": handler_next_birthday,
#     "back": mode_change,
# }

# NAME_COMMANDS_NOTES = {
#     "help": handler_help,
#     "hello": handler_hello,
#     "goodbye": handler_exit,
#     "close": handler_exit,
#     "exit": handler_exit,
#     "back": mode_change,
#     "add-note": handler_add_note,
#     "change-note": handler_change_note,
#     "show-all-notes": handler_show_all_notes,
#     "find-note": handler_find_note,
#     "delete-note-tag": handler_delete_tag,
#     "delete-note": handler_delete_note,
# }

# def get_command_suggestions(prefix, mode):
#     try:
#         if mode == "1":
#             command_list = NAME_COMMANDS
#         elif mode == "2": 
#             command_list = NAME_COMMANDS_NOTES
#         else:
#             print('COMMANDS.PY')
            
#         # suggestions = [cmd for cmd in command_list.keys() if prefix.lower() in cmd.lower()]
#         # formatted_suggestions = "\n".join(f"{' ' * 60}| {cmd} |" for cmd in suggestions)
#         # user_input = prompt(f"Please enter your command: ", completer=WordCompleter(suggestions, ignore_case=True))
#         # return user_input.lower()
#         suggestions = [cmd for cmd in command_list.keys() if prefix.lower() in cmd.lower()]
#         formatted_suggestions = "\n".join(f"{' ' * 60}| {cmd} |" for cmd in suggestions)
#         user_input = prompt(f"Please enter your command: ", completer=WordCompleter(suggestions, ignore_case=True, splitter=None))
#         return user_input.lower()
#     except KeyboardInterrupt:
#         print("\nCommand input interrupted. Exiting...")
#         exit()


NAME_COMMANDS = {
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
    "back",
}

# 13 add, show, back, change, good bye, close, exit, find, next-birthday, delete-telephone, delete-user, help, hello

NAME_COMMANDS_NOTES = {
    "help",
    "hello",
    "goodbye",
    "close",
    "exit",
    "back",
    "add-note",
    "change-note",
    "show-all-notes",
    "find-note",
    "delete-note-tag",
    "delete-note",
}

# 13 add, show, back, change, good bye, close, exit, find, next-birthday, delete-telephone, delete-user
# 12 

# add, show, change, goodbye, find, back, delete (x2), next-birthday, add-note, change-note, show-all-notes, find-note, delete-note-tag, delete-note


def pretty_table(title=None, title_style=None, header=[], header_style='bold blue', rows=[], row_style='bright_green'): 
         
        table = Table() 
        if title: 
            table.title = title 
            table.title_style = title_style 
            table.title_justify = 'left' 
         
        longest_row = max([len(row) for row in rows]) if rows else 0
        if len(header) < longest_row: 
            for i in range(longest_row - len(header)): 
                header.append(f'Column_{i}') 
         
        for column in header: 
            table.add_column(column, header_style=header_style) 
 
        for row in rows: 
            table.add_row(*row, style=row_style) 
         
        table.show_lines = True 
 
        Console().print(table)


def print_result(result_1):
    rows = []

    for record in result_1:
        if hasattr(record, 'name') and hasattr(record, 'phones') and hasattr(record, 'birthday'):
            name = record.name.value()
            phones = ', '.join(p.value for p in record.phones)
            email = ''
            birthday = date.strftime(record.birthday.value, '%d.%m.%Y') if hasattr(record, "birthday") else ''
            rows.append([name, phones, email, birthday])
        # else:
        #     print(f"Unexpected record type: {record}")
        #     # Add an empty row for unexpected record types
        #     rows.append(["", "", "", ""])

    # Print the table even if there are unexpected record types
    pretty_table(
        title='List of commands with format',
        header=['Name', 'Telephone', 'Address', 'Email', 'Birthday', 'Notes'],
        rows=rows
    )

# , mode

def get_command_suggestions(prefix):
    try:
        # if mode == "1":
        #     command_list = NAME_COMMANDS
        # elif mode == "2": 
        #     command_list = NAME_COMMANDS_NOTES
        # else:
        #     print('COMMANDS.PY')
            
        # suggestions = [cmd for cmd in command_list.keys() if prefix.lower() in cmd.lower()]
        # formatted_suggestions = "\n".join(f"{' ' * 60}| {cmd} |" for cmd in suggestions)
        # user_input = prompt(f"Please enter your command: ", completer=WordCompleter(suggestions, ignore_case=True))
        # return user_input.lower()
        suggestions = [cmd for cmd in NAME_COMMANDS if prefix.lower() in cmd.lower()]
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
            print(user_input_list)
            return user_input_list
        elif user_input == "add-note":
            command = user_input
            name = input("User name: ")
            number = input("Enter number: ")
            birthday = input("Enter birthday: ")
            
            user_input_list = [command, name, number, birthday]
            print(user_input_list)
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
            print(user_input_list)
            return user_input_list
        elif user_input == "change-note":
            command = user_input
            name = input("User name: ")
            number = input("New phone number: ")
            
            user_input_list = [command, name, old_phone_number, new_phone_number]
            print(user_input_list)
            return user_input_list
        elif user_input == "show-all":
            command = user_input
            user_input_list = [command]
            return user_input_list
        elif user_input == "good bye" or user_input == "close" or user_input == "exit":
            exit()
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
        
        
        
        elif user_input == "next-birthday":
            command = user_input
            nextBirthday = input("Give me a date of next birthday: ")
            user_input_list = [command, nextBirthday]
            return user_input_list
        elif user_input == "delete-telephone":
            command = user_input
            phoneNumber = input("Give me a phone number: ")
            user_input_list = [command, phoneNumber]
            return user_input_list
        elif user_input == "delete-note-tag":
            command = user_input
            nameOfNote = input("Give me a name of note tag: ")
            user_input_list = [command, nameOfNote]
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
        
        
        
        return user_input.lower()
    except KeyboardInterrupt:
        print("\nCommand input interrupted. Exiting...")
        exit()
















# from prompt_toolkit import prompt
# from termcolor import colored, cprint
# from prompt_toolkit.completion import WordCompleter
# import address_book as book
# from rich.table import Table
# from rich.prompt import Prompt
# from rich.console import Console

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

# NAME_COMMANDS = {
#     "help",
#     "hello",
#     "add",
#     "change",
#     "show-all",
#     "goodbye",
#     "close",
#     "exit",
#     "find",
#     "delete-telephone",
#     "delete-user",
#     "next-birthday",
#     "back",
# }

# NAME_COMMANDS_NOTES = {
#     "help",
#     "hello",
#     "goodbye",
#     "close",
#     "exit",
#     "back",
#     "add-note",
#     "change-note",
#     "show-all-notes",
#     "find-note",
#     "delete-note-tag",
#     "delete-note",
# }

# # , mode


# def get_command_suggestions(prefix):
#     try:
#         suggestions = [cmd for cmd in NAME_COMMANDS if prefix.lower() in cmd.replace('-', '').lower()]
#         formatted_suggestions = "\n".join(f"{' ' * 60}| {cmd} |" for cmd in suggestions)
        
#         user_input = prompt("Please enter your command: ", completer=WordCompleter(suggestions, ignore_case=True))

#         # Split the user input by spaces and filter out empty strings
#         user_input_list = list(filter(None, user_input.lower().replace('-', ' ').split()))

#         return user_input_list
#     except KeyboardInterrupt:
#         print("\nCommand input interrupted. Exiting...")
#         exit()

# # def print_return(result_1):
# #     if isinstance(result_1, str):
# #         print(result_1)
# #     elif isinstance(result_1, list):
# #         rows = []

# #         for record in result_1:
# #             if isinstance(record, Record):
# #                 name = record.name.value
# #                 phones = ', '.join(p.value for p in record.phones)
# #                 email = ''
# #                 birthday = date.strftime(record.birthday.value, '%d.%m.%Y') if hasattr(record, "birthday") else ''
# #                 rows.append([name, phones, email, birthday])
# #             else:
# #                 print(f"Invalid record object: {record}")

# #         pretty_table(
# #             title='List of commands with format',
# #             header=['Name', 'Telephone', 'Email', 'Birthday'],
# #             rows=rows
# #         )
# #     else:
# #         print("Unexpected result type:", type(result_1))

# #     return result_1


# # def print_result(result_1):
# #     rows = []

# #     for record in result_1:
# #         if hasattr(record, 'name') and hasattr(record, 'phones') and hasattr(record, 'birthday'):
# #             name = record.name.value()
# #             phones = ', '.join(p.value for p in record.phones)
# #             email = ''
# #             birthday = date.strftime(record.birthday.value, '%d.%m.%Y') if hasattr(record, "birthday") else ''
# #             rows.append([name, phones, email, birthday])
# #         else:
# #             print(f"Unexpected record type: {record}")

# #     pretty_table(
# #         title='List of commands with format',
# #         header=['Name', 'Telephone', 'Email', 'Birthday'],
# #         rows=rows
# #     )
# #     print(result_1)



# # def print_result(result_1):
# #     rows = []

# #     for record in result_1:
# #         # if hasattr(record, 'name') and hasattr(record, 'phones') and hasattr(record, 'birthday'):
# #             name = record.name.value()
# #             phones = ', '.join(p.value for p in record.phones)
# #             email = ''
# #             birthday = date.strftime(record.birthday.value, '%d.%m.%Y') if hasattr(record, "birthday") else ''
# #             rows.append([name, phones, email, birthday])
# #         # else:
# #         #     print(f"Unexpected record type: {record}")

# #     # Print the table even if there are unexpected record types
# #     pretty_table(
# #         title='List of commands with format',
# #         header=['Name', 'Telephone', 'Email', 'Birthday'],
# #         rows=rows
# #     )


# def print_result(result_1):
#     rows = []

#     for record in result_1:
#         if hasattr(record, 'name') and hasattr(record, 'phones') and hasattr(record, 'birthday'):
#             name = record.name.value()
#             phones = ', '.join(p.value for p in record.phones)
#             email = ''
#             birthday = date.strftime(record.birthday.value, '%d.%m.%Y') if hasattr(record, "birthday") else ''
#             rows.append([name, phones, email, birthday])
#         # else:
#         #     print(f"Unexpected record type: {record}")
#         #     # Add an empty row for unexpected record types
#         #     rows.append(["", "", "", ""])

#     # Print the table even if there are unexpected record types
#     pretty_table(
#         title='List of commands with format',
#         header=['Name', 'Telephone', 'Email', 'Birthday'],
#         rows=rows
#     )