from .links_repository import LinksRepository
import uuid 
import pytest
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interacao com o banco de dados")
def test_registry_link():
    conn = db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    link_infos = {
        "id": link_id,
        "trip_id": trip_id,
        "link": "algumlink.com",
        "title": "Hotel"
    }

    link_repository.registry_link(link_infos)

@pytest.mark.skip(reason="Interacao com o banco de dados")
def test_find_links_from_trip():
    conn =  db_connection_handler.get_connection()
    link_repository = LinksRepository(conn)

    links = link_repository.find_links_from_trip(trip_id)
    print()
    print(links)

    response = link_repository.find_links_from_trip(trip_id)

    try:
        assert isinstance(response, list)
        assert isinstance(response[0], tuple)
    except AssertionError as e:
        print(f"Erro de asserção: {e}")
