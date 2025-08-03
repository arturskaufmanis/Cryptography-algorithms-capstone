"""
The Message Encoder
=====================
A program that encodes messages using a Caesar cipher with a 15-letter shift.
Each letter is shifted 15 positions forward in the alphabet (cyclically).
"""

# Constants for better maintainability and efficiency
CIPHER_SHIFT = 15
ALPHABET_SIZE = 26
LOWERCASE_A_ASCII = ord('a')
UPPERCASE_A_ASCII = ord('A')


def validate_input(message):
    """
    Validates the input message to ensure it meets requirements.
    
    Args:
        message (str): The message to validate
        
    Returns:
        str: The validated and cleaned message
        
    Raises:
        TypeError: If message is not a string
        ValueError: If message is empty after stripping whitespace
    """
    if not isinstance(message, str):
        raise TypeError("Input must be a string")
    
    cleaned_message = message.strip()
    if not cleaned_message:
        raise ValueError("Message cannot be empty")
    
    return cleaned_message


def shift_character(char):
    """
    Shifts a single character by the cipher shift amount.
    Non-alphabetic characters are returned unchanged.
    
    Args:
        char (str): Single character to shift
        
    Returns:
        str: The shifted character or original if non-alphabetic
    """
    if not char.isalpha():
        return char
    
    # Determine ASCII offset based on case
    ascii_offset = LOWERCASE_A_ASCII if char.islower() else UPPERCASE_A_ASCII
    
    # Calculate shifted position with wraparound using modulo
    shifted_position = (ord(char) - ascii_offset + CIPHER_SHIFT) % ALPHABET_SIZE
    
    # Convert back to character
    return chr(shifted_position + ascii_offset)


def encode_message(message):
    """
    Encodes a message using Caesar cipher with 15-letter shift.
    
    Algorithm:
    - Each alphabetic character is shifted 15 positions forward
    - Case is preserved (uppercase stays uppercase, lowercase stays lowercase)
    - Non-alphabetic characters (spaces, punctuation, numbers) remain unchanged
    - Alphabet wrapping is handled using modulo arithmetic
    
    Args:
        message (str): The message to encode
        
    Returns:
        str: The encoded message
        
    Raises:
        TypeError: If message is not a string
        ValueError: If message is empty
    """
    validated_message = validate_input(message)
    
    # Use list comprehension for efficiency and readability
    encoded_characters = [shift_character(char) for char in validated_message]
    
    return ''.join(encoded_characters)


def display_results(original_message, encoded_message):
    """
    Displays the encoding results in a user-friendly format.
    
    Args:
        original_message (str): The original input message
        encoded_message (str): The encoded message
    """
    # Create visually appealing separator
    separator = "=" * 60
    
    print(f"\n{separator}")
    print("THE MESSAGE ENCODING RESULTS")
    print(f"{separator}")
    print(f"Original Message:  {original_message}")
    print(f"Encoded Message:   {encoded_message}")
    print(f"Cipher Shift:      {CIPHER_SHIFT} letters forward")
    print(f"Message Length:    {len(original_message)} characters")
    print(f"{separator}\n")


def get_user_input():
    """
    Gets and validates user input with clear prompts.
    
    Returns:
        str: The user's message, or None if they want to quit
    """
    print("The Message Encoder")
    print("-" * 20)
    print("Enter a message to encode (or 'quit' to exit)")
    
    try:
        user_input = input("\nMessage: ").strip()
        
        # Check for quit commands
        if user_input.lower() in ['quit', 'exit', 'q']:
            return None
            
        return user_input
        
    except (KeyboardInterrupt, EOFError):
        print("\nOperation cancelled. Goodbye!")
        return None


def ask_continue():
    """
    Asks user if they want to encode another message.
    
    Returns:
        bool: True if user wants to continue, False otherwise
    """
    while True:
        try:
            choice = input("Would you like to encode another message? (y/n): ").strip().lower()
            
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
                
        except (KeyboardInterrupt, EOFError):
            print("\nOperation cancelled.")
            return False


def main():
    """
    Main program function that orchestrates the encoding process.
    Handles all user interaction and error management.
    """
    print("Welcome to the Message Encoder!")
    print("This program encodes messages using a 15-letter shift cipher.\n")
    
    while True:
        try:
            # Get user input
            message = get_user_input()
            
            # Check if user wants to quit
            if message is None:
                break
                
            # Encode the message
            encoded = encode_message(message)
            
            # Display results in formatted output
            display_results(message, encoded)
            
            # Ask if user wants to continue
            if not ask_continue():
                break
                
        except ValueError as e:
            print(f"\nInput Error: {e}")
            print("Please try again with a valid message.\n")
            
        except TypeError as e:
            print(f"\nType Error: {e}")
            print("Please ensure you enter a text message.\n")
            
        except Exception as e:
            print(f"\nUnexpected Error: {e}")
            print("Please try again.\n")
    
    # Goodbye message
    print("\nThank you for using the Message Encoder!")
    print("Goodbye! 🔐")


# Program entry point
if __name__ == "__main__":
    main()
