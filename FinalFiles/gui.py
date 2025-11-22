# CtrlUno Arcade - Turtle Graphics Helper

# Import turtle for graphical text input
import turtle

# SCREEN PRIVACY - Clears screen between turns in hot-seat multiplayer
SCREEN_CLEAR = "\n" * 200

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


def show_game_message(title, message, wait_for_ok=True):
    """
    Displays a game message in a turtle graphics window.
    
    Args:
        title (str): Title for the message window
        message (str): Message to display
        wait_for_ok (bool): Whether to wait for user to click OK
    """
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.penup()
    
    # Display title
    turtle.goto(0, 200)
    turtle.color("black")
    turtle.write(title, align="center", font=("Arial", 24, "bold"))
    
    # Display message (handle multi-line)
    lines = message.split('\n')
    start_y = 150
    for i, line in enumerate(lines):
        if line.strip():
            turtle.goto(0, start_y - (i * 25))
            turtle.color("blue")
            turtle.write(line.strip(), align="center", font=("Arial", 14, "normal"))
    
    turtle.update()
    
    if wait_for_ok:
        turtle.textinput(title, "Press Enter to continue...")
    
    print(message)  # Also print to console

def display_message_on_turtle(message, y_position=0, font_size=14, color="black"):
    """
    Displays a message on the turtle graphics window.
    
    Args:
        message (str): Message to display
        y_position (int): Y coordinate for text
        font_size (int): Font size
        color (str): Text color
    """
    turtle.penup()
    turtle.goto(0, y_position)
    turtle.color(color)
    turtle.write(message, align="center", font=("Arial", font_size, "normal"))
    turtle.update()

def tg_print(message, also_console=True):
    """
    Print message to both turtle graphics window and console.
    
    Args:
        message (str): Message to display
        also_console (bool): Also print to console
    """
    if also_console:
        print(message)
    # Messages will be displayed in the card_visuals function

def verify_player_turn(current_player):
    """
    Displays a blank screen asking if the current player is ready.
    This prevents other players from seeing each other's hands.
    
    Args:
        current_player (int): The player number whose turn it is
    """
    turtle.clearscreen()
    turtle.hideturtle()
    turtle.penup()
    
    # Display turn indicator
    turtle.goto(0, 100)
    turtle.color("black")
    turtle.write(f"Player {current_player}'s Turn", align="center", font=("Arial", 32, "bold"))
    
    # Display instructions
    turtle.goto(0, 0)
    turtle.color("blue")
    turtle.write(f"Are you Player {current_player}?", align="center", font=("Arial", 20, "normal"))
    
    turtle.goto(0, -50)
    turtle.color("gray")
    turtle.write("If yes, click OK to see your hand.", align="center", font=("Arial", 14, "italic"))
    
    turtle.goto(0, -80)
    turtle.write("Make sure other players aren't looking!", align="center", font=("Arial", 12, "italic"))
    
    turtle.update()
    
    # Wait for player confirmation
    turtle.textinput(f"Player {current_player}'s Turn", f"Are you Player {current_player}? Press Enter when ready:")
    
    print(SCREEN_CLEAR)
    print(f"Player {current_player}, it's your turn!")