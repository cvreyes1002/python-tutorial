from bs4 import BeautifulSoup

with open("website.html", encoding="utf_8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())

all_anchor_tags = soup.find_all("a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
    # print(tag)
    # print(tag.getText())
    # print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)

