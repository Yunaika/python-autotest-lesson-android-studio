def abs_path_from_project(relative_path: str):
    import python_autotest_lesson_android_studio
    from pathlib import Path

    return (
        Path(python_autotest_lesson_android_studio.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )
