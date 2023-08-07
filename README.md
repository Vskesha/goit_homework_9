# goit_homework_9

This is a simple console bot for managing phonebook

Program supports next commands (listed in COMMANDS in console_bot_helper.py):

| Action           | Commands                     |
|:-----------------|:-----------------------------|
| add_number       | add / plus / create / +      |
| change_number    | change / modify / replace    |
| delete_number    | delete / remove / del        |
| exit             | goodbye / close / exit / bye |
| greet            | hello / hi                   |
| show_number      | phone / get                  |
| show_all_numbers | show all / all               |
| save_to_file     | save / save all / write      |

Enter one of the listed commands followed by name and phone number if needed

`command` [`user name` [`phone number`]]. Values must be separated with space.

All phone numbers after exiting are saved to `phonebook.txt` in current directory


Simple example of using:

`>>> hi`

`How can I help you?`

`>>> add vaSyl bol 078-102-37-47`

`Vasyl Bol's phone 078-102-37-47 was added to phonebook`

`>>> show vaSYL BOL`

`Wrong value. There is no such command show`

`>>> phone vaSYL BOL`

`078-102-37-47`

`>>> all`

`Vasyl Bol: 078-102-37-47`