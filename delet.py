#deletar tarefas
import pymysql


conexao = pymysql.connect(db='tarefas', user='root', passwd='')


cursor = conexao.cursor()

cursor.execute("DELETE FROM tarefa1 WHERE name_tarefa = 'Limpar casa'")


conexao.commit()


conexao.close()