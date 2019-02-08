
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from collections import defaultdict
import re
import json
import os
import time
import arrow
import random


# In[ ]:


class Attraction:
    
    def __init__(self, d=None):
        
        self.name_ = None
        self.about_ = None
        self.attr_url_ = None
        self.rank_ = 0
        self.address_ = None
        self.reviews_ = 0
        self.rating_ = 0
        self.cat_ = []
        self.id_ = None
    
    @property
    def name(self):
        return self.name_
    
    @name.setter
    def name(self, s):
        if isinstance(s, str) and s.strip():
            self.name_ = s.strip().lower()
            
    @property
    def about(self):
        return self.about_
    
    @about.setter
    def about(self, s):
        if isinstance(s, str) and s.strip():
            self.about_ = s
            
    @property
    def attr_id(self):
        return self.id_
    
    @attr_id.setter
    def attr_id(self, s):
        if isinstance(s, str) and s.strip():
            self.id_ = s
            
    @property
    def attr_url(self):
        return self.attr_url_
    
    @attr_url.setter
    def attr_url(self, s):
        if isinstance(s, str) and s.strip():
            self.attr_url_ = s
            
    @property
    def rank(self):
        return self.rank_
    
    @rank.setter
    def rank(self, r):
        self.rank_ = r 
            
    @property
    def address(self):
        return self.address_
    
    @address.setter
    def address(self, s):
        if isinstance(s, str) and s.strip():
            self.address_ = s.strip().lower()
            
    @property
    def cat(self):
        return self.cat_
    
    @cat.setter
    def cat(self, s):
        if isinstance(s, list):
            self.cat_ = s
            
    @property
    def reviews(self):
        return self.reviews_
    
    @reviews.setter
    def reviews(self, s):
        if isinstance(s, int):
            self.reviews_ = s
            
    @property
    def rating(self):
        return self.rating_
    
    @rating.setter
    def rating(self, s):
        self.rating_ = s
            
    def to_dict(self):
        
        return {'name': self.name_, 
                'about': self.about_,
                'attr_url': self.attr_url_,
                'rank': self.rank,
                'address': self.address_,
                'reviews': self.reviews_,
                'rating': self.rating_,
                'cat': self.cat_,
                'id': self.id_}
        
class Review:
    
    def __init__(self):
        
        self.id_ = None
        self.attr_id_ = None
        self.title_ = None
        self.text_ = None
        self.by_user_ = None
        self.rating_ = 0
        self.date_of_experience_ = None
        self.date_of_writing_ = None
        
    @property
    def review_id(self):
        return self.id_
    
    @review_id.setter
    def review_id(self, s):
        if isinstance(s, str):
            self.id_ = s
            
    @property
    def attr_id(self):
        return self.attr_id_
    
    @attr_id.setter
    def attr_id(self, s):
        if isinstance(s, str):
            self.attr_id_ = s
            
    @property
    def title(self):
        return self.title_
    
    @title.setter
    def title(self, s):
        if isinstance(s, str):
            self.title_ = s
    
    @property
    def text(self):
        return self.text_
    
    @text.setter
    def text(self, s):
        if isinstance(s, str):
            self.text_ = s
            
    @property
    def by_user(self):
        return self.by_user_
    
    @by_user.setter
    def by_user(self, s):
        if isinstance(s, str):
            self.by_user_ = s
            
    @property
    def rating(self):
        return self.rating_
    
    @rating.setter
    def rating(self, s):
        self.rating_ = s
            
    @property
    def date_of_experience(self):
        return self.date_of_experience_
    
    @date_of_experience.setter
    def date_of_experience(self, s):
        if isinstance(s, str):
            self.date_of_experience_ = s  
            
    @property
    def date_of_writing(self):
        return self.date_of_writing_
    
    @date_of_writing.setter
    def date_of_writing(self, s):
        if isinstance(s, str):
            self.date_of_writing_ = s 
            
    def to_dict(self):
        
        return {'id': self.id_,
                'attr_id': self.attr_id_,
               'title': self.title_,
               'text': self.text_,
                'by_user': self.by_user_,
               'rating': self.rating_,
               'date_of_experience': self.date_of_experience_,
               'date_of_writing': self.date_of_writing_}
            
