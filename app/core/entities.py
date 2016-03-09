import mongoengine as m
import os
import base64
import re


class NoteReference(m.EmbeddedDocument):
    id = m.ObjectIdField()
    resume = m.StringField(max_length=32, unique=True)


class Notebook(m.Document):
    slug = m.StringField(max_length=255, unique=True)
    notes = m.EmbeddedDocumentListField(NoteReference)

    def clean(self):
        if not self.slug:
            self.slug = self.generate_slug()

    def add_note(self, note):
        note.notebook = self
        note.save()

        reference = NoteReference()
        reference.id = note.id
        reference.resume = note.resume

        self.notes.append(reference)

    def remove_note(self, note):
        to_remove = [x for x in self.notes if x.id == note.id]

        for reference in to_remove:
            self.notes.remove(reference)

    def list_notes(self):
        ids = [x.id for x in self.notes]
        return Note.objects(id__in=ids)

    def generate_slug(self):
        slug = base64.encodestring(os.urandom(8)).strip()
        slug = re.sub('[^0-9A-Za-z]', '', slug)

        if Notebook.objects(slug=slug).count():
            slug = self.generate_slug()

        return slug


class Note(m.Document):
    resume = m.StringField(max_length=32)
    contents = m.StringField()
    notebook = m.ReferenceField('Notebook')
