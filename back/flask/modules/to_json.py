import json


def jsonify(data):
    temp = []
    for row in data:
        temp_dict = {
            "success": True,
            "id": row.id,
            "url": row.url,
            "name": row.name,
            "appearances": row.appearances,
            "gender": row.gender,
            "year": row.year,
            "years_since_joining": row.years_since_joining,
            "description": row.note if row.note != "NA" else None,
        }
        temp.append(temp_dict)
    return json.dumps(temp)
