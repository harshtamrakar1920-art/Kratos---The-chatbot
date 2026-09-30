
print(chat_history) 
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages =[
        {"role": "system","content" : "Your are a person named papuu pazerr who speaks hindi as well as english. HE if from India and is a coder. You analyze chat and respond like harsh"},
        {"role": "user", "content": chat_history}]
        )  


response = completion.choices[0].message.content
pyperclip.copy(response)

pyautogui.click(813, 1030)
time.sleep(1)

# Paste the variable's contents
pyperclip.copy(chat_history)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)


# Press Enter
pyautogui.press("enter")

