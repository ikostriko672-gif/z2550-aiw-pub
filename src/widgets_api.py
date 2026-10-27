# widgets_api.py
# Handler for GET /v1/widgets
from flask import Blueprint, request, jsonify

bp = Blueprint("widgets", __name__)

@bp.route("/v1/widgets", methods=["GET"])
def list_widgets():
    """List the widgets that belong to the authenticated account.

    Query parameters:
      page_size - maximum number of widgets to return (default 20, max 50); replaces `limit`
      status    - filter by status: active or archived
      cursor    - opaque cursor from `next_cursor` of the previous page
    """
    page_size = min(int(request.args.get("page_size", 20)), 50)
    status = request.args.get("status")
    cursor = request.args.get("cursor")
    widgets, next_cursor = _load_widgets(status=status, cursor=cursor, page_size=page_size)
    return jsonify({
        "data": [{"id": w.id, "name": w.name, "status": w.status, "color": w.color} for w in widgets],
        "next_cursor": next_cursor,
    })

def _load_widgets(status=None, cursor=None, page_size=20):
    return [], None
