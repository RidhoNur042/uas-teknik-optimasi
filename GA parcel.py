import random

# =========================================
# GENETIC ALGORITHM - PARCEL LEBARAN
# =========================================

class GeneticAlgorithmParcel:
    def __init__(self, params, items, budget):
        self.pop_size = params['pop_size']
        self.cr = params['crossover_rate']
        self.mr = params['mutation_rate']
        self.max_gen = params['max_gen']

        self.items = items
        self.prices = [i[1] for i in items]
        self.dimension = len(items)
        self.budget = budget

        self.history_min = []  # menyimpan nilai minimum tiap iterasi

    # =========================
    # OBJECTIVE FUNCTION
    # =========================
    def objective_function(self, chromosome):
        total_price = sum(
            chromosome[i] * self.prices[i]
            for i in range(self.dimension)
        )
        if total_price <= self.budget:
            return self.budget - total_price
        else:
            return 10**6  # penalti jika melebihi budget

    # =========================
    # FITNESS FUNCTION
    # =========================
    def fitness_function(self, obj_value):
        return 1 / (1 + obj_value)

    # =========================
    # ROULETTE WHEEL SELECTION
    # =========================
    def roulette_selection(self, population, fitness_values):
        total_fitness = sum(fitness_values)
        r = random.uniform(0, total_fitness)
        cumulative = 0

        for i in range(len(population)):
            cumulative += fitness_values[i]
            if cumulative >= r:
                return population[i]
        return population[-1]

    # =========================
    # MAIN GA PROCESS
    # =========================
    def run(self):
        # Populasi awal
        population = [
            [random.randint(0, 1) for _ in range(self.dimension)]
            for _ in range(self.pop_size)
        ]

        for gen in range(self.max_gen):
            obj_values = [self.objective_function(c) for c in population]
            fitness_values = [self.fitness_function(o) for o in obj_values]

            min_value = min(obj_values)
            self.history_min.append(min_value)

            # Seleksi
            selected = [
                self.roulette_selection(population, fitness_values)
                for _ in range(self.pop_size)
            ]

            # Crossover
            offspring = []
            for i in range(0, self.pop_size - 1, 2):
                p1, p2 = selected[i], selected[i + 1]
                if random.random() < self.cr:
                    cut = random.randint(1, self.dimension - 1)
                    offspring.append(p1[:cut] + p2[cut:])
                    offspring.append(p2[:cut] + p1[cut:])
                else:
                    offspring.extend([p1, p2])

            # Mutation
            for child in offspring:
                for j in range(self.dimension):
                    if random.random() < self.mr:
                        child[j] = 1 - child[j]

            # Survival selection
            combined = population + offspring
            scored = []
            for c in combined:
                o = self.objective_function(c)
                scored.append((o, c))

            scored.sort(key=lambda x: x[0])  # minimisasi
            population = [scored[i][1] for i in range(self.pop_size)]

        # =========================
        # OUTPUT 
        # =========================
        print("\nTABEL NILAI MINIMUM TIAP ITERASI")
        print("Iterasi\tNilai Minimum")
        for i, val in enumerate(self.history_min):
            print(f"{i+1}\t\t{val}")

        global_min = min(self.history_min)
        print("\nNILAI MINIMUM GLOBAL / AKHIR :", global_min)

        best = population[0]
        total_price = sum(best[i] * self.prices[i] for i in range(self.dimension))

        print("\nPAKET PARCEL TERBAIK:")
        for i in range(self.dimension):
            if best[i] == 1:
                print("-", self.items[i][0], "Rp", self.items[i][1])

        print("Total Harga :", total_price)
        print("Sisa Budget :", self.budget - total_price)


# =========================================
# PARAMETER 
# =========================================
parameters = {
    'pop_size': 25,
    'crossover_rate': 0.23,
    'mutation_rate': 0.1,
    'max_gen': 55
}

budget = 125000

# =========================================
# DAFTAR PRODUK PARCEL 
# =========================================
products = [
    ("Bear Brand Steril Collagen 189ml", 9900),
    ("Vidoran Xmart 5+ Cokelat 700g", 49400),
    ("Vidoran Xmart 1+ Madu 125g", 10900),
    ("Indomie Nyemek Rendang (2 pcs)", 5900),
    ("Richeese Fire Wings Rich Burger (2 pcs)", 10000),
    ("Herbakof Strong Mint 100ml", 20000),
    ("So Fresh M. Angin Citrus (2x10ml)", 12500),
    ("So Soft 700ml", 16500),
    ("Bagus Karbol Wangi Pine 575ml", 10900),
    ("Bebek Pembersih Kloset 625ml", 19900),
    ("Ploosa Blue Mountain", 14900),
    ("Spongebob Buddies 3D Figure", 29900),
    ("Apolo Snap Toys AST", 29900),
    ("Barbie Jet Tag Snowflakez AST", 49900),
    ("Hot Wheels Silver Pantones / FF 25th", 59900)
]

ga = GeneticAlgorithmParcel(parameters, products, budget)
ga.run()
