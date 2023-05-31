# THIS WAS A BIG FAILURE. AMAZON PREVENTS PEOPLE FROM SCRAPING ON THEIR WEBPAGE :(

# I searched up Makoto Shinkai on Amazon.ca, and extracted
# the information off the search results.

from selenium import webdriver

# import required for selenium 4 but not 3
from selenium.webdriver.chrome.service import Service

# library to export to csv file
import pandas as pd

# define the website that we're targeting
website = 'https://www.amazon.ca/s?k=Makoto+Shinkai&crid=3EZ346UDOWLX&sprefix=makoto+sh%2Caps%2C536&ref=nb_sb_noss_2'

# the path for the chrome driver
path = 'F:/ChromeDriver/chromedriver_win32'

# defining the service & driver (what is going on here?)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

# opening our driver
driver.maximize_window()
driver.implicitly_wait(60)
driver.get(website)


# 'by' is the method used to locate the value (xpath in this case)
# Other methods include id, class, or other similar attributes
# 'value' is the XPath query
# find.element(s) and find.element are two different functions for the same thing
container = driver.find_elements(by='xpath', value='//div[@class="a-section a-spacing-base"]')

# Create an array to hold each of the data sets
titles = []
prices = []
ratings = []
links = []

# Now we iterate through the container, and get
# each of these attributes from each element in the container
for i in container:
    # It helps to write down the structures in a notepad first, then paste
    # them into the xpath query
    title = driver.find_element(by='xpath', value='./div/div/h2/a/span').text
    price = driver.find_element(by='xpath', value='.//div//div//a//span//span').text
    rating = driver.find_element(by='xpath', value='.//div//div//span//span/a/i/span').text

    # Getting a specific prop of an element
    link = driver.find_element(by='xpath', value='.//div//div/h2/a').get_attribute('href')

    titles.append(title)
    prices.append(price)
    ratings.append(rating)
    links.append(link)

# Creating DataFrame and exporting data
dictionary_shinkai = {
        'titles': titles,
        'prices': prices,
        'ratings': ratings,
        'links': links
    }

pd.DataFrame(dictionary_shinkai).to_csv('first_scrape.csv')

driver.quit()

# ISSUES SO FAR
# the Chrome(service=service) caused an error when I only put (service)
# The website opens in a new Chrome browser but closes instantly.
# running the finished script brings an error that says
# that the paths I specified in the loop do not exist
