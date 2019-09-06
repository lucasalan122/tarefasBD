
#concluir tarefas
import pymysql
 
# Abrimos uma conexão com o banco de dados:
conexao = pymysql.connect(db='tarefas', user='root', passwd='')
 
# Cria um cursor:
cursor = conexao.cursor()
 
# Executa o comando:
cursor.execute("UPDATE tarefa1 SET concluida = 'sim' WHERE nome_tarefa = 'Limpar casa'")

conexao.commit()

conexao.close()