class DialogueSystem:
    def __init__(self, dialogues):
        self.dialogues = dialogues
        self.current_index = 0

    def get_current_dialogue(self):
        if self.current_index < len(self.dialogues):
            return self.dialogues[self.current_index]
        return {"speaker": "", "text": ""}

    def advance(self):
        self.current_index += 1