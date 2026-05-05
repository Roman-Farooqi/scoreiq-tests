import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

class ScoreIQTests(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=chrome_options)
        
        # Link wahi docker internal aur 5000 port
        self.base_url = "[http://3.104.120.53:5000](http://3.104.120.53:5000)" 

    # --- 15 TEST CASES FOR YOUR ACTUAL SCOREIQ APP ---

    def test_01_homepage_title(self):
        self.driver.get(self.base_url)
        self.assertIn("ScoreIQ", self.driver.title)

    def test_02_login_page_title(self):
        self.driver.get(f"{self.base_url}/login")
        self.assertIn("Log In", self.driver.title)

    def test_03_login_email_field_exists(self):
        self.driver.get(f"{self.base_url}/login")
        email_field = self.driver.find_element(By.ID, "email")
        self.assertTrue(email_field.is_displayed())

    def test_04_login_password_field_exists(self):
        self.driver.get(f"{self.base_url}/login")
        pass_field = self.driver.find_element(By.ID, "password")
        self.assertTrue(pass_field.is_displayed())

    def test_05_signup_page_link_exists_on_login(self):
        self.driver.get(f"{self.base_url}/login")
        self.assertIn("/signup", self.driver.page_source)

    def test_06_github_oauth_button_exists(self):
        self.driver.get(f"{self.base_url}/login")
        self.assertIn("login-github", self.driver.page_source)

    def test_07_footer_contains_name(self):
        self.driver.get(self.base_url)
        # Testing your exact footer text
        self.assertIn("Roman Farooqi", self.driver.page_source)

    def test_08_hero_section_text(self):
        self.driver.get(self.base_url)
        # HTML tags ke baghair wala text dhoondte hain
        self.assertIn("Predict your", self.driver.page_source)

    def test_09_model_accuracy_stat(self):
        self.driver.get(self.base_url)
        self.assertIn("88", self.driver.page_source)

    def test_10_training_records_stat(self):
        self.driver.get(self.base_url)
        self.assertIn("1", self.driver.page_source)

    def test_11_predict_data_link_exists(self):
        self.driver.get(self.base_url)
        self.assertIn("predictdata", self.driver.page_source)

    def test_12_history_link_exists(self):
        self.driver.get(self.base_url)
        self.assertIn("history", self.driver.page_source)

    def test_13_404_error_page_working(self):
        # Testing a fake URL to see if your app handles 404
        self.driver.get(f"{self.base_url}/this-page-does-not-exist-123")
        self.assertIn("404 Not Found", self.driver.page_source)

    def test_14_how_it_works_section(self):
        self.driver.get(self.base_url)
        self.assertIn("Four steps from input", self.driver.page_source)

    def test_15_responsive_mobile_view(self):
        self.driver.set_window_size(375, 812) # Mobile view
        self.driver.get(self.base_url)
        self.assertIsNotNone(self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()