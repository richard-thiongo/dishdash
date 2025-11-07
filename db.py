import pymysql
 
class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.db = 'dishdash'
        self.connection = None
 
    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                cursorclass=pymysql.cursors.DictCursor
            )
        return self.connection
    
    def get_cursor(self):
        return self.connect().cursor()
    
    def commit(self):
        return self.connect().commit()
 
    def close(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None
 
    # ✅ Context Manager methods
    def __enter__(self):
        # Return cursor so you can use it directly inside `with`
        return self.get_cursor()
 
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:  
            # If an error occurs, rollback transaction
            self.connection.rollback()
        else:
            # If everything was fine, commit changes
            self.connection.commit()
        self.close()