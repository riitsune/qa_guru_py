from _pytest.fixtures import fixture

import shutil
import utils
import os
from zipfile import ZipFile
@fixture(scope="function", autouse=True)
def resources():
    if not os.path.exists(utils.TMP_PATH):
        os.mkdir(os.path.join(utils.PROJECT_ROOT_PATH, "tmp"))

    with ZipFile(os.path.join(utils.TMP_PATH, "resources"), 'w') as new_archive:
        for filename in os.listdir(utils.RESOURCES_PATH):
            new_archive.write(os.path.join(utils.RESOURCES_PATH, filename), arcname=filename)

    yield

    shutil.rmtree(utils.TMP_PATH)