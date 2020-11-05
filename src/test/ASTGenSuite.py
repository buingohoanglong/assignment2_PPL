import unittest
from TestUtils import TestAST
# from AST import *
from tool import *

class ASTGenSuite(unittest.TestCase):
    # Predefined test case
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var:x;"""
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    # Variable declaration test cases
    def test_var_dcl_1(self):
        """Simple program: int main() {} """
        input = """Var:x,y,z;"""
        expect = Program([VarDecl(Id("x"),[],None), VarDecl(Id("y"),[],None), VarDecl(Id("z"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_var_dcl_2(self):
        """Simple program: int main() {} """
        input = """Var:x[5], y[3][4];"""
        expect = Program([VarDecl(Id("x"),[5],None), VarDecl(Id("y"),[3,4],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_var_dcl_3(self):
        """Simple program: int main() {} """
        input = """Var:x = 5, y = 6;"""
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5)), VarDecl(Id("y"),[],IntLiteral(6))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_var_dcl_4(self):
        """Simple program: int main() {} """
        input = """Var:x = True, y = "This is a string";
        Var:a = 6, b = 7.5;"""
        expect = Program([VarDecl(Id("x"),[],BooleanLiteral(True)), VarDecl(Id("y"),[],StringLiteral("This is a string")), VarDecl(Id("a"),[],IntLiteral(6)), VarDecl(Id("b"),[],FloatLiteral(7.5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_var_dcl_5(self):
        """Simple program: int main() {} """
        input = """Var:x[3] = {1,2,3}, y[2][3] = {{4,5,6}, {7,8,9}};"""
        expect = Program([VarDecl(Id("x"),[3], ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])), VarDecl(Id("y"),[2,3], ArrayLiteral([ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)]),ArrayLiteral([IntLiteral(7),IntLiteral(8),IntLiteral(9)])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))

    # Function declaration test cases
    def test_func_dcl_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Parameter: n
            Body:
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("n"),[],None)], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_func_dcl_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Parameter: a[5],b,c[2][3]
            Body:
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"),[5],None), VarDecl(Id("b"),[],None), VarDecl(Id("c"),[2,3],None)], ([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_func_dcl_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: a = 7.5, b[5] = {1,2};
                Var: c[2][3];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([VarDecl(Id("a"),[],FloatLiteral(7.5)), VarDecl(Id("b"),[5],ArrayLiteral([IntLiteral(1), IntLiteral(2)])), VarDecl(Id("c"),[2,3],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_func_dcl_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Parameter: a,b
            Body:
                Var: c = 5;
                a = b + c;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)], ([VarDecl(Id("c"),[],IntLiteral(5))],[Assign(Id("a"), BinaryOp("+",Id("b"),Id("c")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_func_dcl_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Continue;
                Break;
                Return;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([],[Continue(), Break(), Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))

    # Assignment statement test cases
    def test_assign_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a[2][3] = 5;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([],[Assign(ArrayCell(Id("a"),[IntLiteral(2), IntLiteral(3)]), IntLiteral(5))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_assign_stmt_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = b + c * 5.6;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([],[Assign(Id("a"), BinaryOp("+", Id("b"), BinaryOp("*", Id("c"), FloatLiteral(5.6))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))

    def test_assign_stmt_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: a[5];
                a[5+b*2] = True;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([VarDecl(Id("a"),[5],None)],[Assign(ArrayCell(Id("a"),[BinaryOp("+", IntLiteral(5), BinaryOp("*", Id("b"), IntLiteral(2)))]), BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))

    def test_assign_stmt_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a[foo() + 5] = 4.5;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+",CallExpr(Id("foo"),[]),IntLiteral(5))]),FloatLiteral(4.5))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_assign_stmt_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                (foo() + a[1])[2] = foo()[1] + a[2];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(BinaryOp("+",CallExpr(Id("foo"),[]),ArrayCell(Id("a"),[IntLiteral(1)])),[IntLiteral(2)]),BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(1)]),ArrayCell(Id("a"),[IntLiteral(2)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    # If statement test cases
    def test_if_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                If a!=b Then a = b; EndIf.  
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [If([(BinaryOp("!=",Id("a"),Id("b")), [], [Assign(Id("a"),Id("b"))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_if_stmt_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                If a+b>c Then 
                    print("Greater than");
                ElseIf a+b < c Then
                    print("Less than");
                Else
                    print("Equal");
                EndIf.
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        If( \
                            [   \
                                (BinaryOp(">", BinaryOp("+",Id("a"),Id("b")), Id("c")), [],  [CallStmt(Id("print"), [StringLiteral("Greater than")])]), \
                                (BinaryOp("<", BinaryOp("+",Id("a"),Id("b")), Id("c")), [],  [CallStmt(Id("print"), [StringLiteral("Less than")])])  \
                            ],  \
                            (   \
                                [], \
                                [CallStmt(Id("print"), [StringLiteral("Equal")])]  \
                            )   \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_if_stmt_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                If isEqual(a,b) Then
                    Var: c; 
                    c = a - b;
                Else
                    Var: d[4][5] = {1,2,3};
                    d[2][3] = a + b;
                EndIf.
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        If( \
                            [   \
                                (CallExpr(Id("isEqual"),[Id("a"),Id("b")]), [VarDecl(Id("c"),[],None)],  [Assign(Id("c"),BinaryOp("-",Id("a"),Id("b")))]), \
                            ],  \
                            (   \
                                [VarDecl(Id("d"),[4,5],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))], \
                                [Assign(ArrayCell(Id("d"),[IntLiteral(2),IntLiteral(3)]), BinaryOp("+",Id("a"),Id("b")))]  \
                            )   \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_if_stmt_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                If True Then 
                ElseIf False Then
                Else
                EndIf.
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        If( \
                            [   \
                                (BooleanLiteral(True), [],  []), \
                                (BooleanLiteral(False), [],  [])  \
                            ],  \
                            (   \
                                [], \
                                []  \
                            )   \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_if_stmt_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                If True Then 
                    If False Then x = y; EndIf.
                Else
                    If True Then y = x; Else x = y; EndIf.
                EndIf.
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        If( \
                            [   \
                                (BooleanLiteral(True), [],  [If([(BooleanLiteral(False), [], [Assign(Id("x"),Id("y"))])],([],[]))]), \
                            ],  \
                            (   \
                                [], \
                                [If([(BooleanLiteral(True), [], [Assign(Id("y"),Id("x"))])],([],[Assign(Id("x"),Id("y"))]))]  \
                            )   \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    # While statement test cases
    def test_while_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: x = 0;
                While x < 100 Do x = x + 1; EndWhile.  
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([VarDecl(Id("x"),[],IntLiteral(0))], [While(BinaryOp("<",Id("x"),IntLiteral(100)), ([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_while_stmt_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                While True && False Do 
                EndWhile.  
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [While(BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)), ([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_while_stmt_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                While foo() =/= goo() Do
                    While foo() || goo() Do
                        x = y;
                    EndWhile. 
                EndWhile.  
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        While(  \
                            BinaryOp("=/=", CallExpr(Id("foo"),[]), CallExpr(Id("goo"),[])),    \
                            (   \
                                [], \
                                [While(BinaryOp("||",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[])), ([], [Assign(Id("x"),Id("y"))]))]  \
                            )   \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_while_stmt_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                While foo() =/= goo() Do
                    While !!foo() Do
                        Var: x, y[2][2][2] = {{{1,2},{3,4}},{{5,6},{7,8}}};
                    EndWhile. 
                EndWhile.  
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        While(  \
                            BinaryOp("=/=", CallExpr(Id("foo"),[]), CallExpr(Id("goo"),[])),    \
                            (   \
                                [], \
                                [While(UnaryOp("!",UnaryOp("!",CallExpr(Id("foo"),[]))), ([VarDecl(Id("x"),[],None), VarDecl(Id("y"),[2,2,2], ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]), ArrayLiteral([IntLiteral(3),IntLiteral(4)])]), ArrayLiteral([ArrayLiteral([IntLiteral(5),IntLiteral(6)]), ArrayLiteral([IntLiteral(7),IntLiteral(8)])])]))], []))]  \
                            )   \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_while_stmt_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                If True Then 
                    While True Do
                    EndWhile.
                EndIf.
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        If( \
                            [   \
                                (BooleanLiteral(True), [],  [While(BooleanLiteral(True), ([],[]))]), \
                            ],  \
                            (   \
                                [], \
                                []  \
                            )   \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    # Dowhile statement test cases
    def test_do_while_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: x = 0;
                Do x = x + 1; While x < 100 EndDo.  
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([VarDecl(Id("x"),[],IntLiteral(0))], [Dowhile(([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(1)))]), BinaryOp("<",Id("x"),IntLiteral(100)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_do_while_stmt_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Do While True && False
                EndDo.  
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Dowhile(([],[]), BinaryOp("&&",BooleanLiteral(True),BooleanLiteral(False)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_do_while_stmt_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Do
                    Do
                        x = y;
                    While foo() || goo()
                    EndDo.
                While foo() =/= goo() 
                EndDo.  
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        Dowhile(  \
                            (   \
                                [], \
                                [Dowhile(([], [Assign(Id("x"),Id("y"))]), BinaryOp("||",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[])))]  \
                            ),   \
                            BinaryOp("=/=", CallExpr(Id("foo"),[]), CallExpr(Id("goo"),[]))    \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_do_while_stmt_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Do
                    Do
                        Var: x, y[2][2][2] = {{{1,2},{3,4}},{{5,6},{7,8}}};
                    While !!foo()
                    EndDo. 
                While foo() =/= goo()
                EndDo.  
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        Dowhile(  \
                            (   \
                                [], \
                                [Dowhile(([VarDecl(Id("x"),[],None), VarDecl(Id("y"),[2,2,2], ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]), ArrayLiteral([IntLiteral(3),IntLiteral(4)])]), ArrayLiteral([ArrayLiteral([IntLiteral(5),IntLiteral(6)]), ArrayLiteral([IntLiteral(7),IntLiteral(8)])])]))], []), UnaryOp("!",UnaryOp("!",CallExpr(Id("foo"),[]))))]  \
                            ),   \
                            BinaryOp("=/=", CallExpr(Id("foo"),[]), CallExpr(Id("goo"),[]))    \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_do_while_stmt_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                If True Then 
                    Do
                    While True
                    EndDo.
                EndIf.
            EndBody."""
        expect = Program([  \
            FuncDecl(   \
                Id("foo"),  \
                [], \
                (   \
                    [], \
                    [   \
                        If( \
                            [   \
                                (BooleanLiteral(True), [],  [Dowhile(([],[]), BooleanLiteral(True))]) \
                            ],  \
                            (   \
                                [], \
                                []  \
                            )   \
                        )   \
                    ]   \
                )   \
            )   \
        ])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    # Break statement test cases
    def test_break_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Break;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))

    # Continue statement test cases
    def test_continue_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Continue;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))

    # Return statement test cases
    def test_return_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Return;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))

    def test_return_stmt_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Return foo(x+.y);
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Return(CallExpr(Id("foo"),[BinaryOp("+.",Id("x"),Id("y"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))

    def test_return_stmt_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Return a * (b-c) + 1;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Return(BinaryOp("+", BinaryOp("*", Id("a"), BinaryOp("-",Id("b"),Id("c"))), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))

    # Call statement and Function call expression test cases
    def test_call_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                thisIsAFunction();
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [CallStmt(Id("thisIsAFunction"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_call_stmt_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a_b_c_d(foo() + goo());
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [CallStmt(Id("a_b_c_d"), [BinaryOp("+", CallExpr(Id("foo"), []), CallExpr(Id("goo"), []))])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_func_call_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a[5][7] = foo(foo(x,y) \. foo(x+y, x-y));
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Assign(ArrayCell(Id("a"),[IntLiteral(5),IntLiteral(7)]), CallExpr(Id("foo"), [BinaryOp("\.", CallExpr(Id("foo"), [Id("x"),Id("y")]), CallExpr(Id("foo"), [BinaryOp("+",Id("x"),Id("y")), BinaryOp("-",Id("x"),Id("y"))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_func_call_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                foo(a[2][1])[1][2] = goo(a[1] + b[2])[2];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(CallExpr(Id("foo"),[ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(1)])]),[IntLiteral(1),IntLiteral(2)]),ArrayCell(CallExpr(Id("goo"),[BinaryOp("+",ArrayCell(Id("a"),[IntLiteral(1)]),ArrayCell(Id("b"),[IntLiteral(2)]))]),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_func_call_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                foo(foo(foo(foo(1))))[1] = foo(foo(1))[2];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(1)])])])]),[IntLiteral(1)]),ArrayCell(CallExpr(Id("foo"),[CallExpr(Id("foo"),[IntLiteral(1)])]),[IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    # For statement test cases
    def test_for_stmt_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                For (i=0, i<10, 2) Do
                    writeln(i);
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [For(Id("i"), IntLiteral(0), BinaryOp("<",Id("i"),IntLiteral(10)), IntLiteral(2), ([], [CallStmt(Id("writeln"), [Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_for_stmt_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                For (i=0, 1, 1) Do
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [For(Id("i"), IntLiteral(0), IntLiteral(1), IntLiteral(1), ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_for_stmt_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                For (i=0, 1, 1) Do
                    For (j=1, True, foo()) Do
                    EndFor.
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [For(Id("i"), IntLiteral(0), IntLiteral(1), IntLiteral(1), ([], [For(Id("j"), IntLiteral(1), BooleanLiteral(True), CallExpr(Id("foo"),[]), ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_for_stmt_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                For (i=0, 1, 1) Do
                    x = y + 1;
                EndFor.
                For (j=1, True, foo()) Do
                    y = x + 1;
                EndFor.
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [For(Id("i"), IntLiteral(0), IntLiteral(1), IntLiteral(1), ([], [Assign(Id("x"),BinaryOp("+",Id("y"),IntLiteral(1)))])),    For(Id("j"), IntLiteral(1), BooleanLiteral(True), CallExpr(Id("foo"),[]), ([], [Assign(Id("y"),BinaryOp("+",Id("x"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_for_stmt_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                For (i=0, 1, 1) Do
                    For (j=1, True, foo()) Do
                        y = x + 1;
                        Continue;
                    EndFor.   
                EndFor.
                For (j=1, True, foo()) Do
                    y = x + 1;
                    Break;
                EndFor.
                Return;                
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[For(Id("i"),IntLiteral(0),IntLiteral(1),IntLiteral(1),([],[For(Id("j"),IntLiteral(1),BooleanLiteral(True),CallExpr(Id("foo"),[]),([],[Assign(Id("y"),BinaryOp("+",Id("x"),IntLiteral(1))),Continue()]))])),For(Id("j"),IntLiteral(1),BooleanLiteral(True),CallExpr(Id("foo"),[]),([],[Assign(Id("y"),BinaryOp("+",Id("x"),IntLiteral(1))),Break()])),Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    # Exp1 test cases
    def test_exp1_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = (True == False) || (True != False);
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Assign(Id("x"), BinaryOp("||", BinaryOp("==",BooleanLiteral(True),BooleanLiteral(False)), BinaryOp("!=",BooleanLiteral(True),BooleanLiteral(False))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_exp1_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                y = (5e7 == 7e5) && ("abc" =/= "cba");
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Assign(Id("y"), BinaryOp("&&", BinaryOp("==",FloatLiteral(5e7),FloatLiteral(7e5)), BinaryOp("=/=",StringLiteral("abc"),StringLiteral("cba"))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_exp1_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = ({1,2} > {2,1}) <= (0xABC < 0o123);
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Assign(Id("a"), BinaryOp("<=", BinaryOp(">",ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(2),IntLiteral(1)])), BinaryOp("<",IntLiteral(0xABC),IntLiteral(0o123))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_exp1_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = (5.e+7 >. 7.e-5) >= (0xABC <. 0o123);
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Assign(Id("a"), BinaryOp(">=", BinaryOp(">.",FloatLiteral(5.e+7),FloatLiteral(7.e-5)), BinaryOp("<.",IntLiteral(0xABC),IntLiteral(0o123))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))


    def test_exp1_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = (0.0 >=. 0.01) <=. (0xABC >=. 0o123);
            EndBody."""
        expect = Program([FuncDecl(Id("foo"), [], ([], [Assign(Id("a"), BinaryOp("<=.", BinaryOp(">=.",FloatLiteral(0.0),FloatLiteral(0.01)), BinaryOp(">=.",IntLiteral(0xABC),IntLiteral(0o123))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    # Exp2 test cases
    def test_exp2_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = 5 + 3 + x - y;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),BinaryOp("-",BinaryOp("+",BinaryOp("+",IntLiteral(5),IntLiteral(3)),Id("x")),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_exp2_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                y = foo() -. goo(x+y+z, x+.y+.z) - 2;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("y"),BinaryOp("-",BinaryOp("-.",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[BinaryOp("+",BinaryOp("+",Id("x"),Id("y")),Id("z")),BinaryOp("+.",BinaryOp("+.",Id("x"),Id("y")),Id("z"))])),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_exp2_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = foo()[x+.(y-z)-.t];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[]),[BinaryOp("-.",BinaryOp("+.",Id("x"),BinaryOp("-",Id("y"),Id("z"))),Id("t"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_exp2_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = "this" + "is" - "a" +. {1,2,3};
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),BinaryOp("+.",BinaryOp("-",BinaryOp("+",StringLiteral("this"),StringLiteral("is")),StringLiteral("a")),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))


    def test_exp2_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a[x+.y][x-.y] = foo({1,2,3} +. {4,5,6});
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("+.",Id("x"),Id("y")),BinaryOp("-.",Id("x"),Id("y"))]),CallExpr(Id("foo"),[BinaryOp("+.",ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    # Exp3 test cases
    def test_exp3_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = 5 * 3 * x \ y;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),BinaryOp("\\",BinaryOp("*",BinaryOp("*",IntLiteral(5),IntLiteral(3)),Id("x")),Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_exp3_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                y = foo() \. goo(x*y*z, x*.y*.z) % 2;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("y"),BinaryOp("%",BinaryOp("\.",CallExpr(Id("foo"),[]),CallExpr(Id("goo"),[BinaryOp("*",BinaryOp("*",Id("x"),Id("y")),Id("z")),BinaryOp("*.",BinaryOp("*.",Id("x"),Id("y")),Id("z"))])),IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_exp3_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = foo()[x*.(y\z)\.t];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),ArrayCell(CallExpr(Id("foo"),[]),[BinaryOp("\.",BinaryOp("*.",Id("x"),BinaryOp("\\",Id("y"),Id("z"))),Id("t"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_exp3_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = "this" * "is" % "a" \. {1,2,3};
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),BinaryOp("\.",BinaryOp("%",BinaryOp("*",StringLiteral("this"),StringLiteral("is")),StringLiteral("a")),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))


    def test_exp3_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a[x*.y][x\.y] = foo({1,2,3} % {4,5,6});
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(Id("a"),[BinaryOp("*.",Id("x"),Id("y")),BinaryOp("\.",Id("x"),Id("y"))]),CallExpr(Id("foo"),[BinaryOp("%",ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    # Exp4 test cases
    def test_exp4_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = !y;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),UnaryOp("!",Id("y")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_exp4_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                y = !!!!!!!x;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("y"),UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",UnaryOp("!",Id("x")))))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    # Exp5 test cases
    def test_exp5_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = a + --b;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),BinaryOp("+",Id("a"),UnaryOp("-",UnaryOp("-",Id("b")))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_exp5_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = -a + -.-.-.b;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),BinaryOp("+",UnaryOp("-",Id("a")),UnaryOp("-.",UnaryOp("-.",UnaryOp("-.",Id("b"))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))


    def test_exp5_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                a = a + --.--.--.b;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("a"),BinaryOp("+",Id("a"),UnaryOp("-",UnaryOp("-.",UnaryOp("-",UnaryOp("-.",UnaryOp("-",UnaryOp("-.",Id("b")))))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    # Exp6, Exp7 test cases
    def test_exp6_7_1(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x[1[1[2]]] = (x+y)[3];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(Id("x"),[ArrayCell(IntLiteral(1),[ArrayCell(IntLiteral(1),[IntLiteral(2)])])]),ArrayCell(BinaryOp("+",Id("x"),Id("y")),[IntLiteral(3)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_exp6_7_2(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                (x+y)[x[2][x[3]]] = 1;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(BinaryOp("+",Id("x"),Id("y")),[ArrayCell(Id("x"),[IntLiteral(2),ArrayCell(Id("x"),[IntLiteral(3)])])]),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))


    def test_exp6_7_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x[2] = {1,2,3}[3] + {{1,2},{3,4}}[0][1];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(Id("x"),[IntLiteral(2)]),BinaryOp("+",ArrayCell(ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]),[IntLiteral(3)]),ArrayCell(ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]),[IntLiteral(0),IntLiteral(1)])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_exp6_7_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                foo()[foo()[1] + goo()[1]] = x[2][y[4][5]];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(ArrayCell(CallExpr(Id("foo"),[]),[BinaryOp("+",ArrayCell(CallExpr(Id("foo"),[]),[IntLiteral(1)]),ArrayCell(CallExpr(Id("goo"),[]),[IntLiteral(1)]))]),ArrayCell(Id("x"),[IntLiteral(2),ArrayCell(Id("y"),[IntLiteral(4),IntLiteral(5)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))


    def test_exp6_7_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = y[1][2][3][4][5];
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),ArrayCell(Id("y"),[IntLiteral(1),IntLiteral(2),IntLiteral(3),IntLiteral(4),IntLiteral(5)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    # Literal test cases
    def test_literal_1(self):   # ???
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = 0 + 199 - 0xFF * 0XABC \ 0o567 % 0O77;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),BinaryOp("-",BinaryOp("+",IntLiteral(0),IntLiteral(199)),BinaryOp("%",BinaryOp("\\",BinaryOp("*",IntLiteral(255),IntLiteral(2748)),IntLiteral(375)),IntLiteral(63))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_literal_2(self):   # ???
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = 12.0e3 +. 12e3 -. 12.e5 *. 12.0e3 \. 12000. % 120000e-1;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),BinaryOp("-.",BinaryOp("+.",FloatLiteral(12000.0),FloatLiteral(12000.0)),BinaryOp("%",BinaryOp("\.",BinaryOp("*.",FloatLiteral(1200000.0),FloatLiteral(12000.0)),FloatLiteral(12000.0)),FloatLiteral(12000.0))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))


    def test_literal_3(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = True || (False && !False);
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),BinaryOp("||",BooleanLiteral(True),BinaryOp("&&",BooleanLiteral(False),UnaryOp("!",BooleanLiteral(False)))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_literal_4(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: x = "This is a string", y = "";
                Var: z = **comment** "This \\n is \t a '" string '"";
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("x"),[],StringLiteral("This is a string")),VarDecl(Id("y"),[],StringLiteral("")),VarDecl(Id("z"),[],StringLiteral("This \\n is 	 a '\" string '\""))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,374))


    def test_literal_5(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: x = {}, y;
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("x"),[],ArrayLiteral([])),VarDecl(Id("y"),[],None)],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_literal_6(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: x = {{},{},{},{}};
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([]),ArrayLiteral([]),ArrayLiteral([]),ArrayLiteral([])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_literal_7(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                x = {{{1,2},{3,4},{5,6}},{{7,8},{9,10},{11,12}}};
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[Assign(Id("x"),ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(5),IntLiteral(6)])]),ArrayLiteral([ArrayLiteral([IntLiteral(7),IntLiteral(8)]),ArrayLiteral([IntLiteral(9),IntLiteral(10)]),ArrayLiteral([IntLiteral(11),IntLiteral(12)])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,377))


    def test_literal_8(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: x = {1,1.2,"string",True,{1,2,3}};
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("x"),[],ArrayLiteral([IntLiteral(1),FloatLiteral(1.2),StringLiteral("string"),BooleanLiteral(True),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_literal_9(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                Var: x = {**comment** {1,2 **comment**},    {3,**comment**4}};
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2)]),ArrayLiteral([IntLiteral(3),IntLiteral(4)])]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,379))


    def test_literal_10(self):
        """Simple program: int main() {} """
        input = """
        Function: foo
            Body:
                foo(1,2e5,"string",False,{1,2,3});
            EndBody."""
        expect = Program([FuncDecl(Id("foo"),[],([],[CallStmt(Id("foo"),[IntLiteral(1),FloatLiteral(2e5),StringLiteral("string"),BooleanLiteral(False),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)])])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

