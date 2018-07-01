# roboterアプリ

import csv
import os

while True:
    # 名前の受け取り
    name = input('こんにちは！私の名前はRobokoです。あなたの名前は何ですか？')
    break

# 好きなレストランの受け取り、ranking.csvに出力
is_exists_ranking_csv = os.path.exists('ranking.csv')
if is_exists_ranking_csv == False:
    like_restaurant = input('{}さん。どこのレストランが好きですか？'.format(name))
    with open('ranking.csv', 'w') as csv_file:
        field_names = ['Name', 'Count']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        writer.writerow({'Name': like_restaurant.title(), 'Count': 1})
else:
    with open('ranking.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            # TODO: row['Count']が一番多いものをおすすめするように実装
            input('私のおすすめのレストランは{}です。このレストランは好きですか？[Yes/No]'.format(row['Name']))
        like_restaurant = input('{}さん。どこのレストランが好きですか？'.format(name))
    with open('ranking.csv', 'r+') as csv_file:
        # TODO: おすすめのレストランがcsvにあれば名前は追記しないでCountに+1する
        writer = csv.writer(csv_file, lineterminator='\n')
        print(writer)
        writer.writerow([like_restaurant, 1])

print('{}さん。ありがとうございました。良い一日を！さようなら。'.format(name))



