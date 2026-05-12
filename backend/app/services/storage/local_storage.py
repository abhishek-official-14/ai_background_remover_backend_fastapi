from pathlib import Path


class LocalStorage:
    @staticmethod
    def exists(path: str) -> bool:
        return Path(path).exists()

    @staticmethod
    def to_url(path: str) -> str:
        return f'/static/{Path(path).name}'
