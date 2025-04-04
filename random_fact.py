import requests

def get_random_fact():
    """
    Fetches a random interesting fact from the Useless Facts API.

    Returns:
        str: A random fact.
    """
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        fact_data = response.json()
        return fact_data['text']
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch a fact: {e}"

if __name__ == "__main__":
    print(get_random_fact())