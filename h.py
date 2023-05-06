import numpy as np

def topsis(data, weights, criteria_impact):
    normalized_data = np.zeros(data.shape)
    for i in range(data.shape[1]):
        column = data[:, i]
        column_min = np.min(column)
        column_max = np.max(column)
        normalized_data[:, i] = (column - column_min) / (column_max - column_min)
    
    weighted_normalized_data = normalized_data * weights
    
    ideal_positive = np.amax(weighted_normalized_data, axis=0)
    ideal_negative = np.amin(weighted_normalized_data, axis=0)
    
    distances = np.zeros((data.shape[0], 2))
    for i in range(data.shape[0]):
        V = weighted_normalized_data[i, :]
        D_plus = np.sqrt(np.sum((V - ideal_positive)**2))
        D_minus = np.sqrt(np.sum((V - ideal_negative)**2))
        distances[i, 0] = D_minus / (D_plus + D_minus)
        distances[i, 1] = i
    
    distances = distances[np.argsort(distances[:, 0])][::-1]
    
    results = np.zeros((data.shape[0], data.shape[1] + 1))
    results[:, :-1] = data
    results[:, -1] = distances[:, 1]
    
    return results

# Mahasiswa Data
data = np.array([[3,3,3,2],
		[3,3,2,2],
		[4,4,1,1],
		[1,4,2,1]])

# Bobot Data
weights = np.array([3, 4, 5, 4])

# Kriteria Impact
criteria_impact = np.array([1, 1, -1, 1])

# Aplikasikan Metode TOPSIS
results = topsis(data, weights, criteria_impact)

# Tampilkan Hasil
print("Nama\tC1\tC2\tC3\tC4\tNilai")
for i in range(data.shape[0]):
    print("%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.6f" % (i + 1, data[i, 0], data[i, 1], data[i, 2], data[i, 3], results[i, -1]))
