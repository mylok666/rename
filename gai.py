import os


def replaceDirName(rootDir):
    dirs = os.listdir(rootDir)
    # 遍历每一个文件夹
    for i,dir in enumerate(dirs):
        # 输出老文件夹的名字
        print('oldname is:' + dir)


        # 主要目的是在数字统一为4位，不够的前面补0
        temp = "%02d" % int(i+1)

        # 老文件夹的名字
        oldname = os.path.join(rootDir, dir)
        # 新文件夹的名字
        newname = os.path.join(rootDir, temp)

        # 用新文件夹的名字替换老文件夹的名字
        # rename(*args, **kwargs):重命名文件或目录
        os.rename(oldname, newname)


if __name__ == '__main__':
    rootdir = './data/ped1/training'
    replaceDirName(rootdir)
