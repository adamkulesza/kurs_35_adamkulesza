import os
import json
import xml.etree.ElementTree as ET

# Ścieżka do pliku tekstowego z danymi
DATA_FILE = os.path.join(os.path.dirname(__file__), 'shots.txt')
from models import db, Shots

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
