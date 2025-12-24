# ===============================
# Ranking do maior para o menor
# ===============================

def ranking_by_highest_grade(students):
    copy_students = students.copy()
    ordered = []

    while copy_students:
        best = max(copy_students, key=lambda s: s["average"])
        ordered.append(best)
        copy_students.remove(best)

    return ordered

# ===============================
# Ranking do menor para o maior
# ===============================

def ranking_by_lowest_grade(students):
    copy_students = students.copy()
    ordered = []

    while copy_students:
        worst = min(copy_students, key=lambda s: s["average"])
        ordered.append(worst)
        copy_students.remove(worst)

    return ordered

# ===============================
# Aprovados e Reprovados
# ===============================

def approved_and_no_approved(students):
    return {
        "approved": [s for s in students if s["average"] >= 6],
        "reproved": [s for s in students if s["average"] < 6]
    }