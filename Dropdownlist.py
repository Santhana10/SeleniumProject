from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class List:
    def __init__(self,driver):
        self.d=driver

    def Gender(self):
        self.d.find_element(By.ID, "male").click()

    def Days(self):
        checkboxes = self.d.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']/input[@type='checkbox']")
        print(f"Total checkboxes found: {len(checkboxes)}")
        for checkbox in checkboxes:
            checkbox_value = checkbox.get_attribute('value').strip().lower()
            print(f"Checkbox ID: {checkbox.get_attribute('id')}, Value: {checkbox.get_attribute('value')}")
            if checkbox_value in ["monday","tuesday","wednesday","thursday","friday"]:
                  checkbox.click()

    def CountrySelection(self):
        Country = self.d.find_element(By.ID, "country")
        Dropdown = Select(Country)
        Dropdown.select_by_index(5)
        selected_option = Dropdown.first_selected_option
        print(f"selected value: {selected_option.get_attribute('value')}, Text: {selected_option.text}")

    def ColorsSelection(self):
        colors_dropdown = self.d.find_element(By.XPATH, "//select[@id='colors']")
        all_colors = colors_dropdown.find_elements(By.TAG_NAME, "option")
        act = ActionChains(self.d)
        for color in all_colors:
            if color.text.strip().lower() in ["yellow", "white"]:
                act.key_down(Keys.CONTROL)
                act.click(color)
        act.key_up(Keys.CONTROL).perform()
        selected_colors = [color.text for color in all_colors if color.is_selected()]
        print(f"Selected colors: {selected_colors}")

    def Sortedlist(self):
        Animals = self.d.find_element(By.XPATH, "//select[@id='animals']")
        carnivores = Animals.find_elements(By.TAG_NAME, "option")
        act = ActionChains(self.d)
        for pet in carnivores:
            selected_pet = pet.get_attribute('value').strip().lower()
            if selected_pet in ["cat", "dog"]:
                act.key_down(Keys.CONTROL)
                act.click(pet)
        act.key_up(Keys.CONTROL).perform()
        get_values = [pet.text for pet in carnivores if pet.is_selected()]
        print(f"Selected Animal: {get_values}")





