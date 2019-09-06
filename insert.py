#Inserir tarefas
import pymysql


conexao = pymysql.connect(db='tarefas', user='root', passwd='')

cursor = conexao.cursor()


cursor.execute("INSERT INTO tarefa1 (concluida, nome_tarefa) VALUES ('nao', 'Limpar casa')")


conexao.commit()


conexao.close()