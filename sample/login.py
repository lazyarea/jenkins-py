# -*- conding:utf8 -*-

def divide(num1, num2):
  """josan"""
  return num1 / num2

def login(driver, url, email, passwd, wait=5):
    driver.implicitly_wait( wait )
    driver.get( url )
    driver.find_element_by_xpath('//*[@id="pbhello"]/span/a').click()
    driver.find_element_by_id('username').send_keys(email)
    driver.find_element_by_id('passwd').send_keys(passwd)
    driver.find_element_by_xpath('//*[@id="persistent"]').click()
    driver.find_element_by_xpath('//*[@id=".save"]').click()


def logout(driver, wait=5):
    driver.find_element_by_link_text("ログアウト").click()
