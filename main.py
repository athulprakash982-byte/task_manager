from tasks.task import Task
def main():
    print("=== Task Manager ===")
    task1=Task("Learn python","Complete oop")
    task2=Task("Learn swim","deep dive")

    print(task1.show_task())
    print(task2.show_task())

    print(task1.mark_complete())

    print(task1.show_task())
    print(task2.show_task())

if __name__=="__main__":
    main()
