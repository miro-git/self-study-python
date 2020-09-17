import time
import os
import pandas

if os.path.exists("files/temps_today.csv"):
    data = pandas.read_csv("files/temps_today.csv")
    print(type(data))
    print(data.mean())
else:
    print("File does not exist.")
      