import sqlalchemy as db
import json
from sqlalchemy.orm import sessionmaker


class MyDatabase:
    def connect_db(self, uri) -> None:
        self.engine = db.create_engine("sqlite:///{0}".format(uri))
        self.connection = self.engine.connect()
        self.metadata = db.MetaData()

    def load_table(self, table_name: str) -> db.sql.schema.Table:
        table = db.Table(
            table_name, self.metadata, autoload=True, autoload_with=self.engine
        )
        return table

    def _jsonify(self, data):
        temp = []
        for row in data:
            temp_dict = {
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
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            result = session.query(Model).filter(Model.name.like(query_keyword)).all()
        json_data = self._jsonify(result)
        return json_data

    def select_all(self, Model) -> list:
        Session = sessionmaker(bind=self.engine)
        with Session() as session:
            result = session.query(Model).all()
        json_data = self._jsonify(result)
        return json_data
