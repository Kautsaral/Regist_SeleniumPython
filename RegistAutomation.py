import  unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegist(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    #TestCase1 
    def test_a_failed_regist_with_emptydata(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol signup
        time.sleep(2)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/form[1]/input[1]").send_keys("") #isi username
        time.sleep(2)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/input[2]").send_keys("") #isi email
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
        browser.get_screenshot_as_file("test_a_failed_regist_with_emptydata.png") #screenshot 
    
     #TestCase2
    def test_a_failed_regist_with_empty_email_and_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol signup
        time.sleep(2)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/form[1]/input[1]").send_keys("Tester") #isi username
        time.sleep(2)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/input[2]").send_keys("") #isi email
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
        browser.get_screenshot_as_file("test_a_failed_regist_with_empty_email_and_password.png") #screenshot 
        
    #TestCase3
    def test_a_failed_regist_with_empty_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol signup
        time.sleep(2)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/form[1]/input[1]").send_keys("Tester") #isi username
        time.sleep(2)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/input[2]").send_keys("tester1@yahoo.com") #isi email
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
        browser.get_screenshot_as_file("test_a_failed_regist_with_empty_password.png") #screenshot 
     
    #TestCase4
    def test_a_failed_regist_with_specialcharacter_in_name(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol signup
        time.sleep(2)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/form[1]/input[1]").send_keys("Tester!#") #isi username
        time.sleep(2)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/input[2]").send_keys("tester1@yahoo.com") #isi email
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("tester1") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
        browser.get_screenshot_as_file("test_a_failed_regist_with_specialcharacter_in_name.png") #screenshot 
    
    #TestCase5
    def test_a_failed_regist_with_same_data(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol signup
        time.sleep(2)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/form[1]/input[1]").send_keys("Tester1") #isi username
        time.sleep(2)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/input[2]").send_keys("tester1@yahoo.com") #isi email
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("tester1") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text
        
        self.assertIn('Oops...', response_data)
        self.assertEqual(response_message, 'Gagal Register!')
        browser.get_screenshot_as_file("test_a_failed_regist_with_same_data.png") #screenshot 
    
    #TestCase6
    def test_a_success_regist(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("http://barru.pythonanywhere.com/") # buka situs
        time.sleep(2)
        browser.find_element(By.ID,"signUp").click() # klik tombol signup
        time.sleep(2)
        browser.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/form[1]/input[1]").send_keys("Tester2") #isi username
        time.sleep(2)
        browser.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/form[1]/input[2]").send_keys("tester2@yahoo.com") #isi email
        time.sleep(2)
        browser.find_element(By.ID,"password_register").send_keys("tester2") # isi password
        time.sleep(2)
        browser.find_element(By.ID,"signup_register").click() # klik tombol sign in
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"swal2-content").text

        self.assertIn('berhasil', response_data)
        self.assertEqual(response_message, 'created user!')
        browser.get_screenshot_as_file("test_a_success_regist.png") #screenshot 
            
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
        