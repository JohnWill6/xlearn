#encoding=utf-8

import sys

def load_model(path):
    # non-zero index
    si = []
    with open(path, "r") as fin:
        i = 0
        for line in fin:
            i += 1
            if i < 7:
                continue
            else:
                w = float(line.strip())
                if w != 0:
                    si.append(i-6)
    return si

def main():
    num_fields = int(sys.argv[1])
    model = sys.argv[2]
    si = load_model(model)
    
    single = []   # 单特征
    combine = []  # 组合特征
    for i in si:
        if i <= num_fields:
            single.append(i)
        else:
            s1 = i/num_fields
            s2 = i%num_fields
            combine.append(str(s1)+"#"+str(s2))

    # 过滤掉的单特征
    filter = list(set(range(1, num_fields+1)) \
            - set(single))

    print "保留的单特征："
    for i in single:
        print i

    print "保留的组合特征："
    for i in combine:
        print i

    print "过滤的单特征"
    for i in filter:
        print i

if __name__ == "__main__":
    main()


