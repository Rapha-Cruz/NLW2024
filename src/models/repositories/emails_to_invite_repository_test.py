import pytest
from src.models.settings.db_connection_handler import db_connection_handler
import uuid 
from .emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="Interacao com o banco de dados")
def test_registry_email():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails_trip_infos = {
        "id" : str(uuid.uuid4()),
        "trip_id" : trip_id,
        "email" : "oimail@gmail.com"
    }

    emails_to_invite_repository.registry_email(emails_trip_infos)

@pytest.mark.skip(reason="Interacao com o banco de dados")
def test_find_emails_from_trip():
    conn =  db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    emails = emails_to_invite_repository.find_emails_from_trip(trip_id)
    print()
    print(emails)