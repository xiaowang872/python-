import subprocess
import os


def execute_script(script_name):
    # 构建脚本的完整路径
    script_path = os.path.join(os.getcwd(), script_name)
    try:
        # 使用subprocess.run来执行脚本
        result = subprocess.run(['python', script_path], capture_output=True, text=True, encoding='utf-8', check=True)
        print(f"{script_name} executed successfully:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}:")
        # 注意：由于我们设置了capture_output=True和text=True，stderr会被自动捕获到e.stderr中
        print(e.stderr)


def main():
    while True:
        # 提示用户输入
        user_input = input("Please enter:\n0 to exit\n1 to execute Change_QQ_number.py(修改发送人)\n2 to execute send_mail.py(发送)\n3 to execute View_historical_QQ_numbers.py(查看历史qq号)\n4 to execute Delete historical QQ numbers(清空历史qq号)\n")

        # 根据用户输入执行相应操作
        if user_input == '1':
            print("请输入新的QQ号（例如：3637094000）：")
            execute_script('Change_QQ_number.py')
        elif user_input == '2':
            execute_script('send_mail.py')
        elif user_input == '3':
            execute_script('View_historical_QQ_numbers.py')
        elif user_input == '4':
            execute_script('Delete_historical_QQ_numbers.py')
        elif user_input == '0':
            print("Exiting the program.")
            break  # 退出循环

        else:
            print("Invalid input. Please enter 1, 2, 3 or 0.")


if __name__ == "__main__":
    main()