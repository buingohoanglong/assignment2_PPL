import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # Predefined testcases
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    # Test valid variable declaration
    def test_var_dcl_1(self):
        input = """Var: a = 5;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_var_dcl_2(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_var_dcl_3(self):
        input = """Var: c, d = 6, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_var_dcl_4(self):
        input = """Var: c, d = 6.5e-3, e, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_var_dcl_5(self):
        input = """Var: c, d = False, e = True, f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_var_dcl_6(self):
        input = """Var: m, n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_var_dcl_7(self):
        input = """Var: m = "This is a \\t string", n[10];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_var_dcl_8(self):
        input = """Var: a = 5;
        Var     : b=0.e3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_var_dcl_9(self):
        input = """Var: a = 5, b, c = 6;
        Var     : d=0.e3,   e = "string";
        Var : f = {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_var_dcl_10(self):
        input = """Var: a,b,c;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    # Test invalid variable declaration
    def test_invalid_var_dcl_1(self):
        input = """: a = 5;"""
        expect = "Error on line 1 col 0: :"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_invalid_var_dcl_2(self):   
        input = """b[2][3] = {{2,3,4},{4,5,6}};"""
        expect = "Error on line 1 col 0: b"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_invalid_var_dcl_3(self):
        input = """Var: c, d = 6, e, f,"""
        expect = "Error on line 1 col 20: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_invalid_var_dcl_4(self):
        input = """Var: c, d = 6.5e-3; e, f;"""
        expect = "Error on line 1 col 20: e"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_invalid_var_dcl_5(self):
        input = """Var c, d = False, e = True, f;"""
        expect = "Error on line 1 col 4: c"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    # Test valid function declaration
    def test_valid_func_dcl_1(self):
        input = """
Function: main
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_valid_func_dcl_2(self):
        input = """
Function: main
    Parameter: n
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_valid_func_dcl_3(self):
        input = """
Function: main
    Parameter: a,b[5],  c[2][3][4]
    Body:
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_valid_func_dcl_4(self):
        input = """
Function: main
    Body:
        Var : a = 1, b = 2;
        c = a + b;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_valid_func_dcl_5(self):
        input = """
Function: sum
    Body:
        Var : a = 1, b = 2;
        Var : c = 3;
        c = a + c;
        c = b + c;
        Return c;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    # Test invalid function declaration
    def test_invalid_func_dcl_1(self):  
        input = """Function: main"""
        expect = "Error on line 1 col 14: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_invalid_func_dcl_2(self):
        input = """
Function: main
    Parameter:
    Body:
    EndBody."""
        expect = "Error on line 4 col 4: Body"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_invalid_func_dcl_3(self):
        input = """
Function: main
    Parameter: n = 5
    Body:
    EndBody."""
        expect = "Error on line 3 col 17: ="
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_invalid_func_dcl_4(self):
        input = """
Function: main
    Parameter: a, b; c
    Body:
    EndBody."""
        expect = "Error on line 3 col 19: ;"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_invalid_func_dcl_5(self):
        input = """
Function: sum
    Parameter: n
    Body:
        c = a + b;
        Var : d = 5;
        d = d + c;
    EndBody."""
        expect = "Error on line 6 col 8: Var"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    # Test valid assignment statement
    def test_valid_assign_stmt_1(self):
        input = """
Function: sum
    Body:
        a = b + c + 5;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_valid_assign_stmt_2(self):
        input = """
Function: sum
    Body:
        a = {{1,2}, {3,4}, {5,6}};
        a[1] = {4,3};
        a[0][1] = 1;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))
    
    def test_valid_assign_stmt_3(self):
        input = """
Function: sum
    Parameter: n
    Body:
        a = {{1,2}, {3,4}, {5,6}};
        a[x] = {4,3};
        a[x+y][x-y] = {1,2};
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    # Test invalid assignment statement
    def test_invalid_assign_stmt_1(self):
        input = """
