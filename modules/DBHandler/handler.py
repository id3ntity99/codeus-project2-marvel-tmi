import sqlalchemy as db


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

    def get_keys(self, table) -> list:
        return table.columns.keys()

    def get_schema(self, table_name: str) -> db.sql.schema.Table:
        return self.metadata.tables[table_name]
