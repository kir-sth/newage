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
    first_photo = form.get("first_photo", {"first_photo_id": None, "first_photo": None})
    json.update(first_photo)
    second_photo = form.get("second_photo", {"second_photo_id": None, "second_photo": None})
    json.update(second_photo)
    third_photo = form.get("third_photo", {"third_photo_id": None, "third_photo": None})
    json.update(third_photo)
    # json is ready to be uploaded to the database
    # tba: json -> database 
    print(json)
