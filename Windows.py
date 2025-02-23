from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Switch_Window:
    def __init__(self, driver):
        self.d = driver

    def NewTab(self):
        self.d.find_element(By.XPATH, "//button[text()='New Tab']").click()
        original_window = self.d.current_window_handle
        MyWindow = self.d.window_handles
        for windows in MyWindow:
            if windows != original_window:
                self.d.switch_to.window(windows)
                print("Switched to:", windows)
            if self.d.title == "Your Store":
                WebDriverWait(self.d, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Cameras']"))).click()
                self.d.save_screenshot("Camera.png")
        self.d.close()
        self.d.switch_to.window(original_window)

    def NewWindow(self):
        self.d.find_element(By.XPATH, "//button[text()='Popup Windows']").click()
        original_window = self.d.current_window_handle
        Popup = self.d.window_handles
        print(Popup)
        for Popupwindows in Popup:
            if Popupwindows != original_window:
                try:
                  self.d.switch_to.window(Popupwindows)
                  print(f"Switched to Popup: {Popupwindows} | Title: {self.d.title}")
                  try:
                    self.d.maximize_window()
                  except Exception as e:
                      print("Maximize window failed:", str(e))
                  if self.d.title=='Selenium':
                     RandomValue = WebDriverWait(self.d, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='mx-auto text-center p-4']/h1")))
                     print(RandomValue.text)
                  else:
                    print("Switched window not found for the text")
                  self.d.close()
                  print(f"Closed Popup: {Popupwindows}")
                except Exception as e:
                   print(f"Error handling popup {Popupwindows}: {str(e)}")

        if original_window in self.d.window_handles:
            self.d.switch_to.window(original_window)
            print("Switched back to main window:", original_window)
        else:
            print("Main window is no longer available.")