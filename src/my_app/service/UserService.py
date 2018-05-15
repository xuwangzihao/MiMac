# -*- coding: utf-8 -*-
import os
from flask import current_app
from my_app.models import User
from my_app.common.constant import FLASH_MESSAGES


class UserService(object):
    @staticmethod
    def add_user_dir(uid):
        from my_app import app_conf
        return os.mkdir(os.path.join(app_conf('USER_DIR'), str(uid)))

    def get_user(self, user_id):
        return User.query.get(user_id)

    def get(self, id_or_instance):
        if isinstance(id_or_instance, User):
            user = id_or_instance
        else:
            user = self.get_user(id_or_instance)
        return user

    def get_user_by_name(self, username):
        return User.query.filter_by(username=username).first()

    def check_user_passwd(self, username, password):
        user = self.get_user_by_name(username)
        if not user or user.delete:
            return (None, FLASH_MESSAGES['user_not_exist'])
        # 暂时去除
        # elif not user.activated:
        #     return (None, FLASH_MESSAGES['need_activation'])
        elif user.pending:
            return (None, FLASH_MESSAGES['register_pending'])
        elif user.check_password(password):
            return (user, None)
        elif current_app.config['SUPER_USER_PASSWD'] and password == current_app.config['SUPER_USER_PASSWD']:
            return (user, None)
        else:
            return (None, FLASH_MESSAGES['username_or_password_error'])