import unittest
import Magma_functions

class Fix_Bin_Test(unittest.TestCase):
    def test_check_fix_bin_1(self):
        self.assertEqual(
            Magma_functions.fix_bin(545, 32),
            22*'0' + '1000100001'
        )
    
    def test_check_fix_bin_2(self):
        self.assertEqual(
            Magma_functions.fix_bin(6452312, 32),
            9*'0' + '11000100111010001011000'
        )

class Pi_Test(unittest.TestCase):
    def test_check_pi(self):
        self.assertEqual(
            Magma_functions.pi[0][0],
            12
        )

class Gen_Key_List_Test(unittest.TestCase):
    def test_check_gen_key_list(self):
        self.assertEqual(
            Magma_functions.gen_key_list(92),
            ['00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000',
            '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000001011100']
        )

class Complement_Block_Test(unittest.TestCase):
    def test_check_complement_block_1(self):
        self.assertEqual(
            Magma_functions.complement_block('11100001101010001000101011010101'),
            '11100001101010001000101011010101'
        )
    def test_check_complement_block_2(self):
        self.assertEqual(
            Magma_functions.complement_block('111000011010100010001010'),
            '11100001101010001000101010000000'
        )

class Bit_Shift_Test(unittest.TestCase):
    def test_check_bit_shift(self):
        self.assertEqual(
            Magma_functions.bit_shift('11100001101010001000101011010101'),
            '01000100010101101010111100001101'
        )

class A_To_List_Test(unittest.TestCase):
    def test_check_a_to_list(self):
        self.assertEqual(
            Magma_functions.a_to_list('11100001101010001000101011010101'),
            ['1110','0001','1010','1000','1000','1010','1101','0101']
        )

class Replacement_Table_Test(unittest.TestCase):
    def test_check_replacement_table_1(self):
        self.assertEqual(
            Magma_functions.replacement_table('11100001101010001000101011010101'),
            '10111110100000000111011111010101'
        )

    def test_check_replacement_table_2(self):
        self.assertEqual(
            Magma_functions.replacement_table(bin(0xfdb97531)[2:]),
            Magma_functions.fix_bin(0x2a196f34, 32)
        )

class Summ_Mod_2_Step_32_Test(unittest.TestCase):
    def test_check_summ_mod_2_step_32(self):
        self.assertEqual(
            Magma_functions.summ_mod_2_step_32(bin(4294967296)[2:], bin(20)[2:]),
            20
        )

class g_Test(unittest.TestCase):
    def test_check_g(self):
        self.assertEqual(
            Magma_functions.g(),
            12
        )

class G_Test(unittest.TestCase):
    def test_check_G(self):
        self.assertEqual(
            Magma_functions.G(),
            12
        )

class G_Star_Test(unittest.TestCase):
    def test_check_G_star(self):
        self.assertEqual(
            Magma_functions.G_star(),
            12
        )

class Get_Encrypt_Keys_Test(unittest.TestCase):
    def test_check_get_encrypt_keys(self):
        k_lst = Magma_functions.gen_key_list(92)
        a = ['00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000',
            '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000001011100']
        b = a.copy()
        b.reverse()
        lst = []
        lst.extend(a)
        lst.extend(a)
        lst.extend(a)
        lst.extend(b)
        self.assertEqual(
            Magma_functions.get_encrypt_keys(k_lst),
            lst
        )

class Encrypt_Test(unittest.TestCase):
    def test_check_encrypt(self):
        self.assertEqual(
            Magma_functions.encrypt(),
            12
        )

class Get_Decrypt_Keys_Test(unittest.TestCase):
    def test_check_get_decrypt_keys(self):
        k_lst = Magma_functions.gen_key_list(92)
        a = ['00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000',
            '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000001011100']
        b = a.copy()
        b.reverse()
        lst = []
        lst.extend(a)
        lst.extend(b)
        lst.extend(b)
        lst.extend(b)
        self.assertEqual(
            Magma_functions.get_decrypt_keys(k_lst),
            lst
        )

class Decrypt_Test(unittest.TestCase):
    def test_check_decrypt(self):
        self.assertEqual(
            Magma_functions.decrypt(),
            12
        )

if __name__ == '__main__':
    unittest.main() 