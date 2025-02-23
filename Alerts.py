from selenium.webdriver.common.by import By

class Handle_Alert:
    def __init__(self,driver):
        self.d=driver

    def DynamicButton(self):
        button = self.d.find_element(By.XPATH, "//button[@onclick='toggleButton(this)']")
        print(f"Before Click: {button.text}")
        button.click()
        print(f"After Click: {button.text}")

    def Popup(self):
        self.d.find_element(By.ID, "alertBtn").click()
        my_alert = self.d.switch_to.alert
        print(my_alert.text)
        my_alert.accept()

    def ConfirmationAlertbox(self):
        self.d.find_element(By.ID, "confirmBtn").click()
        MyAlert = self.d.switch_to.alert
        print(MyAlert.text)
        MyAlert.accept()

    def PromptAlert(self):
        self.d.find_element(By.ID, "promptBtn").click()
        Alert1 = self.d.switch_to.alert
        Alert1.send_keys("Prasanth")
        Alert1.accept()
        Response = self.d.find_element(By.ID, "demo")
        print(Response.text)



