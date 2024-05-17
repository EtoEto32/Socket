# サーバー側
import socket  # ソケット通信に関するライブラリ
import threading  # スレッドを使うためのライブラリ

from constCS import HOST, PORT  # なんか、警告でたのでこの書き方にしてみた

# グローバル変数でクライアントの接続を管理
clients = []  # クライアントの接続を管理するリスト


def handle_client(conn, addr):  # クライアントの接続を管理する関数
    print(f"接続：{addr}")  # 接続したクライアントのアドレスを表示
    while True:  # クライアントからのメッセージを受信し続ける
        data = conn.recv(1024)
        if not data:  # データがない場合はbreak
            break
        print(data.decode())  # 受信したデータを表示


def send_to_all_clients(message):  # 全クライアントにメッセージを送信する関数
    for client in clients:  # クライアントの数だけ繰り返す
        client.send(message.encode())  # クライアントにメッセージを送信


s = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # ソケットを作成ここも何故かエラーがでたので書き方をサンプルと変えた
s.bind((HOST, PORT))  # サーバーのホスト名とポート番号をバインドする
s.listen(2)  # 2つのクライアント接続を待ち受ける
try:
    # 2つのクライアントが接続するまで待つ
    while len(clients) < 2:
        conn, addr = s.accept()
        clients.append(conn)
        client_thread = threading.Thread(
            target=handle_client, args=(conn, addr)
        )  # クライアントの接続を管理するスレッドを作成
        client_thread.start()  # スレッドを開始

    # すべてのクライアントが接続したらメッセージを送信
    message = input("サーバーからのメッセージ: ")
    send_to_all_clients(message)
finally:  # 通信が終わったらソケットを閉じる、じゃないと最初から閉じてしまう
    for client in clients:
        client.close()  # クライアントのソケットを閉じる
    s.close()  # ソケットを閉じる
