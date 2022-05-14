import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

### seleniumでのクリック関数を定義
def web_ck(driver,a_xpath,t_sleeptime) :
    driver.find_element_by_xpath(a_xpath).click()
    time.sleep(int(t_sleeptime))

### seleniumでのリスト選択関数を定義
def web_listselect(driver,a_xpath,b_value,t_sleeptime) :
    dropdown = driver.find_element_by_xpath(a_xpath)
    select = Select(dropdown)
    try :
        select.select_by_value(b_value)
    except :
        select.select_by_visible_text(b_value)
    time.sleep(int(t_sleeptime))

### seleniumでの入力関数を定義
def web_nyuryoku(driver,a_xpath,b_naiyou,t_sleeptime) :
    texts_title = driver.find_element_by_xpath(a_xpath)
    texts_title.send_keys(b_naiyou)
    time.sleep(int(t_sleeptime))

### seleniumでのセレクト関数を定義
def web_select(driver,a_xpath,t_sleeptime) :
    driver.find_element_by_xpath(a_xpath).select
    time.sleep(int(t_sleeptime))

### seleniumでのクリア関数を定義
def web_clear(driver,a_xpath,t_sleeptime) :
    driver.find_element_by_xpath(a_xpath).send_keys((Keys.CONTROL + "a"))
    driver.find_element_by_xpath(a_xpath).send_keys(Keys.DELETE)
    time.sleep(int(t_sleeptime))
