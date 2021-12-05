# import time
# f = [[int(j[0]) for j in str(i).split(' ')] for i in open('day02/input')]
# f = [[print(j.format(time.sleep(1))) for j in i.split(' ')] for i in open('day02/input')]

# data = [0, 0, 0, 0]
# def calc(arr):
#     match(arr[0]):
#         case 'forward':
#             data[0] += arr[1]
#             data[3] += arr[1] * data[1]
#         case 'up':
#             data[2] -= arr[1]
#             data[1] -= arr[1]
#         case 'down':
#             data[2] += arr[1]
#             data[1] += arr[1]
# [calc([int(j) if j[:-1].isdigit() else j for j in i.split(' ')]) for i in open('day02/input')]
# print(data[0] * data[2])
# print(data[0] * data[3])

# data = {
#     'forward': float(),
#     'up': -int(),
#     'down': int()
# }

# def convert(arr):
#     match(arr[0]):
#         case 'forward':
#             return float(j[0])
#         case 'up':
# f = [convert(i.split(' ')) for i in open('day02/input')]
# print(f)

# method = {'forward': True,'up': False,'down': False}
# hoz = sum([int(i[-2:-1]) if method[i[:-3]] else 0 for i in open('day02/input')])
# method = {'forward': None,'up': False,'down': True}
# depth = sum([int(i[-2:-1]) if method[i[:-3]] else 0 for i in open('day02/input')])
# print(depth)

def day02():
    return day02_01(), day02_02()




# hoz = sum([int(i[-2:-1]) if len(i) == 10 else 0 for i in open('day02/input')])
# depth = sum([int(i[-2:-1]) if len(i) == 7 else -int(i[-2:-1]) if len(i) == 5 else 0 for i in open('day02/input')])
# print(hoz * depth)

def day02_01():
    return (sum([int(i[-2:-1]) if len(i) == 10 else 0 for i in open('day02/input')]) * sum([int(i[-2:-1]) if len(i) == 7 else -int(i[-2:-1]) if len(i) == 5 else 0 for i in open('day02/input')]))



# aim = sum([int(i[-2:-1]) if len(i) == 7 else -int(i[-2:-1]) if len(i) == 5 else 0 for i in open('day02/input')])



# hoz = sum([int(i[-2:-1]) if len(i) == 10 else 0 for i in open('day02/input')])
# depth = sum([int(i[-2:-1]) * aim if len(i) == 10 else cheat(i) for i in open('day02/input')])
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