file_path = 'Historical_QQ_Number.txt'

try:
    with open(file_path, 'w', encoding='utf-8') as file:
        # 不写入任何内容，直接关闭文件，这将清空文件
        pass
    print(f"文件 {file_path} 的内容已被清空。")
except IOError:
    print(f"无法清空文件 {file_path}。请检查文件路径和权限。")