class User:
    
    def __init__(self):
        
        self.name_ = None
        self.age_ = None
        self.gender_ = None
        self.loc_ = None
        self.tags_ = []
        self.attr_ids_ = []
    
    @property
    def name(self):
        return self.name_
    
    @name.setter
    def name(self, s):
        if isinstance(s, str) and s.strip():
            self.name_ = s.strip()
            
    @property
    def age(self):
        return self.age_
    
    @age.setter
    def age(self, s):
        if isinstance(s, str):
            self.age_ = s  
            
    @property
    def gender(self):
        return self.gender_
    
    @gender.setter
    def gender(self, s):
        if isinstance(s, str):
            self.gender_ = s  
    
    @property
    def loc(self):
        return self.loc_
    
    @loc.setter
    def loc(self, s):
        if isinstance(s, str):
            self.loc_ = s
            
    @property
    def tags(self):
        return self.tags_
    
    @tags.setter
    def tags(self, s):
        if isinstance(s, list):
            self.tags_ = s
            
    @property
    def attr_ids(self):
        return self.attr_ids_
    
    @attr_ids.setter
    def attr_ids(self, s):
        if isinstance(s, list):
            self.attr_ids_ = s
            
    def to_dict(self):
        
        return {'name': self.name_,
               'age': self.age_,
               'gender': self.gender_,
               'location': self.loc_,
               'tags': self.tags_,
               'attr_ids': self.attr_ids_}
    
            
class Tareviews:
    
    def __init__(self, headless=False, max_ranking=30):
        
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--incognito')
        options.add_argument('--start-maximized')
        
        if headless:
            options.add_argument('--headless')
        
        try:
            self.attraction_ids = {u['id'] for u in json.load(open(os.path.join('data', 'attractions.json')))}
        except:
            self.attraction_ids = set()
        
        print(f'available attraction ids: {len(self.attraction_ids)}')
        
        self.attractions = []
        self.reviews = []
        self.users = []
        
        try:
            self.user_nicknames = {u['name'] for u in json.load(open(os.path.join('data', 'users.json')))}
        except:
            self.user_nicknames = set()
            
        print(f'available user nicknames: {len(self.user_nicknames)}')
        
        try:
            self.review_ids = {u['id'] for u in json.load(open(os.path.join('data', 'reviews.json')))}
        except:
            self.review_ids = set()
            
        print(f'available reviews: {len(self.review_ids)}')

        self.driver = webdriver.Chrome('webdriver/chromedriver', options=options)
        
    def get_attr_info(self, attr_item):
        
        """
        collects basic attraction information for A SINGLE ATTRACTION from the attraction list (NOT on individual attraction pages!)
        handles both the top ranked and normal attractions
        returns an instance of the Attraction class 
        """
        
        attraction = Attraction()
        
        pref = 'attractions-attraction-overview-main-TopPOIs__'
            
        # try to find attraction ranking; if successfull, it's one of the top attractions, otherwise it's a normal attraction
        try:
            attraction.rank = int(attr_item.find_element_by_xpath(f'.//div[contains(@class, "{pref}item_position--")]').text.strip())
        except:
            pass
            
        if attraction.rank:
     
            info = attr_item.find_element_by_xpath(f'.//div[contains(@class, "{pref}info--")]')

