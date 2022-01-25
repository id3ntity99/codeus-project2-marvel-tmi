import sqlalchemy as db
import json
from sqlalchemy.orm import sessionmaker
import warnings


class SessionManager(object):
    def __init__(self, engine):
        self.engine = engine
        self.session = None

    def __enter__(self):
        Session = sessionmaker()
        self.session = Session(bind=self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


class MyDatabase:
    def __init__(self):
        self.engine = None
        warnings.warn("The DBHandler module is deprecated", DeprecationWarning)

    def connect_db(self, uri) -> None:
        self.engine = db.create_engine("sqlite:///{0}".format(uri))
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

    def disconnect_db(self) -> None:
        self.engine.dispose()

    def _jsonify(self, data):
        temp = []
        for row in data:
            temp_dict = {
                "success": True,
                "id": row.id,
                "url": row.url,
                "name": row.name,
                "appearances": row.appearances,
                "gender": row.gender,
                "year": row.year,
                "years_since_joining": row.years_since_joining,
                "description": row.note if row.note != "NA" else None,
            }
            temp.append(temp_dict)
        return json.dumps(temp)

    def get_keys(self, table) -> list:
        return table.columns.keys()

    def select_where_name_is(self, Model, keyword: str):
        query_keyword = "%{0}%".format(keyword)
        manager = SessionManager(self.engine)
        with manager:
            result = (
                manager.session.query(Model)
                .filter(Model.name.like(query_keyword))
                .all()
            )
        # 데이터베이스 검색 결과가 없으면 아래 메시지를 리턴
        if not result:
            err_msg = {"success": False, "message": "요청하신 데이터를 찾을 수 없습니다"}
            return json.dumps(err_msg)
        json_data = self._jsonify(result)
        return json_data

    def select_all(self, Model) -> list:
        manager = SessionManager(self.engine)
        with manager:
            result = manager.session.query(Model).all()
        json_data = self._jsonify(result)
        return json_data
