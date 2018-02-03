# -*- coding: utf-8 -*-
from apistar import typesystem


class PseudoSchema(typesystem.Object):
    properties = {
        'name': typesystem.string(
            max_length=100,
            description="name of pseudo",
        ),  # Use lowercase functions for inline declarations.
    }