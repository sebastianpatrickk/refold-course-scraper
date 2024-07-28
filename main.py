from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Initialize lists to store module and lesson links
courseModules = []
lessonLinks = []
lessonsHtml = []

# Open a browser window and navigate to the login page
driver = webdriver.Chrome()
driver.get("https://academy.refold.la/products/teach-yourself-a-language-course")
time.sleep(2)  # Wait for the page to load

# Login process
driver.find_element(By.ID, "member_email").send_keys("sebastianpatrickklen@gmail.com")
driver.find_element(By.ID, "member_password").send_keys("BHY6ruj*tpe*anj@dqt")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(2)  # Wait for the page to load after login

# Extract the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

# Define a function to filter links based on specific criteria
def filter_links(tag):
    return tag.name == 'a' and tag.get('id', '').startswith('category-') and tag.get('href', '').startswith('https://academy.refold.la/products/teach-yourself-a-language-course/categories')

# Use the filter function to find all matching links and store their hrefs
matching_links = soup.find_all(filter_links)
for link in matching_links:
    courseModules.append(link.get('href'))

# Save the links to a file
with open('modules.txt', 'w') as file:
    for link in courseModules:
        file.write(link + '\n')


# Loop through each module link and extract the lesson links
for module in courseModules:
    driver.get(module)
    time.sleep(2)  # Wait for the page to load

    # Extract the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # Define a function to filter links based on specific criteria
    def filter_lesson_links(tag):
        return tag.name == 'a' and tag.get('href', '').startswith('/products/teach-yourself-a-language-course/categories')

    # Use the filter function to find all matching links and store their hrefs
    matching_links = soup.find_all(filter_lesson_links)
    for link in matching_links:
        lessonLinks.append(link.get('href'))

# Save the links to a file
with open('lessons.txt', 'w') as file:
    for link in lessonLinks:
        file.write(link + '\n')

# Loop through each lesson link and extract the lesson content
for lesson in lessonLinks:
    time.sleep(2)  # Wait for the page to load

    # Extract the page source and parse it with BeautifulSoup
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # Define a function to filter links based on specific criteria
    target_div = soup.find('div', class_='section section--global section--product')

    # Check if the target div is found
    if target_div:
        # Extract and print the inner HTML
        inner_html = target_div.prettify()
        print(inner_html)
        lessonsHtml.append(inner_html)
    else:
        print("Target div not found.")


# Save the HTML content of each lesson to a file
with open('lessonsHtml.html', 'w', encoding='utf-8') as file:
    for html_content in lessonsHtml:
        file.write(html_content + '\n\n---\n\n')


# TODO: Download all pages and extract the video links adn course texts
# TODO: Download the lesson pages html like save in browser

# Here is a ID <div class="kjb-video-responsive">
#   <div id="wistia_mjv6qbhimh"
#     class="wistia_embed wistia_async_mjv6qbhimh "
#     data-track-progress="eyJhbGciOiJIUzI1NiJ9.eyJhY3Rvcl90eXBlIjoiTWVtYmVyIiwiYWN0b3JfaWQiOjIyMjM2NDY1NDAsInByb2R1Y3RfaWQiOjIxNDgyMzc3NjEsInBvc3RfaWQiOjIxNjg4NjcwMDZ9.treWs35CCEkxpr1yFtFC0D1W_fsCLmlb06Ug8h10fEQ"
#     data-tracked-percent="100">&nbsp;</div>
# </div>

# Go to embeded video page and add get this https://embed-ssl.wistia.com/deliveries/e2102656835cdf41f110e63030a5a9ce.bin https://www.cisdem.com/resource/download-wistia-videos.html#URL

# Close the browser
driver.quit()