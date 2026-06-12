from time import sleep
import pytest

''''@pytest.mark.smoke
def test_login():
    print("login page testcase")
@pytest.mark.p3
@pytest.mark.smoke
def test_trash():
    print("trash testcase")
@pytest.mark.reg
def test_compose():
    print("compose testcase")
@pytest.mark.p3
def test_bin():
    print("bin testcase")'''
'''class TestInsta:
    @pytest.mark.regression
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    def chat(self):
        print("chat testcase")
    def test_register(self):
        print("register testcase")'''
'''class TestInsta:
    @pytest.mark.regression
    @pytest.mark.high
    def test_post(self):
        print("post testcase")
    @pytest.mark.critical
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    @pytest.mark.low
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.high
    def test_register(self):
        print("register testcase")'''
''''@pytest.mark.imp
class TestInsta:
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class Testfb:
    def test_chat(self):
        print("chat testcase")
@pytest.mark.imp
class Testsample:
    def test_register(self):
        print("register testcase")'''
''''@pytest.mark.imp
class TestInsta:
    @pytest.mark.m1
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class Testfb:
    @pytest.mark.m2
    def test_chat(self):
        print("chat testcase")
    @pytest.mark.m1
    def test_register(self):
        print("register testcase")'''
''''@pytest.mark.m1
@pytest.mark.m2
@pytest.mark.m3
@pytest.mark.m4
@pytest.mark.m5
@pytest.mark.m6
def test_chat():
    print("chat testcase")'''

'''pytestmark = pytest.mark.smoke
def test_fun1():
    print("funtion testcase")
class TestSample:
    def test_tc1(self):
        print("test method1")
    def test_tc2(self):
        print("test method2")'''




