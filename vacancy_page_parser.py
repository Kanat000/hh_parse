from config import get_soup


class VacancyPageParser:
    def __init__(self, urls):
        self.__urls = urls

    def link_collect(self):
        try:
            company_links = []
            for url in self.__urls:
                soup = get_soup(url)
                link_elements = soup.find_all('a', {'class': 'bloko-link_kind-tertiary'})
                for element in link_elements:
                    link = str(element.get('href'))
                    if link not in company_links:
                        if '?dpt=' not in link:
                            company_links.append(link)

            return company_links

        except Exception as e:
            error_file = open("error.txt", "a")
            error_file.write('\n' + str(e))