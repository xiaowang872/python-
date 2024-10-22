# 脚本名称：modify_and_save_email.py

# 定义要修改的文件和保存旧email的文件
target_file = 'send_mail.py'  # 假设文件名已更改为main.py
last_email_file = 'Historical_QQ_Number.txt'

# 提示用户输入新的QQ号
new_qq = input()
new_email = f"{new_qq}@qq.com"

# 读取整个文件内容并找到旧的email地址
old_email = None
with open(target_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith("msg['To'] = "):
            # 提取旧邮箱地址，去掉前后的引号和可能的空格
            old_email_candidate = stripped_line.split("'")[3]
            old_email = old_email_candidate.strip()
            break  # 找到后退出循环

# 确保找到了旧的email地址
if old_email is None:
    print("未找到旧的电子邮件地址。")
else:
    # 将旧的email地址追加写到last.txt文件中
    with open(last_email_file, 'a', encoding='utf-8') as file:
        file.write(old_email + '\n')  # 添加换行符以便下次追加时不会覆盖

    # 修改target_file中的email地址
    modified_lines = []
    for line in lines:
        if line.strip().startswith("msg['To'] = "):
            line = f"msg['To'] = '{new_email}'\n"  # 替换为新邮箱地址，并添加换行符
        modified_lines.append(line)

        # 将修改后的内容写回target_file文件
    with open(target_file, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

        # 打印成功消息，使用实际的旧email地址
    print(f"已成功将{target_file}中的收件人地址修改为{new_email}，并将旧地址{old_email}追加到{last_email_file}中。")