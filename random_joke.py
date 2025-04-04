import requests


def get_random_joke():
    """
    Fetches a random joke from the Official Joke API.

    Returns:
        str: A random joke in the format "Setup - Punchline".
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad HTTP responses
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch a joke: {e}"


if __name__ == "__main__":
    print(get_random_joke())
