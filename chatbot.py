bot_talk = {'����ɂ���':'�n�C�I�R���j�`���B�i�C�J�S���E�f�X�J�H','��ЊT�v���m�F�������ł�':'�R�`���f�C�J�K�f�V���E�J�Hhttp://isc21.co.jp/info/gaiyou.html','���肪�Ƃ��������܂�':'�}�^�m�S�����E�I�}�`�V�e�I���}�X�B'}
while True:
    command = input('bot> ')
    responce = ""
    # �����̃L�[���܂܂�Ă��邩�`�F�b�N����
    for key in bot_talk:
        if key in command:
            responce = bot_talk[key]
            break
    # �����ɓo�^���Ȃ���΋󕶎��ŕԂ��̂Ŕ��肳���
    if not responce:
        responce = '�X�~�}�Z���I���J���}�Z���B'
    print(responce)
    if '����Ȃ�' in command:
        break