from selenium import webdriver
import time


def fillDayForm(myUserName, myPassword):
    browser = webdriver.Firefox()
    url = "https://hsm.sspu.edu.cn/selfreport/Default.aspx"
    browser.get(url)
    usr = browser.find_element_by_id("username")
    usr.send_keys(myUserName)
    pas = browser.find_element_by_id("password")
    pas.send_keys(myPassword)
    button = browser.find_element_by_class_name("submit_button")
    button.click()
    url = "https://hsm.sspu.edu.cn/selfreport/DayReport.aspx"
    browser.get(url)
    temperature = browser.find_element_by_id("p1_TiWen-inputEl")
    temperature.send_keys("36")
    button = browser.find_element_by_id("p1_ctl00_btnSubmit")
    button.click()
    button = browser.find_element_by_id("fineui_24")
    button.click()
    browser.close()


if __name__ == "__main__":
    myUserName = "your username"
    myPassword = "your password"
    fillDayForm(myUserName, myPassword)
    print("done")
