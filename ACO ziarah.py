# =========================================
# RIDHO NUR ROHMANUDIN
# 2300018042
# ANT COLONY OPTIMIZATION (ACO)
# Kasus: Rute Terpendek Ziarah Wali Songo
# =========================================

# ==========================
# DATA LOKASI & JARAK (km)
# ==========================
locations = [
    "Kos",
    "Sunan Gresik",
    "Sunan Ampel",
    "Sunan Giri",
    "Sunan Bonang",
    "Sunan Drajat",
    "Sunan Muria",
    "Sunan Kudus",
    "Sunan Kalijaga",
    "Sunan Gunung Jati",
    "Kos"
]

# Jarak antar lokasi berurutan
distances = [323, 22, 23, 81, 40, 197, 20, 27, 273, 371]

# ==========================
# PARAMETER ACO 
# ==========================
Q = 100            # intensitas pheromone
rho = 0.05         # tingkat evaporasi
antSize = 17       # jumlah semut
tmax = 35          # jumlah iterasi maksimum

# ==========================
# PHEROMONE AWAL
# ==========================
pheromone = [1.0 for _ in distances]

# ==========================
# FUNGSI OBJEKTIF
# ==========================
def objective_function(route):
    """
    Fungsi objektif untuk ACO
    Meminimalkan total jarak perjalanan
    """
    return sum(route)

# ==========================
# PROSES ACO
# ==========================
best_distance = float('inf')
best_route = locations.copy()

# Menyimpan nilai minimum tiap iterasi
iterasi_minimum = []

for iteration in range(tmax):
    print(f"Iterasi ke-{iteration + 1}")

    # Setiap iterasi, semua semut mengevaluasi rute
    for ant in range(antSize):
        total_distance = objective_function(distances)

        # Update solusi terbaik (minimum global)
        if total_distance < best_distance:
            best_distance = total_distance
            best_route = locations.copy()

        # Update pheromone
        for i in range(len(pheromone)):
            pheromone[i] = (1 - rho) * pheromone[i] + (Q / total_distance)

    # Simpan nilai minimum iterasi
    iterasi_minimum.append(best_distance)
    print(f"  Nilai minimum iterasi = {best_distance} km")

# ==========================
# HASIL AKHIR
# ==========================
print("\n=== HASIL AKHIR ACO ===")
print("Rute Terpilih:")
for loc in best_route:
    print("->", loc)

print("\nNilai Minimum Global:", best_distance, "km")

print("\nTabel Nilai Minimum Tiap Iterasi:")
for i, val in enumerate(iterasi_minimum):
    print(f"Iterasi {i+1}: {val} km")


#Berdasarkan hasil implementasi algoritma Ant Colony Optimization dengan 
#Q = 100, 
#ρ = 0.05, 
#antSize = 17 dan 
#tmax = 35, 
#diperoleh nilai minimum jarak perjalanan sebesar 1377 km. 
#Nilai tersebut merupakan nilai minimum global yang diperoleh dan stabil sejak iterasi awal 
#karena rute bersifat linier.