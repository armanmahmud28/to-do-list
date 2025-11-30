def is_valid_title(title: str) -> bool:
    if not title or title.strip() == "":
        return False
    return True


def is_valid_index(index: int, tasks: list) -> bool:
    return 0 <= index < len(tasks)
