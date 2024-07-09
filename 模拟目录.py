class file():#定义文件类型，包含上级文件，此文件名，文件内容
    def __init__(self,father,name):
        file.father = father
        file.name = name
        file.son = []
file_0 = file(-1,'0')

#用一个列表直接存储所有文件，文件类用来存关系
files = []
files.append(file_0)
located = 0#当前打开文件在files的索引

while True:
    line = input().split()#将输入转换为长度为2的列表，第一个元素是命令。第二个是操作文件名
    cmdkey = line[0]
    if len(line) > 1:
        newfile = line[1]#操作文件名

    if cmdkey == 'mkdir':#在该文件下新建一个文件
        for j in files:
            if newfile == j.name:#判断是否已经存在
                print('文件已存在')
                continue
            else:
                class file():  # 定义文件类型，包含上级文件，此文件名，文件内容
                    def __init__(self, father, name):
                        file.father = father
                        file.name = name
                        file.son = []
                new = file(files[located].name,newfile)
                files[located].son.append(new)
                files.append(new)
                print('新建文件',newfile)
                break
    if cmdkey == 'cd':#cd
        if newfile == '..':#返回0号文件
            located = 0
        else:#打开文件
            for i in files:
                if i.name == line[1]:
                    located = files.index(i)#当前打开文件索引切换为所命令的
                    print('进入文件',i.name)
                    break

    if cmdkey == 'pwd':
        path = ''
        path = '/'+files[located].name +path
        while located > 0:
            for k in files:
                if k.name == files[located].father:
                    located = files.index(k)  # 当前打开文件索引切换为所命令的
                    path = '/'+files[located].name + path
                    break
        print(path)
    if cmdkey == 'get':
        for l in files:
            print(l.father,l.name,l.son)
