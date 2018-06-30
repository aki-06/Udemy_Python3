# tarfile圧縮展開

import tarfile
import os
import pathlib
import shutil

# shutil.rmtree('test_dir')
# os.mkdir('test_dir')
# pathlib.Path('test_dir/test.txt').touch()
# os.mkdir('test_dir/sub_dir')
# pathlib.Path('test_dir/sub_dir/test.txt').touch()
#
# with open('test_dir/test.txt', 'w') as f:
#     f.write('test')
#
# with open('test_dir/sub_dir/test.txt', 'w') as f:
#     f.write('sub')

# tarの圧縮
# with tarfile.open('test.tar.gz', 'w:gz') as tr:
#     tr.add('test_dir')

# tarの展開
# with tarfile.open('test.tar.gz', 'r:gz') as tr:
#     tr.extractall(path='test_tar')

# 展開せずに中身を見る
with tarfile.open('test.tar.gz', 'r:gz') as tr:
    with tr.extractfile('test_dir/sub_dir/test.txt') as f:
        print(f.read())