#!/usr/bin/python
import psycopg2
# �R�l�N�V�����쐬_xxxxx�͓K�X�ϊ�
conn = psycopg2.connect("dbname=xxxxx host=xxxxx user=xxxxx password=xxxxx")
# �J�[�\���쐬
cur = conn.cursor()
# SQL�R�}���h���s_xxxxx�͓K�X�ϊ�(�v���[�X�z���_�[�g�p�B�G�X�P�[�v������ɂ����)
cur.execute("INSERT INTO xxxxx (xxxxx, xxxxx) VALUES (%s, %s)", (xxxxx, "xxxxx"))
# SQL���ʂ��󂯎��_xxxxx�͓K�X�ϊ�
cur.execute("SELECT * FROM xxxxx;")
cur.fetchone()
# �R�~�b�g
conn.commit()
# �N���[�Y
cur.close()
conn.close()
print ("QueryOK\n")