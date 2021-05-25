from command import Send


class Execute(Send):

    def execute(self, socket, args) -> str:
        args.insert(0, 'exec')
        return super().execute(socket, args)

    def help(self) -> str:
        return 'Executes a command into the connected node.\n'
