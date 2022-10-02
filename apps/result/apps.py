from django.apps import AppConfig


class ResultConfig(AppConfig):
    name = "apps.result"

class StudentsConfig(AppConfig):
    name = "apps.students"

    def ready(self):
        import apps.students.signals

