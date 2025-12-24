# ===============================
# Cálculo da média
# ===============================

def average_grade(data):
    result = []
    for aluno in data:
        media = sum(aluno["grade"]) / len(aluno["grade"])
        result.append({
            "name": aluno["name"],
            "average": round(media, 1)
        })
    return result