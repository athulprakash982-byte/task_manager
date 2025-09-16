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
    
    def edit_task(self, new_name, new_description):
        self.name = new_name
        self.description = new_description
        return f"Task updated to: {new_name} - {new_description}"
        