Function: sum
    Parameter: n
    Body:
        a = {{1,2}, {3,4}, {5,6}};
        a[0,1] = 1;
    EndBody."""
        expect = "Error on line 6 col 11: ,"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_invalid_assign_stmt_2(self):
        input = """
Function: sum
    Parameter: n
    Body:
        a = {{1,2}, {3,4}, {5,6}};
        a[0] = a[1] = {1,2};
    EndBody."""
        expect = "Error on line 6 col 20: ="
        self.assertTrue(TestParser.checkParser(input,expect,239))

    # Test valid if statement
    def test_valid_if_stmt_1(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        If a > 0 Then
            printStrLn("a is bigger than 0");
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_valid_if_stmt_2(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        Var: b = 6;
        If a > b Then
            printStrLn("a is bigger than b");
        Else
            printStrLn("a is smaller than b");
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_valid_if_stmt_3(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        Var: b = 6;
        If a > b Then
            printStrLn("a is bigger than b");
        ElseIf a < b Then
            printStrLn("a is smaller than b");
        Else
            printStrLn("a equals b");
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_valid_if_stmt_4(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        Var: b = 6;
        If a > b Then
            printStrLn("a is bigger than b");
        ElseIf a < b Then
            printStrLn("a is smaller than b");
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_valid_if_stmt_5(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        If a % 5 == 0 Then
            printStrLn("a % 5 == 0");
        ElseIf a % 5 == 1 Then
            printStrLn("a % 5 == 1");
        ElseIf a % 5 == 2 Then
            printStrLn("a % 5 == 2");
        ElseIf a % 5 == 3 Then
            printStrLn("a % 5 == 3");
        Else
            printStrLn("a % 5 == 4");
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    # Test invalid if statement
    def test_invalid_if_stmt_1(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        If (a > 0) :
            printStrLn("a is bigger than 0");
    EndBody."""
        expect = "Error on line 5 col 19: :"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_invalid_if_stmt_2(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        Var: b = 6;
        If a > b Then
            printStrLn("a is bigger than b");
        Else
            printStrLn("a is smaller than b");
    EndBody."""
        expect = "Error on line 10 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_invalid_if_stmt_3(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        Var: b = 6;
        If (a > b) Then
            printStrLn("a is bigger than b");
        Else If (a < b) Then
            printStrLn("a is smaller than b");
        Else
            printStrLn("a equals b");
        EndIf.
    EndBody."""
        expect = "Error on line 13 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_invalid_if_stmt_4(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        Var: b = 6;
        If a > b Then
            printStrLn("a is bigger than b");
        ElseIf a < b Then
            printStrLn("a is smaller than b");
        EndIf
    EndBody."""
        expect = "Error on line 11 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_invalid_if_stmt_5(self):
        input = """
Function: main
    Body:
        Var: a = 5;
        If a % 5 == 0 Then
            printStrLn("a % 5 == 0");
        ElseIf a % 5 == 1 Then
            printStrLn("a % 5 == 1");
        ElseIf a % 5 == 2 Then
            printStrLn("a % 5 == 2");
        ElseIf a % 5 == 3 Then
            printStrLn("a % 5 == 3");
        Else
            printStrLn("a % 5 == 4");
        Else
            printStrLn("??????");
        EndIf.
    EndBody."""
        expect = "Error on line 15 col 8: Else"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    # Test valid for statement
    def test_valid_for_stmt_1(self):
        input = """
Function: main
    Body:
        For (i = 0, i < 10, 1) Do
            printStrLn(string_of_int(i));
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_valid_for_stmt_2(self):
        input = """
Function: main
    Body:
        For (i = 0, True, (i+5) * 2) Do
            printStrLn(string_of_int(i));
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_valid_for_stmt_3(self):
        input = """
Function: main
    Body:
        For (i = 0, i < 10, 1) Do
            
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_valid_for_stmt_4(self):
        input = """
Function: main
    Body:
        For (i = 0, i < 10, 1) Do
            Var: j;
            j = i + 1;
            printStrLn(string_of_int(i + j));
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_valid_for_stmt_5(self):
        input = """
Function: main
    Body:
        Var: a[3][2] = {{1,2},{3,4},{5,6}};
        For (i = 0, i < 3, 1) Do
            For (j = 0, j < 2, 1) Do
                printStrLn(string_of_int(a[i][j]));
            EndFor.            
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    # Test invalid for statement
    def test_invalid_for_stmt_1(self):
        input = """
Function: main
    Body:
        For (i = 0, i < 10, 1 Do
            printStrLn(string_of_int(i));
        EndFor.
    EndBody."""
        expect = "Error on line 4 col 30: Do"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_invalid_for_stmt_2(self):
        input = """
Function: main
    Body:
        For (i = 0, True; (i+5) * 2) Do
            printStrLn(string_of_int(i));
        EndFor.
    EndBody."""
        expect = "Error on line 4 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_invalid_for_stmt_3(self):
        input = """
Function: main
    Body:
        For (i = 0, i < 10, ) Do
            i = i + 1;
        EndFor.
    EndBody."""
        expect = "Error on line 4 col 28: )"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_invalid_for_stmt_4(self):
        input = """
Function: main
    Body:
        For (i = 0, i < 10, 1) :
            Var: j;
            j = i + 1;
            printStrLn(string_of_int(i + j));
        EndFor.
    EndBody."""
        expect = "Error on line 4 col 31: :"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_invalid_for_stmt_5(self):
        input = """
Function: main
    Body:
        Var: a[3][2] = {{1,2},{3,4},{5,6}};
        For (i = 0, i < 3, 1) Do
            Var: j = 0;
            For ( , j < 2, 1) Do
                printStrLn(string_of_int(a[i][j]));
            EndFor.            
        EndFor.
    EndBody."""
        expect = "Error on line 7 col 18: ,"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    # Test valid while statement
    def test_valid_while_stmt_1(self):
        input = """
Function: main
    Body:
        Var: i = 0;
        While (i < 10) Do
            printStrLn(string_of_int(i));
            i =  i + 1;
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_valid_while_stmt_2(self):
        input = """
Function: main
    Body:
        Var: i = 0;
        While True Do
            printStrLn(string_of_int(i));
            i = (i+5) * 2;
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_valid_while_stmt_3(self):
        input = """
Function: main
    Body:
        Var: i = 0;
        While sqrt(i) < 10 Do
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_valid_while_stmt_4(self):
        input = """
Function: main
    Body:
        Var: i = 0;
        While (i < 10) Do
            Var: j;
            j = i + 1;
            printStrLn(string_of_int(i + j));
            i = i + 1;
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_valid_while_stmt_5(self):
        input = """
Function: main
    Body:
        Var: a[3][2] = {{1,2},{3,4},{5,6}}, i = 0;
        While i < 3 Do
            Var: j = 0;
            While j < 2 Do
                printStrLn(string_of_int(a[i][j]));
                j =  j + 1;
            EndWhile.
            i = i + 1;            
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))

    # Test invalid while statement
#     def test_invalid_while_stmt_1(self):
#         input = """
# Function: main
#     Body:
#         Var: i = 0;
#         While True 
#             printStrLn(string_of_int(i));
#             i =  i + 1;
#         EndWhile.
#     EndBody."""
#         expect = "Error on line 6 col 12: printStrLn"
#         self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_invalid_while_stmt_2(self):
        input = """
Function: main
    Body:
        Var: i = 0;
        While True Do
            printStrLn(string_of_int(i));
            i = (i+5) * 2;
    EndBody."""
        expect = "Error on line 8 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_invalid_while_stmt_3(self):    # ???
        input = """
Function: main
    Body:
        Var: i = 0;
        While i < 10 Do
        End While.
    EndBody."""
        expect = "E"
        self.assertTrue(TestParser.checkParser(input,expect,267))

#     def test_invalid_while_stmt_4(self):
#         input = """
# Function: main
#     Body:
#         Var: i = 0;
#         While (i < 10) :
#             Var: j;
#             j = i + 1;
#             printStrLn(string_of_int(i + j));
#             i = i + 1;
#         EndWhile.
#     EndBody."""
#         expect = "Error on line 5 col 23: :"
#         self.assertTrue(TestParser.checkParser(input,expect,268))

#     def test_invalid_while_stmt_5(self):
#         input = """
# Function: main
#     Body:
#         Var: a[3][2] = {{1,2},{3,4},{5,6}}, i = 0;
#         While i < 3 Do
#             Var: j = 0;
#             While  Do
#                 printStrLn(string_of_int(a[i][j]));
#                 j =  j + 1;
#             EndWhile.
#             i = i + 1;            
#         EndWhile.
#     EndBody."""
#         expect = "Error on line 7 col 19: Do"
#         self.assertTrue(TestParser.checkParser(input,expect,269))

    # Test valid do while statement
    def test_valid_do_while_stmt_1(self):
        input = """
Function: main
    Body:
        Var: i = 0;
        Do
            printStrLn(string_of_int(i));
            i =  i + 1;
        While (i < 10)
        EndDo.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_valid_do_while_stmt_2(self):
        input = """
Function: main
    Body:
        Var: a[3][2] = {{1,2},{3,4},{5,6}}, i = 0;
        Do
            Var: j = 0;
            Do
                printStrLn(string_of_int(a[i][j]));
                j =  j + 1;
            While j < 2
            EndDo.
            i = i + 1;   
        While i < 3         
        EndDo.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    # Test invalid do while statement
    def test_invalid_do_while_stmt_1(self):
        input = """
Function: main
    Body:
        Var: i = 0;
        Do
            printStrLn(string_of_int(i));
            i =  i + 1;
        While (i < 10)
        EndWhile.
    EndBody."""
        expect = "Error on line 9 col 8: EndWhile"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_invalid_do_while_stmt_2(self):
        input = """
Function: main
    Body:
        Var: a[3][2] = {{1,2},{3,4},{5,6}}, i = 0;
        Do
            Var: j = 0;
            Do
                printStrLn(string_of_int(a[i][j]));
                j =  j + 1;
            While j < 2
            i = i + 1;   
        While i < 3         
        EndDo.
    EndBody."""
        expect = "Error on line 11 col 12: i"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_invalid_do_while_stmt_3(self):
        input = """
Function: main
    Body:
        Var: a[3][2] = {{1,2},{3,4},{5,6}}, i = 0;
        Do
            Var: j = 0;
            Do :
                printStrLn(string_of_int(a[i][j]));
                j =  j + 1;
            While j < 2
            EndDo.
            i = i + 1;   
        While i < 3         
        EndDo.
    EndBody."""
        expect = "Error on line 7 col 15: :"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    # Test valid break/continue/return statement
    def test_valid_break_stmt(self):
        input = """
Function: main
    Body:
        For (i = 0, i < 10, 1) Do
            If (i % 10 == 5) Then
                Break;
            EndIf.
            i = i + 1;
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))

    def test_valid_continue_stmt(self):
        input = """
Function: main
    Body:
        Var: a[3][2] = {{1,2},{3,4},{5,6}}, i = 0;
        While i < 3 Do
            Var: j = 0;
            If i < j Then
                Continue;
            EndIf.
            While (j < 2) Do
                printStrLn(string_of_int(a[i][j]));
                j =  j + 1;
                If j == 3 Then
                    Continue;
                EndIf.
            EndWhile.
            i = i + 1;           
        EndWhile.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_valid_return_stmt_1(self):
        input = """
Function: main
    Body:
        Return 0;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_valid_return_stmt_2(self):
        input = """
Function: main
    Body:
        Return;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_valid_return_stmt_3(self):
        input = """
Function: main
    Body:
        Return x * (sqrt(y) \ (z + 1)) + sqrt(power(x,2) + power(y,2));
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    # Test valid call statement
    def test_valid_call_stmt_1(self):
        input = """
Function: main
    Body:
        printLn();
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))    

    def test_valid_call_stmt_2(self):
        input = """
Function: main
    Body:
        sqrt(x*x + y * y);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))    

    def test_valid_call_stmt_3(self):
        input = """
