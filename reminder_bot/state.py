

class State:

    """
    Represents a state of the world that is relevant to the bot's operations
    """

    def __init__(self):
        pass

    def implies(self, other_state):
        all_conditions_met = True
        for condition in other_state:
            if condition not in self.conditions:
                all_conditions_met = False
        return all_conditions_met

