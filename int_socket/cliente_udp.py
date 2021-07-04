import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket Criado com Sucesso!')

host = 'localhost'
porta = 5433
mensagem = '\nOlá servidor'

try:
    print('Cliente:' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print('\nCliente: Fechando a conexão')
    s.close()

