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

def load_fmap(path):
    fmap = {i:str(i) for i in range(1, num_fields+1)}
    with open(path, "r") as fin:
        for line in fin:
            a, b, c = line.strip().split(" ")
            fmap[int(a) + num_fields + 1] = str(b) + "#" + str(c)

def main():
    num_fields = int(sys.argv[1]) + 1
    model_path = sys.argv[2]
    fi_path    = sys.argv[3]
    si = load_model(model_path)
    fmap = load_fmap(fi_path)
    
    single = []   # 单特征
    combine = []  # 组合特征
    for i in si:
        if i in fmap:
            if "_" in fmap[i]:
                combine.append(fmap[i])
            else:
                single.append(fmap[i])

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


