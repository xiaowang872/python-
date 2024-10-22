# 打开并读取文件内容
file_path = 'Historical_QQ_Number.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取文件中的所有行
        lines = file.readlines()
        # 打印每一行
        for line in lines:
            print(line.strip())  # 使用strip()方法去除每行末尾的换行符
except FileNotFoundError:
    print(f"文件 {file_path} 未找到，请检查文件路径是否正确。")
except IOError:
    print(f"读取文件 {file_path} 时发生错误。")