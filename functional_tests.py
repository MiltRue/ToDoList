import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()

    def test_can_start_todo_list(self):
        # Check out this sick to-do app homepage!
        self.browser.get("http://localhost:8000")

        # The page title/header even mention to-do lists!
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # Lets add an item
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), 
                         "Enter a to-do item")

        # We type "Eat chicken nuggets" into a text box
        inputbox.send_keys("Eat chicken nuggets")

        # We hit enter, and the page updates
        # The list now reads "1: Eat chicken nuggets"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn("1: Eat chicken nuggets", [row.text for row in rows])

        # We can add another item, "Eat french fries"
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Eat french fries")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Another page update, showing both items
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn("1: Eat chicken nuggets", [row.text for row in rows])
        self.assertIn("2: Eat french fries", [row.text for row in rows])

        # We're happy the app works, so we log off

if __name__ == "__main__":
    unittest.main()