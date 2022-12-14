pi =[[12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1],
     [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
     [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
     [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
     [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
     [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
     [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
     [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]]

def fix_bin(num, length) -> str:
    return bin(num)[2:].zfill(length)

def gen_key_list(key) -> list:
    k_lst = []
    key = fix_bin(key, 256)
    for i in range(8):
        k_lst.append(key[32*i:32*(i+1)])
    return k_lst

def complement_block(a) -> str:
    if len(a) % 32 == 0:
        return a
    else:
        return a + '1' + (32-1-len(a))*'0'

def bit_shift(a) -> str:
    return a[11:] + a[0:11]

def a_to_list(a) -> list:
    lst = []
    temp = ''
    for i in range(8):
        temp = a[4*i:4*(i+1)]
        lst.append(temp)
    return lst

def replacement_table(a) -> str:
    res = ''
    q = ''
    a_lst = a_to_list(a)
    for i in range(8):
        res += fix_bin(pi[7-i][int(a_lst[i],2)], 4)
    return res

def summ_mod_2_step_32(a, k) -> int:
    if type(a) == str:
        a = int(a, 2)
    if type(k) == str:
        k = int(k, 2)
    return (a + k) % pow(2, 32)

def g(k, a) -> str:
    return bit_shift(replacement_table(fix_bin(summ_mod_2_step_32(a, k), 32)))

def G(k, a1, a0) -> tuple:
    if type(a0) == str:
        a0 = int(a0, 2)
    if type(a1) == str:
        a1 = int(a1, 2)
    t = int(g(k, a0) , 2) ^ a1
    return (fix_bin(a0, 32), fix_bin(t, 32))

def G_star(k, a1, a0) -> str:
    # return (g(k, a0) ^ a1) + a0
    if type(a0) == str:
        a0 = int(a0, 2)
    if type(a1) == str:
        a1 = int(a1, 2)
    t = int(g(k, a0) , 2) ^ a1
    return fix_bin(t, 32) + fix_bin(a0, 32)

def get_encrypt_keys(k_lst) -> list:
    p = [i for i in k_lst]
    k = []
    k.extend(p)
    k.extend(p)
    k.extend(p)
    p = [i for i in reversed(k_lst)]
    k.extend(p)
    return k

def encrypt(key, a) -> str:
    a = fix_bin(a, 64)
    a = complement_block(a)
    a1 = a[:32]
    a0 =  a[32:]
    k_lst = gen_key_list(key)
    k = get_encrypt_keys(k_lst)
    arg = (a1, a0)
    for i in range(31):
        arg = G(k[i], arg[0], arg[1])
    return G_star(k[31], arg[0], arg[1])

def get_decrypt_keys(k_lst) -> list:
    k = [i for i in k_lst]
    p = [i for i in reversed(k_lst)]
    k.extend(p)
    k.extend(p)
    k.extend(p)
    return k

def decrypt(key, a) -> str:
    a = fix_bin(a, 64)
    a = complement_block(a)
    a1 = a[:32]
    a0 =  a[32:]
    k_lst = gen_key_list(key)
    k = get_encrypt_keys(k_lst)
    arg = (a1, a0)
    for i in range(31,0,-1):
        arg = G(k[i], arg[0], arg[1])
    return G_star(k[0], arg[0], arg[1])