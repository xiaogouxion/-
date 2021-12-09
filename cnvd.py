from selenium import webdriver
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Chrome
import time
driver = webdriver.Chrome()
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {

  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
     })
  """
})


url="https://www.cnvd.org.cn/user/login"
driver.get(url)
'''driver.refresh()  # 刷新页面
html = driver.page_source
driver.refresh()
print("当前i=%d,leng=%d"%(list[i],leng))
driver.close()
'''
time.sleep(4)
img = driver.find_element_by_xpath('//*[@id="codeSpan"]').screenshot_as_png
chaojiying = Chaojiying_Client('xiaogouxion', 'xiaogouxion', '924150')
dic=chaojiying.PostPic(img, 1902)
yanzheng=dic['pic_str']
driver.find_element_by_xpath('//*[@id="email"]').send_keys("cnvd账号")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("cnvd密码")
driver.find_element_by_xpath('//*[@id="myCode"]').send_keys(yanzheng)
driver.find_element_by_xpath('/html/body/div[4]/div/form/div/p[5]/a/span').click()
time.sleep(2)

i=0
list1 = open("c.txt")
list2 = open("d.txt")
for a, b in zip(list1, list2):
    search_window = driver.current_window_handle
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/a[1]/span').click()
    search_window = driver.current_window_handle
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="softStyleId"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/form[1]/div[2]/div[10]/p/select/option[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="select2-param_province-container"]').click()
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys("未知")
    driver.find_element_by_xpath('/html/body/span/span/span[1]/input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="titlel"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[3]/div/div/form[1]/div[2]/div[12]/p/select/option[11]').click()
    driver.find_element_by_xpath('//*[@id="remoteCommandExecutionType"]').click()
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/form[1]/div[2]/div[13]/div[11]/p[1]/select/option[5]').click()
    driver.find_element_by_xpath('//*[@id="remoteCommandExecutionMiddleware"]').click()
    driver.find_element_by_xpath(
        '/html/body/div[3]/div/div/form[1]/div[2]/div[13]/div[11]/p[2]/select/option[7]').click()
    driver.find_element_by_xpath('//*[@id="unitName"]').send_keys("用友NC")
    driver.find_element_by_xpath('//*[@id="flowIP"]').send_keys(b)
    driver.find_element_by_xpath('//*[@id="remoteCommandExecutionTool"]').send_keys("在指定页面内容下存在命令执行，可直接写入命令 进行执行")
    driver.find_element_by_xpath('//*[@id="title"]').send_keys("用友NC存在命令执行")
    driver.find_element_by_xpath('//*[@id="url"]').send_keys(a)
    driver.find_element_by_xpath('//*[@id="description"]').send_keys(
        "用友NC对外开放了BeanShell的测试接口，未经身份验证的攻击者利用该测试接口，通过向目标服务器发送恶意构造的Http请求，在目标系统上直接执行任意代码，从而获得目标服务器权限")
    driver.find_element_by_xpath('//*[@id="tempWay"]').send_keys("更改删除此接口或者禁止访问")

    time.sleep(5)

    driver.find_element_by_xpath('//*[@id="flawAttFile"]').send_keys(r"D:\autoit\556.docx")

    time.sleep(30)
    i = i + 1
    print(i)


