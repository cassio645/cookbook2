from .import imagekit
import base64


class ImagekitClient(object):
    """
    Classe para se conectar com o site imagekit.io
    """
    def __init__(self, file):
        self.file = self.convert_to_binary(file=file)
        self.file_name = file.name

    def convert_to_binary(self, file):
        # Converte um arquivo em binário com o base64
        self.binary_file = base64.b64encode(file.read())
        return self.binary_file

    def upload_media_file(self):
        # Faz o upload do arquivo binário e retorna o response
        response = imagekit.upload_file(
            file = self.file,
            file_name = self.file_name
        )
        return response.response_metadata.raw


class ImagekitDelete(object):
    '''
     Se conecta com o site imagekit.io para apagar uma imagem.
    '''
    def __init__(self, file_id):
        self.file_id = file_id
    
    def delete_image(self):
        # Deleta imagem a partir do file_id
        delete = imagekit.delete_file(file_id=self.file_id)
        return delete.response_metadata.raw