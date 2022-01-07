import datetime
from selenium import webdriver
import time
import schedule


# On Break / Resume
def break_resume():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.get("http://worklogin.cdnsolutionsgroup.com/index.php/userlog/logtimecal")

    # user ID/Pass
    username = driver.find_element_by_id("exampleInputEmail")
    password = driver.find_element_by_id("exampleInputPassword")

    # Shree
    # username.send_keys("shivamshrivastava@cdnsol.com")
    # password.send_keys("cdn123")

    # Anl
    username.send_keys("anilchourasiya@cdnsol.com")
    password.send_keys("anil@1992")

    driver.find_element_by_name("submit").click()
    # Stop program for 2 secs so that page can load properly
    time.sleep(2)
    button_start = driver.find_element_by_id('starttime')
    button_stop = driver.find_element_by_id('stoptime')
    try:
        button_start.click()
    except Exception:
        button_stop.click()
    time.sleep(15)


# log-out at 11:55pm every day if not done manually
def logout():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    driver.get("http://worklogin.cdnsolutionsgroup.com/index.php/userlog/logtimecal")

    # user ID/Pass
    username = driver.find_element_by_id("exampleInputEmail")
    password = driver.find_element_by_id("exampleInputPassword")

    # username.send_keys("")
    # password.send_keys("")

    username.send_keys("")
    password.send_keys("")

    driver.find_element_by_name("submit").click()
    # Stop program for 2 secs so that page can load properly
    time.sleep(2)

    button_end_day_dropdown1 = driver.find_element_by_class_name(u'navbar-toggler')
    button_end_day_dropdown1.click()
    time.sleep(2)

    button_end_day = driver.find_element_by_id('navbarDropdown')
    button_end_day.click()
    time.sleep(2)

    button_end_day = driver.find_element_by_id('endtime')
    button_end_day.click()
    time.sleep(3)

    button_end_day = driver.find_element_by_class_name('confirm')
    button_end_day.click()
    time.sleep(2)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def job():
    print("I am doing this job!")


# schedule.every().monday.at("22:05").do(job)
schedule.every().tuesday.at("22:36").do(break_resume)
schedule.every().tuesday.at("22:37").do(break_resume)
# schedule.every().wednesday.at("14:00").do(job)
# schedule.every().thursday.at("14:00").do(job)
# schedule.every().friday.at("14:00").do(job)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Automate stuffs')
    # break_resume()
    logout()
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
