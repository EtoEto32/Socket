import socket

from constCS import HOST, PORT  # 必要な定数のみをインポート

# whileと標準入力使えばチャット機能を設けられるのでは、、、？
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"接続されました：{HOST,PORT}が接続先です。")
while True:
    msg = input("Client:")  # 送信メッセージを入力
    s.send(msg.encode())  # メッセージを送信
    data = s.recv(1024)  # 相手からメッセージを受け取る
    print("受信", repr(data.decode()))  # 受信メッセージを表示
s.close()  # 接続を閉じる
