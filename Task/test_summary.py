from summary_page import *
def test_summary(driver):
    driver.get("https://arjitnigam.github.io/myDreams/dreams-total.html")
    summary=SummaryPage(driver)
    text=summary.get_page_text()
    assert "Good Dreams: 6" in text
    assert "Bad Dreams: 4" in text
    assert "Total Dreams: 10" in text
    assert "Recurring Dreams: 2" in text
    stext=summary.summary_text()
    assert "Flying over mountains" in stext
    assert "Lost in maze" in stext