import os
from base64 import encodestring
from app.framework.storage.repository import BaseRepository
from entities import Notebook


class NotebookRepository(BaseRepository):
    collection_name = 'notebooks'
    entity = Notebook

    def generate_slug(self):
        slug = encodestring(os.urandom(12)).strip()
        other = self.find_one_by({'slug': slug})

        if other:
            slug = self.generate_slug()

        return slug

    def pre_save(self, notebook):
        if not notebook.id and not notebook.slug:
            notebook.slug = self.generate_slug()
