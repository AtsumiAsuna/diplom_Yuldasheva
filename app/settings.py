from PyQt6.QtCore import QSettings


class AppSettings:
    def __init__(self) -> None:
        self.settings = QSettings("GusHubApp", "GushubManager")

    def is_fully_configured(self) -> bool:
        """
        Проверяет, есть ли все необходимые данные для работы приложения
        """
        github_token = self.get_github_token()
        login = self.get_gushub_login()
        password = self.get_gushub_password()
        
        return (
            github_token is not None and github_token != "" and
            login is not None and login != "" and
            password is not None and password != ""
        )
    
    # GitHub Token
    def get_github_token(self) -> str | None:
        return self.settings.value("github/token", None)

    def set_github_token(self, token: str) -> None:
        self.settings.setValue("github/token", token)

    def delete_github_token(self) -> None:
        self.settings.remove("github/token")

    # Gushub Login
    def get_gushub_login(self) -> str | None:
        return self.settings.value("gushub/login", None)

    def set_gushub_login(self, login: str) -> None:
        self.settings.setValue("gushub/login", login)

    def delete_gushub_login(self) -> None:
        self.settings.remove("gushub/login")

    # Gushub Password
    def get_gushub_password(self) -> str | None:
        return self.settings.value("gushub/password", None)

    def set_gushub_password(self, password: str) -> None:
        self.settings.setValue("gushub/password", password)

    def delete_gushub_password(self) -> None:
        self.settings.remove("gushub/password")

    # Gushub Credentials
    def get_gushub_credentials(self) -> tuple[str, str] | None:
        login = self.get_gushub_login()
        password = self.get_gushub_password()
        return login, password

    def set_gushub_credentials(self, login: str, password: str) -> None:
        """
        Устанавливает логин и пароль Gushub одним вызовом
        """
        self.set_gushub_login(login)
        self.set_gushub_password(password)

    def delete_gushub_credentials(self) -> None:
        self.delete_gushub_login()
        self.delete_gushub_password()

    # Gushub Token
    def get_gushub_token(self) -> str | None:
        return self.settings.value("gushub/token", None)

    def set_gushub_token(self, token: str) -> None:
        self.settings.setValue("gushub/token", token)

    # Database settings
    def get_database_host(self) -> str:
        return self.settings.value("database/host", "localhost")

    def set_database_host(self, host: str) -> None:
        self.settings.setValue("database/host", host)

    def get_database_user(self) -> str:
        return self.settings.value("database/user", "root")

    def set_database_user(self, user: str) -> None:
        self.settings.setValue("database/user", user)

    def get_database_password(self) -> str:
        return self.settings.value("database/password", "")

    def set_database_password(self, password: str) -> None:
        self.settings.setValue("database/password", password)

    def get_database_name(self) -> str:
        return self.settings.value("database/name", "diplom_gushub")

    def set_database_name(self, name: str) -> None:
        self.settings.setValue("database/name", name)

    def get_database_settings(self) -> dict:
        return {
            "host": self.get_database_host(),
            "user": self.get_database_user(),
            "password": self.get_database_password(),
            "database": self.get_database_name()
        }

    # Очистка (если нужно)
    def clear(self) -> None:
        self.settings.clear()
