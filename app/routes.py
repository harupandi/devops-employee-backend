from flask import Blueprint, jsonify, request
from .data import EMPLOYEES

employees_bp = Blueprint("employees", __name__)

@employees_bp.get("/employees")
def list_employees():
    # Simulates a paginated DB query.
    try:
        page = max(int(request.args.get("page", 1)), 1)
        limit = min(max(int(request.args.get("limit", 10)), 1), 50)
    except ValueError:
        return jsonify({"error": "page and limit must be integers"}), 400

    total = len(EMPLOYEES)
    start = (page - 1) * limit
    end = start + limit
    items = EMPLOYEES[start:end]

    return jsonify({
        "data": items,
        "pagination": {
            "page": page,
            "limit": limit,
            "total": total,
            "total_pages": (total + limit - 1) // limit
        }
    })

@employees_bp.get("/employees/<int:employee_id>")
def get_employee(employee_id):
    employee = next((e for e in EMPLOYEES if e["id"] == employee_id), None)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify({"data": employee})

@employees_bp.post("/employees")
def create_employee():
    payload = request.get_json(silent=True) or {}
    required = ["first_name", "last_name", "department", "role", "email"]

    missing = [field for field in required if not payload.get(field)]
    if missing:
        return jsonify({"error": "Missing required fields", "fields": missing}), 400

    new_id = max(e["id"] for e in EMPLOYEES) + 1 if EMPLOYEES else 1
    employee = {"id": new_id, **{field: payload[field] for field in required}}
    EMPLOYEES.append(employee)

    return jsonify({"data": employee}), 201

@employees_bp.put("/employees/<int:employee_id>")
def update_employee(employee_id):
    employee = next((e for e in EMPLOYEES if e["id"] == employee_id), None)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    payload = request.get_json(silent=True) or {}
    allowed = ["first_name", "last_name", "department", "role", "email"]

    for field in allowed:
        if field in payload:
            employee[field] = payload[field]

    return jsonify({"data": employee})

@employees_bp.delete("/employees/<int:employee_id>")
def delete_employee(employee_id):
    employee = next((e for e in EMPLOYEES if e["id"] == employee_id), None)
    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    EMPLOYEES.remove(employee)
    return "", 204
