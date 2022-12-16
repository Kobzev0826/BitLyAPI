import requests, os, sys, argparse
import bit_ly
from urllib.parse import urlparse
from dotenv import load_dotenv


if __name__ == '__main__':

  parser = argparse.ArgumentParser(description="work with bit.ly API")
  parser.add_argument('link',help='link for check')
  app_args = parser.parse_args()

  try:
    load_dotenv()
    token = os.environ["BITLY_TOKEN"]
  except KeyError as e:
    print(f"Error: {e} \n no token in system environment")
    sys.exit()

  link_for_check = app_args.link#input("Enter your link: ")

  try:
    parsed_link = urlparse(link_for_check)
    link = f'{parsed_link.netloc}{parsed_link.path}'
    if bit_ly.is_bitlink(token, link):
      print(f'переходов по ссылке {bit_ly.count_clicks(token, link)}')
    else:
      print(f"Битлинк {bit_ly.get_short_link(token, link_for_check)}")

  except requests.exceptions.HTTPError as e:
    print(f"Error:{e} \n your link <{link_for_check}> is incorrect \n")
    sys.exit()
