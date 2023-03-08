

class ReminderPolicy:

    """
    A reminder policy is a state-action representation that controls what actions should be taken in a given state.

    Some example reminders:

        1. "Remind me of my friend's birthday so I can text him that day"

            This reminder would likely consist of a policy with a single state action pair. If today's date is the same
             date as my friend's birthday, then send a reminder text to me.

        2. "Remind me of my wife's birthday a week in advance so I can buy her a present"

        3. "Remind me to change my air filter at the beginning of every month"

    """