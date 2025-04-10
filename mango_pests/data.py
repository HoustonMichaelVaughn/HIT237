from re import sub
# Custom Python class for pests/dieaseas
#   Sources:
#   https://www.w3schools.com/python/python_classes.asp
#   https://www.w3schools.com/python/python_file_open.asp
#   https://www.w3schools.com/django/django_slug_field.php
#   TO-DO:
#   Possibly implement django model of generating slugs? See above source
#   Investigate what will happen if images are made more responsive?


class Intrusion:
    #   I don't we are allowed to use Django models for this class so I've made manually made
    #   a url slug generator that way it's much nicer than %20,%20, etc
    #   cardtitle: The name of the pest (Used for card and else where)
    #   cardtext: Text to be used for the card
    #   image: the link to the image (Might be refactored to make it more responsive)
    #   detailedinfo: Information displayed on project_detail
    #   symptoms: symptoms displayed. Must be dictionary to indicate level
    #   treatments: passed as a list, used in project_detail
    #   urlslug is self made by slugger function, used for neater URLs

    def __init__(self, cardtitle, cardtext, image, detailedinfo, symptoms, treatments):
        self.cardtitle = cardtitle
        self.cardtext = cardtext
        self.image = image
        self.detailedinfo = detailedinfo
        self.symptoms = symptoms 
        self.treatments = treatments
        self.urlslug = self.slugger(cardtitle)

    def dictionaryconstruct(self):
         return{"cardtitle": self.cardtitle,
             "cardtext": self.cardtext,
             "image": self.image,
             "detailedinfo": self.detailedinfo,
             "urlslug": self.urlslug,
             "symptoms": self.symptoms,
             "treatments": self.treatments}
    
    def slugger(self, cardtitle):
        return sub(r'[^A-Za-z]+','-',cardtitle)


MikeZebrowski = Intrusion(
    'A wild Mike Zebrowski',
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""",
    'images/pests/temporary-zebrowski.jpg',
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap, 
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""",
    {"warning":"Sticky honeydew secretion on leaves, branches, and fruit",
     "danger":"Presence of sooty mold growing on the honeydew", 
     "warning":"Yellowing or wilting of leaves", 
     "danger":"Deformed and scarred fruit"},
    ["Use of insecticidal soap or horticultural oils to target the pests", "Apply systemic insecticides to control mealybug populations",
     "Regularly remove infested branches and leaves", "Introduce natural predators like ladybugs or parasitic wasps"]
)


Pestsdiseases = [MikeZebrowski]
