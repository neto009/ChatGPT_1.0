class Chat:
    def __init__(self, data):
        self.id = data.id
        self.object = data.object
        self.created = data.created
        self.model = data.model
        self.choices = [Choice(choice_data) for choice_data in data.choices or []]
        self.usage = data.usage
        self.system_fingerprint = data.system_fingerprint

    def to_dict(self):
        choices_dict = [choice.to_dict() for choice in self.choices]
        return {
            'id': self.id,
            'object': self.object,
            'created': self.created,
            'model': self.model,
            'choices': choices_dict,
            'usage': self.usage,
            'system_fingerprint': self.system_fingerprint
        }

class Choice:
    def __init__(self, data):
        self.index = data.index
        self.message = Message(data.message or {})
        self.finish_reason = data.finish_reason

    def to_dict(self):
        return {
            'index': self.index,
            'message': self.message.to_dict(),
            'finish_reason': self.finish_reason
        }

class Message:
    def __init__(self, data):
        self.role = data.role
        self.content = data.content

    def to_dict(self):
        return {
            'role': self.role,
            'content': self.content
        }
