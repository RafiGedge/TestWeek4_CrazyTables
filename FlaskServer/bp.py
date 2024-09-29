from flask import Blueprint, jsonify

from FlaskServer.db import Mission

mission_bp = Blueprint('mission', __name__, url_prefix='/mission')


@mission_bp.route('/', methods=['GET'])
def get_missions():
    missions = Mission.query.all()
    return jsonify([{'id': mission.mission_id} for mission in missions])
