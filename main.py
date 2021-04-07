
with open("nginx_logs.txt", "r", encoding='utf-8') as file:
    x = [line.split(" ") for line in file]
    for i in range(len(x)):
        p = (x[i][0], x[i][5], x[i][6])
        print(p)
