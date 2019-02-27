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
            
    def to_dict(self):
        
        return {'id': self.id_,
                'attr_id': self.attr_id_,
               'title': self.title_,
               'text': self.text_,
                'by_user': self.by_user_,
               'rating': self.rating_,
               'date_of_experience': self.date_of_experience_,
               'date_of_writing': self.date_of_writing_}