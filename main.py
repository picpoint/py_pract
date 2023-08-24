# Программа для перевода IP адреса в двоичный формат
ip = input("Введите IP адрес: ")
ip = ip.split(".")
ip_bin = []

if len(ip) > 4 or len(ip) < 4:
    print("Введён некоректный IP")
else:
    for i in ip:
        if int(i) < 0 or int(i) > 255:
            print("Введённый IP некоректен")
            exit(0)
    for i in ip:
        i_octet = bin((int(i)))[2:]
        while len(i_octet) < 8:
            i_octet = "0" + i_octet

        print(i, " -> ", i_octet)
        ip_bin.append(i_octet)

print(ip_bin)