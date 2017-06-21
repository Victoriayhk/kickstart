# *-* coding: utf-8 *-*

import os
import sys
from shutil import copyfile
import argparse


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c',
        '--clear',
        action='store_true',
        help='clear all data, and get ready for the contest',
    )
    parser.add_argument(
        '-r',
        '--run',
        type=str,
        help='run the code with data: sample(1), small(2), large(3)',
    )
    parser.add_argument(
        '-b',
        '--backup',
        action='store_true',
        help='back up the last small data and source code.',
    )
    parser.add_argument(
        '-p',
        '--python',
        action='store_true',
        help="some problem should be solved in python",
    )
    flags, other_argvs = parser.parse_known_args()
    pro_id = 'X'
    for x in other_argvs:
        if len(x) == 1 and x.upper() in 'ABCDE':
            pro_id = x
            break

    return flags, pro_id


def main(flags, pro_id):
    if flags.clear:
        # 删除源代码
        src_folder = 'src/'
        if not os.path.exists(src_folder):
            os.mkdir(src_folder)
        for src_file in os.listdir(src_folder):
            os.remove(src_folder + src_file)

        # 重置源代码为模板代码, 准备数据文件夹
        if not os.path.exists('data/'):
            os.mkdir('data/')
        else:
            for data_file in os.listdir('data/'):
                os.remove('data/' + data_file)
        for pro in "ABCDE":
            copyfile('template/test.cpp', 'src/' + pro + '.cpp')
            open('data/' + pro + '-sample.in', 'w').close()

        # 删除备份文件
        backup_folder = 'backup/'
        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)
        for backup_file in os.listdir(backup_folder):
            os.remove(backup_folder + backup_file)

    if flags.backup:
        backup_file = 'backup/' + pro_id + '.cpp.bak'
        copyfile('src/' + pro_id + '.cpp', backup_file)
        if os.path.exists('src/' + pro_id + '.py'):
            copyfile('src/' + pro_id + '.py', 'backup/' + pro_id + '.py.bak')

    if flags.run and pro_id != 'X':
        print "run {0}...".format(pro_id)

        # 确定跑python还是.cpp
        if "p" in flags.run:
            run_command = 'python src/' + pro_id + '.py {0} {0}.out'
        else:
            os.system("g++ -std=c++11 src/{0}.cpp -o src/{0}".format(pro_id))
            if sys.platform == "win32":
                run_command = 'src\\' + pro_id + '.exe {0} {0}.out'
            else:
                run_command = 'src/' + pro_id + ' {0} {0}.out'

        # 确定数据文件
        data_folder = 'data/'
        for x in os.listdir(data_folder):
            if not x.endswith('.in') or x.find(pro_id) == -1:
                continue;

            real_x = os.path.join(data_folder, x)
            if x.lower().find("sample") >= 0 and "1" in flags.run:
                print run_command.format(real_x)
                os.system(run_command.format(real_x))
            if x.lower().find('small') >= 0 and "2" in flags.run:
                print run_command.format(real_x)
                os.system(run_command.format(real_x))
            if x.lower().find('large') >= 0 and "3" in flags.run:
                print run_command.format(real_x)
                os.system(run_command.format(real_x))

    if flags.python and pro_id != 'X':
        if os.path.exists('src/' + pro_id + '.py'):
            copyfile('src/' + pro_id + '.py', 'backup/' + pro_id + '.py.bak')
        copyfile('template/test.py', 'src/' + pro_id + '.py')


if __name__ == "__main__":
    flags, pro_id = arg_parse()
    main(flags, pro_id)
