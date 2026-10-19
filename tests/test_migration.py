from sqlalchemy import create_engine, inspect


def test_users_table_exists():
    engine = create_engine("sqlite:///test.db")

    inspector = inspect(engine)##コード調査

    assert "users" in inspector.get_table_names()
