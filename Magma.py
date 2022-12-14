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
key = input('Введите секретный ключ')

file_name_choose = input('Введите:  \n 1 для чтения из open_text.txt (зашифрования) \n 2 для чтения из close_text.txt (расшифрования)  \n')
if file_name_choose == '1':
    fr = open('open_text.txt', encoding='utf-8')
    # text = []
    text = ''
    while True:
        letter = fr.read(1)
        if not letter:
            break
        # text.append(letter)
        text += letter
    fw = open('close_text.txt', 'w', encoding='utf-8')
    # m = Magma_functions.get_encrypt_block(text, n)
    # sym = RSA_functions.encrypt(m, e, n)
    # fw.write(sym) 
    for sym in Magma_functions.encrypt(key, text):
        fw.write(sym)
        # fw.write(sym.encode('utf-8').decode('utf-8'))

elif file_name_choose == '2':
    fr = open('close_text.txt', encoding='utf-8')
    # text = []
    text = ''
    while True:
        letter = fr.read(1)
        if not letter:
            break
        # text.append(letter)
        text += letter
    fw = open('open_text.txt', 'w', encoding='utf-8')
    # c = Magma_functions.get_decrypt_block(text, n)
    for sym in Magma_functions.decrypt(key, text):
        fw.write(sym)
        # fw.write(sym.encode('utf-8').decode('utf-8'))

fr.close()
fw.close()