
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


# In[1]:


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
    
    def from_dict(self, dict_):
        
        self.name = dict_['name']
        self.about = dict_['about']
        self.attr_url = dict_['attr_url']
        self.rank = dict_['rank']
        self.address = dict_['address']
        self.reviews = dict_['reviews']
        self.rating = dict_['rating']
        self.cat = dict_['cat']
        self.attr_id = dict_['id']
        
        return self
        
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
    
    def from_dict(self, dict_):
        
        self.review_id = dict_['id']
        self.attr_id = dict_['attr_id']
        self.title = dict_['title']
        self.text = dict_['text']
        self.by_user = dict_['by_user']
        self.by_user = dict_['by_user']
        self.rating = dict_['rating']
        self.date_of_experience = dict_['date_of_experience']
        self.date_of_writing = dict_['date_of_writing']
        
        return self
            
class User:
    
    def __init__(self):
        
        self.name_ = None
        self.age_ = None
        self.gender_ = None
        self.loc_ = None
        self.tags_ = []
    
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
            
    def to_dict(self):
        
        return {'name': self.name_,
               'age': self.age_,
               'gender': self.gender_,
               'location': self.loc_,
               'tags': self.tags_}
    
    def from_dict(self, dict_):
        
        self.name = dict_['name']
        self.age = dict_['age']
        self.gender = dict_['gender']
        self.location = dict_['location']
        self.tags = dict_['tags']
        
        return self
    
      


# In[ ]:



