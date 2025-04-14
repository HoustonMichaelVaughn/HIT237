from re import sub
# Custom Python class for pests/dieaseas
#   Sources:
#   https://www.w3schools.com/python/python_classes.asp
#   https://www.w3schools.com/python/python_file_open.asp
#   https://www.w3schools.com/django/django_slug_field.php
#   TO-DO:
#   Possibly implement django model of generating slugs? See above source
#   Investigate what will happen if images are made more responsive?
SEVERITY_WARNING = "warning"
SEVERITY_DANGER = "danger"

class Intrusion:
    #   I don't think we are allowed to use Django models for this class so I've made manually made
    #   a url slug generator that way it's much nicer than %20,%20, etc
    #   cardtitle: The name of the pest (Used for card and else where)
    #   cardtext: Text to be used for the card
    #   image: the link to the image (Might be refactored to make it more responsive)
    #   detailedinfo: Information displayed on project_detail
    #   symptoms: symptoms displayed. Must be a list of tuples
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
    
    def slugger(self, cardtitle):
        return sub(r'[^A-Za-z]+','-',cardtitle)


Pest1 = Intrusion(
    'Mango anthracnose, mango blossom blight', # Title
    """Anthracnose means 'coal', so fungi that produce dark spots are often given this name. Glomerella cingulata (it also has the name of Colletotrichum gloeosporioides). 
    Glomerella is the sexual stage of the fungus, and Colletotrichum the asexual stage. """, # Brief description
    'mango_pests/static/images/pests/Mango Anthracnose Fruits.jpg',
    'mango_pests/static/images/pests/Mango Anthracnose Leaves.jpg',# Location of image
    """The fungus causes severe damage during wet weather. It causes a blight of flowers and young shoots, leaf spots, and fruit rots. 
   Young infected fruits develop black spots, shrivel and fall off. Spots of Glomerella are usually larger on the leaves.
   Primary Host is the mango but many other crops are hosts of this fungus, including avocado, capsicum, coffee, eggplant, papaya, tomato and yam.""", # Detailed description
    [
    (SEVERITY_WARNING, "Flower blights, and spots on young leaves and fruits in wet weather"),
    (SEVERITY_DANGER, "Low yield and Shoot dieback"),
    (SEVERITY_WARNING, "Early Leaf Fall"),
    (SEVERITY_DANGER, "Infection of mature fruit leads to losses in storage"),
    ], # Symptoms combined with warning signs
    ["Pruning of Trees to less than 4m tall- to facilitate air circulation and humidity reduction. Diseased branches should be burnt with fallen leaves.",
     "Propagation of Resistant Varieties- IndoChine/Philippine varieties have developed a level of Resistance to Anthracnose, 
     introduction of this Mango Species should be thoroughly studied.", 
     "In Australia, several fungicides are registered from the control of anthracnose, including mancozeb, copper (copper hydroxide, copper oxide, copper oxychloride or copper sulphate), 
     prochloraz, or azoxystrobin. See guide to their use: https://www.dpi.nsw.gov.au/__data/assets/pdf_file/0011/125876/mango-anthracnose-pf19.pdf)."] # How to treat
)

Pest2 = Intrusion(
    'Powdery Mildew', # Title
    """One of the dangerous pests that often appear during the mango budding season is powdery mildew. Powdery mildew is caused by the Oidium sp fungus. causes 
    the disease that affects mango trees of all ages, from gardens to commercial farms. """, # Brief description
    'mango_pests/static/images/pests/Mango Powdery Mildew.jpg', # Location of image
    """The disease often causes severe damage during the period when mango begins to produce buds, buds, flowers and young fruit from the winter season to early spring, 
    especially when the environment is cool, humid and foggy. When the leaves are at a light green stage, the disease can develop on the upper surface of the leaves. 
    In dense, humid garden conditions, the fungus also spreads to the old leaves, although these leaves are rarely dropped, but the fungal disease has greatly affected 
    the photosynthesis of the plant. """, # Detailed description
    [
    ("warning", "The entire affected part is covered with a white chalk powder, especially the bunch of young fruit buds."),
    ("danger", "The damaged young parts will then rot, dry out and fall off, severely affecting the mango yield."),
    ("warning", "When the disease is severe, the leaves will wrinkle, dry and fall."),
    ("danger", "The disease also slows down the growth rate, or can cause tree death"),
    ], # Symptoms combined with warning signs
    ["Select less susceptible varieties to plant.",
     "Conduct regular inspection and surveillance procedures during the stage of producing buds, flowers and young fruits to make appropriate and timely intervention 
     i.e. quarantine, culling or treatment.",
     "The procedure of spraying chemicals should be timely and efficient to prevent infection, i.e in gardens with high risk of infection, or mango orchards that had been affected in the previous season.",
     "Proper Planning i.e. tree spacing, irriation, pest deterring infrastructure, etc. of the mango orchard or mango farms ", 
     "Proper maintenance of mango orchards (diseased fallen should be collected and incenarated, or mixed with lime and buried).",
     "Use correct proportion of Fertilizer Components- increase the amount of potassium fertilizer, add extra calcium (SPC-Cal (Calcium nitrate)) to help improve the soil.",] # How to treat
)

Pest3 = Intrusion(
    'A wild Mike Zebrowski', # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""", # Brief description
    'images/pests/temporary-zebrowski.jpg', # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""", # Detailed description
    [
    ("warning", "Sticky honeydew secretion on leaves, branches, and fruit"),
    ("danger", "Presence of sooty mold growing on the honeydew"),
    ("warning", "Yellowing or wilting of leaves"),
    ("danger", "Deformed and scarred fruit"),
    ], # Symptoms combined with warning signs
    ["Use of insecticidal soap or horticultural oils to target the pests", "Apply systemic insecticides to control mealybug populations",
     "Regularly remove infested branches and leaves", "Introduce natural predators like ladybugs or parasitic wasps"] # How to treat
)

Pest4 = Intrusion(
    'A wild Mike Zebrowski', # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""", # Brief description
    'images/pests/temporary-zebrowski.jpg', # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""", # Detailed description
    [
    ("warning", "Sticky honeydew secretion on leaves, branches, and fruit"),
    ("danger", "Presence of sooty mold growing on the honeydew"),
    ("warning", "Yellowing or wilting of leaves"),
    ("danger", "Deformed and scarred fruit"),
    ], # Symptoms combined with warning signs
    ["Use of insecticidal soap or horticultural oils to target the pests", "Apply systemic insecticides to control mealybug populations",
     "Regularly remove infested branches and leaves", "Introduce natural predators like ladybugs or parasitic wasps"] # How to treat
)


Pest5 = Intrusion(
    'A wild Mike Zebrowski', # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""", # Brief description
    'images/pests/temporary-zebrowski.jpg', # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""", # Detailed description
    [
    ("warning", "Sticky honeydew secretion on leaves, branches, and fruit"),
    ("danger", "Presence of sooty mold growing on the honeydew"),
    ("warning", "Yellowing or wilting of leaves"),
    ("danger", "Deformed and scarred fruit"),
    ], # Symptoms combined with warning signs
    ["Use of insecticidal soap or horticultural oils to target the pests", "Apply systemic insecticides to control mealybug populations",
     "Regularly remove infested branches and leaves", "Introduce natural predators like ladybugs or parasitic wasps"] # How to treat
)

Pest6 = Intrusion(
    'A wild Mike Zebrowski', # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""", # Brief description
    'images/pests/temporary-zebrowski.jpg', # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""", # Detailed description
    [
    ("warning", "Sticky honeydew secretion on leaves, branches, and fruit"),
    ("danger", "Presence of sooty mold growing on the honeydew"),
    ("warning", "Yellowing or wilting of leaves"),
    ("danger", "Deformed and scarred fruit"),
    ], # Symptoms combined with warning signs
    ["Use of insecticidal soap or horticultural oils to target the pests", "Apply systemic insecticides to control mealybug populations",
     "Regularly remove infested branches and leaves", "Introduce natural predators like ladybugs or parasitic wasps"] # How to treat
)

Pest7 = Intrusion(
    'A wild Mike Zebrowski', # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""", # Brief description
    'images/pests/temporary-zebrowski.jpg', # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""", # Detailed description
    [
    ("warning", "Sticky honeydew secretion on leaves, branches, and fruit"),
    ("danger", "Presence of sooty mold growing on the honeydew"),
    ("warning", "Yellowing or wilting of leaves"),
    ("danger", "Deformed and scarred fruit"),
    ], # Symptoms combined with warning signs
    ["Use of insecticidal soap or horticultural oils to target the pests", "Apply systemic insecticides to control mealybug populations",
     "Regularly remove infested branches and leaves", "Introduce natural predators like ladybugs or parasitic wasps"] # How to treat
)




Pestsdiseases = [Pest1,Pest2,Pest3,Pest4,Pest5,Pest6,Pest7]
