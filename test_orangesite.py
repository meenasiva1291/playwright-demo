import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    #Given I am on the orange hrm login page
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page.locator("#app")).to_match_aria_snapshot("- img \"company-branding\"\n- heading \"Login\" [level=5]\n- paragraph: \"Username : Admin\"\n- paragraph: \"Password : admin123\"\n- text:  Username\n- textbox \"Username\"\n- text:  Password\n- textbox \"Password\"\n- button \"Login\"\n- paragraph: Forgot your password?\n- link:\n  - /url: https://www.linkedin.com/company/orangehrm/mycompany/\n- link:\n  - /url: https://www.facebook.com/OrangeHRM/\n- link:\n  - /url: https://twitter.com/orangehrm?lang=en\n- link:\n  - /url: https://www.youtube.com/c/OrangeHRMInc\n- paragraph: OrangeHRM OS 5.7\n- paragraph:\n  - text: /© \\d+ - \\d+/\n  - link \"OrangeHRM, Inc\":\n    - /url: http://www.orangehrm.com\n  - text: . All rights reserved.\n- img \"orangehrm-logo\"")
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()
    #when I login with valid credentials
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    #Then I should see the dashboard page indicating successful login
    expect(page.locator("#app")).to_match_aria_snapshot("- text: \n- paragraph: Time at Work\n- separator\n- img \"profile picture\"\n- paragraph: Punched Out\n- paragraph: \"/Punched Out: Mar 29th at \\\\d+:\\\\d+ PM \\\\(GMT 7\\\\)/\"\n- text: /\\d+[hmsp]+ [\\d,.]+[bkmBKM]+ Today/\n- button \"\"\n- separator\n- paragraph: This Week\n- paragraph: /Sep \\d+ - Sep \\d+/\n- text: \n- paragraph: /\\d+[hmsp]+ [\\d,.]+[bkmBKM]+/")
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

#AAA[Arrange,Act,Assert]
#BDD[Given,when,then]