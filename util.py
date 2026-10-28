import gzip
import os
import shutil

def make_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def write_gz(path):
    """path 옆에 path.gz 를 만든다 (대시보드가 작은 압축본을 받아 브라우저에서 풂). 임시 파일에 쓴 뒤 교체."""
    tmp = f'{path}.gz.tmp'
    with open(path, 'rb') as src, open(tmp, 'wb') as raw:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw, compresslevel=9, mtime=0) as dst:
            shutil.copyfileobj(src, dst)
    os.replace(tmp, f'{path}.gz')
    return os.path.getsize(f'{path}.gz')
