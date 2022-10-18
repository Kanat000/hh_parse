from company_parser import CompanyParser
from database import Sqlite
from vacancy_filter import SearchVacancy
from vacancy_page_parser import VacancyPageParser

if __name__ == '__main__':
    Key_Words = ['Python', 'Java', 'Javascript', 'Spring', 'Frontend', 'design', 'C++',
                 'C#', 'QA', 'Devops', 'manager', 'marketing', 'android', 'ios']
    sqlite = Sqlite()
    sqlite.create_company_table()

    search = SearchVacancy()
    urls = search.get_urls(Key_Words)

    vacancy_parser = VacancyPageParser(urls)
    company_links = vacancy_parser.link_collect()
    print(company_links)
    company_parser = CompanyParser()

    for link in company_links:
        data = company_parser.data_collect(link)
        company_parser.data_save(data)
