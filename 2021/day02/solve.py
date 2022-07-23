def day02():
    return day02_01(), day02_02()

def day02_01():
    return (sum([int(i[-2:-1]) if len(i) == 10 else 0 for i in open('day02/input')]) * sum([int(i[-2:-1]) if len(i) == 7 else -int(i[-2:-1]) if len(i) == 5 else 0 for i in open('day02/input')]))

aim = 0
def cheat(i):
    global aim
    if i.startswith('down'):
        aim += int(i[-2:-1])
    else:
        aim -= int(i[-2:-1])
    return 0
    
def day02_02():
    return(sum([int(i[-2:-1]) if len(i) == 10 else 0 for i in open('day02/input')]) * sum([int(i[-2:-1]) * aim if len(i) == 10 else cheat(i) for i in open('day02/input')]))