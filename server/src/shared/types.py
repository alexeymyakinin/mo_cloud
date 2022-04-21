from enum import Enum, auto


class UserTaskType(str, Enum):
    assignee = auto()
    watcher = auto()
    author = auto()
