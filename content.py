from bs4 import BeautifulSoup

# Step 1: Read the HTML file
with open('lessonsHtml.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find all divs with class 'panel__block'
panel_blocks = soup.find_all('div', class_='panel__block')

# Initialize the content array
content = []

# Remove all classes and kjb-settings-id attributes from the panel blocks
for panel_block in panel_blocks:
    for element in panel_block.find_all(True):  # True finds all tags
        if 'class' in element.attrs:
            del element['class']
        if 'kjb-settings-id' in element.attrs:
            del element['kjb-settings-id']
        if "data-pm-slice" in element.attrs:
            del element['data-pm-slice']
    content.append(panel_block.prettify())



# panel_block_ids = []
# with open('lessons.txt', 'r', encoding='utf-8') as file:
#     panel_block_ids = [line.strip() for line in file.readlines()]

panel_block_ids = []
with open('lessons.txt', 'r', encoding='utf-8') as file:
    panel_block_ids = [line.strip() for line in file.readlines() if line.strip() != "/products/teach-yourself-a-language-course/categories"]

print(len(panel_block_ids), len(content))

# Add each panel block in the content array panel_block_ids
contentWithIds = []

# for panel_block_id in panel_block_ids:
#     for panel_block in content:
#         panel_block_soup = BeautifulSoup(panel_block, 'html.parser')
#         # Find the div element with class 'panel__block'
#         div_element = panel_block_soup.find('div', class_='panel__block')
#         div_element.attrs["id"] = panel_block_id
#
#         contentWithIds.append(div_element)
for i, panel_block_id in enumerate(panel_block_ids):
    if i < len(content):  # Ensure we do not go out of bounds
        panel_block_soup = BeautifulSoup(content[i], 'html.parser')
        div_element = panel_block_soup.find('div', class_='panel__block')
        if div_element:  # Check if the div element exists
            div_element['id'] = panel_block_id
            contentWithIds.append(panel_block_soup)


# Step 2: Write the content to a new HTML file
with open('lessonsHtmlWithIds.html', 'w', encoding='utf-8') as file:
    for panel_block in contentWithIds:
        file.write(panel_block.prettify())
        file.write('\n\n')