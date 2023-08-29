# Программа для перевода IP адреса и маски в двоичный формат
ip = input("Введите IP адрес: ")
mask = input("Введите маску: ")
ip = ip.split(".")
mask = mask.split(".")
ip_bin = []
mask_bin = []
err_msg_mask = ""


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

        ip_bin.append(i_octet)

print("IP -> ", ip_bin)



if len(mask) != 4:
    print("Маска не корректна")
    exit(0)
else:
    for i in mask:
        if int(i) < 0 or int(i) > 255:
            print("Значение одного из октетов не корректно.")
            exit(0)
        else:
            mask_octet = (bin(int(i))[2:])
            while len(mask_octet) < 8:
                mask_octet = "0" + mask_octet

            mask_bin.append(mask_octet)


if err_msg_mask != "":
    print(err_msg_mask)

print("MASK -> ", mask_bin)


