from Tools import is_


class Handler(object):

    def __init__(self, dp):
        self.x_dispatcher = dp
        self.dp = self.x_dispatcher.dp

    def register_commands_event(self):
        ...

    def register_message_event(self):
        ...

    def register_callback_event(self):
        ...

    def register_state_event(self):
        ...
