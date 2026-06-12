import requests

def fetch_difficulty_data():
    url = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"取得失敗: {e}")
        return None