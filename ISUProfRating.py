from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chromedriver_path = '/usr/local/bin/chromedriver'

options = webdriver.ChromeOptions()

options.add_argument('--headless') # Run Chrome in headless mode (no GUI)

prefs = {"profile.managed_default_content_settings.images": 2,
         "profile.default_content_setting_values.javascript": 2,
         "profile.managed_default_content_settings.fonts": 2 }
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

try:
    # URL of the RateMyProfessors search page
    url = 'https://www.ratemyprofessors.com/search/professors/452?q=*'
    # Open the URL in the Chrome browser 
    driver.get(url)

    # Inject JavaScript to disable all stylesheets (CSS)
    disable_css_script = """
    var stylesheets = document.styleSheets;
    for (var i = 0; i < stylesheets.length; i++) {
        stylesheets[i].disabled = true;
    }
    """
    driver.execute_script(disable_css_script)

    profCount = driver.find_element(By.XPATH, "//h1")
    profCount = profCount.text.split()[0]

    count = 0
    while True:
        try:
            count = count + 1
            # Use JavaScript to click the button to avoid interception
            driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//button[text() = 'Show More']"))

            time.sleep(1)  # Wait for the content to load after clicking

            if count == profCount:
                break
        except:
            # If the "Show More" button is not found, break the loop
            break
    # Print out each professor's name found on the page
    teacherCards = driver.find_elements(By.CLASS_NAME, 'TeacherCard__StyledTeacherCard-syjs0d-0')
    
    for teacherCard in teacherCards:
        profName = teacherCard.find_element(By.CLASS_NAME, 'CardName__StyledCardName-sc-1gyrgim-0')

        profRating = teacherCard.find_element(By.CLASS_NAME, 'CardNumRating__CardNumRatingNumber-sc-17t4b9u-2')

        profDepartment = teacherCard.find_element(By.CLASS_NAME, 'CardSchool__Department-sc-19lmz2k-0')

        # print(checkCount)
        print(f'Professor Name: {profName.text} | Rating: {profRating.text} | Department: {profDepartment.text}')
        print("--" * 50)
finally:
    # Close the browser window
    driver.quit()