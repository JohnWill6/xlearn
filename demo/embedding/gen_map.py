#coding=utf-8

import sys

def second_order(num_fields, start):
    fm  = {}
    idx = start
    for i in range(1, num_fields):
        for j in range(i+1, num_fields+1):
            fea = str(i) + " " + str(j)
            idx += 1
            fm[fea] = idx
    return fm

def main():
    num_fields = int(sys.argv[1])
    fea_map = {}
    fea_map.update(second_order(num_fields, len(fea_map)))
    for item in sorted(fea_map.items(), key=lambda x:x[1]):
        print str(item[1]) + " " + str(item[0])

if __name__ == "__main__":
    main()
