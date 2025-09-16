class Task:
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.complted=False

    def mark_complete(self):
        self.complted=True
        return f"Task {self.name} marked completed"
    def show_task(self):
        status="✓" if self.complted else "✗"
        return f"[{status}] {self.name}: {self.description}"
        