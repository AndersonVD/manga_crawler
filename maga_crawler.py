import requests
from tqdm import tqdm

headers = {
    "sec-ch-ua": '""Opera GX";v="93", "Not/A)Brand";v="8", "Chromium";v="107"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0",
    "x-requested-with": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded"
}


def search_page():
    url = "https://mangalivre.net/lib/search/series.json"

    TERMO_BUSCA = "mob psycho 100"

    payload = f"search={TERMO_BUSCA.replace(' ', '+')}"

    response = requests.request("POST", url, data=payload, headers=headers)
    response = response.json()
    return response


def chapter_list(id_serie):
    url = f"https://mangalivre.net/series/chapters_list.json?page=1&id_serie={id_serie}"

    response = requests.request("GET", url, headers=headers)
    response = response.json()
    chapter_list = []
    for chapter in response["chapters"]:
        chapter_list.append(chapter)

    return chapter_list


def link_images(id_chapter):
    url = f"https://mangalivre.net/leitor/pages/{id_chapter}.json"

    response = requests.request("GET", url, headers=headers)
    response = response.json()
    link_images = []
    for image in response["images"]:
        link_images.append(image["legacy"])

    return link_images


def dowload_images(images):
    for image in tqdm(images):
        with open(f"images/{images.index(image)}.jpg", "wb") as file:
            file.write(requests.get(image).content)

    return True


if __name__ == "__main__":
    page_content = search_page()
    print("Busca realizada com sucesso!")
    chapter_list = chapter_list(page_content["series"][0]["id_serie"])
    print("Lista de capítulos obtida com sucesso!")
    scan = 1
    scan_path = ""
    while scan_path == "":
        try:
            scan_path = chapter_list[0]['releases'][f'_scan{scan}']['id_release']
        except:
            scan += 1
    
    link_images = link_images(scan_path)
    print("Lista de imagens obtida com sucesso!")
    dowload_images(link_images)
    print(link_images)