Function: main
    Body:
        sum(a,b,c,d,e,f);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))    

    def test_valid_call_stmt_4(self):
        input = """
Function: main
    Body:
        a(b(c(d(e(f())))));
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))    

    def test_valid_call_stmt_5(self):
        input = """
Function: main
    Body:
        sqrt(sum(power(x,2) , power(y,2)));
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))    

    # Test invalid call statement
    def test_invalid_call_stmt_1(self):
        input = """
Function: main
    Body:
        printLn()
    EndBody."""
        expect = "Error on line 5 col 4: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,285))    

    def test_invalid_call_stmt_2(self):
        input = """
Function: main
    Body:
        sqrt(x*x + y * y;
    EndBody."""
        expect = "Error on line 4 col 24: ;"
        self.assertTrue(TestParser.checkParser(input,expect,286))    

    def test_invalid_call_stmt_3(self):
        input = """
Function: main
    Body:
        sum(a,b;c,d,e,f);
    EndBody."""
        expect = "Error on line 4 col 15: ;"
        self.assertTrue(TestParser.checkParser(input,expect,287))    

    def test_invalid_call_stmt_4(self):
        input = """
Function: main
    Body:
        a(b(c(d(e(f();)))));
    EndBody."""
        expect = "Error on line 4 col 21: ;"
        self.assertTrue(TestParser.checkParser(input,expect,288))    

    def test_invalid_call_stmt_5(self): # ???
        input = """
Function: main
    Body:
        Sqrt(sum(power(x,2) , power(y,2)));
    EndBody."""
        expect = "S"
        self.assertTrue(TestParser.checkParser(input,expect,289))    

    # Test expression
    def test_expression_1(self):
        input = """
Function: main
    Body:
        x = a + b - c * d \ f % 5 ;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))    

    def test_expression_2(self):
        input = """
