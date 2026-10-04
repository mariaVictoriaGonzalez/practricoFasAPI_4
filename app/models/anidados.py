from .clientes import ClientePublic
from .servicio import ServicioPublic


class ClienteNested(ClientePublic):

    servicio: ServicioPublic | None = None


class ServicioNested(ServicioPublic):

    clientes: list[ClientePublic] = []

    