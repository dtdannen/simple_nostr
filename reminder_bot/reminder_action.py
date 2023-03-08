

class ReminderAction:

    """
    Represents an action to be taken. This could include:

        - sending a NOSTR message

    """

    def __init__(self, action_type, parameters):
        self.action_type = action_type
        self.parameters = parameters


    def execute(self):
        """
        Says how to execute the action based on the action type and parameters
        :return:
        """


