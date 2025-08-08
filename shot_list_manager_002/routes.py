import os
from flask import Blueprint, render_template, request, redirect, url_for
import xml.etree.ElementTree as ET
from werkzeug.utils import secure_filename
from flask import current_app

my_blueprint = Blueprint('my_blueprint', __name__)
my_blueprint_002 = Blueprint('my_blueprint_002', __name__)



users = [
    {
        "scene_id": "1",
        "shot_id_name": "CD_23_0001",
        "time_to_roll_the_shot": "30",
        "camera_shot_type": "Wide shot",
        "camera_movement": "Doll shot",
        "camera_id": "1",
        "shot_description": "Marek siedzi w trumnie, maluje usta. Robert/krasnal obok, je jabłko",
        "lighting": "natural",
        "actors": "Wiktoria, Nikolas, Rafał, Hubert, KURCZAK",
        "props": "cofin",
        "xmlFilename": "C0128M01",
        "videoCodec": "AVC_3840_2160_H422IP@L51",
        "deviceModel": "ILME-FX3",
        "lensModel": "24-70mm F2.8 DG DN II | Art 024",
        "frameCount": "250",
        "captureFps": "23.98p",
        "pixel": "3840",
        "numOfVerticalLine": "2160",
        "aspectRatio": "16:9",
        "audioChannels": "2",
        "audioCodec": "LPCM16"
    }
]

def parse_uploaded_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        ns = {'nrt': 'urn:schemas-professionalDisc:nonRealTimeMeta:ver.2.20'}

        video_frame = root.find('.//nrt:VideoFormat/nrt:VideoFrame', ns)
        video_layout = root.find('.//nrt:VideoFormat/nrt:VideoLayout', ns)
        audio_format = root.find('.//nrt:AudioFormat', ns)
        audio_codec = root.find('.//nrt:AudioFormat/nrt:AudioRecPort', ns)
        device = root.find('.//nrt:Device', ns)
        lens = root.find('.//nrt:Lens', ns)
        frame_count = root.find('.//nrt:LtcChangeTable/nrt:LtcChange[@status="end"]', ns)

        return {
            "videoCodec": video_frame.attrib.get('videoCodec') if video_frame is not None else '',
            "captureFps": video_frame.attrib.get('captureFps') if video_frame is not None else '',
            "pixel": video_layout.attrib.get('pixel') if video_layout is not None else '',
            "numOfVerticalLine": video_layout.attrib.get('numOfVerticalLine') if video_layout is not None else '',
            "aspectRatio": video_layout.attrib.get('aspectRatio') if video_layout is not None else '',
            "audioChannels": audio_format.attrib.get('numOfChannel') if audio_format is not None else '',
            "audioCodec": audio_codec.attrib.get('audioCodec') if audio_codec is not None else '',
            "deviceModel": device.attrib.get('modelName') if device is not None else '',
            "lensModel": lens.attrib.get('modelName') if lens is not None else '',
            "frameCount": frame_count.attrib.get('frameCount') if frame_count is not None else ''
        }

    except Exception as e:
        print(f"Błąd parsowania XML: {e}")
        return {key: "error" for key in [
            "videoCodec", "captureFps", "pixel", "numOfVerticalLine", "aspectRatio",
            "audioChannels", "audioCodec", "deviceModel", "lensModel", "frameCount"
        ]}

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
            case "delete_user":
                print(form_type)
                user_name = request.form.get("delete_shot_id_name")
                for user in users:
                    if user["shot_id_name"] == user_name:
                        users.remove(user)
                        break
        return redirect(url_for("my_blueprint_002.shot_list"))

    return render_template("shot_list.html", users=users)
