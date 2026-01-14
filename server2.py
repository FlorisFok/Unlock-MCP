from fastmcp import FastMCP
from fastmcp.tools import Tool

mcp = FastMCP(name="StringOperationsTools")
unlocked_tools = False

def invert(text: str) -> str:
    """
    Reverses the character order of a string by inverting its sequence.
    
    This function takes a string input and returns a new string with all characters
    arranged in reverse order. It uses Python's slice notation with a step of -1
    to efficiently reverse the string without modifying the original input. The
    function will print the operation being performed to the console for debugging
    and logging purposes before computing and returning the inverted result.
    
    Args:
        text (str): The input string to be reversed. Can be any string value
                   including empty strings, single characters, or multi-word text.
                   Special characters, numbers, and whitespace are preserved.
                   
    Returns:
        str: A new string containing all characters from the input string
             arranged in reverse order from last to first character.
             
    Example:
        invert("hello") returns "olleh"
        invert("Python") returns "nohtyP"
        invert("12345") returns "54321"
        invert("a b c") returns "c b a"
    """
    print(f"Inverting: {text}")
    return text[::-1]

def skip_every_second(text: str) -> str:
    """
    Extracts every second character from a string starting with the first character.
    
    This function implements a character filtering operation that selects characters
    at even indices (0, 2, 4, 6, etc.) from the input string, effectively skipping
    every second character. It uses Python's slice notation with a step of 2 to
    efficiently extract the desired characters without creating intermediate strings.
    The function will print the operation being performed to the console for debugging
    purposes before processing and returning the filtered result.
    
    Args:
        text (str): The input string from which to extract every second character.
                   Can be any string value including empty strings, single characters,
                   or lengthy text. All character types are supported.
                   
    Returns:
        str: A new string containing only the characters at even indices from
             the original string, maintaining their relative order but with
             every second character removed.
             
    Example:
        skip_every_second("hello") returns "hlo"
        skip_every_second("Python") returns "Pto"
        skip_every_second("abcdef") returns "ace"
        skip_every_second("a") returns "a"
    """
    print(f"Skipping every second char in: {text}")
    return text[::2]

def caps(text: str) -> str:
    """
    Converts all alphabetic characters in a string to uppercase format.
    
    This function transforms the input string by converting all lowercase letters
    to their uppercase equivalents while preserving all other characters including
    numbers, special symbols, whitespace, and punctuation marks in their original
    form. It uses Python's built-in upper() method which follows Unicode standards
    for case conversion. The function will print the conversion operation to the
    console for debugging and logging purposes before processing and returning
    the uppercased result.
    
    Args:
        text (str): The input string to be converted to uppercase. Can contain
                   any combination of letters, numbers, special characters,
                   whitespace, and punctuation marks. Non-alphabetic characters
                   remain unchanged during the conversion process.
                   
    Returns:
        str: A new string with all alphabetic characters converted to uppercase
             while maintaining the exact same length and structure as the input,
             with non-alphabetic characters preserved unchanged.
             
    Example:
        caps("hello") returns "HELLO"
        caps("Python123") returns "PYTHON123"
        caps("Hello World!") returns "HELLO WORLD!"
        caps("mix3d C4s3") returns "MIX3D C4S3"
    """
    print(f"Converting to CAPS: {text}")
    return text.upper()


@mcp.tool
def access_string_operation_tools() -> str:
    """
    Call this tool to access the string operations tools.
    """
    global unlocked_tools
    print("Accessing tools...")
    
    # Only add tools if this is the first session to unlock
    if not unlocked_tools:
        print("Adding tools...")
        mcp.add_tool(Tool.from_function(invert))
        mcp.add_tool(Tool.from_function(skip_every_second))
        mcp.add_tool(Tool.from_function(caps))
        unlocked_tools = True
    
    
    return (
        "Tools unlocked successfully!"
    )


if __name__ == "__main__":
    # Run the server in stdio mode for local communication
    mcp.run(transport="stdio")
