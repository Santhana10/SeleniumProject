from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver
from Dropdownlist import List
from BasicDetails import Details
from Alerts import Handle_Alert
from Windows import Switch_Window
from DatePicker import Launch

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

class Main:
    def __init__(self):
        print("Launching browser...")
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://testautomationpractice.blogspot.com/")
        self.driver.maximize_window()

        # Create instances of all classes
        self.details = Details(self.driver)
        self.list_actions = List(self.driver)
        self.alert_handler = Handle_Alert(self.driver)
       # self.window_handler = Switch_Window(self.driver)
        self.Datepicker1 = Launch(self.driver)



    def execute(self):
      try:
        print("Executing Details...")
        self.details.Input()

        print("Executing List Actions...")
        self.list_actions.Gender()
        self.list_actions.Days()
        self.list_actions.CountrySelection()
        self.list_actions.ColorsSelection()
        self.list_actions.Sortedlist()

        print("Executing Alerts Handling...")
        self.alert_handler.DynamicButton()
        self.alert_handler.Popup()
        self.alert_handler.ConfirmationAlertbox()
        self.alert_handler.PromptAlert()

        #print("Executing Window handling...")
        #self.window_handler.NewTab()
        #self.window_handler.NewWindow()

        print("Executing DatePicker handling...")
        #self.Datepicker1.PickDate()
        #self.Datepicker1.DatePick2()
        #self.Datepicker1.DatePick3()
        self.Datepicker1.DoubleClick()
        self.Datepicker1.DragAndDrop()

      except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")

if __name__ == "__main__":
    main_obj = Main()
    main_obj.execute()