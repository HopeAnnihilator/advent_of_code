def day08():
    f = [[j.split(' ') for j in i.strip('\n').split(' | ')] for i in open('day08/input').readlines()]
    
    out = {'rows': []}
    lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

    for item in f:
        tmp = {}
        for i in range(10):   
            tmparr = [] 
            for val in item[0]:
                if len(val) == lengths[i]:
                    tmparr.append(''.join(sorted([i for i in val])))
            if len(tmparr) == 1:
                tmp[i] = tmparr[0]
            else:
                tmp[i] = tmparr

        tmp[6] = find_val(tmp[6], tmp[1])
        tmp[0] = find_val(tmp[0], intersection(tmp[6], tmp[4]))
        tmp[9].pop(tmp[9].index(tmp[6])); tmp[9].pop(tmp[9].index(tmp[0])); tmp[9] = tmp[9][0]
        tmp[5] = intersection(tmp[6], tmp[9])
        tmp[2].pop(tmp[2].index(tmp[5])); tmp[3].pop(tmp[3].index(tmp[5]))
        tmp[3] = find_val(tmp[3], str([i for i in tmp[6] if i not in intersection(tmp[6], tmp[5])][0]))
        tmp[2].pop(tmp[2].index(tmp[3])); tmp[2] = tmp[2][0]

        digits = [tmp[i] for i in tmp.keys()]
        total = ""
        for val in item[1]:
            val = ''.join(sorted([i for i in val]))
            i = digits.index(val)
            total += str(i)
            if i in out.keys():
                out[i] += 1
            else:
                out[i] = 1
        out['rows'].append(int(total))
    part1 = out[1] + out[4] + out[7] + out[8]
    part2 = sum(out['rows'])
    return part1, part2


def intersection(val1, val2):
    result = ""
    for i in val1:
        if i in val2:
            result += i
    return result


def find_val(vals, check):
    check = [i for i in check]
    for item in vals:
        item = [n for n in item]
        for i in check:
            if i not in item:
                return ''.join(item)
