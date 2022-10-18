from config import get_soup
from database import Sqlite


class CompanyParser:
    __base_url = 'https://hh.kz/'
    __db = Sqlite()

    def data_collect(self, link):
        try:
            soup = get_soup(self.__base_url + link)
            name = soup.find('span', {'data-qa': 'company-header-title-name'}).text
            logo = soup.find('img', {'data-qa': 'company-logo-image'}).get('src')
            description = soup.find('div', {'class': 'g-user-content'}).findAll('p')[0].text
            number_of_active_positions = int(soup.find('span', {'class': 'bloko-text_tertiary'}).text)
            return {'name': name, 'description': description, 'link': link, 'logo': logo,
                    'active_vacancy_count': number_of_active_positions}
        except Exception as e:
            error_file = open("error.txt", "a")
            error_file.write('\n' + str(e))

    def data_save(self, data):
        try:
            if not self.__db.exists_company(data['link']):
                self.__db.insert_company(data)
        except Exception as e:
            error_file = open("error.txt", "a")
            error_file.write('\n' + str(e))
