import time
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import path_to_driver


class SearchVacancy:
    __driver = webdriver.Chrome(path_to_driver)

    def get_urls(self, Key_Word_Array):
        try:
            self.__driver.maximize_window()
            url_array = []
            for Key_Word in Key_Word_Array:
                self.__driver.get("https://hh.kz/")
                self.__driver.refresh()
                advanced_search = self.__driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]'
                                                                       '/div/div[3]/div[1]/div[1]'
                                                                       '/div/div/div[2]/div/form'
                                                                       '/div/div[1]/fieldset/span'
                                                                       '/a/span')
                advanced_search.click()

                search_key_word_input = self.__driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]'
                                                                             '/div[1]/div/div/div[1]/form/div[1]'
                                                                             '/div/div[2]/div[1]/fieldset/input')

                search_key_word_input.send_keys(Key_Word)

                WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                         '/html/body/div[9]/ul')))
                search_key_word_input.send_keys(Keys.ARROW_DOWN)
                search_key_word_input.send_keys(Keys.ENTER)

                search_key_using_filter = self.__driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]'
                                                                               '/div[1]/div/div/div[1]/form/div[1]/div')
                search_field_check_boxes = search_key_using_filter.find_elements(By.TAG_NAME, 'span')

                for search_field_check_box in search_field_check_boxes:
                    search_field_check_box.click()

                self.__driver.find_element(By.XPATH, '//*[@id="HH-React-Root"]/div/div[3]'
                                                     '/div[1]/div/div/div[1]/form/div[15]/div[2]').click()

                WebDriverWait(self.__driver, 10).until(
                    EC.visibility_of_any_elements_located((By.CLASS_NAME, 'serp-item')))

                url = self.__driver.current_url.replace('items_on_page=50', 'items_on_page=20')
                url_parse = urlparse(url)
                base_url = url_parse.scheme + '://' + url_parse.netloc + url_parse.path
                if 'area=40' in url_parse.query:
                    if 'professional_role=96' in url_parse.query:
                        url_array.append(url)
                    else:
                        url_array.append(base_url + '?professional_role=96' + url_parse.query)
                else:
                    url_array.append(base_url + '?area=40' + url_parse.query)
                url_array.append(base_url + '?page=1' + url_parse.query)
            return url_array

        except Exception as e:
            error_file = open("error.txt", "a")
            error_file.write('\n' + str(e))
