from datetime import datetime

class Task:

    def __init__(
            self,
            id = None,
            name = '', 
            description = '', 
            status = 1, 
            created_on = datetime.now().strftime('%d/%m/%Y %H:%M:%S'), 
            completed_on = None
        ):
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.created_on = created_on
        self.completed_on = completed_on
        pass

    def get_id(self):
        return int(self.id)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_status(self):
        return self.status

    def get_created_on(self):
        return self.created_on

    def get_completed_on(self):
        return self.completed_on

    def set_id(self, id):
        self.id = id
        pass

    def set_name(self, name):
        self.name = name
        pass

    def set_description(self, description):
        self.description = description
        pass

    def set_status(self, status):
        self.status = status
        pass

    def set_created_on(self, created_on):
        self.created_on = created_on
        pass

    def set_completed_on(self, completed_on):
        self.completed_on = completed_on
        pass
        