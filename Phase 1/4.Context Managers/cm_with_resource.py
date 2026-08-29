class Database:
    def __enter__(self):
        print("Connecting To Database")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Closing Database Connection")

    def query(self):
        print("Running Query")

with Database() as db:
    db.query()