#             for tag in info.find_elements_by_xpath('.//span[contains(@class, "attractions-commerce-CategoryTag__category_tag--")]'):
#                 if tag.text.strip():
#                     attraction.cat = tag.text.lower().strip()
          
            try:
                a_with_name = info.find_element_by_xpath(f'.//a[contains(@class, "{pref}name--")]')
                attraction.name = a_with_name.text.strip().lower()
                attraction.attr_url = a_with_name.get_attribute('href')
                attraction.attr_id = re.search(r'd\d+', attraction.attr_url).group(0)
            except:
                pass
          
            try:
                attraction.reviews = int(re.search(r'\d+\,*\d*', info.find_element_by_xpath('.//span[contains(@class, "reviewCount")]').text).group(0).replace(',',''))
            except:
                attraction.reviews = 0
            
            if attraction.reviews:
                
                try:
                    rating_span = info.find_element_by_xpath('.//span[contains(@class, "ui_bubble_rating")]')
                    attraction.rating = int(re.search(r'(?<=bubble_)\d+', rating_span.get_attribute('class')).group(0))/10
                except:
                    pass
            else:
                attraction.rating = 0
            
        else:
            
#             try:
#                 attraction.cat = attr_item.find_element_by_xpath('.//div[@class="tag_line"]').text.lower().strip()
#             except:
#                 pass
            
            try:
                title_block = attr_item.find_element_by_css_selector('div.listing_title')
                a_with_name = title_block.find_element_by_xpath('.//a[@href]')
                attraction.name = a_with_name.text.strip().lower()
                attraction.attr_url = a_with_name.get_attribute('href')
                attraction.attr_id = re.search(r'd\d+', attraction.attr_url).group(0)
            except:
                pass
        
            try:
                rating_div = attr_item.find_element_by_xpath('.//div[@class="listing_rating"]')
                review_counts = rating_div.text.strip().lower()
                attraction.reviews = int(re.search(r'\d+\,*\d*', review_counts).group(0).replace(',',''))
                rating_span = rating_div.find_element_by_xpath('.//span[contains(@class, "ui_bubble_rating")]')
                attraction.rating = int(re.search(r'(?<=bubble_)\d+', rating_span.get_attribute('class')).group(0))/10
            except:
                pass
            
        return attraction
    
    def get_attrs_info(self, url):
        
        """
        collect basic arttraction information FOR ALL ATTRACTIONS from the attraction list
        """
        
        self.driver.get(url)
        
        pref = 'attractions-attraction-overview-main-TopPOIs__'
        
        # is this the top attraction overview page?  
        try:
            top_attractions_title = self.driver.find_element_by_xpath(f'//div[contains(@class, "{pref}title--")]')
        except:
            top_attractions_title = None
            
        if top_attractions_title:

            is_top = True
            # wait for the top attractions block
            WebDriverWait(self.driver, 15)                 .until(EC.presence_of_element_located((By.XPATH, f'//div[contains(@class, "{pref}wrapper--")]')))
        else:
            is_top = False
            
        
        see_more_clicked = False                          
        keep_going = True
                                             
        while keep_going:
            
            filtered_list = self.driver.find_element_by_xpath('//div[@id="FILTERED_LIST"]')
            
            if is_top:
                
                if (not see_more_clicked):
                    lst = filtered_list.find_element_by_xpath(f'.//div[contains(@class, "{pref}initial_set--")]')
                else:
                    # we'll browse the additional block that appeared after See More was clicked
                    lst = filtered_list.find_element_by_xpath(f'.//div/div[contains(@class, "{pref}wrapper--")]')
                
                for j, i in enumerate(lst.find_elements_by_xpath(f'.//li[contains(@class, "{pref}item--")]'), 1):
                
                    attraction = self.get_attr_info(i)
                    
                    if attraction.attr_id:
                        self.attraction_ids.add(attraction.attr_id)
                    
                    self.attractions.append(attraction)
 
                # got through the attractions on the initial list. now what? click on See More
                if not see_more_clicked:
                
                    self.driver.find_element_by_xpath(f'//div[contains(@class, "{pref}see_more--")]').click()
                    
                    time.sleep(random.choice(range(1,5)))
                    see_more_clicked = True
                    continue
                
                # wait for the pagination wrapper
                pagination_wrapper = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, 
                                                                      '//div[contains(@class, "attractions-attraction-overview-main-Pagination__wrapper--")]')))
            
            
                previous_button, selected_button, next_button, last_page = self.pagination_on_attraction_list_pages(pagination_wrapper, is_top=is_top)
                    
                next_button.click()
                time.sleep(random.choice(range(1,4)))
                
                is_top = False
                
            else:
                
                for d in filtered_list.find_elements_by_xpath('.//div[@class="attraction_element_tall"]'):
                    
                    attraction = self.get_attr_info(d)
                    
                    if attraction.attr_id:
                        self.attraction_ids.add(attraction.attr_id)
                        
                    self.attractions.append(attraction)
                
                
                # find next button; there's no next button on the last page
                
