class User:
    
    def __init__(self):
        
        self.name_ = None
        self.real_name_ = None
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
    def real_name(self):
        return self.real_name_
    
    @name.setter
    def real_name(self, s):
        if isinstance(s, str) and s.strip():
            self.real_name_ = s.strip()
            
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
                'real_name': self.real_name_,
               'age': self.age_,
               'gender': self.gender_,
               'location': self.loc_,
               'tags': self.tags_}
    
    def from_dict(self, dict_):
        
        self.name = dict_.get('name', None)
        self.real_name = dict_.get('real_name', None)
        self.age = dict_.get('age', None)
        self.gender = dict_.get('gender', None)
        self.location = dict_.get('location', None)
        self.tags = dict_.get('tags', None)
        
        return self