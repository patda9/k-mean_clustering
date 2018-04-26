import plotly as py
import plotly.graph_objs as go

from preprocessing import *
from data_mapping import *

def euclidian_distance(p, q, k):
    eu_d = np.zeros((k, len(p))) # q is centroid ex. (x, y)
    for i in range(0, len(q)):
        for j in range(0, len(p)):
            eu_d[i][j] = np.linalg.norm(q[i] - p[j])
    return eu_d.T

def initialize_centroids(cent, p):
    rand_i = []
    for i in range(0, len(cent)):
        rand_int = np.random.randint(0, len(p))
        while(rand_int in rand_i):
            rand_int = np.random.randint(0, len(p))
        cent[i] = p[rand_int]
        rand_i.append(rand_int)

def update_centroid(p, cents, eu_d):
    clusters = [[] for x in range(0, len(cents))]
    prev_cents = np.array(cents)

    for i in range(0, len(eu_d)):
        closest = np.argmin(eu_d[i])
        cents[closest] = (cents[closest] + p[i]) / 2
        clusters[closest].append(p[i])

    cents_diff = np.square(np.subtract(cents, prev_cents))
    sum_cents_diff = np.sum(cents_diff)

    return [np.array(clusters), cents_diff, sum_cents_diff]

np.set_printoptions(suppress = True)

E = np.inf
k = 4

## Data mining course dataset ##
# data_set = data_map(preprocess('./dresses_attribute_sales.csv'))
## Data mining course dataset ##

test_data_set = np.array([[185, 72], [170, 56], [168, 60], [179, 68], [182, 72], [188, 77]], dtype = np.float32)
data_set = np.random.randint(200, size = (3200, 2))

centroids = np.zeros((k, len(data_set[0]))) # random pick centroids k = 2

initialize_centroids(centroids, data_set)

i = 0
while(E > 0.0000001):
    print('Itteration:', i)
    euclidian_distances = euclidian_distance(data_set, centroids, k)
    updates = update_centroid(data_set, centroids, euclidian_distances)
    clusters = updates[0]
    E = updates[2]
    print('Updated Centroids:')
    print(centroids)
    print('e_sqr:', updates[1])
    print('E_sqr:' , E)
    print('At index', i, 'Clusters:')
    print(clusters)
    i += 1

for i in range(0, len(clusters)):
    clusters[i] = np.transpose(clusters[i])
    print(clusters[i])
centroids = centroids.T

trace1 = go.Scatter(
    x = clusters[0][0],
    y = clusters[0][1],
    name = 'Cluster1',
    mode = 'markers',
    marker = dict(
        size = 8,
        color = '#33ffdd')
)

trace2 = go.Scatter(
    x = clusters[1][0],
    y = clusters[1][1],
    name = 'Cluster2',
    mode = 'markers',
    marker = dict(
        size = 8,
        color = '#32ff23')
)

trace3 = go.Scatter(
    x = clusters[2][0],
    y = clusters[2][1],
    name = 'Cluster3',
    mode = 'markers',
    marker = dict(
        size = 8,
        color = '#ffdd11')
)

trace4 = go.Scatter(
    x = clusters[3][0],
    y = clusters[3][1],
    name = 'Cluster4',
    mode = 'markers',
    marker = dict(
        size = 8,
        color = '#ff2222')
)

trace5 = go.Scatter(
    x = centroids[0],
    y = centroids[1],
    name = 'Centroid',
    mode = 'markers',
    marker = dict(
    size = 16,
    color = '#000000',
    )
)

layout = go.Layout(
    title= '4-Mean Clustering',
    hovermode= 'closest'
)

data = [trace1, trace2, trace3, trace4, trace5]
fig= go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename = 'example.html')