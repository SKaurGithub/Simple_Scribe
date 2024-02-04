"""
********************* SIMPLE SCRIBE *********************

This program is a word-processing tool, 
which should help users to create, edit and format text. 

"""

# Text attributes
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
ITALICS = '\033[3m'


# Prompt user for input, which will be used to edit and format.
print("\n***** Welcome to Simple Scribe! *****")
print("-" * 80)
user_text = input("Please enter your text:\n")
print("\n" + "-" * 80)
print(f"Thank you. You have entered:\n{user_text}")
print("-" * 80)


done = False
while not done:
    # Display the main menu to the user.
    main_menu = input("Would you like to:\n"
                      "1. Edit your text\n"
                      "2. Format your text\n"
                      "3. View the current version of your text\n"
                      "4. Exit\n"
                      "\nPlease enter the number of the option "
                      "you would like to choose (1-4):\n")


    if main_menu == "1":
        # If "Edit" option chosen,
        # user will be asked to enter the text they want to edit.
        find_text = input("\nYou have selected \"Edit text\".\n\n"
                          "Please enter the part of your text "
                          "you would like to \033[4mchange\033[0m.\n"
                          "You may enter one or more words or letters, "
                          "separated by space.\n"
                          "To return to the main menu, enter the number 0:\n")

        # Give the option to return to main menu,
        # in case above selection was by mistake.
        if find_text == "0":
            print("")
            continue


        while True:
            # Check if entered text is in user_text;
            # if so, ask user for new text to replace initial part of text.
            if find_text in user_text:
                replace_text = input("\nPlease enter the \033[4mnew\033[0m "
                                     "part of your text, "
                                     "which you would like "
                                     "to replace the above with:\n")
                user_text = user_text.replace(find_text, replace_text)
                print("-" * 80)
                print(f"The amended text is: {user_text}")
                print("-" * 80 + "\n")
                break
            # Executes if entered text is not in user_text.
            else:
                find_text = input("\nEntered word(s)/letter(s) "
                                  "not found in your text.\n"
                                  "Please enter the part of your text "
                                  "you would like to \033[4mchange\033[0m.\n"
                                  "This must exist in your text "
                                  "(case-sensitive).\n")


    elif main_menu == "2":
        # If "Format" option chosen,
        # user will be asked to enter the text they want to format.
        format_text = input("\nYou have selected \"Format text\".\n\n"
                            "Please enter the part of your text "
                            "you would like to \033[4mformat\033[0m.\n"
                            "You may enter one or more words or letters.\n"
                            "To return to the main menu, enter 0:\n")

        # Give the option to return to main menu,
        # in case above selection was by mistake.
        if format_text == "0":
            print("")
            continue

        while True:
            # Check if entered text is in user_text;
            if format_text in user_text:
                break
            else:
                format_text = input("\nEntered word(s)/letter(s) "
                                    "not found in your text.\n"
                                    "Please enter the part of your text "
                                    "you would like to \033[4mformat\033[0m.\n"
                                    "This must exist in your text "
                                    "(case-sensitive).\n")


        end = False
        while not end:
            # As entered text is in user_text,
            # user will be presented a format menu.
            format_menu = input("\nPlease select an option (1-5):\n"
                                "1. Bold\n"
                                "2. Italics\n"
                                "3. Underline\n"
                                "4. Undo all above changes\n"
                                "5. Change case\n")


            if format_menu == "1":
                # Format text to bold.
                formatted_text = '\033[1m' + format_text + '\033[0m'
                user_text = user_text.replace(format_text, formatted_text)
                print("-" * 80)
                print(f"You have selected \"Bold\".\n"
                      f"The amended text is: {user_text}")
                print("-" * 80 + "\n")
                break


            elif format_menu == "2":
                # Format text to italics.
                formatted_text = '\033[3m' + format_text + '\033[0m'
                user_text = user_text.replace(format_text, formatted_text)
                print("-" * 80)
                print(f"You have selected \"Italics\".\n"
                      f"The amended text is: {user_text}")
                print("-" * 80 + "\n")
                break


            elif format_menu == "3":
                # Format text to underline.
                formatted_text = '\033[4m' + format_text + '\033[0m'
                user_text = user_text.replace(format_text, formatted_text)
                print("-" * 80)
                print(f"You have selected \"Underline\".\n"
                      f"The amended text is: {user_text}")
                print("-" * 80 + "\n")
                break


            elif format_menu == "4":
                # Undo all above changes
                formatted_text = '\033[0m' + format_text
                user_text = user_text.replace(format_text, formatted_text)

                # The below will remove all text attributes,
                # which will allow the user to re-edit or
                # re-format the same part of the text
                user_text = user_text.replace('\033[0m', '')
                user_text = user_text.replace('\033[1m', '')
                user_text = user_text.replace('\033[4m', '')
                user_text = user_text.replace('\033[3m', '')
                print("-" * 80)
                print(f"You have selected \"Undo all above changes\".\n"
                      f"The amended text is: {user_text}")
                print("-" * 80 + "\n")
                break


            elif format_menu == "5":
                # Format text by changing case;
                # providing user different options.
                while True:
                    case_change = input("\nWould you like to change to\n"
                                        "1. UPPER case,\n"
                                        "2. lower case or\n"
                                        "3. Capitalise first letter(s) "
                                        "of your word(s)? (1-3):\n")
                   
                    # Change to upper case
                    if case_change == "1":
                        user_text = user_text.replace(format_text,
                                                      format_text.upper())
                        print("-" * 80)
                        print(f"You have selected \"UPPER case\".\n"
                              f"The amended text is: {user_text}")
                        print("-" * 80 + "\n")
                        end = True
                        break


                    # Change to lower case
                    elif case_change == "2":
                        user_text = user_text.replace(format_text,
                                                      format_text.lower())
                        print("-" * 80)
                        print(f"You have selected \"lower case\".\n"
                              f"The amended text is: {user_text}")
                        print("-" * 80 + "\n")
                        end = True
                        break


                    # Capitalise words
                    elif case_change == "3":
                        user_text = user_text.replace(format_text,
                                                      format_text.title())
                        print("-" * 80)
                        print(f"You have selected \"Capitalise\".\n"
                              f"The amended text is: {user_text}")
                        print("-" * 80 + "\n")
                        end = True
                        break


                    else:
                        print("\nInvalid entry. "
                              "Please choose by entering a number 1-3.")

            else:
                print("Invalid entry.")


    elif main_menu == "3":
        # View current version of text.
        print("\n" + "-" * 80)
        print(f"The current version of your text looks like this:")
        print(f"{user_text}")
        print("-" * 80)


    elif main_menu == "4":
        # Exit
        print("\nThank you for using Simple Scribe!\n"
              "We look forward to see you again!")
        break


    else:
        print("\nInvalid entry.")
