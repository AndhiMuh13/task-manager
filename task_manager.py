tasks = []


def add_task(task):
    tasks.append(task)


def remove_task(task):
    tasks.remove(task)


def list_tasks():
    return tasks
