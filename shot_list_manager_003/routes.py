import os
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import current_app
from file_handler import load_users_from_file, save_users_to_file, parse_uploaded_xml

my_blueprint = Blueprint('my_blueprint', __name__)
my_blueprint_002 = Blueprint('my_blueprint_002', __name__)




DATA_FILE = os.path.join(os.path.dirname(__file__), 'shots.txt')


users = load_users_from_file()


@my_blueprint.route('/')
def intro():
    return render_template("intro.html")

@my_blueprint_002.route('/shot_list',methods=["GET", "POST"])
def shot_list():
    if request.method == "POST":
        form_type = request.form.get("form_type")
        match form_type:
            case "add_user":
                print(form_type)

                shot_id_name = request.form.get("shot_id_name")
                form_errors = {}

                # Walidacja pustego pola
                if not shot_id_name:
                    form_errors["shot_id_name"] = "❌ required"

                # Sprawdzenie unikalności
                elif any(user["shot_id_name"] == shot_id_name for user in users):
                    form_errors[
                        "shot_id_name"] = "❌ That shot already exists – you can't add it. Please delete and add again."

                # Jeśli są błędy, zwróć formularz z komunikatem
                if form_errors:
                    return render_template("shot_list.html", users=users, form_errors=form_errors)

                xml_file = request.files.get("xml_file")
                xml_data = {
                    "videoCodec": "",
                    "audioChannels": "",
                    "deviceModel": "",
                    "lensModel": "",
                    "xmlFilename": ""
                }


                if xml_file and xml_file.filename.endswith('.XML'):
                    filename = secure_filename(xml_file.filename)
                    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                    xml_file.save(filepath)

                    parsed_data = parse_uploaded_xml(filepath)
                    xml_data.update(parsed_data)
                    xml_data["xmlFilename"] = filename

                    print("✅ Parsed XML data:", xml_data)


                new_user = {
                    "scene_id": request.form.get("scene_id"),
                    "shot_id_name": request.form.get("shot_id_name"),
                    "time_to_roll_the_shot": request.form.get("time_to_roll_the_shot"),
                    "camera_shot_type": request.form.get("camera_shot_type"),
                    "camera_movement": request.form.get("camera_movement"),
                    "camera_id": request.form.get("camera_id"),
                    "shot_description": request.form.get("shot_description"),
                    "lighting": request.form.get("lighting"),
                    "actors": request.form.get("actors"),
                    "props": request.form.get("props"),
                    **xml_data
                }
                users.append(new_user)
                users.sort(key=lambda user: user["shot_id_name"])
                save_users_to_file(users)
            case "delete_user":
                print(form_type)
                user_name = request.form.get("delete_shot_id_name")
                for user in users:
                    if user["shot_id_name"] == user_name:
                        users.remove(user)
                        save_users_to_file(users)
                        break
        return redirect(url_for("my_blueprint_002.shot_list"))

    return render_template("shot_list.html", users=users)
