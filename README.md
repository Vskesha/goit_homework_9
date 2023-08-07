# goit_homework_9

This is a simple console bot for managing phonebook

Program supports next commands (listed in COMMANDS in console_bot_helper.py):

--------------------|-------------------------------------
       Action       |     Commands
--------------------|-------------------------------------
add_number__________|_ add / plus / create / +____________
change_number_______|_ change / modify / replace__________
delete_number_______|_ delete / remove / del______________
exit________________|_ goodbye / close / exit / bye_______
greet_______________|_ hello / hi_________________________
show_number_________|_ phone / get________________________
show_all_numbers____|_ show all / all_____________________
save_to_file________|_ save / save all / write____________
--------------------|-------------------------------------

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