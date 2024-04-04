from selenium import webdriver

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to a web page
driver.get("https://www.example.com Find the element that's name attribute is 'q' (the Google search box)
input_element = driver.find_element_by_name("q")

# Type in the search term
input_element.send_keys("Selenium")

# Submit the form
input_element.submit()

# Wait for the page to load
driver.implicitly_wait(10)

# Find the first search result
first_result = driver.find_element_by_css_selector("div.rc")

# Print the title of the first search result
print(first_result.text)

# Close the browser window
driver.close()
