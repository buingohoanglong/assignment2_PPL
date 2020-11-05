import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    # Test normal identifier
    def test_normal_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("aBc", "aBc,<EOF>",1))

    def test_normal_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("a1c", "a1c,<EOF>",2))

    def test_normal_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("a_c", "a_c,<EOF>",3))

    def test_normal_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("a", "a,<EOF>",4))

    def test_normal_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>",5))

    # Test invalid identifier   ?????????
    def test_invalid_identifier_1(self):
        self.assertTrue(TestLexer.checkLexeme("Abc", "Error Token A",6))

    def test_invalid_identifier_2(self):
        self.assertTrue(TestLexer.checkLexeme("_bc", "Error Token _",7))     

    def test_invalid_identifier_3(self):
        self.assertTrue(TestLexer.checkLexeme("9bc", "9,bc,<EOF>",8))     

    def test_invalid_identifier_4(self):
        self.assertTrue(TestLexer.checkLexeme("a:bc", "a,:,bc,<EOF>",9))     

    def test_invalid_identifier_5(self):
        self.assertTrue(TestLexer.checkLexeme("ABC", "Error Token A",10))    

    # Test normal integer literal
    def test_normal_int_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme("123", "123,<EOF>",11))  

    def test_normal_int_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>",12))  

    def test_normal_int_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme("0x123", "0x123,<EOF>",13))  

    def test_normal_int_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme("0xDEF", "0xDEF,<EOF>",14))  

    def test_normal_int_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme("0X123", "0X123,<EOF>",15))  

    def test_normal_int_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme("0XDEF", "0XDEF,<EOF>",16))  

    def test_normal_int_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme("0o123", "0o123,<EOF>",17))  

    def test_normal_int_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme("0o567", "0o567,<EOF>",18))  

    def test_normal_int_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme("0O123", "0O123,<EOF>",19))  

    def test_normal_int_literal_10(self):
        self.assertTrue(TestLexer.checkLexeme("0O567", "0O567,<EOF>",20))  

    # Test invalid integer literal
    def test_invalid_int_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme("0123", "0,123,<EOF>",21))  

    def test_invalid_int_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme("00123", "0,0,123,<EOF>",22))  

    def test_invalid_int_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme("1A2", "1,Error Token A",23))  

    def test_invalid_int_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme("12A", "12,Error Token A",24))  

    def test_invalid_int_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme("0x0123", "0,x0123,<EOF>",25))  

    def test_invalid_int_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme("0XAGB", "0XA,Error Token G",26))  

    def test_invalid_int_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme("0XABG", "0XAB,Error Token G",27))  

    def test_invalid_int_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme("0o0123", "0,o0123,<EOF>",28))  

    def test_invalid_int_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme("0O182", "0O1,82,<EOF>",29))  

    def test_invalid_int_literal_10(self):
        self.assertTrue(TestLexer.checkLexeme("0O128", "0O12,8,<EOF>",30)) 

    # Test normal float literal
    def test_normal_float_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3", "12.0e3,<EOF>",31)) 

    def test_normal_float_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e-3", "12.0e-3,<EOF>",32)) 

    def test_normal_float_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e+3", "12.0e+3,<EOF>",33)) 

    def test_normal_float_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme("0.012E3", "0.012E3,<EOF>",34)) 

    def test_normal_float_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme("0.0e3", "0.0e3,<EOF>",35)) 

    def test_normal_float_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme("12e3", "12e3,<EOF>",36)) 

    def test_normal_float_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme("0E12", "0E12,<EOF>",37)) 

    def test_normal_float_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme("0e012", "0e012,<EOF>",38)) 

    def test_normal_float_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme("0e0", "0e0,<EOF>",39)) 

    def test_normal_float_literal_10(self):
        self.assertTrue(TestLexer.checkLexeme("12.e3", "12.e3,<EOF>",40)) 

    def test_normal_float_literal_11(self):
        self.assertTrue(TestLexer.checkLexeme("0.E3", "0.E3,<EOF>",41)) 

    def test_normal_float_literal_12(self):
        self.assertTrue(TestLexer.checkLexeme("12000.", "12000.,<EOF>",42)) 

    def test_normal_float_literal_13(self):
        self.assertTrue(TestLexer.checkLexeme("0.", "0.,<EOF>",43)) 

    def test_normal_float_literal_14(self):
        self.assertTrue(TestLexer.checkLexeme("120000e-1", "120000e-1,<EOF>",44)) 

    def test_normal_float_literal_15(self):
        self.assertTrue(TestLexer.checkLexeme("000.000", "000.000,<EOF>",45)) 

    # Test invalid float literal
    def test_invalid_float_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme(".0e-3", ".,0e-3,<EOF>",46))  # why . ?

    def test_invalid_float_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme(".0e3", ".,0e3,<EOF>",47))  # why . ?

    def test_invalid_float_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme("e+3", "e,+,3,<EOF>",48)) 

    def test_invalid_float_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme("0.0e", "0.0,e,<EOF>",49)) 

    def test_invalid_float_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme("0.0+3", "0.0,+,3,<EOF>",50)) 

    def test_invalid_float_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme(".e3", ".,e3,<EOF>",51)) # why . ?

    def test_invalid_float_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme(".3", ".,3,<EOF>",52)) # why . ?

    def test_invalid_float_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme("0e3.12", "0e3,.,12,<EOF>",53)) # why . ?

    def test_invalid_float_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>",54)) 

    def test_invalid_float_literal_10(self):
        self.assertTrue(TestLexer.checkLexeme("12e^3", "12,e,Error Token ^",55)) 

    # Test normal string literal
    def test_normal_string_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcABC" """, """abcABC,<EOF>""",56))     

    def test_normal_string_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc`~xyz" """, """abc`~xyz,<EOF>""",57))     

    def test_normal_string_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc!xyz" """, """abc!xyz,<EOF>""",58))     

    def test_normal_string_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc@xyz" """, """abc@xyz,<EOF>""",59))     

    def test_normal_string_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc#xyz" """, """abc#xyz,<EOF>""",60))     

    def test_normal_string_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc$xyz" """, """abc$xyz,<EOF>""",61))     

    def test_normal_string_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc%xyz" """, """abc%xyz,<EOF>""",62))     

    def test_normal_string_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc^yz" """, """abc^yz,<EOF>""",63))     

    def test_normal_string_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc&xyz" """, """abc&xyz,<EOF>""",64))     

    def test_normal_string_literal_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc*xyz" """, """abc*xyz,<EOF>""",65))     

    def test_normal_string_literal_11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc()xyz" """, """abc()xyz,<EOF>""",66))     

    def test_normal_string_literal_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc_-xyz" """, """abc_-xyz,<EOF>""",67))     

    def test_normal_string_literal_13(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc+=xyz" """, """abc+=xyz,<EOF>""",68))     

    def test_normal_string_literal_14(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc{}xyz" """, """abc{}xyz,<EOF>""",69))     

    def test_normal_string_literal_15(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc|xyz" """, """abc|xyz,<EOF>""",70))     

    def test_normal_string_literal_16(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc:;xyz" """, """abc:;xyz,<EOF>""",71))     

    def test_normal_string_literal_17(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\'xyz" """, """abc\\'xyz,<EOF>""",72))     

    def test_normal_string_literal_18(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"xyz" """, """abc'"xyz,<EOF>""",73))     

    def test_normal_string_literal_19(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc<,xyz" """, """abc<,xyz,<EOF>""",74))     

    def test_normal_string_literal_20(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc.>xyz" """, """abc.>xyz,<EOF>""",75))     

    def test_normal_string_literal_21(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc?/xyz" """, """abc?/xyz,<EOF>""",76))     

    def test_normal_string_literal_22(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\\\xyz" """, """abc\\\\xyz,<EOF>""",77))     

    def test_normal_string_literal_23(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\bxyz" """, """abc\bxyz,<EOF>""",78))     

    def test_normal_string_literal_24(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\fxyz" """, """abc\\fxyz,<EOF>""",79))     

    def test_normal_string_literal_25(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\rxyz" """, """abc\\rxyz,<EOF>""",80))     

    def test_normal_string_literal_26(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\nxyz" """, """abc\\nxyz,<EOF>""",81))     

    def test_normal_string_literal_27(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\txyz" """, """abc\\txyz,<EOF>""",82))     

    def test_normal_string_literal_28(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc xyz" """, """abc xyz,<EOF>""",83))     

    def test_normal_string_literal_29(self):
        self.assertTrue(TestLexer.checkLexeme(""" "" """, """,<EOF>""",84))     

    def test_normal_string_literal_30(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc  xyz" """, """abc  xyz,<EOF>""",85))   

    # Test invalid string literal
    def test_invalid_string_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc"xyz" """, """abc,xyz,Unclosed String:  """,86))
    def test_invalid_string_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc"def"xyz" """, """abc,def,xyz,<EOF>""",87))   

    def test_invalid_string_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc'xyz" """, """Illegal Escape In String: abc'x""",88)) 

    def test_invalid_string_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\'xyz" """, """Illegal Escape In String: abc'x""",89))

    def test_invalid_string_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abcxyz """, """Unclosed String: abcxyz """,90))   

    def test_invalid_string_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\xyz" """, """Illegal Escape In String: abc\\x""",91))   

    def test_invalid_string_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\"xyz" """, """abc,xyz,Unclosed String:  """,92))   

    def test_invalid_string_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\"xyz" """, """Illegal Escape In String: abc\\\"""",93))   

    def test_invalid_string_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\nxyz" """, """Unclosed String: abc""",94))   # ???

    def test_invalid_string_literal_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc"'xyz" """, """abc,Error Token '""",95))   

    # Test normal array
    def test_normal_array_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme("{1, 2, 3, 4, 5}", "{,1,,,2,,,3,,,4,,,5,},<EOF>",96)) 

    def test_normal_array_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme("{{1, 2}, {4, 5}, {3, 5}}", "{,{,1,,,2,},,,{,4,,,5,},,,{,3,,,5,},},<EOF>",97))

    def test_normal_array_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme("{}", "{,},<EOF>",98)) 

    # Test invalid array
    def test_invalid_array_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme("{1,2,3,4,5", "{,1,,,2,,,3,,,4,,,5,<EOF>",99))

    def test_invalid_array_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme("{{1, 2}, {4, 5, {3, 5}}}", "{,{,1,,,2,},,,{,4,,,5,,,{,3,,,5,},},},<EOF>",100))    



    # Predefined testcases
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

