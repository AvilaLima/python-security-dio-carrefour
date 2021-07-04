import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket: Criado com sucesso')

host = 'localhost'
porta = 5432

s.bind((host,port))

mensagem = 'Servidor: Olá Cliente'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('\nServidor enviando mensagem...')
        s.sendto(dados + mensagem.encode()), end)