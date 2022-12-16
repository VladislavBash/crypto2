import Magma_functions
# choose = input('Введите:  \n 1 для ввода открытого и закрытого ключей  \n 2 для генерации открытого и закрытого ключей  \n')
# choose = input('Введите секретный ключ')

# # while True:

# if choose == '1':
#     # e, n = input('Введите открытый ключ (e, n) ').split()
#     key = input('Введите секретный ключ')
# elif choose == '2':
#     # open_key = get_random() # TO_DO FOR BIG NUMBERS
#     # close_key = get_random() # TO_DO FOR BIG NUMBERS
#     e, n, d = Magma_functions.gen_keys()
#     fw = open('keys.txt', 'w', encoding='utf-8')
#     fw.write('e     ' + str(e) +'\n')
#     fw.write('n     ' + str(n) +'\n')
#     fw.write('d     ' + str(d) +'\n')
#     fw.close()
#     print("e - ", e)
#     print("n - ", n)
#     print("d - ", d)
# e = int(e)
# n = int(n)
# d = int(d)

    # if check_keys(open_key, close_key):
    #     break
    # elif choose == '1':
    #     print('Ключи не подходят\n')
while True:
    key = input('Введите секретный ключ  ')
    if len(bin(int(key, 16))[2:]) == 256:
        break 
    print('Неправильный ввод, повторите попытку')

while True:
    chipering_choose = input('Введите:  \n 1 для чтения из open_text.txt (зашифрования) \n 2 для чтения из close_text.txt (расшифрования)  \n')
    if (chipering_choose == '1') or (chipering_choose == '2'):
        break
    print('Неправильный ввод, повторите попытку')

while True:
    choose = input('Введите:  \n 1 для работы с символами UTF-8 \n 2 для работы с 16-ичным кодом   \n 3 для работы с 2-ичным кодом   \n')
    if (choose == '1') or (choose == '2') or (choose == '3'):
        break
    print('Неправильный ввод, повторите попытку')

if chipering_choose == '1':
    fr = open('open_text.txt', encoding='utf-8')
    # text = []
    bin_text = ''
    while True:
        letter = fr.read(1)
        if not letter:
            break
        # text.append(letter)
        if choose == '1':
            bin_text += bin(ord(letter))[2:].zfill(8)
        elif choose == '2':
            bin_text += bin(int(letter, 16))[2:].zfill(4)
        elif choose == '3':
            bin_text += letter
    fw = open('close_text.txt', 'w', encoding='utf-8')
    # m = Magma_functions.get_encrypt_block(text, n)
    # sym = RSA_functions.encrypt(m, e, n)
    # fw.write(sym) 
    sym = Magma_functions.encrypt(key, bin_text)
    if choose == '1':
        for i in range(0, len(sym), 8):
            fw.write(chr(int(sym[i:i+4], 2)))
            fw.write(chr(int(sym[i+4:i+8], 2)))
    elif choose == '2':
        for i in range(0, len(sym), 8):
            fw.write(hex(int(sym[i:i+4], 2))[2:])
            fw.write(hex(int(sym[i+4:i+8], 2))[2:])
    elif choose == '3':
        fw.write(sym)
        # fw.write(sym.encode('utf-8').decode('utf-8'))

elif chipering_choose == '2':
    fr = open('close_text.txt', encoding='utf-8')
    # text = []
    bin_text = ''
    while True:
        letter = fr.read(1)
        if not letter:
            break
        # text.append(letter)
        if choose == '1':
            bin_text += bin(ord(letter))[2:].zfill(8)
        elif choose == '2':
            bin_text += bin(int(letter, 16))[2:].zfill(4)
        elif choose == '3':
            bin_text += letter
    fw = open('open_text.txt', 'w', encoding='utf-8')
    # c = Magma_functions.get_decrypt_block(text, n)
    sym = Magma_functions.decrypt(key, bin_text)
    if choose == '1':
        for i in range(0, len(sym), 8):
            fw.write(chr(int(sym[i:i+4], 2)))
            fw.write(chr(int(sym[i+4:i+8], 2)))
    elif choose == '2':
        for i in range(0, len(sym), 8):
            fw.write(hex(int(sym[i:i+4], 2))[2:])
            fw.write(hex(int(sym[i+4:i+8], 2))[2:])
    elif choose == '3':
        fw.write(sym)
        # fw.write(sym.encode('utf-8').decode('utf-8'))

fr.close()
fw.close()