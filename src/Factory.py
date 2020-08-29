from src.Comment import Comment
from src.ExtractFollowers import ExtractFollowers

class Factory:

    COMMENT = 'comment'
    EXTRACT = 'extract'

    def get(self, driver, flow):
        if flow == self.COMMENT:
            postId = input('Qual o id do post? ')

            return Comment(driver, postId)

        if flow == self.EXTRACT:
            userProfile = input('Qual perfil gostaria de extrair? ')
            maxFollowers = input('Qual a quantidade de seguidores? ')

            return ExtractFollowers(driver, userProfile, maxFollowers)
