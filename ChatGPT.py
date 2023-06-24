import os
import openai
print('''GPT 3.5:
1.4K:Input $0.0015 / 1K tokens Output $0.002 / 1K tokens(Chatting)
2.16K:Input $0.003 / 1K tokens Output $0.004 / 1K tokens(Writting)
3.Feature:Linux Terminal
Which do you want?''')
systemis = 'F'
which = int(input())
if which == 1:
    mode = "gpt-3.5-turbo"
elif which == 2:
    mode = "gpt-3.5-turbo-16k"
elif which == 3:
    mode = "gpt-3.5-turbo"
    systemis = 'T'
print('''1.more creative
2.more balanced
3.more accurate
Which do you want?''')
whicht = int(input())
if whicht == 1:
    temp = 2
elif whicht == 2:
    temp = 0.8
elif whicht == 3:
    temp = 0.4
limit = 0
ismax = 0
# 设置OpenAI API的访问密钥
openai.api_key = API-KEY

# 聊天模型的模型ID
model_id = mode

# 聊天历史列表
chat_history = []

# 定义聊天函数
def chat_with_gpt(prompt):
    if systemis == 'F':
        history = chat_history + [{"role": "user", "content": prompt}]
    elif systemis == 'T':
        history = chat_history + [{"role": "system", "content": "You act as a Linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. Do no write explanations. Do not type commands unless I instruct you to do so. When I need to tell you something in English I will do so by putting text inside curly brackets."},{"role": "user", "content": prompt}]
    try:
        if ismax == 0:
            response = openai.ChatCompletion.create(
                model=model_id,
                messages=history,
                #max_tokens=50,
                n=1,
                stop=None,
                temperature=temp,
                #log_level="info",  # 开启日志级别为 "info"
                #model="text-davinci-003"
            )
        elif ismax == 1:
            response = openai.ChatCompletion.create(
                model=model_id,
                messages=history,
                max_tokens=limit,
                n=1,
                stop=None,
                temperature=temp,
                #log_level="info",  # 开启日志级别为 "info"
                #model="text-davinci-003"
            )
    except Exception as e:
        print("Error:",e)
    message = response.choices[0].message.content.strip()
    # 添加当前用户输入到聊天历史中
    chat_history.append({"role": "user", "content": prompt})
    # 添加 ChatGPT 的回复到聊天历史中
    chat_history.append({"role": "assistant", "content": message})
    # 获取输入和输出的令牌数量
    input_tokens = response['usage']['prompt_tokens']
    output_tokens = response['usage']['completion_tokens']
    if which == 1 or which == 3:
        print("Input money:$", input_tokens*0.0000015)
        print("Output money:$", output_tokens*0.000002)
        print("Total money:$",input_tokens*0.0000015+output_tokens*0.000002)
    if which == 2:
        print("Input money:$", input_tokens*0.000003)
        print("Output money:$", output_tokens*0.000004)
        print("Total money:$",input_tokens*0.000003+output_tokens*0.000004)
    return message

# 命令行交互
while True:
    user_input = input("User: ")
    if user_input[:7] == "/limit ":
        try:
            limit = int(user_input[7:])
            if limit == -1:
                ismax = 0
                limit = 0
                print("Refresh OK")
            else:
                ismax = 1
                print("Set",limit,"OK")
        except:
            print("NaN")
    else:
        # 发送用户输入到ChatGPT并获取响应
        response = chat_with_gpt(user_input)
        
        # 控制对话历史长度
        max_history_length = 3  # 最大对话历史长度
        chat_history = chat_history[-max_history_length:]  # 仅保留最近的几个对话历史

        # 打印ChatGPT的响应
        print("ChatGPT: " + response)

    
