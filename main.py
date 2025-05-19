import numpy as np
from dataclasses import dataclass


class User:
    id: str


class Comment:
    id: str
    text: str
    user: User


@dataclass
class Conversation:
    users: list[User]
    comments: list[Comment]
