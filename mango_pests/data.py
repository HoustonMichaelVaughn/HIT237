from re import sub
# Custom Python class for pests/dieaseas
#   Sources:
#   https://www.w3schools.com/python/python_classes.asp
#   https://www.w3schools.com/python/python_file_open.asp
#   https://www.w3schools.com/django/django_slug_field.php
#   TO-DO:
#   Possibly implement django model of generating slugs? See above source


class Intrusion:
    #   I don't we are allowed to use Django models for this class so I've made manually made
    #   a url slug generator that way it's much nicer than %20,%20, etc
    def __init__(self, cardtitle, cardtext, image, detailedinfo):
        self.cardtitle = cardtitle
        self.cardtext = cardtext
        self.image = image
        self.detailedinfo = detailedinfo
        self.urlslug = self.slugger(cardtitle)

    def dictionaryconstruct(self):
         return{"cardtitle":self.cardtitle,
             "cardtext":self.cardtext,
             "image":self.image,
             "detailedinfo": self.detailedinfo,
             "urlslug": self.urlslug}
    
    def slugger(self, cardtitle):
        return sub(r'[^A-Za-z]+','-',cardtitle)


MikeZebrowski = Intrusion(
    'A wild Mike Zebrowski',
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""",
    'images/pests/temporary-zebrowski.jpg',
    """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras ac faucibus leo. Morbi id tristique leo. 
    Nullam et tempor nibh, nec pharetra diam. Mauris auctor, justo et pulvinar sollicitudin, dolor metus eleifend purus, 
    sed congue turpis lectus at eros. Sed placerat malesuada neque, vitae tincidunt quam varius vel. 
    Pellentesque porta nunc eget auctor fermentum. Integer vel molestie magna. 
    Aliquam ac lorem euismod, consectetur libero sed, lacinia ante. 
    Curabitur lobortis pretium eros, at laoreet nisi placerat a. Cras nec mi arcu. Nunc purus nunc, auctor sed eleifend non, 
    congue non elit. Etiam posuere sed purus in tincidunt. Nullam dignissim sit amet est dignissim porta. 
    Curabitur facilisis enim in lectus sodales euismod. Fusce in luctus felis. Ut eget turpis sit amet justo mollis semper. 
    Vestibulum sollicitudin eros tincidunt orci condimentum, non eleifend eros volutpat. Donec mollis convallis vulputate. 
    Curabitur dictum sed tellus ut pharetra. Lorem ipsum dolor sit amet, consectetur adipiscing elit.""")


Pestsdiseases = [MikeZebrowski]
