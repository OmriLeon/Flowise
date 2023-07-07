import local_llm_model
import persistent_memory
import conversation

class Agent:
    def __init__(self, agent_id, model_id, memory_id):
        self.agent_id = agent_id
        self.model_id = model_id
        self.memory_id = memory_id
        self.model = None
        self.memory = None

    def createAgent(self):
        self.model = local_llm_model.loadModel(self.model_id)
        self.memory = persistent_memory.PersistentMemory(self.memory_id)

    def startConversation(self, conversation_id):
        conv = conversation.Conversation(conversation_id, self.agent_id)
        conv.startConversation()

    def storeConversation(self, conversation_id):
        conv = conversation.Conversation(conversation_id, self.agent_id)
        self.memory.storeConversation(conv)

    def retrieveConversation(self, conversation_id):
        return self.memory.retrieveConversation(conversation_id)