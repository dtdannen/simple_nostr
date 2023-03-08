

class Bot:
    """
        A bot that can check state conditions and take actions w.r.t. a user
    """

    def __init__(self, user):
        self.user = user
        self.policies = set()
        self.current_state =

    def add_policy(self, policy):
        self.policies.add(policy)

    def run(self):
        while True:
            for policy in self.policies:
                for state in policy:
                    if current_state.implies(state):
                        policy.get_action(state).execute()


