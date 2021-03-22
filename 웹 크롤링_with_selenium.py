# request: 빠르게 스크래핑 가능하지만 javascript에 의한 동적인 환경에서는 스크래핑 불가
# Selenium: request보다 느리지만 사용자 시나리오대로 스크래핑이 가능

#selenium 사용한 웹 크롤링
def get_schedule(url):
    from selenium import webdriver
    import time
    from selenium.webdriver.common.keys import Keys
    
    result = []

    driver = webdriver.PhantomJS('./phantomjs')
    driver.get(url)
    time.sleep(1)

    driver.find_element_by_css_selector('#s9iPrd > svg').click()
    time.sleep(2)
    driver.find_element_by_css_selector('#yuynLe > ul > li:nth-child(5) > div.PsKE7e.r8s4j-R6PoUb.IKA38e.baH5ib > div > div').click()
    time.sleep(1)
    driver.find_element_by_css_selector('#yuynLe > ul > li:nth-child(5)').click()
    time.sleep(1)
    driver.find_element_by_css_selector('#yuynLe > ul > li:nth-child(5) > div.oGuwee.iJZYsf.jymhMd.Mkt3Tc > ul > li:nth-child(1) > div > div > a').click()
    time.sleep(1)
    text = driver.find_elements_by_css_selector('#h\.p_QRw1Ox9CU40P > div > div > ul')
    time.sleep(1)

    for i in text:
        result = i.text.split('\n')

    driver.close()
    return(result)

print(get_schedule('https://sites.google.com/view/kkbizintelligence/lab-home'))