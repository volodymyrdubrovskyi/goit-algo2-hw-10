# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects  # Множина предметів, які викладач може викладати
        self.assigned_subjects = set()  # Множина предметів, які призначено викладачу

def create_schedule(subjects, teachers):
    # Копіюємо множину предметів, щоб відстежувати непризначені предмети
    subjects_to_cover = subjects.copy()
    # Список викладачів, які будуть в розкладі
    schedule = []
    while subjects_to_cover:
        # Знайдемо викладача, який покриває найбільшу кількість непризначених предметів
        best_teacher = None
        subjects_covered_by_best = set()
        for teacher in teachers:
            # Предмети, які викладач може викладати і які ще не призначені
            available_subjects = teacher.can_teach_subjects & subjects_to_cover
            if available_subjects:
                if not best_teacher:
                    best_teacher = teacher
                    subjects_covered_by_best = available_subjects
                else:
                    # Якщо викладач покриває більше предметів
                    if len(available_subjects) > len(subjects_covered_by_best):
                        best_teacher = teacher
                        subjects_covered_by_best = available_subjects
                    # Якщо кількість предметів однакова, обираємо наймолодшого
                    elif len(available_subjects) == len(subjects_covered_by_best):
                        if teacher.age < best_teacher.age:
                            best_teacher = teacher
                            subjects_covered_by_best = available_subjects
        if not best_teacher:
            # Немає викладачів, які можуть покрити залишені предмети
            return None
        # Призначаємо викладачу предмети
        best_teacher.assigned_subjects = subjects_covered_by_best
        schedule.append(best_teacher)
        # Видаляємо покриті предмети з множини непризначених
        subjects_to_cover -= subjects_covered_by_best
        # Видаляємо викладача зі списку, щоб не розглядати його повторно
        teachers.remove(best_teacher)
    return schedule

if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
        Teacher('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
        Teacher('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
        Teacher('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
        Teacher('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
        Teacher('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
        Teacher('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
    ]
    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)
    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
