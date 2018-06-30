# subprocessでコマンドを実行する
import os
import subprocess

# 非推奨
# os.system('ls')

# subprocess.run(['ls', '-al'])

# 非推奨
# subprocess.run('ls -la | grep test', shell=True)

# grepを行いたい場合
p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(['grep', 'test'], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()
output = p2.communicate()[0]
print(output)