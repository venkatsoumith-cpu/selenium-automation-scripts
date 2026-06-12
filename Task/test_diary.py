from diary_page import *
def test_dream_entries(driver):
    driver.get("https://arjitnigam.github.io/myDreams/dreams-diary.html")
    diary=DiaryPage(driver)
    rows=diary.get_rows()
    assert len(rows)==10
    for row in rows:
        cols=row.find_elements("tagname","td")
        dream_name=cols[0].text
        days_ago=cols[1].text
        dream_type=cols[2].text
        assert dream_name !=""
        assert days_ago !=""
        assert dream_type in ["Good","Bad"]