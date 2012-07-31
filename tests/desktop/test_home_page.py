#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
from selenium.common.exceptions import InvalidElementStateException
from selenium.webdriver.common.by import By
from unittestzero import Assert
from pages.desktop.consumer_pages.home import Home


class TestHomePage:
        base_url = "https://marketplace-dev.allizom.org/en-US"
        categories_base = "//div[@id='page']" + \
                          "/section[@class='categories slider full']" + \
                          "/div[@class='promo-slider']" + \
                          "/ul[@class='content']"
        
        categories = [{'text': 'Entertainment', 'link': base_url + '/apps/entertainment', 'class': 'arrow img entertainment'},
                      {'text': 'Finance', 'link': base_url + '/apps/finance', 'class': 'arrow img finance'},
                      {'text': 'Games', 'link': base_url + '/apps/games', 'class': 'arrow img games'},
                      {'text': 'Music', 'link': base_url + '/apps/music', 'class': 'arrow img music'},
                      {'text': 'News', 'link': base_url + '/apps/news', 'class': 'arrow img news'},
                      {'text': 'Productivity', 'link': base_url + '/apps/productivity', 'class': 'arrow img productivity'},
                      {'text': 'Social Networking', 'link': base_url + '/apps/social-networking', 'class': 'arrow img social-networking'},
                      {'text': 'Travel', 'link': base_url + '/apps/travel', 'class': 'arrow img travel'}]
                              
        @pytest.mark.nondestructive
        def test_all_categories_are_present(self, mozwebqa):

            home_page = Home(mozwebqa)
            home_page.go_to_homepage()
            Assert.true(home_page.is_the_current_page)
            category_list = home_page.find_elements(By.XPATH, TestHomePage.categories_base + '/li')
            # check the number of caterogies is correct
            Assert.true(len(category_list) == len(TestHomePage.categories))
            # check the link, class and text
            index = 0
            for category in category_list:
                    Assert.true(category.text == TestHomePage.categories[index]['text'])
                    Assert.true(category.find_element(By.TAG_NAME, 'a').get_attribute('href') == TestHomePage.categories[index]['link'])
                    Assert.true(category.find_element(By.TAG_NAME, 'div').get_attribute('class') == TestHomePage.categories[index]['class'])
                    index += 1    
