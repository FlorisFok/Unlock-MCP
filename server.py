from fastmcp import FastMCP
from fastmcp.tools import Tool

mcp = FastMCP(name="DynamicCalculatorTools")
unlocked_tools = False


def add_numbers(a: int, b: int) -> int:
    """
    Performs mathematical addition of two integer values.
    
    This function takes two integer parameters and returns their sum using 
    standard arithmetic addition. It will print the operation being performed
    to the console for debugging purposes before computing and returning the result.
    
    Args:
        a (int): The first integer operand to be added
        b (int): The second integer operand to be added
        
    Returns:
        int: The mathematical sum of the two input integers (a + b)
        
    Example:
        add_numbers(5, 3) returns 8
        add_numbers(-2, 7) returns 5
    """
    print(f"Adding {a} and {b}")
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """
    Performs mathematical multiplication of two integer values.
    
    This function takes two integer parameters and returns their product using
    standard arithmetic multiplication. It will print the operation being performed
    to the console for debugging purposes before computing and returning the result.
    The multiplication follows standard mathematical rules including handling of
    negative numbers and zero values.
    
    Args:
        a (int): The first integer operand to be multiplied
        b (int): The second integer operand to be multiplied
        
    Returns:
        int: The mathematical product of the two input integers (a × b)
        
    Example:
        multiply_numbers(4, 6) returns 24
        multiply_numbers(-3, 5) returns -15
        multiply_numbers(0, 100) returns 0
    """
    print(f"Multiplying {a} and {b}")
    return a * b


def greet(name: str) -> str:
    """
    Generates a personalized greeting message for a specified individual.
    
    This function creates a warm, welcoming greeting message that incorporates
    the provided name parameter. It's designed to make users feel welcomed
    when they gain access to the unlocked tools in this dynamic MCP server.
    The function will print the greeting action to the console for logging
    purposes before returning the formatted greeting string.
    
    Args:
        name (str): The name of the person to greet. Can be any string value
                   representing a person's name, username, or identifier.
                   
    Returns:
        str: A formatted greeting message that includes the provided name
             and a welcome message indicating successful tool access.
             
    Example:
        greet("Alice") returns "Hello, Alice! Welcome to the unlocked tools."
        greet("Bob") returns "Hello, Bob! Welcome to the unlocked tools."
    """
    print(f"Greeting {name}")
    return f"Hello, {name}! Welcome to the unlocked tools."


@mcp.tool
def access_calculator_tools() -> str:
    """
    Call this tool to access the calculator tools.
    """
    global unlocked_tools
    print("Accessing tools...")
    
    # Only add tools if this is the first session to unlock
    if not unlocked_tools:
        print("Adding tools...")
        mcp.add_tool(Tool.from_function(add_numbers))
        mcp.add_tool(Tool.from_function(multiply_numbers))
        mcp.add_tool(Tool.from_function(greet))
        unlocked_tools = True
    
    
    return (
        "Tools unlocked successfully!"
    )


if __name__ == "__main__":
    # Run the server in stdio mode for local communication
    mcp.run(transport="stdio")
