from prompt_toolkit import prompt
from termcolor import colored, cprint
from prompt_toolkit.completion import WordCompleter
from main import handler_help, handler_hello, handler_add, handler_change, handler_show_all, handler_exit, handler_find, handler_delete_phone, handler_delete_user, handler_next_birthday, handler_add_note, handler_change_note, handler_show_all_notes, handler_find_note, handler_delete_tag, handler_delete_note, mode_change
import address_book as book

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
    "back": mode_change,
}

NAME_COMMANDS_NOTES = {
    "help": handler_help,
    "hello": handler_hello,
    "goodbye": handler_exit,
    "close": handler_exit,
    "exit": handler_exit,
    "back": mode_change,
    "add-note": handler_add_note,
    "change-note": handler_change_note,
    "show-all-notes": handler_show_all_notes,
    "find-note": handler_find_note,
    "delete-note-tag": handler_delete_tag,
    "delete-note": handler_delete_note,
}

def get_command_suggestions(prefix, mode):
    try:
        if mode == "1":
            command_list = NAME_COMMANDS
        elif mode == "2": 
            command_list = NAME_COMMANDS_NOTES
        else:
            print('COMMANDS.PY')
            
        suggestions = [cmd for cmd in command_list.keys() if prefix.lower() in cmd.lower()]
        formatted_suggestions = "\n".join(f"{' ' * 60}| {cmd} |" for cmd in suggestions)
        user_input = prompt(f"Please enter your command: ", completer=WordCompleter(suggestions, ignore_case=True))
        return user_input.lower()
    except KeyboardInterrupt:
        print("\nCommand input interrupted. Exiting...")
        exit()