class Tareviews:
    
    def __init__(self, headless=False, save_every=20):
  
  """
  note: because there doesn't seem to be a working way to get rid of the annoying "allow location" notifications
  in Chrome at the moment, we don't implement the tart when you search for a location forst and then go to the things-to-do 
  page. Instead, as a temporary somlutions, we hardcode a number of the things-to-do page urls to choose from. 
  """
  
  options = webdriver.ChromeOptions()
  options.add_argument('--ignore-certificate-errors')
  options.add_argument('--ignore-ssl-errors')
  options.add_argument('--incognito')
  options.add_argument('--start-maximized')
  prefs = {"profile.default_content_setting_values.notifications" : 2}
  options.add_experimental_option("prefs",prefs)
  
  if headless:
      options.add_argument('--headless')
  
  self.locations = {'sydney': 'https://www.tripadvisor.com.au/Attractions-g255060-Activities-Sydney_New_South_Wales.html',
                   'melbourne': 'https://www.tripadvisor.com.au/Attractions-g255100-Activities-Melbourne_Victoria.html',
                   'perth': 'https://www.tripadvisor.com.au/Attractions-g255103-Activities-Perth_Greater_Perth_Western_Australia.html',
                   'brisbane': 'https://www.tripadvisor.com.au/Attractions-g255068-Activities-Brisbane_Brisbane_Region_Queensland.html',
                   'adelaide': 'https://www.tripadvisor.com.au/Attractions-g255093-Activities-Adelaide_Greater_Adelaide_South_Australia.html',
                   'hobart': 'https://www.tripadvisor.com.au/Attractions-g255097-Activities-Hobart_Greater_Hobart_Tasmania.html',
                   'darwin': 'https://www.tripadvisor.com.au/Attractions-g255066-Activities-Darwin_Top_End_Northern_Territory.html',
                   'canberra': 'https://www.tripadvisor.com.au/Attractions-g255057-Activities-Canberra_Australian_Capital_Territory.html'}
  
  self.attractions = []
  self.reviews = []
  self.users = []
  
  self.attraction_ids = set()
  self.review_ids = set()

  self.driver = webdriver.Chrome('webdriver/chromedriver', options=options)
  self.WAIT_SEC = 20
  self.WAIT_SEC_SHORT = 8
  
  self.save_every = save_every
  
    def get_attr_info(self, attr_item):
  
  """
  collects basic attraction information for A SINGLE ATTRACTION from the attraction list (NOT on individual attraction pages!)
  handles both the top ranked and normal attractions
  returns an instance of the Attraction class 
  
  note: the number of reviews on the top attraction list is not always the same as on the individual attraction pages (for whatever reason)!
         - we trust the number on the attraction page more
         - so, no need to collect the number of reviews on the top attraction list
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
    
      try:
          a_with_name = info.find_element_by_xpath(f'.//a[contains(@class, "{pref}name--")]')
          attraction.name = a_with_name.text.strip().lower()
          attraction.attr_url = a_with_name.get_attribute('href')
          attraction.attr_id = re.search(r'd\d+', attraction.attr_url).group(0)
      except:
          pass
    
#             try:
#                 attraction.reviews = int(re.search(r'\d+\,*\d*', info.find_element_by_xpath('.//span[contains(@class, "reviewCount")]').text).group(0).replace(',',''))
#             except:
#                 attraction.reviews = 0
      
#             if attraction.reviews:
          
#                 try:
#                     rating_span = info.find_element_by_xpath('.//span[contains(@class, "ui_bubble_rating")]')
#                     attraction.rating = int(re.search(r'(?<=bubble_)\d+', rating_span.get_attribute('class')).group(0))/10
#                 except:
#                     pass
#             else:
#                 attraction.rating = 0
      
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
  
#             try:
#                 rating_div = attr_item.find_element_by_xpath('.//div[@class="listing_rating"]')
#                 review_counts = rating_div.text.strip().lower()
#                 attraction.reviews = int(re.search(r'\d+\,*\d*', review_counts).group(0).replace(',',''))
#                 rating_span = rating_div.find_element_by_xpath('.//span[contains(@class, "ui_bubble_rating")]')
#                 attraction.rating = int(re.search(r'(?<=bubble_)\d+', rating_span.get_attribute('class')).group(0))/10
#             except:
#                 pass
      
  return attraction
    
    def get_attrs_info(self, location, use_local=False):
  
  """
  collect basic attraction information FOR ALL ATTRACTIONS from the attraction list
  """
  
  self.location = location.lower().strip()
  
  if not self.location in self.locations:
      raise Exception(f'your location ({location}) is not supported!')
      
  self.ATR_FILE = os.path.join('data', f'attractions_{self.location}.json')
  self.USR_FILE = os.path.join('data', f'users_{self.location}.json')
  self.REV_FILE = os.path.join('data', f'reviews_{self.location}.json')
  
  if use_local:
      
      # check for a local attraction file
      try:
          self.attractions = [Attraction().from_dict(a) for a in json.load(open(self.ATR_FILE))] 
          self.attraction_ids = {r.attr_id for r in self.attractions}
          print(f'found {len(self.attraction_ids)} attractions stored locally')
      except:
          print('no locally stored attractions!')
          
      # check for a local review file
      try:
          self.reviews = [Review().from_dict(r) for r in json.load(open(self.REV_FILE))]
          self.review_ids = {r.review_id for r in self.reviews}
          print(f'found {len(self.review_ids)} reviews stored locally')
      except:
          print('no locally stored reviews!')
          
      # check for a local user file
      try:
          self.users = [User().from_dict(r) for r in json.load(open(self.USR_FILE))]
          self.user_ids = {r.name for r in self.users}
          print(f'found {len(self.user_ids)} user names stored locally')
      except:
          print('no locally stored users!')
      
      if len(self.attractions) > 0:
          return self
      
  print(f'attractions: {len(self.attractions)}, reviews: {len(self.reviews)}, users: {len(self.users)}')
      
  print(f'starting to collect attraction information from attraction list for {self.location.upper()}')
  
  self.driver.get(self.locations[self.location])
  
  pref = 'attractions-attraction-overview-main-TopPOIs__'
  
  # is this the top attraction overview page?  
  try:
      top_attractions_title = self.driver.find_element_by_xpath(f'//div[contains(@class, "{pref}title--")]')
  except:
      top_attractions_title = None
      
  if top_attractions_title:

      is_top = True
      # wait for the top attractions block
      WebDriverWait(self.driver, 15)           .until(EC.presence_of_element_located((By.XPATH, f'//div[contains(@class, "{pref}wrapper--")]')))
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
          pagination_wrapper = WebDriverWait(self.driver, self.WAIT_SEC)                               .until(EC.visibility_of_element_located((By.XPATH, 
                                                                '//div[contains(@class, "attractions-attraction-overview-main-Pagination__wrapper--")]')))
      
      
          previous_button, selected_button, next_button, last_page = self.pagination_on_attraction_list_pages(pagination_wrapper, is_top=is_top)
              
          next_button.click()
          time.sleep(random.choice(range(1,5)))
          
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
          pagination_wrapper = WebDriverWait(self.driver, self.WAIT_SEC)                           .until(EC.visibility_of_element_located((By.XPATH, '//div[@class="pagination"]')))

          previous_button, selected_button, next_button, last_page = self.pagination_on_attraction_list_pages(pagination_wrapper, is_top=is_top)
          
          if (selected_button < last_page) and next_button:
              
              next_button.send_keys(Keys.ENTER)
              time.sleep(random.choice(range(1,5)))
              
          else:
              
              keep_going = False
  
  print(f'done. found {len(self.attractions)} attractions')
  
  total_attrs = len(self.attractions)
  
#         digs = len(str(total_attrs))
  
  print(f'looking for additional attraction information...')
  
  attractions_ = []
  
  t0 = time.time()
  
  for i, a in enumerate(self.attractions, 1):
          
      a = self.get_attr_about_and_address(a)
      attractions_.append(a)
      
      m, s = divmod(time.time() - t0, 60)
      
      print(f'{i}/{total_attrs} ({100*i/total_attrs:03.1f}%) done. elapsed time: {m:02.0f} min {s:02.0f} sec')
      
  self.attractions = attractions_
  
  self.save(what=['attractions'])
  
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
          visible_page_numbers = [int(_) for _ in pagination_wrapper.find_element_by_xpath('.//div[@class="pageNumbers"]')                                   .text.strip().lower().split() if _.isdigit()]
                  
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
          
          next_button = WebDriverWait(self.driver, self.WAIT_SEC)                       .until(EC.element_to_be_clickable((By.XPATH, '//div[contains(@class, "pagination")]/a[contains(@class, "next")]')))
      except:
          pass
      
          
  return (previous_button, selected_button, next_button, last_page)
    
    def check_pagination_reviews(self):
  
  previous_button = selected_button = last_page = next_button = None
  
  # run until all buttons get some value
  while not all([previous_button, selected_button, last_page, next_button]):
  
      # previous button: find the very first one from the top; supposed to be an element
      try:
          previous_button = self.driver.find_element_by_css_selector('div.unified.ui_pagination>a.nav.previous.ui_button.secondary')
      except:
          print('review pagination: no PREVIOUS button found!')
              
      # selected button, element
      try:
          selected_button = self.driver.find_element_by_css_selector('div.pageNumbers>a.pageNum.current')
      except:
          print('review pagination: no SELECTED button found')
              
      # last page; integer number
      ns = [t.get_attribute('data-page-number')
                for t in self.driver.find_elements_by_css_selector('div.mobile-more>div>div.unified.ui_pagination>div.pageNumbers>a[data-page-number]')]
      try:
          last_page = max([int(s) for s in ns])
      except:
          print('review pagination: no LAST PAGE NUMBER found')
      
      # next button; element  
      try:
          next_button = self.driver.find_element_by_css_selector('div.unified.ui_pagination>a.nav.next.taLnk.ui_button.primary')
      except:
          print('review pagination: no NEXT button found!')
  
  return (previous_button, selected_button, next_button, last_page)
    
    
    def get_user_details(self, review_container):
  
  """
  find and return user name and location
  """
  
  user = User()
  
  try:
      info_text = review_container.find_element_by_css_selector('div.info_text')
  except:
      print(f'no infotext..')
      
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
  
      time.sleep(random.choice(range(3,6)))
  except:
      print('didnt click infotext!')
  
  try:
      t_ = WebDriverWait(self.driver, self.WAIT_SEC)           .until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.memberdescriptionReviewEnhancements'))).text
      user.age = re.search(r'\d+\-\d+', t_).group(0)
      user.gender ='f' if 'woman' in t_ else 'm' if 'man' in t_ else None
  except:
#             print('can\'t find lines with user details. skipping searching for age and gender')
      pass
  
  try:
      user.tags = [t.text.strip().lower() for t in self.driver.find_elements_by_css_selector('a.memberTagReviewEnhancements')]
  except:
      pass
  
  try:
      
      WebDriverWait(self.driver, self.WAIT_SEC)           .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body>span>div.ui_close_x')))           .click()
      time.sleep(random.choice(range(2,5)))
      
  except:
      print('can\'t close the customer info pop-up!')
  
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
      rev.date_of_experience = arrow.get(review_container                                          .find_element_by_xpath('.//div[@data-prwidget-name="reviews_stay_date_hsx"]')                                          .text.split(':')[-1].strip(), 'MMMM YYYY')                                           .format('MM/YYYY')
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
  
  print(f'attraction: {attraction.name}...')
  
  try:
      self.driver.get(attraction.attr_url)
  except:
      print(f'can\'t get attraction url {attraction.attr_url}')
      return attraction

  try:
      reviews_block = WebDriverWait(self.driver, self.WAIT_SEC).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div#REVIEWS')))
  except:
      print('no reviews block! reloading..')
      self.driver.get(attraction.attr_url)
  
  try:
      self.driver.find_element_by_css_selector('span>div>span.viewMore').click()
      time.sleep(random.choice(range(1,4))) 
  except:
      pass
  
  category_span = None
  
  try:
      category_span = WebDriverWait(self.driver, self.WAIT_SEC)                           .until(EC.visibility_of_element_located((By.CSS_SELECTOR, 
                                                                   'span.is-hidden-mobile.header_detail.attractionCategories>div.detail')))

  except:
      print(f'no category span found for {attraction.name}!')
      
  if category_span:
      
      try:
          attraction.cat = [c.lower().strip() for c in category_span.text.split(',')]
      except:
          print(f'can\'t extract attraction categories from {category_span.text}!')  
  
  attraction.reviews = 0
  
  review_count_span = None
  
  try:
      review_count_span = WebDriverWait(self.driver, self.WAIT_SEC_SHORT)                               .until(EC.visibility_of_element_located((By.CSS_SELECTOR, 
                                                                       'div.headerInfoWrapper>div.ratingContainer>a>span.reviewCount')))
  except:
      print(f'can\'t find the review count span for {attraction.name}')
  
  if review_count_span:
      try:
          # text is like 7,260 Reviews or 220 Reviews; 377 Reviews
          attraction.reviews = int(re.search(r'\d+(?=\s+Review)', review_count_span.text.replace(',','')).group(0))
      except:
          print(f'problem with extracting review count from {review_count_span.text.upper()} for {attraction.name}!')
                                     
  try:
      attraction.rating = float(self.driver.find_element_by_css_selector('div.section.rating>span.overallRating').text.strip())
  except:
      if attraction.reviews:
          print(f'can\'t find rating for {attraction.name} although it has {attraction.reviews} reviews!')                      
  try:
      attraction.address = WebDriverWait(self.driver, self.WAIT_SEC_SHORT)                   .until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.contactInfo>div.detail_section.address'))).text
  except:                   
      print(f'can\'t find the address section for {attraction.name}')
      
  try:
      # if theres an option to extend description via clicking More, do it
      self.driver.find_element_by_xpath('.//span[contains(@class, "attractions-attraction-detail-about-card-Description__readMore--")]').click()
      about = self.driver.find_element_by_xpath('.//div[contains(@class, "attractions-attraction-detail-about-card-Description__modalText--")]').text
      # close the window with full description
      self.driver.find_element_by_xpath('.//div[contains(@class, "overlays-pieces-CloseX__close--")]').click()
  except:
      pass
  
  about = ''
  
  # if description is short, just pick it up
  try:
      about = self.driver.find_element_by_xpath('//div[contains(@class, "attractions-attraction-detail-about-card-AttractionDetailAboutCard__section--") and not(contains(@class, "title"))]').text
  except:
      pass
  
  try:
      about = self.driver.find_element_by_xpath('//div[contains(@class, "attractions-supplier-profile-SupplierAbout__about--")]').text
  except:
      pass
  
  attraction.about = about
  
  return attraction
    
    def get_attrs_about_and_address(self):
  
  """
  get additional information about the attractions from the attraction pages;
  spacifically, we are after the "about" section and location address
  """
  
  total_attrs = len(self.attractions)
  
#         digs = len(str(total_attrs))
  
  print(f'looking for additional attraction information...')
  
  attractions_ = []
  
  t0 = time.time()
  
  for i, a in enumerate(self.attractions, 1):
          
      a = self.get_attr_about_and_address(a)
      attractions_.append(a)
      
      m, s = divmod(time.time() - t0, 60)
      
      print(f'{i}/{total_attrs} ({100*i/total_attrs:03.1f}%) done. elapsed time: {m:02.0f} min {s:02.0f} sec')
      
  self.attractions = attractions_
  
  self.save(what=['attractions'])
  
  return self
    
    def get_users_and_reviews(self):
  
  """
  for all available attractions, visit attraction page and collect all reviews and user information
  """
  
  rev_ids = set()
  usr_ids = set()
  
  t0 = time.time()
  
  for i, a in enumerate(self.attractions[::-1], 1):
      
      print(f'#{i}/{len(self.attractions)}: {a.name.upper()} (id:{a.attr_id})...')
      
      if a.attr_id in ['d654640', 'd256584', 'd256558', 'd10062913', 'd522372', 'd522360']:
          print(f'skipping {a.name}...')
          continue
            
      if i > 1:
          
          m, s = divmod(time.time() - t0, 60)
          h, m = divmod(m, 60)
          
          print(f'time so far: {h:02.0f} h {m:02.0f} m {s:02.0f} s')
      
      # if no reviews are available, move on to next attraction
      if not a.reviews:
          print('no reviews for this attraction, moving on...')
          continue
      
      # if there are some reviews, visit the attraction page
      self.driver.get(a.attr_url)    
      
      # select English reviews only
      radio_en = None
      try:
          radio_en = WebDriverWait(self.driver, 15)               .until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ui_radio.item[data-value="en"][data-tracker="English"]')))
      except:
          print('can\'t find the English radio button!')
          
      if radio_en:
          
          try:
              radio_en.click()
              time.sleep(random.choice(range(1,4)))
              # check that the reviews updated to English only; note: radio button text is like "English (3,122)"
              n_eng_reviews = int(re.search(r'\d+', radio_en.text.replace(',','')).group(0))
              print(f'selected reviews in English - {n_eng_reviews} reviews available')
              # is this the same as in the review block header? text here is supposed ot be like "1 - 10 of 3,122 reviews"
              el = self.driver.find_element_by_css_selector('div[data-contextchoice="DETAIL"]>div.pagination-details').text.replace(',','')
              n_reviews_hdr = int(re.search(r'(?<=of)\s+\d+', el).group(0).strip())
              if n_eng_reviews != n_reviews_hdr:
                  print(f'warning: expected {n_eng_reviews} English reviews but see {n_reviews_hdr} in the header!')
          except:
              print('can\'t click the English radio button!')
      
      # look at the attraction ranking tagline
      ranking_tag = self.driver.find_element_by_css_selector('span.header_popularity.popIndexValidation').text.strip()
      
      cids = set()  # collected review ids
      
      while len(cids) < a.reviews: 
              
          try:
              review_containers = WebDriverWait(self.driver, self.WAIT_SEC)                       .until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.review-container')))
          except:
              print('no review containers found!')
              continue
              
          rev_block_done = False 
          
          c_url = self.driver.current_url
              
          while not rev_block_done:
             
              try:
                  for j, rev_container in enumerate(review_containers, 1):
              
                      try:
                          rev = self.get_review(rev_container)
                      except:
                          print('didn\'t get review! reloading the page')
                          raise Exception()
                      
                      rev.attr_id = a.attr_id
                      
                      try:
                          user = self.get_user_details(rev_container)
                      except:
                          print('didnt get user!')
                          raise Exception()
                      
                      rev.by_user = user.name
                      
                      if rev.review_id not in rev_ids:
                          self.reviews.append(rev)
                          rev_ids.add(rev.review_id)
                          
                      if user.name not in usr_ids:
                          usr_ids.add(user.name)
                          self.users.append(user)
      
                      cids.add(rev.review_id)
         
                      if len(cids)%self.save_every == 0:
                          print(f'{len(cids)}/{a.reviews} reviews...')
                          self.save(what=['users', 'reviews'])
             
                  rev_block_done = True

              except:
                  print('couldn\'t finish the review block! reloading page...')
                  
                  self.driver.get(c_url)
                  try:
                      review_containers = WebDriverWait(self.driver, self.WAIT_SEC)                           .until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'div.review-container')))
                      print(f'found {len(review_containers)} review containers')
                  except:
                      print('no review containers found!')
                      continue
             
          pagination_found = False
         
          while not pagination_found:
         
              try:   
                  previous_button, selected_button, next_button, last_page = self.check_pagination_reviews()
                  pagination_found = True
              except:
                  print('can\'t find pagination! trying again...')
          
          # on the very last page buttons previous and next are visible but the next button is disabled (not ckickable)
          if 'disabled' not in next_button.get_attribute('class'):
              
              try:
                  next_button.click()
                  sc = random.choice(range(3,7))
                  time.sleep(sc)
              except:
                  print('can\'t click next, switching to direct url for the next page..')
                  
                  current_url = self.driver.current_url 
                  print('current_url=',current_url)
                  
                  # there are 10 reviews on each full page and urls look like this:
                  # 
                  # p2: https://www.tripadvisor.com.au/Attraction_Review-g255093-d270480-Reviews-or10-Adelaide_Central_Market-Adelaide_Greater_Adelaide_South_Australia.html
                  # p3: https://www.tripadvisor.com.au/Attraction_Review-g255093-d270480-Reviews-or20-Adelaide_Central_Market-Adelaide_Greater_Adelaide_South_Australia.html
                  
                  new_review_page_url = None
                  
                  offset_ = None
                         
                  try:
                      offset_ = re.search(r'(?<=or)\d+(?=\-)', current_url).group(0)
                      print('offset_=',offset_)
                  except:
                         print('no offset!')
                  if offset_:
                      new_review_page_url = current_url.replace(f'-or{offset_}-', f'-or{str(int(offset_) + 10)}-')
                      print('new_review_page_url=',new_review_page_url)
                      self.driver.get(new_review_page_url)
    
          else:
              
              print(f'last page. collected {len(cids)}/{a.reviews} reviews')
              if (len(cids) < a.reviews):
                  print('although collected fewer reviews than expected, moving on to next attraction')
                  break
      
      self.save(what=['users', 'reviews'])

  self.driver.quit()
  
  return self       
    
    def save(self, what):
  
  
  if not os.path.exists('data'):
      os.mkdir('data')
  
  if ('attractions' in what) and self.attractions:
      json.dump([a.to_dict() for a in self.attractions], open(os.path.join('data', f'attractions_{self.location}.json'), 'w'))
  if ('users' in what) and self.users:
      json.dump([u.to_dict() for u in self.users], open(os.path.join('data', f'users_{self.location}.json'), 'w'))
  if ('reviews' in what) and self.reviews:
      json.dump([r.to_dict() for r in self.reviews], open(os.path.join('data', f'reviews_{self.location}.json'), 'w'))
  
  return self 
  


# In[ ]:


if __name__ == '__main__':
    
    ta = Tareviews(save_every=30, headless=True)         .get_attrs_info(location='Melbourne', use_local=True)         .get_users_and_reviews()



