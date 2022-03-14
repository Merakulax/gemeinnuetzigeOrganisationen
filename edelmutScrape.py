from bs4 import BeautifulSoup #Webscraper
import lxml
import requests # HTTP/ library


# Insert the webside link here:
link = lambda page: f"https://edelmut.org/organisationen/page/{page}/"


def get_list_of_links(p_n= 100):
    """Returns all the links in the website
    :param p_n: if no maximum of pages given then stop at 100
    :return: the list of links
    """

    list_o_links = []

    for i in range(1, p_n+1):
        source = requests.get(link(i)).text
        soup = BeautifulSoup(source, 'lxml')
        test = soup.find('div', id="main").section.div.h1.text

        if test == "Fehler 404 – Seite nicht gefunden":
            return list_o_links
        else:
            content = soup.find('ul', class_="geodir-category-list-view clearfix gridview_onefifth geodir-listing-posts geodir-gridview gridview_onefifth")
            for eintrag in content.find_all('li'):
                plink = eintrag.a ["href"][35:]
                if plink not in list_o_links:
                    list_o_links.append(plink)
            print(f"Eintrag {i} von {p_n} gelesen")
    return list_o_links




def main():
    """

    :return:
    """
    n_o_pages = 10
    links_safe = get_list_of_links(n_o_pages)












    return None









if __name__ == '__main__':
    main()