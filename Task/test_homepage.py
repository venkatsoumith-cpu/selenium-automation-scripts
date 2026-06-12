from DreamPortal_home import *
def test_homepage(launch):
    driver=launch
    d=DreamPortal_home(driver)
    d.lanimation()
    d.maincontent_displayed()
    assert d.maincontent_displayed()
    print("Loading animation completed successfully")
    d.MyDreams_displayed()
    assert d.MyDreams_displayed()
    print("My Dreams button displayed successfully")
    d.click_mydreams()
    windows=driver.window_handles
    assert len(windows)==3

