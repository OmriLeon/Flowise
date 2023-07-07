class Conversation:
    def __init__(self, conversation_id, agent_id):
        self.conversation_id = conversation_id
        self.agent_id = agent_id
        self.conversation_history = []

    def start_conversation(self, initial_message):
        self.conversation_history.append(initial_message)
        return self.conversation_history

    def add_message(self, message):
        self.conversation_history.append(message)
        return self.conversation_history

    def get_conversation(self):
        return self.conversation_history

    def end_conversation(self):
        from persistent_memory import PersistentMemory
        memory = PersistentMemory(self.agent_id)
        memory.store_conversation(self.conversation_id, self.conversation_history)
        self.conversation_history = []