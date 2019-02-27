class Attraction:
    
    def __init__(self, d=None):
        
        self.name_ = None
        self.about_ = None
        self.attr_url_ = None
        self.rank_ = 0
        self.popularity_ = 0
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
    def popularity(self):
        return self.popularity_
    
    @popularity.setter
    def popularity(self, r):
        self.popularity_ = r
            
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

    def from_dict(self, dict_):
        
        self.name = dict_.get('name', None)
        self.about = dict_.get('about', None)
        self.attr_url = dict_.get('attr_url', None)
        self.rank = dict_.get('rank', None)
        self.popularity = dict_.get('popularity', None)
        self.address = dict_.get('address', None)
        self.reviews = dict_.get('reviews', None)
        self.rating = dict_.get('rating', None)
        self.cat = dict_.get('cat', None)
        self.attr_id = dict_.get('id', None)
        
        return self
            
    def to_dict(self):
        
        return {'name': self.name_, 
                'about': self.about_,
                'attr_url': self.attr_url_,
                'rank': self.rank_,
                'popularity': self.popularity_,
                'address': self.address_,
                'reviews': self.reviews_,
                'rating': self.rating_,
                'cat': self.cat_,
                'id': self.id_}