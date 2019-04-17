from functools import wraps
from sys import exit, stderr, stdout
from traceback import print_exc
import requests
import codecs
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from xvfbwrapper import Xvfb
import pyxvfb



def suppress_broken_pipe_msg(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except SystemExit:
            raise
        except:
            print_exc()
            exit(1)
        finally:
            try:
                stdout.flush()
            finally:
                try:
                    stdout.close()
                finally:
                    try:
                        stderr.flush()
                    finally:
                        stderr.close()

    return wrapper


@suppress_broken_pipe_msg
def main():
    #display = Xvfb()
    #display.start()
    for t in range(19,25):
        driver = webdriver.Firefox()
        driver.get(
            'https://docs.google.com/forms/d/1_rp9UTf9G3E-Qvy3lrz-XUxjnXFgw-2lVv9Z8Hury48/viewform?chromeless=1&edit_requested=true')
        # a = driver.find_element_by_id('mal_text')
        # a=driver.find_element_by_class_name("freebirdFormviewerViewItemsItemItemTitle exportItemTitle freebirdCustomFont")

        a = driver.find_element_by_css_selector(
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        # a.send_keys('test')
        # driver.findElement(By.cssSelector("#gLFyf").gLFyf).sendKeys("test");
        # a=driver.find_element_by_class_name('vdLsw gsfi')
        # a=driver.find_element_by_class_name("vdLsw gsfi")
        # i=0
        # print(y)
        # for i in range(5000,len(y)-1):
        #
        #     a.send_keys(y[i]+"\n")
        #     if i == 25000:
        #         break
        #     print(i)

        a.send_keys('49')
        a.send_keys(Keys.SPACE)
        a.send_keys(Keys.SPACE)
        print('sendinf space')
        a.send_keys(Keys.SPACE)
        a.send_keys(Keys.SPACE)
        a.send_keys(Keys.SPACE)
        a = driver.find_element_by_css_selector(
             "div.freebirdFormviewerViewNumberedItemContainer:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1)")
        # a.click()
        #a=driver.find_element_by_css_selector('div.freebirdFormviewerViewNumberedItemContainer:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(5) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
        a.click()
        a = driver.find_element_by_css_selector(
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
        a.send_keys('8')

        s1 = [
            'div.freebirdFormviewerViewNumberedItemContainer:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)',
            'div.freebirdFormviewerViewNumberedItemContainer:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)']

        # return 1 if random.random() < 0.5 else -1

        import random
        x = random.choice([0, 1])

        a = driver.find_element_by_css_selector(s1[x])
        print(x)
        a.click()

        if x == 1:
            a = driver.find_element_by_css_selector(
                'div.freebirdFormviewerViewNumberedItemContainer:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')
            a.click()
            a = driver.find_element_by_css_selector(
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)")
            a.click()
            mp = random.choice([0, 1, 2])
            mpl = [
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
            a = driver.find_element_by_css_selector(mpl[mp])
            a.click()
            mp = random.choice([0, 1])
            op = [
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(8) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(8) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
            a = driver.find_element_by_css_selector(op[mp])
            a.click()
            #a.send_keys(Keys.SPACE)
            #a.send_keys(Keys.SPACE)
            # 3 options
            kk = random.choice([0, 1])
            ll = [
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(2) > content:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)",
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(2) > content:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"]
            a = driver.find_element_by_css_selector(ll[kk])
            print('going')
            # driver.execute_script("window.scrollTo(0, 200)")

            a.click()
            time.sleep(5)
            kk = random.choice([0, 1])
            ll = [
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(3) > content:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)",
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(3) > content:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"]
            a = driver.find_element_by_css_selector(ll[kk])

            a.click()
            time.sleep(5)
            ll = [
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(4) > content:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"]
            a = driver.find_element_by_css_selector(ll[0])

            a.click()
            time.sleep(5)
            ll = [
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(5) > content:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"]
            a = driver.find_element_by_css_selector(ll[0])

            a.click()
            time.sleep(5)
            # how rahul
            a = driver.find_element_by_css_selector(
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(11) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)")

            a.click()
            # nda or etc
            a = driver.find_element_by_css_selector(
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(13) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")
            a.click()
            a = driver.find_element_by_css_selector(
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(14) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")
            a.click()
        else:
            a = driver.find_element_by_css_selector(
                'div.freebirdFormviewerViewNumberedItemContainer:nth-child(5) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)')

            a.click()
            a = driver.find_element_by_css_selector(
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(6) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")
            a.click()
            mp = random.choice([0, 1, 2])
            mpl = [
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(7) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
            a = driver.find_element_by_css_selector(mpl[mp])
            a.click()

            mp = random.choice([0, 1])
            op = [
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(8) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(8) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
            a = driver.find_element_by_css_selector(op[mp])
            a.click()
            # 3 options
            kk = random.choice([0, 1])
            ll = [
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(2) > content:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)",
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(2) > content:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"]
            a = driver.find_element_by_css_selector(ll[kk])
            print('going')
            #driver.execute_script("window.scrollTo(0, 200)")

            a.click()
            time.sleep(5)
            kk = random.choice([0, 1])
            ll = [
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(3) > content:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)",
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(3) > content:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"]
            a = driver.find_element_by_css_selector(ll[kk])


            a.click()
            time.sleep(5)
            ll = [
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(4) > content:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"]
            a = driver.find_element_by_css_selector(ll[0])

            a.click()
            time.sleep(5)
            ll = [
                "div.freebirdFormviewerViewItemsGridRowGroup:nth-child(5) > content:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)"]
            a = driver.find_element_by_css_selector(ll[0])

            a.click()
            time.sleep(5)
            # how rahul
            a = driver.find_element_by_css_selector(
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(11) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)")

            a.click()

            r = random.choice([0, 1])
            l = [
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(13) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(13) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
            a = driver.find_element_by_css_selector(l[r])
            a.click()

            l = [
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(14) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
                "div.freebirdFormviewerViewNumberedItemContainer:nth-child(14) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
            a = driver.find_element_by_css_selector(l[r])
            a.click()

        # time.sleep(10)
        k = random.choice([0, 1, 2])
        print(k, 'reahd')
        l = [
            'div.freebirdFormviewerViewNumberedItemContainer:nth-child(9) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)',
            'div.freebirdFormviewerViewNumberedItemContainer:nth-child(9) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)',
            'div.freebirdFormviewerViewNumberedItemContainer:nth-child(9) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(7) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)']
        a = driver.find_element_by_css_selector(l[k])
        a.click()
        # omen kumn etc
        r = random.choice([0, 1, 2])
        l = [
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(12) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(12) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(12) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
        a = driver.find_element_by_css_selector(l[r])
        a.click()

        a = random.choice([0, 1, 2])

        r = [
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(15) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(15) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(15) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
        l = driver.find_element_by_css_selector(r[a])
        l.click()

        r = [
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(16) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(16) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(16) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
        l = driver.find_element_by_css_selector(r[a])
        l.click()

        a = random.choice([0, 1, 2])

        r = [
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(17) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(17) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(17) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]

        l = driver.find_element_by_css_selector(r[a])

        l.click()
        print('gender', a)

        mf = [1,0,0, 1,0, 1,0, 1, 0,0,0,1, 1,0, 1,0, 1,0,0, 1, 1, 1, 0,1, 1]


        a = mf[t]

        r = [
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(18) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(18) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]

        l = driver.find_element_by_css_selector(r[a])
        l.click()
        print('ok till gender')

        a = random.choice([0, 1, 2, 3])
        l = [
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(19) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(4) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(19) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(19) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(2) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)",
            "div.freebirdFormviewerViewNumberedItemContainer:nth-child(19) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > content:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"]
        lll = driver.find_element_by_css_selector(l[a])
        lll.click()
        time.sleep(5)
        print('asdf all ok')
        a=driver.find_element_by_css_selector('.quantumWizButtonPaperbuttonDark > content:nth-child(3) > span:nth-child(1)')
        print('all ok yeas number:-',t)
        a.click()
        time.sleep(5)
        driver.close()

main()
#display.stop()