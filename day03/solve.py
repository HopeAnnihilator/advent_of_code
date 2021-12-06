def day03():
    f = open('day03/input', 'rb')
    f.readline(); l = f.tell(); f.seek(0, 2); eof = f.tell(); f.seek(0)
    data = {
        'file': f,
        'eof': eof,
        'linelen': l,
        'lines': int(eof / l) + 1,
        'gamma': '',
        'epsilon': '',
        'rowIter': [],
        'linesO': [i for i in range(int(eof / l) + 1)],
        'linesCO': [i for i in range(int(eof / l) + 1)],
        'rowIterTmp': [],
        'oxygenGen': '',
        'co2Scrubber': ''
    }
    return iterator(data)

def iterator(data):
    for i in range(1, data['linelen'] - 1):
        for _ in range(data['lines']):
            data['rowIter'].append(data['file'].read(1).decode())
            data['file'].seek(data['linelen'] - 1, 1)

        check_row(data, 'oxygenGen', 'linesO')
        check_row(data, 'co2Scrubber', 'linesCO')

        data['gamma'] += str(int(data['rowIter'].count('1') > data['lines'] / 2))

        data['rowIter'] = []
        data['file'].seek(i)

    data['epsilon'] = ''.join([str(int(i != '1')) for i in data['gamma']])
    return int(data['gamma'], 2) * int(data['epsilon'], 2), int(data['oxygenGen'], 2) * int(data['co2Scrubber'], 2)

def check_row(data, obj, objValues):
    data['rowIterTmp'] = [data['rowIter'][i] for i in data[objValues]]
    if len(data['rowIterTmp']) == 1:
        data[obj] += data['rowIterTmp'][0]
    else:
        match objValues:
            case 'linesO':
                data[obj] += str(int(data['rowIterTmp'].count('1') > len(data['rowIterTmp']) / 2))
            case 'linesCO':
                data[obj] += str(int(data['rowIterTmp'].count('1') < len(data['rowIterTmp']) / 2))

        n = 0
        while n < len(data[objValues]):
            val = data[objValues][n]
            if data['rowIter'][val] != data[obj][-1]:
                data[objValues].pop(data[objValues].index(val))
            else:
                n += 1