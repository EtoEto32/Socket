# client1.py
import socket

from constCS import HOST, PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ソケットオブジェクトの作成
s.connect((HOST, PORT))  # サーバーに接続
while True:  # サーバーからのメッセージを受け取る
    data = s.recv(1024)  # サーバーからメッセージを受け取る
    if not data:  # メッセージが空の場合、ループを抜ける
        break
    print(
        "サーバー側から受信（クライアント1):", data.decode()
    )  # 受け取ったメッセージを表示
s.close()  # ソケットを閉じる