Function: main
    Body:
        sum(27 % 2 + (x - 5) * 9 \ 3, -y*5 - 3 + 9);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))    

    def test_expression_3(self):
        input = """
Function: main
    Body:
        sum(27. \. 3e-3 +. x*.2. -. 23., -.x +. (y+. -.3.));
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))    

    def test_expression_4(self):
        input = """
Function: main
    Body:
        x = True && !False || !(x && y);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))    

    def test_expression_5(self):
        input = """
Function: main
    Body:
        x = a >= b || a > c && (e <=. f || (e >=. g && a != c && b == d)) && e =/= f;
    EndBody."""
        expect = "Error on line 4 col 24: >"
        self.assertTrue(TestParser.checkParser(input,expect,294))    

    def test_expression_6(self):
        input = """
Function: main
    Body:
        a[3 + foo(2)] = a[b[2][3]] + 4;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))    

    def test_expression_7(self):
        input = """
Function: main
    Body:
        a[x * y - sum(x,y)] = a[b[sum(x,y) * 2][c[x*y][x \ y] - sqrt(power(x,2))]] * sqrt(power(x+y,x*y) + power(y));
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))    

    def test_expression_8(self):
        input = """
Function: main
    Body:
        x[1*7][2.-.3.] = foo(a[2][b[4]+1] - a[c[2][3]][c[4][5]]);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))    

    def test_expression_9(self):
        input = """
