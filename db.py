import typing
import random
from schemas import PhraseInput, PhraseOutput

class Database:
    """
    Our **fake** database.
    """

    def __init__(self):
        self._items: typing.Dict[int, PhraseOutput] = {}  # id: model

    def get_random(self) -> int:
        # Получение случайной фразы
        return random.choice(self._items.keys())

    def get(self, id: int) -> typing.Optional[PhraseOutput]:
        # Получение фразы по ID
        return self._items.get(id)

    def add(self, phrase: PhraseInput) -> PhraseOutput:
        # Добавление фразы

        id = len(self._items) + 1
        phrase_out = PhraseOutput(id=id, **phrase.dict())
        self._items[phrase_out.id] = phrase_out
        return phrase_out

    def delete(self, id: int) -> typing.Union[typing.NoReturn, None]:
        # Удаление фразы

        if id in self._items:
            del self._items[id]
        else:
            raise ValueError("Phrase doesn't exist")