#                 ispopup = self.check_for_popup()
                
#                 if ispopup:
#                     print('there\'s a popup')
#                     self.driver.switch_to.default_content()
                    
                # wait for the pagination wrapper
                pagination_wrapper = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, 
                                                                      '//div[@class="pagination"]')))

                previous_button, selected_button, next_button, last_page = self.pagination_on_attraction_list_pages(pagination_wrapper, is_top=is_top)
                
                print(f'page {selected_button}/{last_page}...')
                
                if (selected_button < last_page) and next_button:
                    
                    next_button.send_keys(Keys.ENTER)
                    time.sleep(random.choice(range(1,5)))
                    
                else:
                    
                    keep_going = False
                    print('last page!')
        
        print(f'collected attractions: {len(self.attractions)}')
        
        return self
    
#     def check_for_popup(self):
        
#         try:
#             pp = self.driver.find_element_by_id('BODY_BLOCK_JQUERY_REFLOW')
#             self.driver.switch_to.default_content()
#             return True
#         except:
#             return False
            
    
    def pagination_on_attraction_list_pages(self, pagination_wrapper, is_top):
        
        """
        
        check status of relevant pagination buttons on the attraction list pages (both top and normal attractions)
        
        """
        
        previous_button = selected_button = last_page = next_button = None
        
        if is_top:
            
            # previous button
            for _ in pagination_wrapper.find_elements_by_xpath('.//div[contains(@class, "attractions-attraction-overview-main-Pagination__disabled--")]'):
                _text = _.text.lower().strip()
                if _text == 'previous':
                    previous_button = _ 
                    break
        else:
            
            try:
                previous_button = pagination_wrapper.find_element_by_xpath('.//div/a[contains(@class, "previous")]')
            except:
                pass
            
        if is_top:   
            # selected button
            for _ in pagination_wrapper.find_elements_by_xpath('.//div[contains(@class, "attractions-attraction-overview-main-Pagination__selected--")]'):
                _text = _.text.lower().strip()
                if _text.isdigit():
                    selected_button = int(_text)
                    break
        else:
            
            try:
                selected_button = int(pagination_wrapper.find_element_by_xpath('.//div[@class="pageNumbers"]/span[contains(@class, "current")]').text.strip().lower())
            except:
                pass
            
        if is_top:
                
            # last page button
            visible_page_numbers = []
            for _ in pagination_wrapper.find_elements_by_xpath('.//div[contains(@class, "attractions-attraction-overview-main-Pagination__link--")]'):
                _text = _.text.lower().strip()
                if _text.isdigit():
                    visible_page_numbers.append(int(_text))
            last_page = max(visible_page_numbers)
       
        else:
            
            try:
                visible_page_numbers = [int(_) for _ in pagination_wrapper.find_element_by_xpath('.//div[@class="pageNumbers"]')                                         .text.strip().lower().split() if _.isdigit()]
                        
                last_page = max(visible_page_numbers)
                
            except:
                pass
            
        if is_top:
            
            # next button
            for _ in pagination_wrapper.find_elements_by_xpath('.//div[contains(@class, "attractions-attraction-overview-main-Pagination__button--")]'):
                _a = _.find_element_by_xpath('.//a')
                if _a and _a.text.strip().lower() == 'next':
                    next_button = _a
                    break
        else:
            
            try:
                
                next_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, 
                                                                      '//div[contains(@class, "pagination")]/a[contains(@class, "next")]')))
            except:
                pass
            
                
        return (previous_button, selected_button, next_button, last_page)
    
    def check_pagination_reviews(self):
        
        previous_button = selected_button = last_page = next_button = None
        
        while not all([previous_button, selected_button, last_page, next_button or (selected_button == last_page)]):
        
            # previous button
            
            try:
                for _ in self.driver.find_elements_by_xpath('//a[contains(@class, "previous") and contains(@class, "nav")]'):
                    _text = _.text.lower().strip()
                    if _text == 'previous':
                        previous_button = _ 
                        break
            except:
                print('no PREVIOUS')
                    
            # selected button
            try:
                for _ in self.driver.find_elements_by_xpath('//a[contains(@class, "current") and contains(@class, "pageNum")]'):
                    _text = _.text.lower().strip()
                    if _text.isdigit():
                        selected_button = int(_text)
                        break
            except:
                print('no SELECTED')
                    
            # last page button
            
            try:
                last_page = max([int(t.text) for t in self.driver.find_elements_by_xpath('//a[@data-page-number]') if t.text.isdigit()])
            except:
                print('no LAST PAGE')
            
            # next button
            
            try:
                for _a in self.driver.find_elements_by_xpath('//a[contains(@class, "next") and contains(@class, "nav")]'):
                    if _a and _a.text.strip().lower() == 'next':
                        next_button = _a
                        break
            except:
                print('no NEXT')
        
        return (previous_button, selected_button, next_button, last_page)
    
    
    def get_user_details(self, review_container):
        
        """
        find and return user name and location
        """
        
        user = User()
        
        try:
            info_text = review_container.find_element_by_css_selector('div.info_text')
        except:
            print(f'no infotext found, no way to get user details..')
            return user
        
        try:
            user.name = info_text.find_element_by_xpath('.//div').text
        except:
            print('can\'t find user nickname!')
        
        try:
            user.loc = info_text.find_element_by_xpath('.//div[@class="userLoc"]').text
        except:
            pass
        
        try:
            info_text.click()
        
            time.sleep(random.choice(range(2,5)))
        except:
            print('didnt click infotext!')
        
        ds = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.memberdescriptionReviewEnhancements')))
        t_ = ds.text
