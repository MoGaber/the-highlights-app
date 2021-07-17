import yake
import warnings
import sys
import numpy as np
import wikipedia

# this notebook is a copy of "generator1.py" but it's used to build the quizes
# refer to "generator1.py" for documentation


sys.path.insert(0, r'C:\Users\gaber\question_generation')
warnings.filterwarnings("ignore")
from pipelines import pipeline

example1 =  """
        Linear regression attempts to model the relationship between two variables by fitting a 
        linear equation to observed data. One variable is considered to be an explanatory variable, 
        and the other is considered to be a dependent variable. For example, a modeler might want to 
        relate the weights of individuals to their heights using a linear regression model.
        """

txt_file = open("store.txt", 'r')
content = txt_file.read()
txt_file.close()
example1 = content


language = "en"
max_ngram_size = 2
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 8

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)

nlp = pipeline("question-generation")

class highlights:
    
    def __init__(self, name):
        self.name = name
        self.text = []
        self.combined_text = example1
        self.keywords = []
        self.study_concepts = {}
        self.quizes = []

    def collect_text(self, text):
        self.text.append(text)
        self.combine_text()
        self.get_keywords()
        self.generate_study_concepts()

    def combine_text(self):
      self.combined_text += "".join(self.text).replace('\n', '')
        
    def get_keywords(self):
      keywords = custom_kw_extractor.extract_keywords(self.combined_text)
      self.keywords += [wikipedia.search(i)[0] for i in np.array(keywords)[:, 0]]
      self.keywords =list(set(self.keywords))

    def generate_study_concepts(self):

      for keyword in self.keywords:
        
          try:
              summary = wikipedia.summary(keyword)
              
          except:
              summary = keyword+ ' refers to multiple concepts. Check https://en.wikipedia.org/wiki/'+ keyword


          self.study_concepts[keyword] = summary


    def show_concepts(self):
      for key, value, in zip(self.study_concepts.keys(), self.study_concepts.values()):
        print(key +":" +'\n' + value)
        print('---------------------')

    def generate_quizes(self):
      self.quizes = nlp(self.combined_text)

    def start_quiz(self):
      for ind, i in enumerate(self.quizes):
        print("Question "+ str(ind+1) +': ' + i['question'])
        print('Answer '+ str(ind+1) +': '+ i['answer'])
        print('-----------------------')

    





highlights_app = highlights('Session1')
highlights_app.generate_quizes()
highlights_app.start_quiz()




