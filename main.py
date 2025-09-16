from tasks.task import Task
def main():
    print("=== Task Manager ===")
    task1=Task("Learn python from ai","Complete oop")
    task2=Task("Learn swim","deep dive")

    print(task1.show_task())
    print(task2.show_task())

    # Edit the task
    print(task1.edit_task("Master Python", "Learn OOP and advanced concepts"))
    print("After editing:")
    print(task1.show_task())

    print(task1.mark_complete())

    print(task1.show_task())
    print(task2.show_task())

if __name__=="__main__":
    main()
