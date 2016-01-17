import mongoengine as m
import os
import base64


class Notebook(m.Document):
    slug = m.StringField(max_length=255, unique=True)
    notes = m.ListField(m.ReferenceField('Note'))

    def clean(self):
        if not self.slug:
            self.slug = self.generate_slug()

    def generate_slug(self):
        slug = base64.encodestring(os.urandom(8)).strip()

        if Notebook.objects(slug=slug).count():
            slug = self.generate_slug()

        return slug


class Note(m.Document):
    name = m.StringField(max_length=255)
    contents = m.StringField()
    notebook = m.ReferenceField('Notebook')
