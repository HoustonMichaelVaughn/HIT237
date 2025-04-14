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
        return sub(r"[^A-Za-z]+", "-", cardtitle)


Pest1 = Intrusion(
    "Queensland Fruit Fly (Bactrocera tryoni) & Jarvis’ Fruit Fly (Bactrocera jarvisi)",  # Title
    "Both species can infest many commercial and native fruits, posing a serious threat to production.",  # Brief description
    "images/pests/queensland-fruit-fly.png",  # AI-generated PNG image
    """Eggs:
- Off-white in colour, about 1 mm long.

Larvae (Immatures):
- Pale (white to cream) maggots with a dark, hook-like feeding mouthpart.
- Can reach about 8 mm in length.

Adults:
- Typically exhibit red-brown or yellow-brown coloration with notable yellow markings.
- Usually measure 9–10 mm long.

Life Cycle:
- Females lay small clusters of roughly 6–10 eggs just under the fruit’s skin.
- Eggs hatch in ~1–2 days; larvae feed for around a week before pupating.
- Adults emerge after 10–12 days in the pupal stage and can live for several months if conditions allow.

Damage:
- Sting or puncture marks on fruit surface.
- Larvae tunnel through pulp, causing premature fruit drop and decay.
- Fruits nearing ripeness are at higher risk of infestation.

Management & Control:
- Observe ICA (Interstate Certification Assurance) rules for moving produce.
- Remove and destroy fallen fruit to limit breeding.
- Monitor with traps; note male lures alone do not eradicate the population.
- Use bait sprays or other approved pest control methods as needed.

Disclaimer:
Information is based on common best practices and may vary with local conditions.

Image Note:
This image is **AI-generated** for educational illustration, based on the original **public domain photograph (Image No. K9588-6) by Scott Bauer,
 USDA Agricultural Research Service**. Actual species appearance may vary.

Information source:
Northern Territory Government. (2010). *Field Guide to Pests, Beneficials, Diseases and Disorders of Mangoes*. 
Department of Resources, Darwin, NT (ISBN 978-0-7245-7200-7).
""",  # Detailed description
    [
        (SEVERITY_WARNING, "Small sting or puncture marks on fruit surface"),
        (SEVERITY_DANGER, "Larval tunneling and fruit decay"),
        (SEVERITY_WARNING, "Discolouration or soft patches on fruit"),
        (SEVERITY_DANGER, "Potential for secondary infections in damaged tissue"),
    ],  # Symptoms
    [
        "Maintain orchard hygiene by removing infested or fallen fruit",
        "Monitor adult populations using lure traps",
        "Use bait sprays and approved pesticides in high-risk periods",
        "Adhere to ICA regulations and quarantine requirements",
        "Encourage natural predators or parasites where feasible",
    ],  # Treatments & preventative measures
)

Pest2 = Intrusion(
    "Anthracnose (Colletotrichum gloeosporioides)",  # Title
    "A common fungal disease affecting mango leaves, twigs, and fruit at various stages of growth.",  # Brief description
    "images/diseases/anthracnose.png",  # Image
    """Anthracnose may appear as small spots or larger brown-black lesions on leaves, stems, and fruit. 
Severe infections can lead to tip dieback and extensive fruit rot, both before and after harvest. 
High humidity, rainfall, and warm temperatures favor disease development. Spores can germinate 
within 24 hours in moist conditions, often overwintering in dead plant material and mummified fruit.

Proper orchard hygiene—including pruning, removal of diseased fruit, and managing 
nutrition (particularly calcium) helps limit anthracnose outbreaks. Strategic fungicide 
applications (pre- and post-harvest) and careful post-harvest handling (ex., forced air cooling) 
are also recommended to reduce infection levels in fruit.

Information source:
Northern Territory Government. (2010). Field Guide to Pests, Beneficials, Diseases and Disorders of Mangoes. 
Department of Resources, Darwin, NT (ISBN 978-0-7245-7200-7).""",  # Source Detailed description
    [
        (SEVERITY_WARNING, "Small dark lesions on leaves or fruit surface"),
        (SEVERITY_WARNING, "Leaf spots coalescing, causing partial defoliation"),
        (SEVERITY_DANGER, "Black or brown spreading lesions on mature fruit"),
        (SEVERITY_DANGER, "Twig dieback and potential fruit drop"),
    ],  # Symptoms combined with severity indicators
    [
        "Prune and dispose of infected twigs, leaves, and fruit to reduce spore reservoirs",
        "Apply recommended pre- and post-harvest fungicides at critical times",
        "Manage orchard conditions (humidity, nutrition) to reduce disease pressure",
        "Use forced air cooling (13–20°C) post-harvest to slow fungal development",
        "Maintain overall orchard hygiene to prevent reinfection",
    ],  # Control and management strategies
)