Function: main
    Body:
        x = a[4][b[5][6]] >. b[c+d][c-d] || !(x&&y || !x&&y); 
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))    

    def test_expression_10(self):
        input = """
Function: main
    Body:
        x = x -. -.(-.y);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))    


    # Test full program
    def test_full_program_1(self):
        input = """Var: x;
Function: fact
    Parameter: n
        Body:
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.
Function: main
    Body:
        x = 10;
        fact (x);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))

    def test_full_program_2(self):
        input = """Var: x[5] = {1,2,3,4,5};
Function: sum
    Parameter: x[5]
        Body:
            Var: sum = 0;
            For (i = 0 , i < 5, 1) Do
                sum = sum + i;
            EndFor.
            Return sum;
        EndBody.
Function: main
    Body:
        sum(x);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_full_program_3(self):
        input = """
Function: radius
    Parameter: x,       y
        Body:
            Var: radius;
            radius = sqrt(x*x + y*y);
            Return radius;
        EndBody.
Function: main
    Body:
        Var : x = 3, y = 4;
        radius(x,   y);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))

    def test_full_program_4(self):
        input = """
Function: radius
    Parameter: x,       y
        Body:
            Var: radius;
            radius = sqrt(x*.x +. y*.y);
            Return radius;
        EndBody.
Function: main
    Body:
        Var : x = 3.5e0, y = 4.6e-0;
        radius(x,   y);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,303))

    def test_full_program_5(self):
        input = """Var: string_list[4] = {"","","","",""};
