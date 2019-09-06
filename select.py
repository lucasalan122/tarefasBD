#tarefas concluidas
import pymysql

conexao = pymysql.connect(db='garagem', user='root', passwd='')


cursor = conexao.cursor()


cursor.execute("SELECT nome_tarefa FROM tarefa1 WHERE concluida = 'sim'")


resultado = cursor.fetchall()

# Mostra o resultado:
print('tarefas concluidas: ')

for linha in resultado :
    print(linha)

# Finaliza a conexão
conexao.close()