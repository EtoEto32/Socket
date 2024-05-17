import socket

from constCS import HOST, PORT  # 必要な定数のみをインポート

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()
print(f"接続されました：{addr}が接続先です。")
while True:
    data = conn.recv(1024)
    if not data:
        break
    print("受信", repr(data.decode()))
    msg = input("Server:")
    conn.send(msg.encode())
conn.close()
#受信メッセージを表示させてから送信メッセージを送れるように
#順番を間違えない
