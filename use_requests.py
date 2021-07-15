import requests

url = 'https://news.detik.com/'
try:
    respon = requests.get(url)
    print(f'Success !! Respon = {respon.status_code}')
    print(f'Content {respon.text}')
except Exception as e:
    print(f'Ada error {e}')

print('Akhir Program !!')
