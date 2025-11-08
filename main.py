from fastmcp import FastMCP
import random
import json

#creating the fastmcp instance 
mcp = FastMCP("simple calculator server")

# adding of two numbers 
@mcp.tool()
def add(a: int, b: int) -> int:
    """ Add two numbers together 

    args : 
    a : 1st number 
    b : 2nd number 

    returns :
    the sum of a and b
    """
    return a + b

@mcp.tool()
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """    generate a random number 

    min value : minimum value default 1
    max_value : maximum value defaut 100

    return :
    return a random number bw them 
    """
    return random.randint(min_val, max_val)

#resourse inetialization 
@mcp.resource("info://server")
def server_info() -> str:
    """"  get info about the server   """
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "a basic mcp server with math tools",
        "tools": ["add", "random_integer"],
        "author": "Ajitesh"
    }
    return json.dumps(info, indent=2)

# optional: simple health check for inspector connection
@mcp.resource("health://check")
def health_check() -> str:
    return "Server is running"

#startig server 
if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8000)

    # this is the main diff in  local and remote server taht in mcp.run() it default parameters are transport =stdio
