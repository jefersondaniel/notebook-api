from flask import Response
from flask.ext.restful import Resource
from app import api
from app.framework.schema import input_schema, output_schema
from schemas import NotebookSchema, NoteSchema, NoteReferenceSchema
from entities import Note, Notebook

INDEX_RESOURCE_OUTPUT = {
    'links': {
        'self': '/',
        'notebooks': '/notebooks',
        'notes': '/notes'
    }
}


@api.resource('/')
class IndexResource(Resource):
    def get(self):
        return INDEX_RESOURCE_OUTPUT


@api.resource('/notebooks')
class NotebookListResource(Resource):
    @input_schema(NotebookSchema())
    @output_schema(NotebookSchema())
    def post(self, notebook):
        notebook.save()
        return notebook


@api.resource('/notebooks/<slug>')
class NotebookResource(Resource):
    @input_schema(NotebookSchema())
    @output_schema(NotebookSchema())
    def post(self, notebook):
        notebook.save()
        return notebook

    @output_schema(NotebookSchema())
    def get(self, slug):
        return Notebook.objects.get(slug=slug)


@api.resource('/notebooks/<notebook_slug>/notes')
class NotebookNoteListResource(Resource):
    @output_schema(NoteReferenceSchema(many=True))
    def get(self, notebook_slug):
        notebook = Notebook.objects.get(slug=notebook_slug)
        return notebook.notes

    @input_schema(NoteSchema())
    @output_schema(NoteSchema())
    def post(self, note, notebook_slug):
        notebook = Notebook.objects.get(slug=notebook_slug)
        notebook.add_note(note)
        notebook.save()

        return note


@api.resource('/notes/<id>')
class NoteResource(Resource):
    @input_schema(NoteSchema(transform_entity=False))
    @output_schema(NoteSchema())
    def put(self, data, id):
        note = Note.objects.get(id=id)
        for key in data:
            setattr(note, key, data[key])
        note.save()
        return note

    @output_schema(NoteSchema())
    def get(self, id):
        return Note.objects.get(id=id)

    def delete(self, id):
        note = Note.objects.get(id=id)
        notebook = note.notebook
        notebook.remove_note(note)
        notebook.save()
        note.delete()

        return '', 204
