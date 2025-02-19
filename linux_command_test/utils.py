from subprocess import PIPE, CalledProcessError, run


class BaseLinuxCommandTest:
    """Базовый класс для тестов."""

    command_name = ''

    def execute_command(self, *args):
        """Выполнение команды."""
        full_command = [self.command_name, *args]
        result = run(full_command, stdout=PIPE, stderr=PIPE, text=True)
        if result.returncode != 0:
            raise CalledProcessError(result.returncode,
                                     full_command,
                                     output=result.stdout,
                                     stderr=result.stderr)
        return result

    def command_activation(self, *args):
        try:
            output = self.execute_command(*args)
        except CalledProcessError as e:
            output = f'Ошибка выполнения {e}'
        except FileNotFoundError:
            output = 'Команда не существует'
        return output
