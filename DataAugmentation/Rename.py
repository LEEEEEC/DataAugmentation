import os


def func(i):
    t = i.find('-')
    return (i[t + 1:-4])


def get_all_files(bg_path):
    files = []

    for f in os.listdir(bg_path):
        if os.path.isfile(os.path.join(bg_path, f)):
            files.append(os.path.join(bg_path, f))
        else:
            files.extend(get_all_files(os.path.join(bg_path, f)))
    files.sort(key=func)  # 排序从小到大
    return files

# #####为重命名数据集路径
files_path = "#####"
file_type = ".json"
file_flag = 1
files = get_all_files(files_path)
for i in files:
    # print(i)
    # src=os.path.join(files_path,i)
    # file_path = os.path.join(files_path,str('%04d' % file_flag) + file_type)
    file_path = os.path.join(files_path,str('%04d' % file_flag) + file_type)
    print(file_path)
    os.rename(i, file_path)
    file_flag = file_flag + 1labe