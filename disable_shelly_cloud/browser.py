from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def disable_cloud_new(ip: str):
    try:
        driver = webdriver.Firefox()
        driver.get(f"http://{ip}/#/settings/cloud")
        sleep(5)

        button = driver.find_element(by=By.ID, value="switch-0")
        button.click()

        driver.quit()
        return True
    
    except Exception as e:
        driver.quit()
        print(e)
        return False


def disable_cloud_old(ip: str):
    try:
        driver = webdriver.Firefox()
        driver.get(f"http://{ip}")
        sleep(5)

        #internet_tab = driver.find_element(by=By.CLASS_NAME, value="settings_tab").find_element(by=By.ID, value="internet")
        internet_tab = driver.find_element(by=By.XPATH, value='//*[@id="internet"]')
        internet_tab.click()

        cloud_div = driver.find_element(by=By.ID, value="cloud_settings")
        cloud_colapse = cloud_div.find_element(by=By.CLASS_NAME, value="colapse.closed")
        cloud_colapse.click()

        cloud_disable = driver.find_element(by=By.ID, value="cloud_disable")
        cloud_disable.click()

        confirm = driver.find_element(by=By.CLASS_NAME, value="btn.btn_yes")
        confirm.click()

        driver.quit()
        return True
    
    except Exception as e:
        driver.quit()
        print(e)
        return False