import sys
sys.stdin = open('2527_input.txt')

for i in range(4):
    x1, y1, x2, y2, nx1, ny1, nx2, ny2 = map(int, input().split())

    if x1 > nx1:
        x1, y1, x2, y2, nx1, ny1, nx2, ny2 = nx1, ny1, nx2, ny2, x1, y1, x2, y2

    '''
    sq1 = (x1, x2, y1, y2)
    sq2 = (nx1, nx2, ny1, ny2)
    '''

    if (x2 == nx1 and y2 == ny1) or (x2 == nx1 and ny2 == y1):
        print('c')
    elif y2 < ny1 or x2 < nx1 or ny2 < y1:
        print('d')
    elif x2 == nx1 or y2 == ny1 or ny2 == y1:
        print('b')
    else:
        print('a')