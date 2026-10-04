import pytest
'''class Testsample:
    def test_m1(self):
        print("method1")
    def test_m2(self):
        print("method2")'''
'''def test_m3():
    print("method3 testcase")
class TestGmail:
    def test_m4(self):
        print("composite testcase")
    def test_m5(self):
        print("Inbox testcase")'''
'''@pytest.mark.smoke
def test_login():
    print("loginpage testcase")
def test_trash():
    print("trashpage testcase")
@pytest.mark.smoke
def test_compose():
    print("compose testcase")
def test_bin():
    print("binpage testcase")'''
'''class TestInsta:
    @pytest.mark.regression
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
    @pytest.mark.regression
    def test_chat(self):
        print("chat testcase")'''
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
'''@pytest.mark.imp
class TestInsta:
    def test_post(self):
        print("post testcase")
    def test_story(self):
        print("story testcase")
class Testfb:
    def test_chat(self):
        print("chat testcase")
    def test_register(self):
        print("register testcase")'''
'''pytestmark=pytest.mark.smoke
def test_fun1():
    print("function testcase")
class Testsample:
    def test_tc1(self):
        print("tc1 testcase")
    def test_tc2(self):
        print("tc2 testcase")'''
'''def test_tc1():
    print("testcase1")
@pytest.mark.skip
def test_tc2():
    print("testcase2")
def test_tc3():
    print("testcase3")
@pytest.mark.skip
def test_tc4():
    print("testcase4")'''
'''testid=3423
def test_tc1():
    print("tc1 testcase")
@pytest.mark.skipif(testid in [5671,2233,3423,7890],reason="testcase not required")
def test_tc2():
    print("tc2 testcase")
def test_tc3():
    print("testcase3")'''
'''def test_chat1():
    print("chat testcase")
def test_status():
    print("status testcase")
def test_chat2():
    print("chat testcase")
@pytest.mark.xfail
def test_channel():
    print("channel testcase")'''





