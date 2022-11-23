import pytest


@pytest.fixture(scope='session', autouse=True)
def patch_selene():
    import python_autotest_lesson_android_studio.utils.selene.patch_selector_strategy  # noqa
    import python_autotest_lesson_android_studio.utils.selene.patch_element_mobile_commands  # noqa
