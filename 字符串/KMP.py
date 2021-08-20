# coding: utf-8

'''
date: 2021/6/2
content:

实现KMP算法
'''

def get_next(l):
    nxt = []
    nxt.append(0)  # next数组第一位是0
    x = 1
    front = 0      # front表示前缀的长度，也表示失配时对应的前一位的next数组中的值

    while x < len(l):
        if l[x] == l[front]:
            front += 1
            x += 1
            nxt.append(front)
        elif front:
            front = nxt[front-1]
        else:
            nxt.append(0)
            front += 1
    return nxt

def search(s, p, nxt):
    point_s = 0  # 主串的指针
    point_p = 0  # 模式串的指针

    while point_s < len(s):
        if s[point_s] == p[point_p]:
            point_s += 1
            point_p += 1
        elif point_p:
            point_p = nxt[point_p - 1]
        else:
            point_s += 1

        if point_p == len(p):
            print(point_s - len(p))
            point_p = nxt[point_p - 1]  #

    return


if __name__ == '__main__':
    s = 'abcdabcfabcfabce'
    p = 'abcf'
    next_table = get_next(p)
    search(s, p, next_table)







