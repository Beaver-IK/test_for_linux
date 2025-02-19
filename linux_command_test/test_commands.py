from subprocess import CompletedProcess

import pytest
from pytest_lazyfixture import lazy_fixture as lf
from utils import BaseLinuxCommandTest

FILES = lf('file_list')
ENV_FILES = lf('env_file_list')


class TestEcho(BaseLinuxCommandTest):
    """Кейс для ECHO."""

    command_name = 'echo'

    @pytest.mark.parametrize(
        'args, expected_output', (
            (['Hello, World!'], 'Hello, World!'),
            (['-n'], ''),
        )
    )
    def test_command(self, args, expected_output):

        output = self.command_activation(*args)
        assert isinstance(output, CompletedProcess), (
            f'Команда не поддерживается. '
            f'{output}'
        )
        assert output.stdout.strip() == expected_output, (
            f'Ожидает вывод: "{expected_output}". '
            f'Вывод: "{output.stdout.strip()}"'
        )


class TestLs(BaseLinuxCommandTest):
    """Кейс для LS."""

    command_name = 'ls'

    @pytest.mark.parametrize(
        'args, expected_output', (
            ([], FILES),
            (['-a',], ENV_FILES),
        )
    )
    def test_command(self, args, expected_output, temp_directory_with_files):
        """Тестируем команду ls с временной директорией."""
        args.append(temp_directory_with_files)
        output = self.command_activation(*args).stdout.rstrip('\n').split('\n')
        print(output)
        assert set(output) == set(expected_output), (
            'Команда неверно определяет содержимое папки.'
        )


class TestWc(BaseLinuxCommandTest):
    """Кейс для WC."""

    command_name = 'wc'

    @pytest.mark.parametrize("args, expected_output", [
        (['-l'], '1'),
        (['-w'], '6'),
        (['-c'], '81'),
    ])
    def test_command(self, args, expected_output, test_file):
        args.append(test_file)
        output = self.execute_command(*args).stdout.split()
        print(test_file)
        assert output[0] == expected_output, (
            f'Ожидается {expected_output}. Вывод: {output[0]}'
        )
        assert output[1] == test_file, (
            f'Ожидается {test_file}. Вывод: {output[1]}'
        )
