# CtrlUno Arcade - Quit Menu
# Application exit confirmation and navigation safety

# Import turtle for graphical text input
import turtle

# Import help menu for navigation
import help_menu

#------------------------------------------------------
# TURTLE GRAPHICS HELPER FUNCTION
#------------------------------------------------------

def show_help_message(title, message, wait_for_ok=True):
    """
    Displays a help message in a turtle graphics window.
    
    Args:
        title (str): Title for the message window
        message (str): Message to display
        wait_for_ok (bool): If True, wait for user to press Enter before continuing
    """
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.penup()
    
    # Display title
    turtle.goto(0, 300)
    turtle.color("black")
    turtle.write(title, align="center", font=("Arial", 24, "bold"))
    
    # Display message (handle multi-line)
    lines = message.split('\n')
    start_y = 250
    for i, line in enumerate(lines):
        if line.strip():
            turtle.goto(0, start_y - (i * 20))
            turtle.color("blue")
            # Adjust font size based on line length for better fitting
            font_size = 10 if len(line) > 80 else 12
            turtle.write(line.strip(), align="center", font=("Arial", font_size, "normal"))
    
    turtle.update()
    
    # Only wait for user input if wait_for_ok is True
    if wait_for_ok:
        turtle.textinput(title, "Press Enter to continue...")

#------------------------------------------------------
# QUIT MENU FUNCTIONS
# Application exit confirmation and navigation safety
#------------------------------------------------------

def quit_menu():
    """
    Exit confirmation system preventing accidental application closure.
    Provides last-chance navigation to help or main menu.
    
    Safety Features:
    - Confirmation required before exiting
    - Access to help if player needs information
    - Return to main menu option
    - Clear exit message when confirmed
    
    Options:
    1. Help: Access game documentation
    2. Main Menu: Return to game selection
    3. Quit: Confirmed application exit with goodbye message
    
    Input validation ensures proper choice handling before exit.
    """
    
    menu_message = """
Are you sure you want to quit?

Options:
- Type 'Q/Quit' to exit the arcade
- Type 'H/Help' to get game help
- Type 'M/Main Menu' to return to the main menu"""

    show_help_message("===== Quit CtrlUno Arcade =====", menu_message, wait_for_ok=False)
    
    confirmation_input = turtle.textinput("Quit Menu", "What would you like to do?")
    if confirmation_input is None:
        show_help_message("No Input", "No input provided. Returning to main menu.", wait_for_ok=False)
        return "main"
    confirmation = confirmation_input.lower()

    
    if confirmation in ["q", "quit"]:
        show_help_message("Goodbye!", "Thank you for playing CtrlUno Arcade! Goodbye!", wait_for_ok=True)
        exit()
    elif confirmation in ["h", "help"]:
        help_menu.help_menu()
    elif confirmation in ["m", "main", "menu", "main menu"]:
        return "main"  # Return to main menu
    else:
        show_help_message("Invalid Input", "Invalid option. Please try again.", wait_for_ok=False)
        quit_menu()

        #Test