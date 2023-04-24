import pandas as pd
import numpy as np
data_full = pd.read_csv("FinalData.csv")

#plot with Masking
import matplotlib.pyplot as plt
#categorize ages

new_feature = (data_full['age'])
#declare variable age
age = 0


def age_category(new_feature):
    if age <19: return 'minor'
    if age <55: return 'adult'
    if age <99: return 'senior'
    return 'none'

vector_age_category = np.vectorize(age_category)
data_full['age class'] = vector_age_category(data_full['age'])
data_full['age class'].value_counts()

#the following is an array of true/false
DOT_true = data_full["HELM_USE"] == 1
#DOT_false = data_full["HELM_USE"] == 0


#only keep the true instances
data_adults = data_full[DOT_true]
data_children = data_full[DOT_true]
data_senior = data_full[DOT_true]