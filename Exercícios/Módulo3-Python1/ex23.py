#Neste script você irá ler o nome de 4 alunos e suas notas e determinar qual aluno possui a maior nota.

list_students = list(map(str,input("Entre com os nomes dos estudantes separados por espaço: ").strip().split()))
list_grades = list(map(int,input("Entre com as notas dos estudantes na ordem dos nomes, separadas por espaço: ").strip().split()))

for i in range(len(list_grades)):
    if list_grades[i] == max(list_grades):
        print(f'A maior nota tirada foi {list_grades[i]} pela(o) aluna(o) {list_students[i]}')