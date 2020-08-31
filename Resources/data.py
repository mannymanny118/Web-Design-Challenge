# imports dependacies
import pandas as pd 
import os 
# sets the directory to current directory 
os.chdir(os.path.dirname(os.path.abspath(__file__))) # sets current directory
# imports cities data into pandas dataframe
cities_df = pd.read_csv("Resources/cities.csv")
# converts dataframe to html formate
html = cities_df.to_html()
# writes data into html file
text_file = open("data.html", "w")
text_file.write(html)
text_file.close()
