import plotly.express as px
from sklearn.decomposition import PCA
import csv 
import pandas as pd

df = pd.read_csv("../features/nci1.csv")
print(df)
string = "x_"
name = []
for i in range(128):
    name.append(string+str(i))
# print(fields)
print(name)
X = df[name]
# print(rows[:][0])

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

fig = px.scatter_3d(
    components, x=0, y=1, z=2, color=df["type"],
    title=f'Total Explained Variance: {total_var:.2f}%',
    labels={'0': 'PC 1', '1': 'PC 2', '2': 'PC 3'}
)
fig.show()