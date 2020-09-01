

class BrickCustomCode(Brick):

    def validate_args(self, args):
        # validate args
        # ...
        return len(self.messages) == 0

    def validate_inputs(self):
        # validate inputs
        # ...
        return len(self.messages) == 0

    def perform_execution(self, ctx: ExecutionContext):
        # ...
        self.status = BrickStatus.SUCCESS

    def perform_light_run(self, ctx: ExecutionContext):
        # ...
        pass
