#!/usr/bin/python
import psycopg2
# コネクション作成_xxxxxは適宜変換
conn = psycopg2.connect("dbname=xxxxx host=xxxxx user=xxxxx password=xxxxx")
# カーソル作成
cur = conn.cursor()
# SQLコマンド実行_xxxxxは適宜変換(プレースホルダー使用。エスケープも勝手にされる)
cur.execute("INSERT INTO xxxxx (xxxxx, xxxxx) VALUES (%s, %s)", (xxxxx, "xxxxx"))
# SQL結果を受け取る_xxxxxは適宜変換
cur.execute("SELECT * FROM xxxxx;")
cur.fetchone()
# コミット
conn.commit()
# クローズ
cur.close()
conn.close()
print ("QueryOK\n")