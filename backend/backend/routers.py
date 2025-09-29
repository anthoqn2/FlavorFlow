class MongoRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'your_app_name':  # replace with your app
            return 'mongo'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'your_app_name':
            return 'mongo'
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'main':  # send only this app to Mongo
            return db == 'mongo'
        return db == 'default'