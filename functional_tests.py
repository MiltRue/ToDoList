import unittest
from selenium import webdriver

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

        # Lets add an item
        self.fail("Finish the test!")

        # We type "Eat chicken nuggets" into a text box

        # We hit enter, and the page updates
        # The list now reads "1: Eat chicken nuggets"

        # We can add another item, "Eat french fries"

        # Another page update, showing both items

        # We're happy the app works, so we log off

if __name__ == "__main__":
    unittest.main()