#         t_ = self.driver.find_element_by_css_selector('ul.memberdescriptionReviewEnhancements').text
        
        try:
            user.age = re.search(r'\d+\-\d+', t_).group(0)
        except:
            print('can\'t find user age!')
        
        user.gender ='f' if 'woman' in t_ else 'm' if 'man' in t_ else None
        
        try:
            user.tags = [t.text.strip().lower() for t in self.driver.find_elements_by_css_selector('a.memberTagReviewEnhancements')]
        except:
            print('can\'t find user tags')
        
        print('trying to close the user info window..')
        self.driver.find_element_by_css_selector('body>span>div.ui_close_x').click()
        time.sleep(random.choice(range(1,4)))
        
        return user
    
    def get_review(self, review_container):
        
        """
        get reviews
        """
        
        rev = Review()
        
        try:
            rev.review_id = review_container.get_attribute('data-reviewid')
        except:
            print('can\'t find review id!')
            
        try:
            rev.rating = int(re.search(r'(?<=bubble_)\d+', review_container.find_element_by_xpath('.//span[contains(@class, "ui_bubble_rating")]').get_attribute('class')).group(0))/10
        except:
            print('can\'t find review rating!') 
            
        try:
            rev.title = review_container.find_element_by_xpath('.//a[contains(@class, "title")]').text
        except:
            print('can\'t find review title!')
            
        try:
            rev.date_of_experience = arrow.get(review_container                                                .find_element_by_xpath('.//div[@data-prwidget-name="reviews_stay_date_hsx"]')                                                .text.split(':')[-1].strip(), 'MMMM YYYY')                                                 .format('MM/YYYY')
        except:
            print('can\'t find review date of experience!')
            
        try:
            rev.date_of_writing = arrow.get(review_container.find_element_by_xpath('.//span[@class="ratingDate"]').get_attribute('title'), 'D MMMM YYYY').format('DD/MM/YYYY')
        except:
            print('can\'t find review date of writing!')
        
        for _ in review_container.find_elements_by_xpath('.//span[contains(@class, "ulBlueLinks")]'):
            if 'more' in _.text.lower():
                _.click()
                time.sleep(random.choice(range(1,5)))
                break
        
        try:
            rev.text = review_container.find_element_by_xpath('.//p[@class="partial_entry"]').text
        except:
            print('can\'t find review text!')
            
        return rev
        
    
    def get_attr_about_and_address(self, attraction):
        
        """
        go to the attraction page and get all useful info;
        - some attractions have NO REVIEWS
        """
        
        try:
            self.driver.get(attraction.attr_url)
        except:
            print(f'can\'t get attraction url {attraction.attr_url}')
            return attraction
        
        reviews_block = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'REVIEWS')))
        
        try:
            self.driver.find_element_by_css_selector('span>div>span.viewMore').click()
            time.sleep(random.choice(range(1,4))) 
        except:
            pass
        
        # category tags
        try:
            cat_span = self.driver.find_element_by_xpath('//span[contains(@class, "header_detail") and contains(@class, "attractionCategories")]')
            attraction.cat = [c.lower().strip() for c in cat_span.text.split(',')]
        except:
            print('can\'t find attraction categories!')   
        
        number_reviews = 0
        
        try:
            # text is like 7,260 Reviews
            number_reviews = int(re.search(r'\d+\,*\d*\s+(?=Review)', self.driver.find_element_by_css_selector('div.ratingContainer>a>span.reviewCount').text).group(0).replace(',','').strip())
        except:
            print(f'can\'t find the number of reviews for attraction id {attraction.attr_id}!')
        
        if number_reviews > attraction.reviews:
            print(f'warning: number of reviews for attraction {attraction.attr_id} increased to {number_reviews} (was {attraction.reviews})!')
        elif number_reviews < attraction.reviews:
            print(f'warning: number of reviews for attraction {attraction.attr_id} decreased to {number_reviews} (was {attraction.reviews})!')
       
        attraction.reviews = number_reviews 
         
        try:
            attraction.address = self.driver.find_element_by_css_selector('div.detail_section.address').text.lower().strip()
        except:
            print(f'can\'t find address for attraction id {attraction.attr_id}!')
            
        try:
            # if theres an option to extend description via clicking More, do it
            self.driver.find_element_by_xpath('.//span[contains(@class, "attractions-attraction-detail-about-card-Description__readMore--")]').click()
            about = self.driver.find_element_by_xpath('.//div[contains(@class, "attractions-attraction-detail-about-card-Description__modalText--")]').text
            # close the window with full description
            self.driver.find_element_by_xpath('.//div[contains(@class, "overlays-pieces-CloseX__close--")]').click()
        except:
            # if description is short, just pick it up
            about = self.driver.find_element_by_xpath('.//div[contains(@class, "attractions-attraction-detail-about-card-AttractionDetailAboutCard__section--") and not(contains(@class, "title"))]').text
        
        attraction.about = about
        
        return attraction
    
    def get_attrs_about_and_address(self):
        
        """
        get additional information about the attractions from the attraction pages;
        spacifically, we are after the "about" section and location address
        """
        
        total_attrs = len(self.attractions)
        
        print(f'looking for additional info for {total_attrs} attractions..')
        
        attractions_ = []
        
        for i, a in enumerate(self.attractions):
                
            a = self.get_attr_about_and_address(a)
            attractions_.append(a)
            
            if (i > 0) and ((i+1)%20 == 0):
                print(f'{i+1}/{total_attrs}...')
            
        self.attractions = attractions_
        
        self.save(what=['attractions'])
        
        return self
    
    def get_users_and_reviews(self):
        
        """
        for all available attractions, visit attraction page and collect all reviews and user information
        """
        
        rev_ids = set()
        usr_ids = set()
        
        for i, a in enumerate(self.attractions, 1):
            
            if (i == 1) or (i%20==0):
                print(f'attraction {i}/{len(self.attractions)}..')
            
            # if no reviews are available, move on to next attraction
            if not a.reviews:
                print('no reviews for this attraction, moving on...')
                continue
            
            # if there are some reviews, visit the attraction page
            self.driver.get(a.attr_url)
            
            cids = set()  # collected review ids
            
            while len(cids) < a.reviews: 
                    
                try:
                    review_containers = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.review-container')))
                    print(f'found {len(review_containers)} review containers')
                except:
                    print('no review containers found!')
                    continue
                    
                rev_block_done = False 
                    
                while not rev_block_done:
                   
                    try:
                        for j, rev_container in enumerate(review_containers, 1):
                    
                            try:
                                rev = self.get_review(rev_container)
                            except:
                                print('didnt get review!')
                                raise Exception()
                            
                            try:
                                rev.attr_id = a.attr_id
                            except:
                                print('didnt assign attraction id to review!')
                            
                            try:
                                user = self.get_user_details(rev_container)
                            except:
                                print('didnt get user!')
                                raise Exception()
                            
                            try:
                                rev.by_user = user.name
                            except:
                                print('didnt assign by_user to review!')
                            
                            try:
                                user.attr_ids.append(a.attr_id)
                            except:
                                print('didnt append attraction id to user attraction ids')
                            
                            if rev.review_id not in rev_ids:
                                self.reviews.append(rev)
                                rev_ids.add(rev.review_id)
                                
                            if user.name not in usr_ids:
                                usr_ids.add(user.name)
                                self.users.append(user)
            
                            cids.add(rev.review_id)
               
                            if len(cids)%20 == 0:
                                print(f'done {len(cids)}/{a.reviews} reviews...')
                                self.save(what=['users', 'reviews'])
                   
                        rev_block_done = True

                    except:
                        print('couldnt finish the review block!')
                   
                pagination_found = False
               
                while not pagination_found:
               
                    try:   
                        previous_button, selected_button, next_button, last_page = self.check_pagination_reviews()
                        pagination_found = True
                    except:
                        print('can\'t find pagination! trying again...')
                
                # on the very last page buttons previous and next are visible but the next button is disabled (not ckickable)
                if 'disabled' not in next_button.get_attribute('class'):
                    next_button.click()
                    sc = random.choice(range(3,7))
                    print(f'clicked NEXT. waiting {sc} seconds...')
                    time.sleep(sc)
                else:
                    print(f'last page. collected {len(cids)}/{a.reviews} reviews')
                    if (len(cids) < a.reviews):
                        print('although collected fewer reviews than expected, moving on to next attraction')
                        break

        self.driver.quit()
        
        return self       
    
    def save(self, what):
        
        if not os.path.exists('data'):
            os.mkdir('data')
        
        if ('attractions' in what) and self.attractions:
            json.dump([a.to_dict() for a in self.attractions], open(os.path.join('data', 'attractions.json'), 'w'))
        if ('users' in what) and self.users:
            json.dump([u.to_dict() for u in self.users], open(os.path.join('data', 'users.json'), 'w'))
        if ('reviews' in what) and self.reviews:
            json.dump([r.to_dict() for r in self.reviews], open(os.path.join('data', 'reviews.json'), 'w'))
        
        return self
        


# In[ ]:


if __name__ == '__main__':
    
    ta = Tareviews(headless=True) \
        .get_attrs_info('https://www.tripadvisor.com.au/Attractions-g255066-Activities-Darwin_Top_End_Northern_Territory.html') \
        .get_attrs_about_and_address().get_users_and_reviews()
