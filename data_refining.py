import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import k_means

df  = pd.read_csv('data.csv')
X = df['speed']/df['rpm']
X=X.values.reshape(-1,1)
cluster = k_means(X,n_clusters = 5)

l=[]
for i in range(0,len(cluster[0])):
	l.append([i,cluster[0][i]])

l = sorted(l, key=lambda x: x[1])
# print(l)

mymap = np.zeros(len(cluster[0]))
for i in range(0,len(cluster[0])):
	mymap[l[i][0]] = i;
# print(mymap)

df['label'] = cluster[1]
for i in range(1,len(cluster[1])-30):
	if(cluster[1][i] == cluster[1][i-1]):
		continue;
	else:
		l=df['label'].loc[i:i+30].value_counts().index.tolist()
		cluster[1][i:i+30] = l[0]
		i=i+29;

df['label'] = mymap[cluster[1]]+1
df.to_csv('out.csv')
fig,ax = plt.subplots(1,1)
ax.scatter(np.arange(len(df)),df['label'])
plt.show()