# ファイル操作

import os
import pathlib
import glob
import shutil

# test.txtが同じディレクトリに存在するか
# print(os.path.exists('test.txt'))

# test.txtがファイルかどうか
# print(os.path.isfile('test.txt'))

# Designがディレクトリかどうか
# print(os.path.isdir('Design'))

# リネーム
# os.rename('test.txt', 'renamed.txt')

# symlink作成
# os.symlink('renamed.txt', 'symlink.txt')

# ディレクトリ作成
# os.mkdir('test_dir')

# ディレクトリ削除
# os.rmdir('test_dir')

# ファイル作成
# pathlib.Path('test.txt').touch()

# ファイル削除
# os.remove('test.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
# test_dirの中のディレクトリを表示
# print(os.listdir('test_dir'))
# pathlib.Path('test_dir/test_dir2/empty.txt').touch()

# test_dir/test_dir2/empty.txtのコピー
# shutil.copy('test_dir/test_dir2/empty.txt',
#             'test_dir/test_dir2/empty2.txt')
# test_dir/test_dir2/配下の確認
# print(glob.glob('test_dir/test_dir2/*'))

# test_dirを削除
# shutil.rmtree('test_dir')

# 現在のディレクトリを表示
print(os.getcwd())