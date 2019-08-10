import pandas as pd

# This function takes a strain_name and returns a dataset of similar strains by the similarity matrix
# specified. The index of the dataframe are all the other strains excluding the strain of interest
def similar_strain(strain, main_dataset, by):
    most_similar_names = by.loc[strain, by.columns != strain].sort_values(ascending = False)
    most_similar_info = main_dataset.loc[most_similar_names.index]
    final = pd.concat([most_similar_names,most_similar_info], axis = 1)
    return final.rename_axis('strains').reset_index()

# 
def find_me_strains(general_liked = [], medical_liked = [], flavors_liked = [], everything = []):
    total_score = len(general_liked) + len(medical_liked) + len(flavors_liked)
    dataset = pd.DataFrame(everything[flavors_liked + general_liked + medical_liked].sum(axis = 1).sort_values(ascending=False)/total_score)
    dataset.columns = ['Similarity_Score']
    return dataset