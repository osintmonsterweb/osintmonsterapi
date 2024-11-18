import requests
 
API_URL = "https://api.osint.monster/api/search"
API_KEY = "yourapiosintmonster" 
 
def search_api(query):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": API_KEY
    }
    payload = {
        "query": query
    }
 
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
 
        if "error" in data:
            print(f"Erreur : {data['error']}")
        elif "results" in data and data["results"]:
            print("Résultats :")
            for idx, result in enumerate(data["results"], start=1):
                print(f"{idx}. {result['response']}")
        else:
            print("Aucun résultat trouvé pour cette requête.")
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite : {e}")
 
if __name__ == "__main__":
    query = input("Entrez votre requête : ").strip()
    if query:
        search_api(query)
    else:
        print("La requête ne peut pas être vide.")
