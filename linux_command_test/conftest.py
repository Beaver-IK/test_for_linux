import os
import tempfile

import pytest


@pytest.fixture
def test_file():
    """Фикстура для создания временного файла."""
    fd, path = tempfile.mkstemp(text=True)
    with os.fdopen(fd, 'w') as tmp:
        tmp.write('Это тестовая строка.\nВнутри тестового файла.')

    yield path
    os.remove(path)


@pytest.fixture
def temp_directory_with_files():
    """Фикстура для создания временной директории с несколькими файлами."""
    with tempfile.TemporaryDirectory() as tmpdir:
        with open(os.path.join(tmpdir, "file1.txt"), "w") as f1:
            f1.write("Content of file1")
        with open(os.path.join(tmpdir, "file2.txt"), "w") as f2:
            f2.write("Content of file2")
        with open(os.path.join(tmpdir, ".env"), "w") as f3:
            f3.write("Content of env file")

        yield tmpdir


@pytest.fixture
def file_list():
    """Фикстура со списком открытых фалов."""
    return ('file1.txt', 'file2.txt')


@pytest.fixture
def env_file_list():
    """Фикстура со списком файлов, учитывая скрытые."""
    return ('file1.txt', 'file2.txt', '.env', '.', '..')
