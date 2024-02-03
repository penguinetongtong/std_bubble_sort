# 버블정렬 오름차순 정렬
a = [90, 39, 2, 1,100, 30000, 230240, -1, -3 , -5000, -10000000000]
N = len(a)

for j in range(1, N):
    for i in range(N-j):
        if a[i] < a[i + 1]:
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
print(a)

# for i in range(N - 1): # N -1 = 3
#     if a[i] > a[i + 1]:
#         temp = a[i]
#         a[i] = a[i + 1]
#         a[i + 1] = temp
# print(N - 1, "번 회전 : ", a)
# for i in range(N - 2): # 2
#     if a[i] > a[i + 1]:
#         temp = a[i]
#         a[i] = a[i + 1]
#         a[i + 1] = temp
# print(N - 2, "번 회전 : ", a)
#
# for i in range(N - 3): # 1
#     if a[i] > a[i + 1]:
#         temp = a[i]
#         a[i] = a[i + 1]
#         a[i + 1] = temp
# print(N - 3, "번 회전 : ", a)

