import os

def _load_env(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')):
    if not os.path.exists(path):
        return
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip())

_load_env()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
myAPIkey = os.environ.get('FRED_API_KEY')
if not myAPIkey:
    raise RuntimeError('FRED_API_KEY가 없습니다. .env.example을 복사해 .env를 만들고 키를 넣어주세요.')
response_method='json'
