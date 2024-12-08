import json
import re
from langchain.tools import tool
import traceback

try:
    from .utils.db import *
    from .llm import get_model
    from .top_bar_wrapper import wrapper
    from .llm_settings import llm_settings

except ImportError:
    from utils.db import *
    from top_bar_wrapper import wrapper
    from llm_settings import llm_settings












def mouse_scroll_(direction: str, amount: int = 1) -> bool:
    """
    A function to scroll the mouse wheel.

    Parameters:
    - direction (str): The direction of the scroll. Possible values are "up" and "down".
    - amount (int): The amount of scrolling to be performed. The default value is 1.

    Returns:
    - bool: True if the scrolling was performed successfully, False otherwise.
    """
    try:
        import pyautogui

        pyautogui.FAILSAFE = False

        if direction == "up":
            pyautogui.scroll(amount)
        elif direction == "down":
            pyautogui.scroll(-amount)
        return True
    except:
        traceback.print_exc()
        return False


mouse_scroll = tool(mouse_scroll_)



def smart_mouse_(goto:str):
    """
    This is an smart mouse you can say the location that you want to move, for example click to search bar. Left click to Pricing column. Click to Login button. 
    """

    try:
        from .cu.ask_anthropic import ask_anthropic
    except ImportError:
        from cu.ask_anthropic import ask_anthropic

    print("smart_mouse_")
    print("goto", goto)
    result = ask_anthropic(f"You are an smart mouse and the user want to {goto}")
    print("result", result)
    return result


smart_mouse = tool(smart_mouse_)



if __name__ == "__main__":
    print(smart_mouse("click to search bar"))
