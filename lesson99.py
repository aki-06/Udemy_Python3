# zipfileの圧縮展開

import zipfile
import glob

# 圧縮
with zipfile.ZipFile('test.zip', 'w') as z:
    # z.write('test_dir')
    # z.write('test_dir/test.txt')
    for f in glob.glob('test_dir/**', recursive=True):
        z.write(f)

# 展開
with zipfile.ZipFile('test.zip', 'r') as z:
    z.extractall('zzz2')