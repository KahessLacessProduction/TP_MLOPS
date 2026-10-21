import requests

BASE_URL = "http://localhost:8000"

# === Test 1 : GET /predict ===
print("=" * 50)
print("Test GET /predict")
print("=" * 50)
response = requests.get(f"{BASE_URL}/predict")
print(f"Status : {response.status_code}")
print(f"Réponse : {response.json()}")

# === Test 2 : POST /predict avec des données ===
print("\n" + "=" * 50)
print("Test POST /predict")
print("=" * 50)

# Maison de 100m², 3 chambres, avec jardin
data = {"size": 100, "nb_rooms": 3, "garden": 1}
response = requests.post(f"{BASE_URL}/predict", json=data)
print(f"Entrée : {data}")
print(f"Status : {response.status_code}")
print(f"Réponse : {response.json()}")

# === Test 3 : POST /predict avec d'autres données ===
print("\n" + "=" * 50)
print("Test POST /predict (2ème exemple)")
print("=" * 50)

data2 = {"size": 75, "nb_rooms": 2, "garden": 0}
response = requests.post(f"{BASE_URL}/predict", json=data2)
print(f"Entrée : {data2}")
print(f"Status : {response.status_code}")
print(f"Réponse : {response.json()}")

print("\n✅ Tous les tests sont passés !")
