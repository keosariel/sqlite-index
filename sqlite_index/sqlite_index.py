from sqlitedict import SqliteDict
import re
import os
import time

__all__ = [ "Index" ]

def timeit(f):
    def wrap(*args, **kwargs):
        time1 = time.time()
        ret = f(*args, **kwargs)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap

class Index(object):
    _ngram_min_length = 1
    _ngram_max_length = None
    _tokenizer = re.compile(r'\w+')    
    
    def __init__(self,fp,_fields=[]):
        """Creates a new `index` or uses an existing one which
        would be loaded from the file `fp`
        
        Params:
            `fp` is the file where the index would be stored, or is
            stored if it already exists
            
            `_fields` these are the available fields in the index
        
        *Note* if the names in `_fields` doesn't exists it would be created
        However the file would be stored with the extension `.sqlite`
        """
        
        fp = fp+".sqlite"
        
        self.index   = None
        self.fp      = fp
        self._fields = _fields
        
        if os.path.exists(fp):
            self.index = SqliteDict(fp, autocommit=True)
        else:
            self.index = SqliteDict(fp, autocommit=True)
            self.index["index"] = {field:{} for field in self._fields}
            
        self.current_index = self.index.get("index",{field:{} for field in self._fields})
        
        for field in self._fields:
            if field not in self.current_index:
                self.current_index[field] = []
    
    @timeit    
    def search(self,query,_fields=[]):
        """Query the index and returns all corresponding `ids`
        
        Params:
            `query` the requested query
            `_fields` what fields to query
        """
        tokens = self._tokenizer.findall(query)
        
        list_of_ids = []
        
        for field in _fields:
            if field in self.current_index:
                for token in tokens:
                    list_of_ids += self.current_index[field].get(token,[])
        
        no_dup_posts = set(list_of_ids)
        return sorted(no_dup_posts,key=lambda idx: list_of_ids.count(idx),reverse=True)
        

    def add(self,value,idx,_fields=[],autocommit=True):
        """Add `value` to the index and also with the corresponding `idx`
        
        Params:
            `value` is a word or sentence
            `idx` is an integer. Think of it as an ID
            
        *Note* the `value` would be added to the fields provided in `_fields`
        """
        
        value = value.lower().strip()
        tokens = self._tokenizer.findall(value)
                
        ngrams = [token[:i] for token in tokens for i in range(self._ngram_min_length,len(token)+1)]
        
        # print(ngrams)
        
        for field in _fields:
            if field in self.current_index:
                for ng in ngrams:
                    if ng not in self.current_index[field]:
                        self.current_index[field][ng] = []
                    
                    if idx not in self.current_index[field][ng]:
                        self.current_index[field][ng].append(idx)

        if autocommit:
            self.commit()

    def remove(self,value,idx,_fields=[],autocommit=True):
        """Remove `value` from the index and also with the corresponding `idx`
        
        Params:
            `value` is a word or sentence
            `idx` is an integer. Think of it as an ID
            
        *Note* the `value` would be removed from the fields provided in `_fields`
        """
        
        value = value.lower().strip()
        tokens = self._tokenizer.findall(value)
                
        ngrams = [token[:i] for token in tokens for i in range(self._ngram_min_length,len(token)+1)]
        
        for field in _fields:
            if field in self.current_index:
                for ng in ngrams:
                    if ng in self.current_index[field]:
                        if idx in self.current_index[field][ng]:
                            # Removes `idx` for index
                            self.current_index[field][ng].remove(idx)

        if autocommit:
            self.commit()
        
    def commit(self):
        # with SqliteDict(self.fp) as index:
        self.index["index"] = self.current_index
        # index.commit()
    
    def as_dict(self):
        return self.current_index

    def __repr__(self):
        return "<Index %s>" % ",".join(f"{k}_ngrams:{len(v)}" for k,v in self.index["index"].items())
