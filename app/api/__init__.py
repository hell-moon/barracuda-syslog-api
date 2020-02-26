from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import errors, tokens, users, domains, accounts, messages, attachments, recipients
