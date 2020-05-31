#
# Copyright (c) 2020 Nox Technologies Ltd <info at noxt eu>
# All rights reserved.
#
# Use is subject to license terms, as specified in the LICENSE file.
#

from flask_restplus import Namespace, Resource, fields
from enum import Enum, auto

api = Namespace('document', validate=True)


class CLASSIFICATION(Enum):
    PUBLIC = auto()
    RESTRICTED = auto()
    CONFIDENTIAL = auto()
    SECRET = auto()
    TOP_SECRET = auto()


document_model = api.model('document', {
    'title': fields.String(),
    'level': fields.String(enum=tuple(x.name for x in CLASSIFICATION))
})

document_result_model = api.model('document_result', {
    'id': fields.String(),
})


@api.route('/')
class DocumentsView(Resource):
    @api.expect(document_model)
    @api.marshal_list_with(document_result_model)
    def post(self):
        return {'id': None}, 201
