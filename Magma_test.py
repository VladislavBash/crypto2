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

class Summ_Mod_2_Step_32_Test(unittest.TestCase):
    def test_check_summ_mod_2_step_32(self):
        self.assertEqual(
            Magma_functions.summ_mod_2_step_32(bin(4294967296)[2:], bin(20)[2:]),
            20
        )

class g_Test(unittest.TestCase):
    def test_check_g_1(self):
        self.assertEqual(
            Magma_functions.g(0x87654321, 0xfedcba98),
            Magma_functions.fix_bin(0xfdcbc20c, 32)
        )

class G_Test(unittest.TestCase):
    def test_check_G(self):
        self.assertEqual(
            Magma_functions.G(0xffeeddcc, 0xfedcba98, 0x76543210),
            (Magma_functions.fix_bin(0x76543210, 32), Magma_functions.fix_bin(0x28da3b14, 32))
        )

class G_Star_Test(unittest.TestCase):
    def test_check_G_star(self):
        self.assertEqual(
            Magma_functions.G_star(0xffeeddcc, 0x239a4577, 0xc2d8ca3d),
            Magma_functions.fix_bin(0x4ee901e5c2d8ca3d, 64)
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

class Encrypt_Block_Test(unittest.TestCase):
    def test_check_encrypt_block(self):
        self.assertEqual(
            Magma_functions.encrypt_block(0xffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff, 0xfedcba9876543210),
            Magma_functions.fix_bin(0x4ee901e5c2d8ca3d, 64)
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

class Decrypt_Block_Test(unittest.TestCase):
    def test_check_decrypt_block(self):
        self.assertEqual(
            Magma_functions.decrypt_block(0xffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff, 0x4ee901e5c2d8ca3d),
            Magma_functions.fix_bin(0xfedcba9876543210, 64)
        )

class GOST_Test(unittest.TestCase):
    def test_check_replacement_table_1(self):
        self.assertEqual(
            Magma_functions.replacement_table(Magma_functions.fix_bin(0xfdb97531, 32)),
            Magma_functions.fix_bin(0x2a196f34, 32)
        )

    def test_check_replacement_table_2(self):
        self.assertEqual(
            Magma_functions.replacement_table(Magma_functions.fix_bin(0x2a196f34, 32)),
            Magma_functions.fix_bin(0xebd9f03a, 32)
        )
    
    def test_check_replacement_table_3(self):
        self.assertEqual(
            Magma_functions.replacement_table(Magma_functions.fix_bin(0xebd9f03a, 32)),
            Magma_functions.fix_bin(0xb039bb3d, 32)
        )
    
    def test_check_replacement_table_4(self):
        self.assertEqual(
            Magma_functions.replacement_table(Magma_functions.fix_bin(0xb039bb3d, 32)),
            Magma_functions.fix_bin(0x68695433, 32)
        )
    
    def test_check_g_1(self):
        self.assertEqual(
            Magma_functions.g(0x87654321, 0xfedcba98),
            Magma_functions.fix_bin(0xfdcbc20c, 32)
        )
    
    def test_check_g_2(self):
        self.assertEqual(
            Magma_functions.g(0xfdcbc20c, 0x87654321),
            Magma_functions.fix_bin(0x7e791a4b, 32)
        )
    
    def test_check_g_3(self):
        self.assertEqual(
            Magma_functions.g(0x7e791a4b, 0xfdcbc20c),
            Magma_functions.fix_bin(0xc76549ec, 32)
        )
    
    def test_check_g_4(self):
        self.assertEqual(
            Magma_functions.g(0xc76549ec, 0x7e791a4b),
            Magma_functions.fix_bin(0x9791c849, 32)
        )
    
    def test_check_get_encrypt_keys(self):
        k_lst = Magma_functions.gen_key_list(0xffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff)
        a = [Magma_functions.fix_bin(0xffeeddcc, 32), Magma_functions.fix_bin(0xbbaa9988, 32), Magma_functions.fix_bin(0x77665544, 32), Magma_functions.fix_bin(0x33221100, 32),
            Magma_functions.fix_bin(0xf0f1f2f3, 32), Magma_functions.fix_bin(0xf4f5f6f7, 32), Magma_functions.fix_bin(0xf8f9fafb, 32), Magma_functions.fix_bin(0xfcfdfeff, 32)]
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

    def test_check_encrypt_block(self):
        self.assertEqual(
            Magma_functions.encrypt_block(0xffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff, 0xfedcba9876543210),
            Magma_functions.fix_bin(0x4ee901e5c2d8ca3d, 64)
        )
    
    def test_check_decrypt_block(self):
        self.assertEqual(
            Magma_functions.decrypt_block(0xffeeddccbbaa99887766554433221100f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff, 0x4ee901e5c2d8ca3d),
            Magma_functions.fix_bin(0xfedcba9876543210, 64)
        )

if __name__ == '__main__':
    unittest.main() 