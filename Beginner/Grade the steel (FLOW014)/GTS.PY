# for _ in range(int(input())):
#     h,c,t = int(input()).split()
for _ in range(int(input())):
    h,c,t = input().split()

    h_true = float(h) > 50
    c_true = float(c) < 0.7
    t_true = float(t) > 5600

    if (h_true and c_true and t_true):
        print(10)
    elif (h_true and c_true):
        print(9)
    elif (c_true and t_true):
        print(8)
    elif (h_true and t_true):
        print(7)
    elif (h_true or c_true or t_true):
        print(6)
    else:
        print(5)