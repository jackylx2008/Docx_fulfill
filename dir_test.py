import os


def get_files_with_key_words(dir: str, ext: str, key_word: str):
    files_no_ext = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            print(file)
            if file.find(key_word) >= 0 and (file.find(ext.upper()) >= 0 or file.find(ext.lower()) >= 0):
                file = file.rsplit('.', 1)[0]
                files_no_ext.append(file)
    return files_no_ext


dir = r"D:\\CloudStation\\Python\\Project\\CNCC2_DesignChange_Doc\\test"

files_name = get_files_with_key_words(dir, "docx", "会展投资合字2019第132号")
print(files_name)


def make_dir(target_dir: str, files_name: list):
    for dir_name in files_name:
        if os.path.exists(dir_name):
            print("目录存在")
        else:
            os.makedirs(target_dir + "\\" + dir_name)


make_dir(dir, files_name)
