import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import metrics

def find_optimal_k(data, max_k=10):
    wcss = []  # within-cluster sum of squares

    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(data.reshape(-1, 1))
        wcss.append(kmeans.inertia_)


    # Calculate the rate of decrease in WCSS
    rate_of_decrease = [wcss[i] - wcss[i+1] for i in range(len(wcss) - 1)]

    print("rate of decrease", rate_of_decrease)

    # Find the "elbow" point where the rate of decrease sharply changes
    optimal_k = rate_of_decrease.index(max(rate_of_decrease)) + 2

    # Plot the elbow curve
    plt.plot(range(1, max_k + 1), wcss)
    plt.plot(range(1, max_k), rate_of_decrease)
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.yscale('log')
    plt.show()

    return optimal_k

def cluster_data(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(data.reshape(-1, 1))
    return kmeans.labels_

data_file = "ESP_Output_01.xlsx"

data = pd.read_excel(data_file)['datapoints']
np_data = data.to_numpy()

# Example usage:
# Generate some sample one-dimensional data
# np.random.seed(0)
# data = np.random.randn(100)

# Find the optimal number of clusters using the elbow method
# k = find_optimal_k(data)

# print(f"Optimal k calculated: {k}")

# Based on the elbow method, choose a suitable number of clusters
optimal_k = 3

# Cluster the data using the optimal number of clusters
labels = cluster_data(np_data, optimal_k)

labelled_data = zip(data, labels)
zeroes = np.zeros(len(data))

color_dict = {
    0: "blue",
    1: "green",
    2: "orange"
}

plt.figure()
for datapoint, cluster_num in labelled_data:
    plt.scatter(datapoint/1000,0, c=color_dict[cluster_num], marker='|',s=700)

plt.xlim(-3,30)
plt.title("Interrupt Timings (Clustered)", fontsize=18)
plt.xlabel("Time (ms)",fontsize=12, x=1.0)
plt.ylabel("Interrupt triggers",fontsize=14)
# plt.legend(["Interrupt Triggered","B", "C"], loc="best")
plt.yticks([])
plt.grid()
plt.show()