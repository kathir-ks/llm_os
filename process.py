import uuid

class Process:

    def __init__(self, parent: 'Process', instructions:list,priority:int,  processID=uuid.uuid4) -> None:
        self.parent = parent
        self.processID = processID
        self.status = 'ready'
        self.instructions = instructions if instructions is not None else []
        self.priority = priority