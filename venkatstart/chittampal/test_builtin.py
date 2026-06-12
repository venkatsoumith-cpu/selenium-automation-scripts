from time import sleep
import pytest

'''class TestSample:
    def test_tc1(self):
        print("testcase1")
    @pytest.mark.skip(reason="low priority")
    def test_tc2(self):
        print("testcase2")
    def test_tc3(self):
        print("testcase3")
    @pytest.mark.skip(reason="not important")
    def test_tc4(self):
        print("testcase4")'''

'''@pytest.mark.skip(reason="all method are not required")
class TestSample:
    def test_tc1(self):
        print("testcase1")
    def test_tc2(self):
        print("testcase2")
class TestSimple:
    def test_tc3(self):
        print("testcase3")
    def test_tc4(self):
        print("testcase4")'''
'''testid = 3428
def test_TC1():
    print("testcas1")
@pytest.mark.skipif(testid in [5671, 2233, 3423, 7890], reason="test_case not required")
def test_TC2():
    print("testcas2")
def test_TC3():
    print("testcas3")'''
'''class TestExe:
    os="mac"
    def test_TC1(self):
        print("testcase1")
    @pytest.mark.skipif(os in ["linux","windows","mac"],reason="platform mismatch")
    def test_TC2(self):
        print("testcase2")
    def test_TC3(self):
        print("testcase3")'''
'''browser="IE"
class TestDemo:
    def test_TC1(self):
        print("method1 testcase")
    def test_TC2(self):
        print("method2 testcase")
    @pytest.mark.skipif(browser="IE",reason="IE not exists")
    class Testsample:
        def test_Tc3(self):
            print("method3 testcase")
        def test_TC4(self):
            print("method4 testcase")'''


