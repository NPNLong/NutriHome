from flask import Blueprint
from .services import personal_detail


personal = Blueprint("personal", __name__)

@personal.route("/api/personal", methods =['GET'])
def show_person_detail():
    return personal_detail()

