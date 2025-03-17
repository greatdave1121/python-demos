import re
import os
import csv
import time
import email
import imaplib
from email.header import decode_header
from playwright.sync_api import sync_playwright

def get_magic_link(email_address, app_password):
    imap_server = "imap.gmail.com"
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_address, app_password)

    mail.select("inbox")

    status, message = mail.search(None, '(FROM "maui-survey@survey.uhero.hawaii.edu" SUBJECT "UHERO Survey")')

    email_ids = message[0].split()
    latest_email_id = email_ids[-1]

    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            response_part = response_part[1]
            msg = email.message_from_bytes(response_part)

            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                subject = subject.decode(encoding or "utf-8")
            
            sender, encoding = decode_header(msg["From"])[0]
            if isinstance(sender, bytes):
                sender = sender.decode(encoding or "utf-8")

            recipient, encoding = decode_header(msg["To"])[0]
            if isinstance(recipient, bytes):
                recipient = recipient.decode(encoding or "utf-8")

            subject = f"\nSubject: {subject}"
            sender = f"From: {sender}"
            recipient = f"To: {recipient}\n"

            body = None
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
                elif part.get_content_type() == "text/html" and not body:
                    body = part.get_payload(decode=True).decode()

            print(subject)
            print(sender)
            print(recipient)

            magic_link = re.findall(r'https?://[^\s]+', body)
            if magic_link:
                magic_link = magic_link[0]
                return magic_link
    mail.logout()        
    return None
               
        
def fill_survey():
    if page.get_by_text("You have completed this month's survey. Please come back next month."):
        print(f"Survey already completed for {email_address}\n")
        return


    try:
        page.get_by_role("link", name="Start survey").click()
        page.get_by_role("textbox", name="What was your address prior to the wildfire?").fill(home_address)
        page.get_by_role("combobox", name="How many adults are in your household (18+ years old)?", exact=True).click()
        page.get_by_role("option", name="2 adults").click()
        page.get_by_role("combobox", name="How many children are in your household (0-17 years old)?", exact=True).click()
        page.get_by_role("option", name="3 children").click()
        page.get_by_role("combobox", name="How many bedrooms does your current housing have?", exact=True).click()
        page.get_by_role("option", name="3 bedrooms").click()
        page.get_by_role("combobox", name="What was your housing prior to the wildfires?", exact=True).click()
        page.get_by_role("option", name="Owned free and clear (no mortgage)").click()
        page.get_by_role("combobox", name="What was your employment status prior to the wildfires?", exact=True).click()
        page.get_by_role("option", name="Full-time").click()
        page.get_by_role("combobox", name="What was your monthly household income prior to the wildfires, from all adults and all sources?", exact=True).click()
        page.get_by_role("option", name="$6,300 - $6,800").click()
        page.get_by_role("checkbox", name="Construction").check()
        page.get_by_role("combobox", name="How long have you lived on Maui?", exact=True).click()
        page.get_by_role("option", name="5 years").nth(0).click()
        page.get_by_role("checkbox", name="West Maui - Olowalu, Lahaina, Ka'anapali, Kahana, Napili, Kapalua").check()
        page.get_by_role("checkbox", name="FEMA landlord (FEMA leasing your property)").check()
        page.get_by_role("combobox", name="Do you still live with the same people as before the wildfires?").click()
        page.get_by_role("option", name="Yes").click()
        page.get_by_role("radio", name="No").check()
        page.get_by_role("button", name="Next").click()

        page.get_by_role("combobox", name="Where do you live now?").click()
        page.get_by_role("option", name="West Maui - Olowalu, Lahaina, Ka'anapali, Kahana, Napili, Kapalua").click()
        page.get_by_role("combobox", name="How long have you lived at your current address?").click()
        page.get_by_role("option", name="5 months").nth(0).click()
        page.get_by_role("combobox", name="What is your current housing?").click()
        page.get_by_role("option", name="Permanent - New construction home you purchased after the fires").click()
        page.get_by_role("combobox", name="How many adults are in your household (18+ years old)?").click()
        page.get_by_role("option", name="2 adults").click()
        page.get_by_role("combobox", name="How many children are in your household (0-17 years old)?").click()
        page.get_by_role("option", name="3 children").click()
        page.get_by_role("combobox", name="How many bedrooms does your current housing have?").click()
        page.get_by_role("option", name="3 bedrooms").click()
        page.get_by_role("combobox", name="Where do you expect to be living a year from now?").click()
        page.get_by_role("option", name="East Maui - Keanae, Nahiku, Hana, Kipahulu").click()
        page.get_by_role("button", name="Next").click()

        page.get_by_role("combobox", name="What is your current employment status?").click()
        page.get_by_role("option", name="Full-time").click()
        page.get_by_role("combobox", name="What is your monthly household income, from all adults and all sources?").click()
        page.get_by_role("option", name="$5,000 - $5,500").click()
        page.get_by_role("checkbox", name="Kula").nth(0).click()
        page.get_by_role("checkbox", name="Construction").click()
        page.get_by_role("combobox", name="Since the last time you participated in the survey").click()
        page.get_by_role("option", name="Yes").click()
        page.get_by_role("radio", name="No").check()
        page.get_by_role("button", name="Next").click()

        page.locator("div").filter(has_text=re.compile(r"^Transportation to/from school or after-school activitiesNot needed$")).locator("span").nth(1).click()
        page.locator("div").filter(has_text=re.compile(r"^Financial AssistanceNot needed$")).locator("span").nth(1).click()
        page.locator("[id=\"\\:rua\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:rub\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:ruc\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:rud\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:rue\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:ruf\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:rug\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:ruh\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:rui\\:-form-item\"] span").first.click()
        page.locator("[id=\"\\:ruj\\:-form-item\"] span").first.click()
        page.get_by_role("checkbox", name="FEMA landlord (FEMA leasing").click()
        page.get_by_role("checkbox", name="Native Hawaiian or Pacific").click()
        page.get_by_role("radio", name="Male", exact=True).click()
        page.locator("[id=\"\\:rvn\\:-form-item\"]").click()
        page.locator("[id=\"\\:rvu\\:-form-item\"]").click()

        page.get_by_role("button", name="Submit").click()

        print("Survey completed successfully!")
    except Exception as e:
        print(f"Error printing out the survey {e}")

    page.pause()




with open("mauiCredentials.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    credentials = list(reader)
    
    for row in credentials:
        email_address = row["email_address"]
        phone_number =  row["phone_number"]
        app_password =  row["app_password"]
        home_address =  row["home_address"]


        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--start-maximized"])
            context = browser.new_context(no_viewport=True)
            page = context.new_page()
            page.goto("https://survey.uhero.hawaii.edu?code=uhero62", timeout=60000)

            page.evaluate("""
                        () => {
                            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
                            Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
                            Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
                        }
                    """)
            page.get_by_role("textbox", name="name@example.com").fill(email_address)
            page.get_by_role("textbox", name="Phone number US").fill(phone_number)
            page.get_by_role("button", name="sign-in with email").click()
            page.get_by_role("button", name="Sign in", exact=True).click()

            print(f"Waiting for magic link for {email_address}...")
            time.sleep(5)
            magic_link = get_magic_link(email_address, app_password)

            if magic_link:
                print(f"Opening magic link for {email_address}: {magic_link}")
                page.goto(magic_link)

                fill_survey()
            else:
                print(f"Magic link not found for {email_address}")

            
            browser.close()        






        






















    










   



    




