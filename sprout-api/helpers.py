import board
import adafruit_mcp3xxx.mcp3008 as MCP

def getPin(pin: int):
    """
    Mini helper function to get pin object from pin number.\n
    getPin(22) -> board.D22
    """
    return getattr(board, f'D{pin}')

def getChannel(channel: int):
    """
    Mini helper function to get MCP channel object from channel number.\n
    getChannel(2) -> MCP.P2
    """
    return getattr(MCP, f'P{channel}')