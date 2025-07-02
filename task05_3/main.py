# Завдання 3 (не обов'язкове)
# Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.
# Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.

import sys
from pathlib import Path
from collections import defaultdict

# створення словника з логами
def parse_log_line(path_log):
    logs = []
    with open(path_log, "r", encoding='utf-8') as file:
        for line in file:
            log_date, log_time, level, log_message = line.strip().split(" ", 3)
            logs.append({
                "date": log_date,
                "time": log_time,
                "level": level,
                "message": log_message
            })
    return logs

# фільтрування логів
def filter_logs_by_level(logs, level):
    level = level.upper()
    return [log for log in logs if log["level"] == level]

# підрахунок логів
def count_logs_by_level(logs):
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)

# виведення таблиці з логами
def display_log_counts(counts):
    print("\nСтатистика логів за рівнями:")
    print(f"{"Рівень":<10} | {"Кількість":<10} |")
    print("-" * 25)
    for level in sorted(counts.keys()):
        print(f"{level:<10} | {counts[level]:<10} |")
    print("-" * 25)

def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент.")
        print("Приклад: python main.py logfile.log")
        sys.exit(1)
    path = Path(sys.argv[1])
    print(path)
    level_filter = sys.argv[2] if len(sys.argv) >= 3 else None
    
    if not path.exists():
        print(f"Шлях {path} не існує.")  
        sys.exit(1)

    logs = parse_log_line(path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        if filtered_logs:
            print(f"\nЗаписи рівня {level_filter.upper()}:")
            for log in filtered_logs:
                print(f"{log["date"]} {log["time"]} {log["level"]} {log["message"]}")
        else:
            print(f"\nНе знайдено записів рівня {level_filter.upper()}")

if __name__ == "__main__":
    main()