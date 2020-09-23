from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time


def train_time():
    flag = True
    sit_flag = False
    print('請輸入日期 格式為yyyy/mm/dd\n')
    while flag:  # 正規化檢查format
        date = input()
        fm = re.compile('[0-9]{4}/[0-9]{2}/[0-9]{2}')
        if fm.match(date) == None:
            print('輸入錯誤')
            print('請重新輸入')
        else:
            lis = []
            lis = date.split('/')
            date = lis[0] + lis[1] + lis[2]
            flag = False
    st_stop = input('啟程站：\n')
    end_stop = input('抵達站：\n')

    arrive_time = input('請選擇出發時間或抵達時間：1.出發 2.抵達\n')
    if arrive_time == '1':
        ar_path = '//*[@id="queryForm"]/div/div[2]/div[2]/div[2]/div[1]/label'
    elif arrive_time == '2':
        ar_path = '//*[@id="queryForm"]/div/div[2]/div[2]/div[2]/div[2]/label'

    train_kind = input('請選擇車種：1.全部 2.對號 3.非對號\n')
    if train_kind == '1':
        xpath = '//*[@id="queryForm"]/div/div[3]/div[1]/div[2]/label[1]'
    elif train_kind == '2':
        xpath = '//*[@id="queryForm"]/div/div[3]/div[1]/div[2]/label[2]'
    elif train_kind == '3':
        xpath = '//*[@id="queryForm"]/div/div[3]/div[1]/div[2]/label[3]'

    sit_condition = input('請選擇轉乘條件：1.限直達 2.接受轉乘 3.指定轉乘\n')
    if sit_condition == '1':
        sit_path = '//*[@id="queryForm"]/div/div[1]/div[5]/div[2]/label[1]'
    elif sit_condition == '2':
        sit_path = '//*[@id="queryForm"]/div/div[1]/div[5]/div[2]/label[2]'
    elif sit_condition == '3':
        sit_flag = True
        sit_path = '//*[@id="queryForm"]/div/div[1]/div[5]/div[2]/label[3]'
        sit_time = input('請選擇轉乘時間： 1.20分以內 2.30分以內 3.50分以內\n')
        #        if sit_time =='1':
        #            c= 0
        #        elif sit_time =='2':
        #            c=1
        #        elif sit_time =='3':
        #            c=2
        #        sitt_path ='//*[@id="transWaitTimeMaxByMinute"]'
        sit_text = input('請輸入轉乘站：\n')
    # google chrome
    google_path = Options()
    google_path.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    auto_path = 'C:\\Users\\yu520530\\Desktop\\autochrome\\chromedriver.exe'
    global driver
    driver = webdriver.Chrome(executable_path=auto_path, options=google_path)
    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime')
    # select where
    btn = driver.find_element_by_link_text('依時刻')
    btn.click()

    # date
    da_te = driver.find_element_by_id('rideDate')
    da_te.clear()
    da_te.send_keys(date)
    # start station
    sta_te = driver.find_element_by_id('startStation')
    sta_te.send_keys(st_stop)
    # end station
    end_te = driver.find_element_by_id('endStation')
    end_te.send_keys(end_stop)
    # kind of train
    btn_trki = driver.find_element_by_xpath(xpath)
    btn_trki.click()
    # arrive
    driver.find_element_by_xpath(ar_path).click()
    # sit
    if sit_flag:
        driver.find_element_by_xpath(sit_path).click()
        # bugggggggggggggggggggggggggggggggg
        s = driver.find_element_by_id('transferDiv')
        s.send_keys(sit_text)
    #        driver.find_element_by_xpath(sitt_path).select_by_index(c)
    else:
        driver.find_element_by_xpath(sit_path).click()
    # select_btn
    btn_sel = driver.find_element_by_xpath('//*[@id="queryForm"]/div/div[3]/div[2]/input')
    btn_sel.click()


def train_station():
    flag = True
    print('請輸入日期 格式為yyyy/mm/dd\n')
    while flag:  # 正規化檢查format
        date = input()
        fm = re.compile('[0-9]{4}/[0-9]{2}/[0-9]{2}')
        if fm.match(date) == None:
            print('輸入錯誤')
            print('請重新輸入')
        else:
            lis = []
            lis = date.split('/')
            date = lis[0] + lis[1] + lis[2]
            flag = False
    station = input('請輸入車站名稱：')
    # google chrome
    google_path = Options()
    google_path.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    auto_path = 'C:\\Users\\yu520530\\Desktop\\autochrome\\chromedriver.exe'
    global driver
    driver = webdriver.Chrome(executable_path=auto_path, options=google_path)
    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime')
    # select where
    btn = driver.find_element_by_link_text('依車站')
    btn.click()
    # date
    da_te = driver.find_element_by_id('rideDate')
    da_te.clear()
    da_te.send_keys(date)
    # station
    sta_te = driver.find_element_by_id('station')
    sta_te.send_keys(station)
    # select_btn
    btn_sel = driver.find_element_by_xpath('//*[@id="queryForm"]/div[1]/div[4]/input')
    btn_sel.click()


def train_No():
    flag = True
    print('請輸入日期 格式為yyyy/mm/dd\n')
    while flag:  # 正規化檢查format
        date = input()
        fm = re.compile('[0-9]{4}/[0-9]{2}/[0-9]{2}')
        if fm.match(date) == None:
            print('輸入錯誤')
            print('請重新輸入')
        else:
            lis = []
            lis = date.split('/')
            date = lis[0] + lis[1] + lis[2]
            flag = False
    sta_no = input('請輸入車次名稱：\n')
    # google chrome
    google_path = Options()
    google_path.binary_location = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    auto_path = 'C:\\Users\\yu520530\\Desktop\\autochrome\\chromedriver.exe'
    global driver
    driver = webdriver.Chrome(executable_path=auto_path, options=google_path)
    driver.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime')
    # select where
    btn = driver.find_element_by_link_text('依車次')
    btn.click()
    # date
    da_te = driver.find_element_by_id('rideDate')
    da_te.clear()
    da_te.send_keys(date)
    # station
    sta_te = driver.find_element_by_id('trainNo')
    sta_te.send_keys(sta_no)
    # select_btn
    btn_sel = driver.find_element_by_xpath('//*[@id="queryForm"]/div/div[4]/input')
    btn_sel.click()


def start():
    choose = input('請選擇列車查詢方式:1.時刻 2.車站 3.車次')
    if choose in '1':
        train_time()
    elif choose in '2':
        train_station()
    elif choose in '3':
        train_No()


start()
