from .models import Pseudo
from .schemas import PseudoSchema
from typing import List

from apistar import Response
from apistar.backends.django_orm import Session


def pseudo_create(session: Session, pseudo: PseudoSchema) -> Response:
    """
    create new pseudo
    """
    p = session.Pseudo(**pseudo)
    p.save()
    return Response(Pseudo(p), status=201)


def get_pseudos(session: Session) -> List(PseudoSchema):
    """
    Return list of Pseudo
    """
    objs = session.Pseudo.objects.all()
    return [PseudoSchema(o) for o in objs]
