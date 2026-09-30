
import os
from openai import OpenAI


client = OpenAI(
    api_key= os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)
command = '''
[4:21 pm, 11/9/2026] Mayank: Tuune apna matter btaya ? Ya phir abhi kch ni bola
[4:21 pm, 11/9/2026] papuu pazerr: Tuune apna matter btaya ? Ya phir abhi kch ni bola
Bagal vale ko bola voh khe rha unko ane do fir baat krna
[4:21 pm, 11/9/2026] Mayank: Hao to rukja
[4:21 pm, 11/9/2026] Mayank: Or kehe dena sir case ki hearing h ,jisko ye document jana
[4:22 pm, 11/9/2026] Mayank: Usme need h iski
[4:22 pm, 11/9/2026] Mayank: 3-4 din baad
[4:22 pm, 11/9/2026] Mayank: Proceeding ke liye zruri h ye
[4:23 pm, 11/9/2026] Mayank: Or bhr mt niklna vha se
[4:23 pm, 11/9/2026] Mayank: Vhi se call lga diyo mujhe
[4:23 pm, 11/9/2026] Mayank: Andr hee beth ke
[4:25 pm, 11/9/2026] papuu pazerr: Kyun
[4:25 pm, 11/9/2026] Mayank: Kyun
Qki ye log bhosad smjhte samne vale ko
[4:25 pm, 11/9/2026] Mayank: Bhr aake dubara andr jayega to aith ke dikhayege
'''
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages =[
        {"role": "system","content" : "Your are a person named papuu pazerr who "
        "speaks hindi as well as english."
        " HE is from India and is a coder. You analyze chat and "
        "respond like harsh"},
             {"role": "user", "content": command}  ]
)

print(completion.choices[0].message.content)
