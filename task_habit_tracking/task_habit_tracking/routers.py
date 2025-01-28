class TestDBRouter:
    """
    Роутер для работы с тестовой базой данных.
    """
    def db_for_read(self, model, **hints):
        return 'test'

    def db_for_write(self, model, **hints):
        return 'test'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'test':
            return True
        return None