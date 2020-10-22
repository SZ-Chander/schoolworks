from selenium import webdriver
browser = webdriver.Chrome()
# browser = webdriver.Chrome(r'D:\games\chromedriver.exe')#if line 2 have bug,please delete line 2 and use line 3,the path in ()is your chromedriver, you need donwload and ready it.
url = 'http://172.18.255.14/a79.htm'

if __name__ == '__main__':
    browser.get(url)
    browser.find_element_by_xpath('//*[@id="edit_body"]/div[3]/div[1]/div/div[2]/div[1]/div/form/input[3]').send_keys('your_number')
    browser.find_element_by_xpath('//*[@id="edit_body"]/div[3]/div[1]/div/div[2]/div[1]/div/form/input[4]').send_keys('your_code')
    elment1 = browser.find_element_by_xpath('//*[@id="edit_body"]/div[3]/div[1]/div/div[2]/div[1]/div/form/input[2]')
    browser.execute_script("arguments[0].click();", elment1)
