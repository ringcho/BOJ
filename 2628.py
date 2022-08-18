x, y = map(int, input().split())
x_list = [0, x]
y_list = [0, y]
N = int(input())

for _ in range(N):
    axis, cut = map(int, input().split())
    if axis == 1:
        x_list.append(cut)
    else:
        y_list.append(cut)
x_list.sort()
y_list.sort()
max_area = 0
for i in range(1, len(y_list)):
    for j in range(1, len(x_list)):
        area = (x_list[j]-x_list[j-1])*(y_list[i]-y_list[i-1])
        if max_area < area:
            max_area = area
print(max_area)