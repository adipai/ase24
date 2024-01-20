import pandas as pd
import numpy as np

data = pd.read_csv("../../Data/soybean.csv")
classes = np.unique(list(data['class!']), return_counts=True)[0]
samples = np.unique(list(data['class!']), return_counts=True)[1]
print("Number of classes: ", len(classes))
for i in range(len(classes)):
    print("Class: ", classes[i])
    print("Samples: ", samples[i])