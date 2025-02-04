from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)

driver.maximize_window()
driver.get("https://eportal.oauife.edu.ng/")

driver.find_element(By.LINK_TEXT, "CONTINUE TO E-PORTAL").click()
driver.find_element(By.LINK_TEXT, "Home").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Stalites").click()

driver.find_element(By.ID, "username").send_keys("ANS/2019/115")
driver.find_element(By.ID, "password").send_keys("0luw@PERFECT")
Select(driver.find_element(By.ID, "SessionF")).select_by_visible_text("2023/2024")
Select(driver.find_element(By.ID, "SemesterF")).select_by_visible_text("Harmattan")
driver.find_element(By.NAME, "Submit").click()

time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="student_dashboard_info_pop"]/div/div/div[3]/button').click()

time.sleep(5)

driver.find_element(By.ID, "ui-id-2").click()
driver.find_element(By.NAME, "hcno").send_keys("?")
Select(driver.find_element(By.ID, "title")).select_by_visible_text("MR")
driver.find_element(By.ID, "halladdr").send_keys("Ojaja Hostel, OAU")
driver.find_element(By.ID, "homeadd").send_keys("7, Road B, Mercyland Estate, Iju-Ota, Ogun state.")
driver.find_element(By.ID, "tribe").send_keys("Yoruba")
driver.find_element(By.ID, "state").send_keys("Ondo")
driver.find_element(By.ID, "place").send_keys("Lagos")
driver.find_element(By.ID, "nation").send_keys("Nigeria")
driver.find_element(By.ID, "reldenom").send_keys("Christainity")
Select(driver.find_element(By.ID, "sex")).select_by_visible_text("Male")
Select(driver.find_element(By.ID, "mstatus")).select_by_visible_text("Single")
driver.find_element(By.ID, "phone").send_keys("09036020584")
Select(driver.find_element(By.ID, "class")).select_by_visible_text("Undergraduate")
driver.find_element(By.ID, "pgname").send_keys("Festus Ogunjobi")
driver.find_element(By.ID, "pgaddress").send_keys("7, Road B, Mercyland Estate, Iju-Ota, Ogun state.")
Select(driver.find_element(By.ID, "pgrelation")).select_by_visible_text("Parents")
driver.find_element(By.ID, "pgphone").send_keys("08023702909")

driver.find_element(By.NAME, "Submit").click()

driver.find_element(By.LINK_TEXT, "OK").click()

Select(driver.find_element(By.NAME, "Arthritis")).select_by_index(1)
Select(driver.find_element(By.NAME, "Asthma")).select_by_index(1)
Select(driver.find_element(By.NAME, "Deformity")).select_by_index(1)
Select(driver.find_element(By.NAME, "Bronchitis")).select_by_index(1)
Select(driver.find_element(By.NAME, "Diabetes")).select_by_index(1)
Select(driver.find_element(By.NAME, "ENTtrouble")).select_by_index(1)
Select(driver.find_element(By.NAME, "Dizziness")).select_by_index(1)
Select(driver.find_element(By.NAME, "DSensitivity")).select_by_index(1)
Select(driver.find_element(By.NAME, "Dysentery")).select_by_index(1)
Select(driver.find_element(By.NAME, "Epilepsy")).select_by_index(1)
Select(driver.find_element(By.NAME, "GUDisease")).select_by_index(1)
Select(driver.find_element(By.NAME, "Fever")).select_by_index(1)
Select(driver.find_element(By.NAME, "Heart")).select_by_index(1)
Select(driver.find_element(By.NAME, "Pressure")).select_by_index(1)
Select(driver.find_element(By.NAME, "Jaundice")).select_by_index(1)
Select(driver.find_element(By.NAME, "Kidney")).select_by_index(1)
Select(driver.find_element(By.NAME, "Bladder")).select_by_index(1)
Select(driver.find_element(By.NAME, "Malaria")).select_by_index(1)
Select(driver.find_element(By.NAME, "Menstrual")).select_by_index(1)
Select(driver.find_element(By.NAME, "Migraine")).select_by_index(1)
Select(driver.find_element(By.NAME, "Filariasis")).select_by_index(1)
Select(driver.find_element(By.NAME, "Poliomyelitis")).select_by_index(1)
Select(driver.find_element(By.NAME, "Rheumatic")).select_by_index(1)
Select(driver.find_element(By.NAME, "Skin")).select_by_index(1)
Select(driver.find_element(By.NAME, "ulcer")).select_by_index(1)
Select(driver.find_element(By.NAME, "Tuberculosis")).select_by_index(1)
Select(driver.find_element(By.NAME, "Schistosomiasis")).select_by_index(1)
Select(driver.find_element(By.NAME, "Sickle")).select_by_index(1)

driver.find_element(By.NAME, "others").send_keys("N/A")
driver.find_element(By.NAME, "indicate").send_keys("N/A")

Select(driver.find_element(By.NAME, "smoke")).select_by_index(1)
driver.find_element(By.NAME, "when1").send_keys("N/A")
driver.find_element(By.NAME, "quantity").send_keys("N/A")

driver.find_element(By.NAME, "activity").send_keys("Coding, Making research, Watching reels, Listening to music, and Sleeping")
Select(driver.find_element(By.NAME, "athletics")).select_by_index(4)
Select(driver.find_element(By.NAME, "sportrep")).select_by_index(1)
driver.find_element(By.NAME, "which1").send_keys("N/A")

Select(driver.find_element(By.NAME, "test")).select_by_index(1)
Select(driver.find_element(By.NAME, "recieved")).select_by_index(1)

driver.find_element(By.NAME, "serious").send_keys("I do not remember having any serious injury.")
driver.find_element(By.NAME, "admission").send_keys("N/A")

driver.find_element(By.NAME, "treatment").send_keys("None")

Select(driver.find_element(By.NAME, "relative")).select_by_index(1)
driver.find_element(By.NAME, "reldetail").send_keys("N/A")

Select(driver.find_element(By.NAME, "immpolio")).select_by_index(1)
Select(driver.find_element(By.NAME, "immsmall")).select_by_index(1)
Select(driver.find_element(By.NAME, "immteta")).select_by_index(1)
Select(driver.find_element(By.NAME, "immtuber")).select_by_index(1)
Select(driver.find_element(By.NAME, "immtypho")).select_by_index(1)
Select(driver.find_element(By.NAME, "immfever")).select_by_index(1)
driver.find_element(By.NAME, "immother").send_keys("None")
driver.find_element(By.NAME, "Submit").click()

driver.find_element(By.LINK_TEXT, "Main Menu Page").click()

time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="student_dashboard_info_pop"]/div/div/div[3]/button').click()

time.sleep(5)

driver.find_element(By.ID, "ui-id-21").click()

time.sleep(5)

driver.quit()


















