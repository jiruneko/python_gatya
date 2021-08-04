import random


hand_dict = {
    '1': 'グー',
    '2': 'チョキ',
    '3': 'パー'
}

print('手を入力してください')
print('1:グー 2:チョキ 3:パー')

player_input = input()
if player_input not in hand_dict:
    print('入力が正しくありません。')
    exit()

player = hand_dict[player_input]
print('入力した手: ' + player)

com_input = random.choice(['1', '2', '3'])
com = hand_dict[com_input]
print('コンピューターの手: ' + com)

print(player + 'vs' + com)


if player == com:
    result = 'あいこ'
elif player == 'グー':
    if com == 'チョキ':
        result = 'あなたの勝ち'
    else:
        result = 'コンピューターの勝ち'
elif player == 'チョキ':
    if com == 'パー':
        result = 'あなたの勝ち'
    else:
        result = 'コンピューターの勝ち'
else:
    if com == 'グー':
        result = 'あなたの勝ち'
    else:
        result = 'コンピューターの勝ち'

print(result)