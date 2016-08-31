# -*- conding:utf8 -*-

import json

def load_json_from_file(path):
    with open(path, 'r') as f:
        obj = json.load(f)
        print (json.dumps(obj))

def take_shot(driver, name='', dir='screenshots/', ext='.png'):
    path = dir + name + ext
    driver.save_screenshot(path)

def wait():
     wait = WebDriverWait(driver, 3)
     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination")))
