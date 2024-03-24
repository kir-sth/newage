def dump_form(form: dict) -> None:
    lat, long = form.get("geo", (None, None))
    json = {
        "lat": lat,
        "long": long,
        "goal": form.get("goal"),
        "city": form.get("city"),
        "gender": form.get("gender"),
        "preference": form.get("preference"),
        "name": form.get("name"),
        "age": form.get("age"),
        "description": form.get("description"),
    }
    if "first_photo" in form:
        json.update(form["first_photo"])
    if "second_photo" in form:
        json.update(form["first_photo"])
    if "third_photo" in form:
        json.update(form["first_photo"])
    json = {key: value for key, value in json.items() if value is not None}
    # json is ready to be uploaded to the database
    # tba: json -> database 

