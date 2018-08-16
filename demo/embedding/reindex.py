#coding=utf-8
import sys

def main():
    num_fields = int(sys.argv[1])
    for line in sys.stdin:
        tokens = line.strip().split(" ")
        label = tokens[0]
        
        output = [label]
        feas = {}
        for item in tokens[1:]:
            fi, fv = item.split(":")
            if "_" in fi:
                s1, s2 = [int(i) for i in fi.split("_")]
                # 重新索引
                d = s1 * num_fields + s2
                feas[d] = fv
            else:
                feas[int(fi)] = fv
        output += [str(k) + ":" + str(feas[k]) for k \
                in sorted(feas.keys())]
        print " ".join(output)

if __name__ == '__main__':
    main()