Pest3 = Intrusion(
    "Mango Fruit Borer (Citripestis eutraphera)",  # Title
    "A caterpillar pest that bores into mango fruit, causing internal damage and potential crop losses.",  # Brief description
    "images/pests/mango-fruit-borer.png",  # PNG format
    """Eggs:
- Typically laid near the stem end of fruit or where two fruits touch.
- Start off white and turn red by the second day, measuring around 1 mm.

Larvae (Immatures):
- Pale pink at first with a dark head, maturing into pinkish-brown or reddish caterpillars.
- Often develop dark bands across the body and can reach up to 15 mm in length.

Adults:
- Dark brown forewings, lighter hindwings with grey borders.
- Wing span is around 24 mm in females and 20 mm in males.

Life Cycle:
- Eggs hatch in 2–3 days.
- Larvae feed for about 14 days before pupating.
- Adults emerge after another 14 days and live for up to 10 days.

Damage:
- Larvae bore into fruit after initial surface feeding, often leaving wet frass near the entry point.
- Internal tunneling causes decay, fruit drop, and makes fruit unmarketable.

Monitoring & Management:
- Check fruit (including fallen ones) for entry holes or visible frass.
- Remove infested fruit immediately to reduce spread.
- Use targeted insecticides if infestations are severe, especially at early larval stages.

Image Note:
This image is AI-generated for educational illustration purposes. It is based on real symptoms of the mango fruit borer (*Citripestis eutraphera*), 
but actual species appearance and damage may vary in natural conditions.

Information source:
Northern Territory Government. (2010). *Field Guide to Pests, Beneficials, Diseases and Disorders of Mangoes*. 
Department of Resources, Darwin, NT (ISBN 978-0-7245-7200-7).
""",  # Detailed description
    [
        (
            SEVERITY_WARNING,
            "Wet-looking frass near stem end or between clustered fruits",
        ),
        (SEVERITY_WARNING, "Small bore holes visible on fruit surface"),
        (SEVERITY_DANGER, "Larval tunneling causing fruit rot and internal breakdown"),
        (SEVERITY_DANGER, "Premature fruit drop with external signs of entry"),
    ],  # Symptoms
    [
        "Inspect fruit frequently for early signs of infestation",
        "Remove and destroy affected fruit to reduce larval spread",
        "Apply appropriate insecticides during early larval stages",
        "Maintain orchard hygiene and monitor fallen fruit",
        "Use pheromone or visual traps where applicable",
    ],  # Treatment & management
)

