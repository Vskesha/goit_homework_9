"""
This is a simple console bot for managing phonebook
"""

from functools import wraps


PHONEBOOK = {}


def input_error(func):
    """Wrapper for handling errors"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except IndexError as e:
            print('Not enough data.', str(e))
        except ValueError as e:
            print('Wrong value.', str(e))
        except KeyError as e:
            print('Wrong key.', str(e)[1:-1])
        except TypeError as e:
            print('Wrong type of value.', str(e))
    return wrapper


def command_parser(user_input: str) -> tuple[callable, str]:
    """
    fetches and returns proper handler and argument of this handler
    from user_input accordingly to the COMMANDS
    :param user_input: str which must start with command followed by name and phone number if needed
    :return: tuple of function and str argument
    """
    if not user_input:
        raise IndexError("Nothing was entered ...")

    func, data = None, []
    lower_input_end_spaced = user_input.lower() + ' '
    for command in WORD_COMMANDS:
        if lower_input_end_spaced.startswith(command + ' '):
            func = WORD_COMMANDS[command]
            data = user_input[len(command) + 1:].strip()

    if not func:
        raise ValueError(f"There is no such command {user_input.split()[0]}")

    return func, data


def handle_add_number(user_input: str) -> str:
    """
    adds name and phone number from given 'user_input' to PHONEBOOK.
    :returns: str with the result of adding.
    :raises: errors if given 'user_input' has no relevant arguments
    """
    data = user_input.rsplit(maxsplit=1)
    if not data:
        raise IndexError("Give me name and phone please")
    if len(data) < 2:
        raise IndexError(f"Enter {'name' if data[0][-1].isdigit() else 'phone'} please.")
    if not data[1][-1].isdigit():
        raise TypeError(f"'{data[1]}' is not a phone number")
    name = data[0].title()
    if name in PHONEBOOK:
        raise KeyError(f"{name}'s phone number already exists in phonebook. "
                       f"Use '{COMMANDS[handle_change_number][0]}' command to replace phone number.")
    phone = data[1]
    PHONEBOOK[name] = phone
    return f"{name}'s phone {phone} was added to phonebook"


def handle_change_number(user_input: str) -> str:
    """
    changes in PHONEBOOK phone number of given in 'user_input' name.
    :returns: str with the result of changing.
    :raises: errors if given 'user_input' has no relevant arguments
    """
    data = user_input.rsplit(maxsplit=1)
    if not data:
        raise IndexError("Give me name and phone please")
    if len(data) < 2:
        raise IndexError(f"Enter {'name' if data[0][-1].isdigit() else 'phone'} please.")
    if not data[1][-1].isdigit():
        raise TypeError(f'"{data[1]}" is not a phone number')

    name = data[0].title()

    if name not in PHONEBOOK:
        raise KeyError(f"There is no any number for name '{name}'. "
                       f"Use '{COMMANDS[handle_add_number][0]}' command to save new number")

    phone = data[1]
    PHONEBOOK[name] = phone

    return f"{name}'s phone was changed to {phone} in phonebook"


def handle_delete_number(name: str) -> str:
    """
    removes phone number of given 'name' from PHONEBOOK.
    :returns: str with the result of deleting.
    :raises: errors if given 'user_input' has no relevant arguments
    """
    name = name.title()
    if not name:
        raise IndexError("Give me name please")

    if name not in PHONEBOOK:
        raise KeyError(f"There is no any number for name '{name}'")

    del PHONEBOOK[name]
    return f"{name}'s number was deleted"


def handle_exit(user_input: str) -> str:
    """
    Saves all phone numbers fromPHONEBOOK to file 'phonebook.txt' in current directory and finishes the program
    :returns: str with the result of saving and 'Goodbye!'.
    """
    msg = handle_save_to_file(user_input)
    return f'{msg}\nGoodbye!'


def handle_greet(user_input: str) -> str:
    """
    returns greeting for user ;)
    """
    return 'How can I help you?'


def handle_save_to_file(user_input: str) -> str:
    """
    Saves all phone numbers from PHONEBOOK to file 'phonebook.txt' in current directory.
    """
    with open('phonebook.txt', 'w') as fh:
        for name, number in PHONEBOOK.items():
            fh.write(f'{name}: {number}\n')
    return "All phone numbers was saved in 'phonebook.txt'"


def handle_show_all_numbers(user_input: str) -> str:
    """
    returns string with all phone numbers in PHONEBOOK.
    """
    if PHONEBOOK:
        return '\n'.join(f'{name}: {phone}' for name, phone in PHONEBOOK.items())
    else:
        return 'Phonebook is empty'


def handle_show_number(name: str) -> str:
    """
    returns string with the phone number of given user's name from PHONEBOOK.
    :raises: errors if given 'data' has no relevant arguments
    """
    name = name.title()
    if not name:
        raise IndexError("Give me name please")

    if name not in PHONEBOOK:
        raise KeyError(f"There is no any number for name '{name}'")

    return PHONEBOOK[name]


def load_phones() -> str:
    """
    writes phone numbers from file 'phonebook.txt' (if exists) to PHONEBOOK
    """
    try:
        with open('phonebook.txt', 'r') as fh:
            while True:
                line = fh.readline()
                if not line:
                    break
                name, number = line.strip().rsplit(': ', maxsplit=1)
                PHONEBOOK[name] = number
        return "Hi! Your phonebook successfully loaded from 'phonebook.txt'."
    except FileNotFoundError:
        return "Hi! Your phonebook is empty so far!"


@input_error
def main() -> bool:
    """
    return True if it needs to stop program. False otherwise.
    """
    user_input = input('>>> ')
    func, argument = command_parser(user_input)
    result = func(argument)
    print(result)
    return result.endswith('Goodbye!')


def prepare() -> None:
    """
    prints instructions to user.
    """
    print(load_phones())
    separator = '--------------------|-------------------------------------'
    print(separator, '\n       Action       |     Commands\n', separator, sep='')
    for func, commands in COMMANDS.items():  # generic way when we add new action
        print(f"{func.__name__[7:]:_<20}|_ {' / '.join(commands):_<35}")
    print(separator)
    print(f"Enter one of the listed commands followed by name and phone number if needed\n"
          f"'command' ['name' ['phone number']]. Values must be separated with space.\n")


COMMANDS = {
    handle_add_number: ['add', 'plus', 'create', '+'],
    handle_change_number: ['change', 'modify', 'replace'],
    handle_delete_number: ['delete', 'remove', 'del'],
    handle_exit: ['goodbye', 'close', 'exit', 'bye'],
    handle_greet: ['hello', 'hi'],
    handle_show_number: ['phone', 'get'],
    handle_show_all_numbers: ['show all', 'all'],
    handle_save_to_file: ['save', 'save all', 'write'],
}
WORD_COMMANDS = {command: func for func, commands in COMMANDS.items() for command in commands}

if __name__ == '__main__':
    prepare()
    while True:
        if main():
            break