Function: get_string_list
    Parameter: list[4]
        Body:
            Var : str_input = "";
            For (i = 0 , i < 4, 1) Do
                str_input = read();
                list[i] = str_input;
            EndFor.
            Return list;
        EndBody.
Function: print_string_list
    Parameter: list[4]
        Body:
            For (i = 0 , i < 4, 1) Do
                printStrLn(list[i]);
            EndFor.
        EndBody.
Function: main
    Body:
        print_string_list(string_list);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,304))

    def test_full_program_6(self):
        input = """
** This is a global variable **
Var: arr[5] = {5,   7, 1,2, 6};

** Sort function **
Function: sort
    Parameter: arr[5]
    Body:
        For (i = 0, i < 5, 1) Do
            For (j = i + 1, j < 5, 1) Do
                If arr[i] < arr[j] Then
                    Var: temp;
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                EndIf.
            EndFor.
        EndFor.
        Return arr;
    EndBody.

** Entry of program **
Function: main
    Body:
        For (i = 0, i < 5, 1) Do
            print(string_of_int(arr[i]));
            print(" ");
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,305))

    def test_full_program_7(self):
        input = """Var: arr[4] = {"This", "is", "a", "testcase"};
** This
* is
* a
* block
* comment ** 
Function: printSth
    Parameter: arr[4]
    Body:
        Var : count = 0;
        While count < 100 Do
            If (count % 3 == 0) || (count % 5 == 0) Then
                printLn("Skip");
                Continue;
            ElseIf (count % 4 == 0) Then
                Break;
            EndIf.
            For (i = 0 , i < 4, 1) Do
                print(string_to_int(arr[i]));
                print(" ");
            EndFor.
            count = count + -1 + 1;
        EndWhile.
    EndBody.

Function: main
    Body:
        printSth(arr);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,306))

    def test_full_program_8(self):
        input = """Var: a[5][6][3]={12,2,5,{65,9,5}};
Function: thisIsAFunction
    Parameter: kdhgf82734jsdh,h44qa43t,r,qrra,az
    Body:
            If (x + foo(5)[6]) Then
                jgf348dh(**lsokf**sfle,zugse, 0, 8+9+7);
                Continue;
            ElseIf True == False Then
                (x + y)
            Else
                return {1,2,3}[1];
            EndIf.
    EndBody.

Function: dcmasci
    Parameter: t4t2, a4, m_34dwq, {}
    Body:
        Var: tngh[7645+ts87443]={};
        Break;
    EndBody."""
        expect = "Error on line 10 col 12: Else"
        self.assertTrue(TestParser.checkParser(input,expect,307))

    def test_full_program_9(self):
        input = """Var: a = {2,3};
Function: x
    Parameter: a
    Body:
        foo()[x + y] = {1,2,3,4}[2] + foo(z);
    EndBody.
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,308))

    def test_full_program_10(self):
        input = """           
Function: foo
    Parameter: a , v , asd[6][21]
    Body:
        Var: a_b_c = 7;
        a_b_c[x + y + foo(z)[0]] = (foo(z))[foo(z)] + foo(z);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,309))
