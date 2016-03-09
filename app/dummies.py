from bson.objectid import ObjectId

dummies = {
    'notebook': [
        {
            '_id': ObjectId('569ba781e138232929c00a86'),
            'slug': 'custom-slug',
            'notes': [
                {
                    'id': '469ba781e138232929c00afa',
                    'resume': 'Hello World'
                }
            ]
        }
    ],
    'note': [
        {
            '_id': ObjectId('469ba781e138232929c00afa'),
            'resume': 'Hello World',
            'contents': 'Hello World',
            'notebook': ObjectId('569ba781e138232929c00a86')
        }
    ]
}
