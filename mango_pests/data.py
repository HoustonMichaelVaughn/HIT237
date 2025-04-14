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
    'A wild Mike Zebrowski', # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""", # Brief description
    'images/pests/temporary-zebrowski.jpg', # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""", # Detailed description
    [
    (SEVERITY_WARNING, "Sticky honeydew secretion on leaves, branches, and fruit"),
    (SEVERITY_DANGER, "Presence of sooty mold growing on the honeydew"),
    (SEVERITY_WARNING, "Yellowing or wilting of leaves"),
    (SEVERITY_DANGER, "Deformed and scarred fruit"),
    ], # Symptoms combined with warning signs
    ["Use of insecticidal soap or horticultural oils to target the pests", "Apply systemic insecticides to control mealybug populations",
     "Regularly remove infested branches and leaves", "Introduce natural predators like ladybugs or parasitic wasps"] # How to treat
)

Pest2 = Intrusion(
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

Pest3 = Intrusion(
    'Mango fruit fly', # Title
    """Fruit flies are particularly detrimental to mango production and marketing, as they can inflict losses ranging from 5% to 80% in mango crops, with severe cases exceeding 90% damage. 
    Furthermore, fruit flies pose challenges for the export of fresh fruits and vegetables, often causing damage during post-harvest processes as well.""", # Brief description
    'mango_pests/static/images/pests/Mango Fruit Fly 1.jpg',
    'mango_pests/static/images/pests/Mango Fruit Fly.jpg',# Location of image
    """The female insect uses its pointed ovipositor to puncture the outer wall of mature fruits, inserting eggs in small clusters within the mesocarp. After about 1-2 days, the eggs hatch. 
    Upon hatching, the maggots feed on the fruit pulp for a duration of 8-10 days, leading to the rotting of infested fruits due to subsequent secondary infections. After this feeding period, 
    the maggots pupate at a depth of 10-15 cm below the soil for approximately one week. Once they emerge as adults, they can live for up to 45 days, at which point the lifecycle continues.""", # Detailed description
    [
    ("warning", "Puncture holes are seen on the fruit and will be soft near the puncture points, sometimes oozing liquid can be seen around the dimples"),
    ("danger",  "Pulp is converted into a bad- smelling, discoloured semi-liquid mass"),
    ("warning", " Fruit will develop large, sunken brown patches or even open wounds"),
    ("danger",  "Fruit will drop prematurely"),
    ], # Symptoms combined with warning signs
    ["Collect fallen-infested rotten fruits and remove fruits with Ovi-punctures and oozing clear sap from the trees if visible at weekly intervals.", 
     "Pick overripe fruits as these are good breeding sites for fruit flies.",
     "Plough the topsoil (5-10 cm deep) to expose the pupae to predators, parasites, and direct sunlight.",
     "Destroy these collected fruits by dumping them in a pit (40-60 cm deep) and cover with soil to eliminate all sources of possible breeding sites.", 
     "The harvested fruits may be treated with hot water for 1 hour at 48oC."] # How to treat
)

Pest4 = Intrusion(
    'Mango Hoppers', # Title
    """There are number of insect pests damaging mango tree but the most important pest that plays a major role in bringing down the fruit yield & loss is the Mango Leaf Hopper.""", # Brief description
    'mango_pests/static/images/pests/Mango Leaf Hopper.jpg', # Location of image
    """Mango Hoppers are wedge shaped insects with golden-brown or dark-brown in colour. The insects look rather like a small cicada. 
    When disturbed, the adults jump off the plant with a clicking sound, fly a short distance & quickly resettle on the plant. The nymphs are greenish with black or brown margins, cannot fly & move rapidly on the plant. 
    The adult insects are often found lined up along the stages of developing fruits. Leaf Hoppers suck the sap from both flowers & young leaves. The leaf hopper lay eggs during flowering & fruiting period into the underside of the midrib of young leaves.
    It is a notorious pest, the insect may survive throughout the year by hiding on the tree trunk.""", # Detailed description
    [
    ("warning", "Leaf Hoppers will be present in large numbers on the flowers & new leaf flushes"),
    ("warning", "Browning and Drying of Flowers"),
    ("danger", "Decreased percentage of fruit set and ultimately reduced production."),
    ], # Symptoms combined with warning signs
    ["Collect and discard the infested plant parts and affected fruits.",
     "Proper Orchard or Farm Maintainance should be observed clean cultivation. Regularly weed orchards because the insect prefers poorly managed orchards.", 
     "Maintain wider spacing, between the plants and ensure proper penetration of sunlight within the orchards.",] # How to treat
)


Pest5 = Intrusion(
    'Mango Stem Borer', # Title
    """The Mango Stem Borer (Batocera rufomaculata sp.) has been observed to cause an alarming situation in old and young orchards, posing a significant threat to mango cultivation""", # Brief description
    'mango_pests/static/images/pests/Mango Stem Borer.jpg', # Location of image
    """The mango stem borer is a serious pest,and the grub stage causes damage by cutting and biting fresh twigs andshoots. When a grub enters a shoot, it digs a tunnel inside the stem, causingthe shoots to dry out. 
    Severe infestation affects the entire shoots and causes the tree to look like it has been burned, resulting in a significant reduction in yield. The pest's larvae live for a long time (about a year) and hibernate inside the dry shoot during the winter. 
    They activate and pupate within as the weather warms up, and adults emerge and begin egg laying during Autumn months.""", # Detailed description
    [
    ("warning", "Tunnels can be found in the tree's periphery or deep within the trunk."),
    ("danger", "Early on, the damage is not evident, but the leaking of sticky fluid from various spots on the tree trunk and branchescan be seen."),
    ("warning", "A limb or two begins to shed leaves and dry up."),
    ("danger", " A hole with seeping sap and frass on the barkare visible indications in advanced stages of illness."),
    ("warning","Branches to turn yellow, followed by drying and dieback of terminal shootsand branches."),
    ( "danger", "Tree Death."), 
    ], # Symptoms combined with warning signs
    ["Destruction of infected branches", 
     "Sanitation of orchard farm",
     "Extracting grubs.", 
     "Integrated Pest Management Programs in Mango Orchards using Chemical and Biological Agents" ,
     "The orchard should be tilled or hoed three times during winter- 15cm deep in soil.",
     "Host-Plant Resistance- cultivating Mango species that are resistant to Stem Borer infestation",
     "Passing X-Rays through the trunk or stem of a Mango Tree."] # How to treat
)

Pest6 = Intrusion(
    'Bacterial Black Spot', # Title
    """The Bacterial Black Spot can potentially be more damaging to flowers than Anthracnose.""", # Brief description
    'mango_pests/static/images/pests/Mango Bacterial Blight Disease Fruit.jpg', # Location of image
    """The disease attacks through natural openings such as stomata, wax and oil glands, leaf and fruit abrasions, leaf scars, and at the apex of branches in the panicle. Damage by adverse environmental conditions such as frost and wind can also create sites for infection. 
    In young trees the disease can cause dieback of branches.""", # Detailed description
    [
    ("warning", "Leaf lesions consist of black, raised, angular areas, restricted by the veins and frequently surrounded by a yellow margin."),
    ("danger", "Elongated stem cankers occur on the bark and can cause terminal dieback."),
    ("warning", "Fruit lesions consist of individual or multiple star-shaped cracks, often appearing with anthracnose lesions in a tearstain pattern."),
    ("danger", "Unlike anthracnose, bacterial lesions do not expand as the fruit ripen."),
    ], # Symptoms combined with warning signs
    ["From pinnacle emergence, apply copper fungicide registered for control of bacterial leaf spot every three weeks.",
     "From fruit set until harvest, copper fungicide every 14–28 days depending on the weather. In dry seasons fewer sprays are needed, saving time and pesticide.",
     "New flush growth should be sprayed during autumn. This prevents a build-up of disease on young foliage. ", 
     "Postharvest treatments will not provide complete disease control. It is important to follow field spray recommendations to reduce the level of postharvest disease", 
     "Cool fruit promptly following harvest.",
     " Site selection and planting density are important in disease control.", 
     " Pruning trees is extremely important. This should be done to remove all sources of inoculum and to maximise air circulation and penetration of sunlight.",
     " Apply fertiliser sparingly and with caution."] # How to treat
)

Pest7 = Intrusion(
    'Sooty Mould', # Title
    """Capnodium mangiferum (mango) Many plants develop sooty moulds when colonised by insects that produce honeydew, e.g., coconut, guava, mango, soursop and ornamentals, e.g., Frangipani.""", # Brief description
    'mango_pests/static/images/pests/Mango Bacterial Blight Disease Leaves.jpg', # Location of image
    """Sooty moulds do not attack plants. The fungi that cause sooty moulds grow on the sugary substances that are produced by insects - mostly, aphids, soft scale (not armoured scale), leafhoppers, planthoppers, psyllids and whiteflies - as they suck the sap of plants. The secretions are known as 'honeydew'. The fungi that grow on honeydew reduce the plants ability to photosynthesise and this may stunt growth, cause leaves to yellow and die early, and may reduce the quality of fruit.""", # Detailed description
    [
    ("warning", "Black Velvety Thin Membranous covering on the leaf blade. The entire leaf blade is covered or it may be only as flakes on the leaf."),
    ("danger", "In severe cases, the tree completely turns black with mould on entire surface of twigs and leaves."),
    ("warning", "The affected leaves curl and shrivel under dry conditions."),
    ("danger", "The fungus multiplies on the ‘honey dew’ secreted by the insects and spreads on the plant surface making it black and ugly owing to the masses of black spores on the leaf surface. The severity of incidence is dependent upon the sugary secretion by the insects."),
    ("warning", "During flowering time, its attack results in reduced fruit set and sometimes causes fruit fall. It is also noticed on fruits of late mango varieties")
    ], # Symptoms combined with warning signs
    ["Pour Hot Water over Ants Nests that are close to Mango Trees", "Prune Branches to prevent access for Ants and other ahrmful Insects",
     "Use Soap Sprays to kill Sap Sucking Insects", "Use Oil and Dishsoap Spray on Infested Leaves", "Synthetic pyrethroid insecticides to kill ants; these insecticides may also be tried against scale insects as they are likely to be effective against the crawlers - crawlers are the active nymphs which spread infestations to new plants and/or new gardens."] # How to treat
)




Pestsdiseases = [Pest1,Pest2,Pest3,Pest4,Pest5,Pest6,Pest7]
