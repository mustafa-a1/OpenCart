import requests


def extract_transactions(api_url):
    response = requests.get(api_url, timeout=30)

    response.raise_for_status()

    transactions = response.json()

    return transactions


if __name__ == "__main__":
    api_url = "https://example.com/api/transactions"

    data = extract_transactions(api_url)

    print(data)
