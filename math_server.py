from mcp.server.fastmcp import FastMCP
mcp = FastMCP("math_server", log_level="DEBUG", port="3003")

@mcp.tool()
def add_numbers(x: int, y: int) -> int:
    return x + y

@mcp.tool()
def substract_numbers(x: int, y: int) -> int:
    return x - y

@mcp.tool()
def multiply_numbers(x: int, y: int) -> int:
    return x * y

if __name__ == "__main__":
    try:
        mcp.run(transport="sse")
    except Exception as e:
        print(f"Error starting server: {e}")