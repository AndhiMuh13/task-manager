from task_manager import add_task, remove_task, list_tasks

def test_add_task():
    add_task("Belajar Python")
    assert "Belajar Python" in list_tasks()

def test_remove_task():
    add_task("Belajar Git")
    remove_task("Belajar Git")
    assert "Belajar Git" not in list_tasks()
