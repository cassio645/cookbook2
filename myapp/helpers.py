from .import imagekit
import base64


class ImagekitClient(object):
    def __init__(self, file):
        self.file = self.convert_to_binary(file=file)
        self.file_name = file.name

    def convert_to_binary(self, file):
        self.binary_file = base64.b64encode(file.read())
        return self.binary_file

    def upload_media_file(self):

        response = imagekit.upload_file(
            file = self.file,
            file_name = self.file_name
        )
        return response.response_metadata.raw


class ImagekitDelete(object):
    def __init__(self, file_id):
        self.file_id = file_id
    
    def delete_image(self):
        delete = imagekit.delete_file(file_id=self.file_id)
        return delete.response_metadata.raw