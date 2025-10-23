# CtrlUno Arcade - Quit Menu
# Application exit confirmation and navigation safety

# Import help menu for navigation
import help_menu

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
    
    """Display quit confirmation prompt."""

    print("\n===== Quit CtrlUno Arcade =====")
    print("Are you sure you want to quit?, or would you like some help first?")
    confirmation = input("To quit type 'quit', to get help, type 'help', or to go back to the main menu, type 'main menu': ").lower()

    
    if confirmation in ["q", "quit"]:
        print("\nThank you for playing CtrlUno Arcade! Goodbye!")
        exit()
    elif confirmation in ["h", "help"]:
        help_menu.help_menu()
    elif confirmation in ["m", "main", "menu", "main menu"]:
        return "main"  # Return to main menu
    else:
        print()
        print("Invalid option. Please try again.")
        quit_menu()