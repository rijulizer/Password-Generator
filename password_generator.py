import pandas as pd
import numpy as np
import os
import pickle

class PasswordGenerator:
    def __init__(self, min_pass_len):
        self.min_pass_len=min_pass_len
        # min_pass_len=16
        self.max_pass_len = self.min_pass_len + 6 #22
        self.speclchar_num_len = 5
        self.movie_data_path = os.getcwd() + '/artifacts/Top_10000_Movies_2.csv'
        self.list_titles_path = os.getcwd() + '/artifacts/list_titles.pkl'

        self.speclchar_num_map = {
        0:"~",
        1:"!",
        2:"@",
        3:"#",
        4:"$",
        5:"%",
        6:"^",
        7:"&",
        8:"*",
        9:"(",
        10:")",
        11:"_",
        12:"+",
        13:"<",
        14:">",
        15:"?",
        16:"{",
        17:"}",
        18:"|"
    }
    
    def read_movie_dataset(self):
        pdf_movies = pd.read_csv(self.movie_data_path)
        # select particular columns
        pdf_movies_processed = pdf_movies[["id","original_language","original_title","popularity","vote_average"]]
        

        pdf_movies_processed.loc[:,'new_titles'] = pdf_movies_processed["original_title"].str.replace(" ", "")
        pdf_movies_processed.loc[:,'new_titles'] = pdf_movies_processed["new_titles"].str.replace(":", "")
        pdf_movies_processed.loc[:,'new_title_len'] = pdf_movies_processed["new_titles"].str.len()
        pdf_movies_processed = (
            pdf_movies_processed[(pdf_movies_processed['new_title_len']
                                .between(self.min_pass_len - self.speclchar_num_len,
                                        self.max_pass_len - self.speclchar_num_len))
                                & (pdf_movies_processed["new_titles"].str.contains('[A-Za-z]', na=False))
                                & (pdf_movies_processed["original_language"]=="en")])
                         #  & (pdf_movies_2["original_title"].str.isalpha() == True)]
        pdf_movies_processed.dropna(inplace=True) 
        titles = pdf_movies_processed["new_titles"].values
        with open(self.list_titles_path, 'wb') as f:
            pickle.dump(titles, f)
        return titles
    
    def read_titles(self):
        try:
            with open(self.list_titles_path, 'rb') as f:
                self.titles = pickle.load(f)
        except FileNotFoundError as e:
            self.titles = self.read_movie_dataset()
        # return self.titles
        
    def generate(self):
        
        # get random lengths of special and numerical characters 
        self.specl_chars_len = np.random.randint(1,self.speclchar_num_len)
        self.num_len = self.speclchar_num_len - self.specl_chars_len

        # get the random starting indexes of special and numerical characters 
        num_start = np.random.randint(1, 9- self.num_len + 1)
        spclchar_start = np.random.randint(0, list(self.speclchar_num_map.keys())[-1] - self.specl_chars_len + 1)

        # create the special and numerical characters 
        spcl_num_chars = ""
        for _ in range(self.specl_chars_len):
            spcl_num_chars += str(self.speclchar_num_map[spclchar_start])
            spclchar_start+=1
        for _ in range(self.num_len):
            spcl_num_chars += str(num_start)
            num_start+=1

        # print((self.specl_chars_len, self.num_len), spclchar_start, num_start, spcl_num_chars)
        
        rand_title = np.random.choice(self.titles, replace=True)
        password = rand_title + spcl_num_chars
        return password

if __name__ == "__main__":
    pg = PasswordGenerator(16)
    pg.read_titles()
    password = pg.generate()
    print("password is - ", password)