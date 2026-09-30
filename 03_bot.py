import pyautogui
import pyperclip
import time
from openai import OpenAI
import os



client = OpenAI(
    api_key= os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def is_last_message_from_sender(chat_log,sender_name ="Mayank"):
    #split the chat log into individuals messages
    messages = chat_log.strip().spilit("\2026")
    # terate through the messages in reverse to find the last message  
    if sender_name in messages:
        return True
    return False

# 1. Click the chrome icon
pyautogui.click(490, 1042)
time.sleep(1)

while True:

    # Give the application time to open/load

    # 2. Drag to select the text
    pyautogui.moveTo(676, 196, duration=0.2)
    pyautogui.dragTo(686, 963, duration=1, button="left")

    # 3. Copy selected text
    pyautogui.hotkey("ctrl", "c")
    time.sleep(1)
    pyautogui.click(1366,735)


    # Give clipboard time to update

    # 4. Get copied text into a variable
    chat_history = pyperclip.paste()

    print(chat_history) 

    if is_last_message_from_sender(chat_history):


        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages =[
                {
            "role": "system",
            "content": """
        You are kratos , a young Indian guy chatting on WhatsApp.

        Reply in natural Hinglish using ONLY Roman/English letters.

        Never use Hindi/Devanagari script.

        Your style should be casual, short and natural, like:
        - "haan re bhidu kya hua 😂"
        -"kuchu puchu khanaya khaya kya"
        - "nahi re bachhi abhi ghar pe hu"
        - "ruk re baba mai check karta hu"
        - "haan baby kal milte hain"
        - "bhiduu ye toh mast hai ek dum jhakas😂"
        - "arey naa re , aisa system nhi "
        - "5 min wait krle berii, aa raha hu bhenhod"

        Do NOT write pure Hindi.
        Do NOT use formal Hindi.
        Do NOT translate English words unnecessarily.

        Use English words naturally:
        "bro", "time", "plan", "work", "call", "meeting", "busy",
        "check", "send", "update", "problem", "idea", etc.

        Match the tone of the conversation.

        Output ONLY the WhatsApp reply.

        output should be the next chat response(text message only)"
        """
        },
                {"role": "user", "content": chat_history}]
                )  


        response = completion.choices[0].message.content
        pyperclip.copy(response)

        pyautogui.click(813, 1030)
        time.sleep(2)

        # Paste the variable's contents
        pyperclip.copy(response)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(2)


        # Press Enter
        pyautogui.press("enter")

