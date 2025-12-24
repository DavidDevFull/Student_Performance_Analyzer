from InquirerPy import prompt

from services.calculations import average_grade

from services.rankings import (
    approved_and_no_approved,
    ranking_by_highest_grade,
    ranking_by_lowest_grade
)
from services.show_informations import (
    ranking_from_largest_to_smallest,
    ranking_from_smallest_to_largest,
    all_approved,
    all_failed
)

# ===============================
# Base de dados
# ===============================

students = [
    {"name": "Lucas Almeida", "grade": [7.5, 8.0, 5.0]},
    {"name": "Mariana Silva", "grade": [4.0, 6.3, 7.0]},
    {"name": "Pedro Santos", "grade": [8.2, 8.5, 4.0]},
    {"name": "Ana Oliveira", "grade": [6.8, 7.5, 5.0]},
    {"name": "Rafaela Costa", "grade": [9.1, 6.0, 7.0]},
    {"name": "Joao Mendes", "grade": [5.4, 7.5, 8.0]},
    {"name": "Carla Pereira", "grade": [3.8, 6.0, 7.3]},
    {"name": "Bruno Rocha", "grade": [8.9, 5.0, 7.0]},
    {"name": "Fernanda Dias", "grade": [7.3, 3.0, 5.7]},
    {"name": "Thiago Ribeiro", "grade": [2.5, 5.7, 9.3]},
]

# ===============================
# Processamento
# ===============================

result_average = average_grade(students)
ranking_max = ranking_by_highest_grade(result_average)
ranking_min = ranking_by_lowest_grade(result_average)
status = approved_and_no_approved(result_average)

# ===============================
# Dicionário para cada chamada de função
# ===============================

actions = {
    "📉 Ranking do maior para o menor": lambda: ranking_from_largest_to_smallest(ranking_max),
    "📈 Ranking do menor para o maior": lambda: ranking_from_smallest_to_largest(ranking_min),
    "✅ Aprovados": lambda: all_approved(status["approved"]),
    "❌ Reprovados": lambda: all_failed(status["reproved"]),
}

# ===============================
# Ação desejada pelo usuário
# ===============================

questions = [
    {
        "type": "list",
        "message": "📝 Demonstração e ordenação das notas",
        "choices": list(actions.keys()) + ["🚪 Sair"],
        "name": "final_choice"
    }
]

def run():
    while True:
        resposta = prompt(questions)["final_choice"]

        if resposta == "🚪 Sair":
            print("\n👋 Encerrando o programa...")
            break

        actions[resposta]()

if __name__ == "__main__":
    run()