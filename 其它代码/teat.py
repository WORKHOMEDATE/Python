import os

def scan_files(directory, prefix=None, postfix=None):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if prefix and not file.startswith(prefix):
                continue
            if postfix and not file.endswith(postfix):
                continue
            files_list.append(os.path.join(root, file))
    return files_list

if __name__ == '__main__':
    directory = input("请输入要扫描的目录 : > ")
    prefix = input("请输入文件名前缀（可选）：> ")
    postfix = input("请输入文件名后缀（可选）：> ")
    files = scan_files(directory, prefix, postfix)
    for file in files:
        print(file)
