import os.path

def total_salary(path): 
    is_exist_file = os.path.isfile(path)
    if not is_exist_file:
        return 0,0
    
    total = 0
    count = 0

    with open(path, "r", encoding="utf-8") as file:
       for i, line in enumerate(file):
           line = line.strip()
           if not line:
                continue
           try:
               name, salary_str = line.split(',', 1)
               salary = int(salary_str)
           except ValueError:
               continue
           
           total += salary
           count += 1

    avg = total / count if count else 0.0
    return total, avg


total, average = total_salary("test1File.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")