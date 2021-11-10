import plotly.express as px
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import csv 
import pandas as pd

df = pd.read_csv("../features/nci2.csv")
# print(df)
string = "x_"
name = []
for i in range(128):
    name.append(string+str(i))
# print(fields)
# print(name)
X = df[name]
# print(rows[:][0])

pca = PCA(n_components=3)
components = pca.fit_transform(X)

total_var = pca.explained_variance_ratio_.sum() * 100

Type = [""]*len(df["type"])

to_draw = [[] for _ in range(3)]
for idx, i in enumerate(range(len(df["type"]))):
    if df["type"][i] == 1:
        to_draw[0].append(components[idx])
    elif df["type"][i] == 2:
        to_draw[1].append(components[idx])
    else:
        to_draw[2].append(components[idx])


def rf(mix):
    xData, yData, zData = [], [], []
    for x,y,z in mix:
        xData.append(x)
        yData.append(y)
        zData.append(z)
    return [xData,yData,zData]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(
   *rf(to_draw[0]), s = 6
)
ax.scatter(
   *rf(to_draw[1]), s = 6
)
ax.scatter(
   *rf(to_draw[2]), s = 6
)
ax.legend(["class 1","class 2","class 3"], loc='best')
#fig.update_traces(marker=dict(size=3.5,
#                          line=dict(width=0.1,
#fig.update_traces(marker=dict(size=3.5,
#                          line=dict(width=0.1,
#                          color='Black')
#                             ),
#              selector=dict(mode='markers'))
#for angle in range(0, 360):
#    ax.view_init(0, angle)
#    print(angle)
#    plt.draw()
#    plt.pause(.001)
ax.view_init(-156,26)
fig.savefig('figure.pdf',bbox_inches='tight')
plt.show()

