from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class Launch:
    def __init__(self, driver):
        self.d = driver

    def PickDate(self):
        Value = self.d.find_element(By.ID,"datepicker")
        Value.click()
        Date = "25"
        Month = "August"
        Year = "2027"
        while True:
             MY_Year = self.d.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text.strip()
             MY_Month = self.d.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text.strip()
             if MY_Year == str(Year) and MY_Month == str(Month):
                print(MY_Year, "&", MY_Month)
                break
             else:
                 if MY_Year < str(Year) or (MY_Year == str(Year) and MY_Month != Month):
                     nav_button = self.d.find_element(By.XPATH, "//span[text()='Next']")
                 else:
                     nav_button = self.d.find_element(By.XPATH, "//span[text()='Prev']")
                 nav_button.click()
        My_Date = self.d.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr[4]/td/a")
        for Dates in My_Date:
            if Dates.text == Date:
                Dates.click()
                break
        print(f"Selected Date :{Value.get_attribute('value')}")

    def DatePick2(self):
        Value1 = self.d.find_element(By.XPATH,"//input[@id='txtDate']")
        Value1.click()
        Date1 = "8"
        Month1 = "Apr"
        Year1 = "2015"
        MMonth = self.d.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
        MMonth.click()
        Month_Select = Select(MMonth)
        Month_Select.select_by_visible_text(Month1)
        YYear = self.d.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
        YYear.click()
        Year_Select = Select(YYear)
        Year_Select.select_by_visible_text(Year1)
        My_Date1 = self.d.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr[2]/td/a")
        for Dates1 in My_Date1:
            if Dates1.text == Date1:
                Dates1.click()
                break
        print(f"Selected Date :{Value1.get_attribute('value')}")

    def DatePick3(self):
        self.d.find_element(By.XPATH,"//input[@id='start-date']").send_keys("08-04-1998")
        self.d.find_element(By.XPATH,"//input[@id='end-date']").send_keys("22-02-2025")
        self.d.find_element(By.XPATH,"//button[@class='submit-btn']").click()
        DateRange = self.d.find_element(By.ID,"result")
        print(DateRange.text)

    def DoubleClick(self):
        act = ActionChains(self.d)
        try:
            ClickOn =  self.d.find_element(By.ID,"field1")
            act.double_click(ClickOn).perform()
            act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
            act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
            Field2 = self.d.find_element(By.ID,"field2")
            Field2.click()
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
            print("Text copied from field1 and pasted to field2")
        except Exception as e:
            print(f"Error occurred: {e}")

    def DragAndDrop(self):
        act = ActionChains(self.d)
        Drag = self.d.find_element(By.ID,"draggable")
        Drop = self.d.find_element(By.ID,"droppable")
        act.drag_and_drop(Drag,Drop).perform()
        print(f"Successfully",Drop.text)





