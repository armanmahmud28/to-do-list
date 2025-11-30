from utils.file_manager import load_tasks, save_tasks
from utils.validator import is_valid_title, is_valid_index


def add_task(title):
    tasks = load_tasks()

    if not is_valid_title(title):
        return False

    tasks.append({
        "title": title.strip(),
        "done": False
    })

    save_tasks(tasks)
    return True


def get_tasks():
    return load_tasks()


def complete_task(index):
    tasks = load_tasks()
    if not is_valid_index(index, tasks):
        return False

    tasks[index]["done"] = True
    save_tasks(tasks)
    return True


def delete_task(index):
    tasks = load_tasks()
    if not is_valid_index(index, tasks):
        return False

    tasks.pop(index)
    save_tasks(tasks)
    return True
