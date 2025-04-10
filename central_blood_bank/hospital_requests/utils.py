CITY_DISTANCES = {
    ("Mansoura", "Cairo"): 120,
    ("Mansoura", "Tanta"): 60,
    ("Mansoura", "Zagazig"): 90,
    ("Mansoura", "Benha"): 110,
    ("Cairo", "Alexandria"): 220,
    ("Tanta", "Cairo"): 100,
    ("Alexandria", "Tanta"): 180,
    ("Zagazig", "Cairo"): 60,
    ("Benha", "Cairo"): 50,
    ("Damietta", "Mansoura"): 70,
    ("Ismailia", "Zagazig"): 80,
    ("Suez", "Cairo"): 140,
    ("Port Said", "Ismailia"): 100,
}

def get_city_distance(city1, city2):
    if city1 == city2:
        return 0
    return CITY_DISTANCES.get((city1, city2)) or CITY_DISTANCES.get((city2, city1)) or float("inf")
