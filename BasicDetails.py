from selenium.webdriver.common.by import By

class Details:
    def __init__(self,driver):
        self.d = driver

    def Input(self):
        self.d.find_element(By.ID,"name").send_keys("Santhanaprasanth")
        self.d.find_element(By.ID, "email").send_keys("santhana.kane@gmail.com")
        self.d.find_element(By.ID, "phone").send_keys("7777776430")
        self.d.find_element(By.ID, "textarea").send_keys("123/3,main cross street, kelambakkam, chennai-600506")
        #d.find_element(By.ID, "field1")






