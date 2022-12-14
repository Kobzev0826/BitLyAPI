import requests


def get_short_link(token, url):
  headers = {"Authorization": f"Bearer {token}"}
  payload = {"long_url": url}
  response = requests.post("https://api-ssl.bitly.com/v4/shorten",
                           headers=headers,
                           json=payload)
  response.raise_for_status()
  return response.json()['link']


def count_clicks(token, url):
  headers = {"Authorization": f"Bearer {token}"}
  payload = {"unit": "day", "units": -1}
  response = requests.get(
    f"https://api-ssl.bitly.com/v4/bitlinks/{url}/clicks/summary",
    headers=headers,
    params=payload)
  response.raise_for_status()
  return response.json()['total_clicks']


def is_bitlink(token, url):
  headers = {"Authorization": f"Bearer {token}"}
  response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{url}",
                          headers=headers)
  return response.ok
