RateMyProfessors Scraper:

This Python script uses Selenium to scrape professor information from RateMyProfessors. It retrieves the names, ratings, and departments of professors from the specified search page.

Features:

Opens the RateMyProfessors search page using a headless Chrome browser.
Disables all stylesheets to simplify the scraping process.
Clicks the "Show More" button to reveal additional professors until all are loaded.
Extracts and prints each professor's name, rating, and department.

Setup:

Dependencies
Selenium: Install via pip.
ChromeDriver: Ensure ChromeDriver is installed and its path is specified in the script.
