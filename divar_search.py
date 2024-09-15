import requests
from bs4 import BeautifulSoup

url = "https://divar.ir/s/tehran/vehicles"
s = 0
index =100
while index >= 0:
    data_index = {"data-index": index}
    response = requests.get(url, params=data_index )
    if response.status_code == 200:
        bs = BeautifulSoup(response.content, "html.parser")
        find_by_class = bs.find_all(class_="post-list__widget-col-c1444")

        for item in find_by_class:
            s += 1
            title = item.find("h2", class_="kt-post-card__title")
            description = item.find("div", class_="kt-post-card__description")

            if title is not None:
                title = title.text.strip()
                print(title)

            if description is not None:
                description = description.text.strip()
                print(description)

            print("--------------------------------")

        
        index -= 1

    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        break

print(f"Total items found: {s}")