Pest4 = Intrusion(
    "Mealybugs (Planococcus citri & Ferrisia virgata)",  # Title
    "Sap-sucking pests that excrete honeydew, potentially leading to sooty mold on mango leaves and fruit.",  # Brief description
    "images/pests/mealybugs.png",  # PNG image path updated
    """Eggs:
- Often pink, oval-shaped, and laid in a cottony mass.

Immatures (Crawlers & Juveniles):
- Citrus mealybug juveniles: Yellowish, oval, and mobile yet smaller than adults.
- Striped mealybug juveniles: Yellow with a powdery coating; stripes become more apparent as they mature.

Adults:
- Citrus mealybug females: Wingless, oval, covered in white, filamentous wax on the body edges (males are small and winged).
- Striped mealybug females: Typically show two dark stripes on the back, encased in a white waxy coating with long, white filaments on the edges and tails.
- Adult sizes range from about 2–5 mm.

Life Cycle:
- Eggs hatch within 1–2 days. Crawlers search for feeding sites on stems, leaves, or fruit.
- They molt through several stages before becoming adults, taking up to about 42 days from egg to maturity.
- Males do not feed once they have wings and primarily serve for reproduction.

Damage:
- Mealybugs feed on sap from leaves, flowers, stems, and fruit, causing stunted growth, yellowing or leaf/fruit drop.
- Infested plant surfaces may develop white waxy deposits and become prone to sooty mold (due to honeydew secretions).
- Ants often protect mealybugs, feeding on their honeydew.

Management:
- Monitor for mealybug presence in fruit and on leaf undersides.
- Prune heavily infested branches.
- Use insecticidal soap or systemic insecticides for high infestation levels.

Information source:
Northern Territory Government. (2010). *Field Guide to Pests, Beneficials, Diseases and Disorders of Mangoes*. 
Department of Resources, Darwin, NT (ISBN 978-0-7245-7200-7).
""",  # Detailed description
    [
        (SEVERITY_WARNING, "Sticky honeydew secretion on leaves, branches, and fruit"),
        (SEVERITY_WARNING, "Yellowing or wilting of leaves"),
        (SEVERITY_DANGER, "Deformed and scarred fruit"),
        (SEVERITY_DANGER, "Presence of sooty mold growing on honeydew"),
    ],  # Symptoms
    [
        "Use insecticidal soap or horticultural oils to target the pests",
        "Apply systemic insecticides to control mealybug populations",
        "Regularly remove infested branches and leaves",
        "Introduce natural predators like ladybugs or parasitic wasps",
    ],  # Treatments & Control methods
)


Pest5 = Intrusion(
    "A wild Mike Zebrowski",  # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""",  # Brief description
    "images/pests/temporary-zebrowski.jpg",  # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""",  # Detailed description
    [
        ("warning", "Sticky honeydew secretion on leaves, branches, and fruit"),
        ("danger", "Presence of sooty mold growing on the honeydew"),
        ("warning", "Yellowing or wilting of leaves"),
        ("danger", "Deformed and scarred fruit"),
    ],  # Symptoms combined with warning signs
    [
        "Use of insecticidal soap or horticultural oils to target the pests",
        "Apply systemic insecticides to control mealybug populations",
        "Regularly remove infested branches and leaves",
        "Introduce natural predators like ladybugs or parasitic wasps",
    ],  # How to treat
)

Pest6 = Intrusion(
    "A wild Mike Zebrowski",  # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""",  # Brief description
    "images/pests/temporary-zebrowski.jpg",  # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""",  # Detailed description
    [
        ("warning", "Sticky honeydew secretion on leaves, branches, and fruit"),
        ("danger", "Presence of sooty mold growing on the honeydew"),
        ("warning", "Yellowing or wilting of leaves"),
        ("danger", "Deformed and scarred fruit"),
    ],  # Symptoms combined with warning signs
    [
        "Use of insecticidal soap or horticultural oils to target the pests",
        "Apply systemic insecticides to control mealybug populations",
        "Regularly remove infested branches and leaves",
        "Introduce natural predators like ladybugs or parasitic wasps",
    ],  # How to treat
)

Pest7 = Intrusion(
    "A wild Mike Zebrowski",  # Title
    """Mike Zebrowski is a figment of my imagination. 
    It was the first royalty free image that I could find to use a temporary placeholder for images.""",  # Brief description
    "images/pests/temporary-zebrowski.jpg",  # Location of image
    """The mango mealybug is a common pest that affects mango trees, causing significant damage to both the fruit and foliage. 
    These pests secrete a waxy coating that protects them while they feed on the plant's sap,  
    weakening the tree and promoting the growth of sooty mold. 
    Mango mealybugs are typically found in clusters on the leaves, branches, and fruits of mango trees.""",  # Detailed description
    [
        ("warning", "Sticky honeydew secretion on leaves, branches, and fruit"),
        ("danger", "Presence of sooty mold growing on the honeydew"),
        ("warning", "Yellowing or wilting of leaves"),
        ("danger", "Deformed and scarred fruit"),
    ],  # Symptoms combined with warning signs
    [
        "Use of insecticidal soap or horticultural oils to target the pests",
        "Apply systemic insecticides to control mealybug populations",
        "Regularly remove infested branches and leaves",
        "Introduce natural predators like ladybugs or parasitic wasps",
    ],  # How to treat
)


Pestsdiseases = [Pest1, Pest2, Pest3, Pest4, Pest5, Pest6, Pest7]
