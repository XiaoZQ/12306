def postition():
    char = input("数图片号码：")
    # dis = 80
    # mid = 40
    pos_dot = ''
    pos_dict = {
        1:'32,37,',
        2:'113,42,',
        3:'179,41,',
        4:'256,42,',
        5:'28,120,',
        6:'109,117,',
        7:'180,118,',
        8:'254,118,'
    }

    tmpList = char.split(',')
    for i in tmpList:
        # row_mpg = (int(i)-1)//4
        # col_mpg = (int(i)-1) % 4
        # pos_dot += str(col_mpg*dis + mid) + ',' + str(row_mpg*dis + mid) + ','
        pos_dot += pos_dict[int(i)]
    return pos_dot[:-1]


if __name__ == '__main__':
    print(postition())
