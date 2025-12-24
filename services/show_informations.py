import matplotlib.pyplot as plt 

# ===============================
# Gráfico dinâmico
# ===============================

def graphic_flexible(students, title):
    names = [s["name"] for s in students] # Extraindo cada nome
    grades = [s["average"] for s in students] # Extraindo cada nota

    plt.bar(names, grades)
    plt.xticks(rotation=45, ha="right")
    plt.ylabel("Média")
    plt.title(title)
    plt.tight_layout()
    plt.show()

# ===============================
# Relatórios no terminal
# ===============================

def ranking_from_largest_to_smallest(ranking_max):
    print("\n🔝 Ranking do maior para o menor:")
    for aluno in ranking_max:
        print(f"{aluno['name']} → {aluno['average']}")

    graphic_flexible(ranking_max, "Ranking do Maior para o Menor")
              
def ranking_from_smallest_to_largest(ranking_min):
    print("\n🔻 Ranking do menor para o maior:")
    for aluno in ranking_min:
        print(f"{aluno['name']} → {aluno['average']}")

    graphic_flexible(ranking_min, "Ranking do Menor para o Maior")
    
def all_approved(approved):
    print("\n✅ Aprovados:")
    for aluno in approved:
        print(f"{aluno['name']} → {aluno['average']}")

    graphic_flexible(approved, "Alunos Aprovados")


def all_failed(reproved):
    print("\n❌ Reprovados:")
    for aluno in reproved:
        print(f"{aluno['name']} → {aluno['average']}")

    graphic_flexible(reproved, "Alunos Reprovados")