from .base_page import BasePage
from .locators import SearchPageLocators
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class SearchPage(BasePage):

	def search_in_Yandex(self):
		self.search_field()
		self.visibility_suggest_table()
		self.tenzor_link_result()

	def search_field(self):
		assert self.is_element_present(*SearchPageLocators.SEARCH_WINDOW), \
			"Нет поля поиск на главной странице"

	def visibility_suggest_table(self):
		search_box = self.browser.find_element(*SearchPageLocators.SEARCH_WINDOW)
		search_box.send_keys('Тензор')
		time.sleep(2)
		assert EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-suggest__popup.mini-suggest__popup_theme_flat.mini-suggest__popup_visible')), "Нет таблицы с подсказками на главной странице"  # проверяем есть ли таблица с подсказками
		search_box.send_keys(Keys.ENTER)

	def tenzor_link_result(self):
		links = self.browser.find_elements(*SearchPageLocators.LINKS_IN_SEARCH)
		items = [elem.text.strip() for elem in links[:5]]

		if "tensor.ru" not in items:
			raise Exception('сайта tensor.ru нет в первых 5 пунктах')





