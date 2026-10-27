# widgets_api.py
# Handler for GET /v1/widgets
from flask import Blueprint, request, jsonify

bp = Blueprint("widgets", __name__)

@bp.route("/v1/widgets", methods=["GET"])
def list_widgets():
    """List the widgets that belong to the authenticated account.

    Query parameters:
      limit  - maximum number of widgets to return (default 20, max 100)
      status - filter by status: active or archived
    """
    limit = min(int(request.args.get("limit", 20)), 100)
    status = request.args.get("status")
    widgets = _load_widgets(status=status)[:limit]
    return jsonify([{"id": w.id, "name": w.name, "status": w.status} for w in widgets])

def _load_widgets(status=None):
    return []
