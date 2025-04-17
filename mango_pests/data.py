from re import sub

# Custom Python class for pests/diseases
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
    # The name of the pest (Used for card and elsewhere)
    # cardtext: Text to be used for the card
    # image: the link to the image
    # detailedinfo: Information displayed on project_detail
    # symptoms: symptoms displayed. Must be a list of tuples
    # treatments: passed as a list, used in project_detail
    # urlslug is self-made by slugger function, used for neater URLs

    def __init__(self, cardtitle, cardtext, image, detailedinfo, symptoms, treatments):
        self.cardtitle = cardtitle
        self.cardtext = cardtext
        self.image = image
        self.detailedinfo = detailedinfo
        self.symptoms = symptoms
        self.treatments = treatments
        self.urlslug = self.slugger(cardtitle)

    # URL slugger method to convert cardtitle to URL-friendly slug
    def slugger(self, cardtitle):
        return sub(r'[^A-Za-z]+','-', cardtitle)

# Define each pest as an instance of Intrusion
Pest1 = Intrusion(
    'Queensland Fruit Fly (Bactrocera tryoni) & Jarvis’ Fruit Fly (Bactrocera jarvisi)',  # Title
    "Both species can infest many commercial and native fruits, posing a serious threat to production.",  # Brief description
    'images/pests/queensland-fruit-fly.png',  # Image path
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
    Information source:
    Northern Territory Government. (2010). *Field Guide to Pests, Beneficials, Diseases and Disorders of Mangoes*.""",  # Detailed description
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
        "Encourage natural predators or parasites where feasible"
    ]  # Treatments & preventative measures
)

Pest2 = Intrusion(
    'Anthracnose (Colletotrichum gloeosporioides)',  # Title
    "A common fungal disease affecting mango leaves, twigs, and fruit at various stages of growth.",  # Brief description
    'images/pests/anthracnose.png',  # Image path
    """Anthracnose may appear as small spots or larger brown-black lesions on leaves, stems, and fruit. Severe infections can lead to tip dieback and extensive fruit rot, both before and after harvest. High humidity, rainfall, and warm temperatures favor disease development. Spores can germinate within 24 hours in moist conditions, often overwintering in dead plant material and mummified fruit.
    Proper orchard hygiene—including pruning, removal of diseased fruit, and managing nutrition (particularly calcium) helps limit anthracnose outbreaks. Strategic fungicide applications (pre- and post-harvest) and careful post-harvest handling (ex., forced air cooling) are also recommended to reduce infection levels in fruit.
    Information source:
    Northern Territory Government. (2010). *Field Guide to Pests, Beneficials, Diseases and Disorders of Mangoes*.""",  # Detailed description
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
        "Maintain overall orchard hygiene to prevent reinfection"
    ]  # Control and management strategies
)

Pest3 = Intrusion(
    'Mango Fruit Borer (Citripestis eutraphera)',  # Title
    "A caterpillar pest that bores into mango fruit, causing internal damage and potential crop losses.",  # Brief description
    'images/pests/mango-fruit-borer.png',  # Image path
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
    Information source:
    Northern Territory Government. (2010). *Field Guide to Pests, Beneficials, Diseases and Disorders of Mangoes*.""",  # Detailed description
    [
        (SEVERITY_WARNING, "Wet-looking frass near stem end or between clustered fruits"),
        (SEVERITY_WARNING, "Small bore holes visible on fruit surface"),
        (SEVERITY_DANGER, "Larval tunneling causing fruit rot and internal breakdown"),
        (SEVERITY_DANGER, "Premature fruit drop with external signs of entry"),
    ],  # Symptoms
    [
        "Inspect fruit frequently for early signs of infestation",
        "Remove and destroy affected fruit to reduce larval spread",
        "Apply appropriate insecticides during early larval stages",
        "Maintain orchard hygiene and monitor fallen fruit",
        "Use pheromone or visual traps where applicable"
    ]  # Treatment & management
)


Pest4 = Intrusion(
    'Mealybugs (Planococcus citri & Ferrisia virgata)',  # Title
    "Sap-sucking pests that excrete honeydew, potentially leading to sooty mold on mango leaves and fruit.",  # Brief description
    'images/pests/mealy-bugs.png',  # image path
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

    Information source:
    Northern Territory Government. (2010). *Field Guide to Pests, Beneficials, Diseases and Disorders of Mangoes*.""",  # Detailed description
    [
        (SEVERITY_WARNING, "White or cottony masses on stems, leaves, or fruit"),
        (SEVERITY_WARNING, "Sticky honeydew attracting ants"),
        (SEVERITY_DANGER, "Sooty mold forming on honeydew-covered surfaces"),
        (SEVERITY_DANGER, "Significant yellowing, leaf drop, or fruit deformities"),
        (SEVERITY_WARNING, "Leaf Hoppers will be present in large numbers on the flowers & new leaf flushes"),
        (SEVERITY_WARNING, "Browning and Drying of Flowers"),
        (SEVERITY_DANGER, "Decreased percentage of fruit set and ultimately reduced production."),
    ],  # Symptoms with severity indicators
    [
        "Reduce ant populations that protect mealybugs for their honeydew",
        "Wash or wipe off small infestations with soapy water or horticultural oils",
        "Use systemic insecticides if populations are extensive",
        "Promote natural predators (e.g., lady beetles, parasitic wasps)",
        "Inspect regularly to catch and treat new infestations early",
        "Use of insecticidal soap or horticultural oils to target the pests",
        "Apply systemic insecticides to control mealybug populations",
        "Regularly remove infested branches and leaves",
        "Introduce natural predators like ladybugs or parasitic wasps"
    ]  # Combined symptoms and treatments
)


Pest5 = Intrusion(
    'Mango Stem Borer',  # Title
    """The Mango Stem Borer (Batocera rufomaculata sp.) has been observed to cause an alarming situation in old and young orchards, posing a significant threat to mango cultivation""",  # Brief description
    'images/pests/mango-stem-borer.jpg',  # image path
    """The mango stem borer is a serious pest, and the grub stage causes damage by cutting and biting fresh twigs and shoots. When a grub enters a shoot, it digs a tunnel inside the stem, causing the shoots to dry out. 
    Severe infestation affects the entire shoots and causes the tree to look like it has been burned, resulting in a significant reduction in yield. The pest's larvae live for a long time (about a year) and hibernate inside the dry shoot during the winter. 
    They activate and pupate as the weather warms up, and adults emerge and begin egg-laying during the autumn months.""",  # Detailed description
    [
        (SEVERITY_WARNING, "Tunnels can be found in the tree's periphery or deep within the trunk."),
        (SEVERITY_DANGER, "Early on, the damage is not evident, but the leaking of sticky fluid from various spots on the tree trunk and branches can be seen."),
        (SEVERITY_WARNING, "A limb or two begins to shed leaves and dry up."),
        (SEVERITY_DANGER, "A hole with seeping sap and frass on the bark are visible indications in advanced stages of illness."),
        (SEVERITY_WARNING, "Branches turn yellow, followed by drying and dieback of terminal shoots and branches."),
        (SEVERITY_DANGER, "Tree Death."),
    ],  # Symptoms combined with warning signs
    [
        "Destruction of infected branches",
        "Sanitation of orchard farm",
        "Extracting grubs.",
        "Integrated Pest Management Programs in Mango Orchards using Chemical and Biological Agents",
        "The orchard should be tilled or hoed three times during winter- 15cm deep in soil.",
        "Host-Plant Resistance - cultivating Mango species that are resistant to Stem Borer infestation",
        "Passing X-Rays through the trunk or stem of a Mango Tree."
    ]  # How to treat
)

Pest6 = Intrusion(
    'Bacterial Black Spot',  # Title
    """The Bacterial Black Spot can potentially be more damaging to flowers than Anthracnose.""",  # Brief description
    'images/pests/mango-bacterial-blight-disease-fruit.jpg',  # Location of image
    """The disease attacks through natural openings such as stomata, wax and oil glands, leaf and fruit abrasions, leaf scars, and at the apex of branches in the panicle. Damage by adverse environmental conditions such as frost and wind can also create sites for infection. 
    In young trees, the disease can cause dieback of branches.""",  # Detailed description
    [
        (SEVERITY_WARNING, "Leaf lesions consist of black, raised, angular areas, restricted by the veins and frequently surrounded by a yellow margin."),
        (SEVERITY_DANGER, "Elongated stem cankers occur on the bark and can cause terminal dieback."),
        (SEVERITY_WARNING, "Fruit lesions consist of individual or multiple star-shaped cracks, often appearing with anthracnose lesions in a tearstain pattern."),
        (SEVERITY_DANGER, "Unlike anthracnose, bacterial lesions do not expand as the fruit ripen."),
    ],  # Symptoms combined with warning signs
    [
        "From pinnacle emergence, apply copper fungicide registered for control of bacterial leaf spot every three weeks.",
        "From fruit set until harvest, copper fungicide every 14–28 days depending on the weather. In dry seasons, fewer sprays are needed, saving time and pesticide.",
        "New flush growth should be sprayed during autumn. This prevents a build-up of disease on young foliage.",
        "Postharvest treatments will not provide complete disease control. It is important to follow field spray recommendations to reduce the level of postharvest disease",
        "Cool fruit promptly following harvest.",
        "Site selection and planting density are important in disease control.",
        "Pruning trees is extremely important. This should be done to remove all sources of inoculum and to maximize air circulation and penetration of sunlight.",
        "Apply fertilizer sparingly and with caution."
    ]  # How to treat
)

Pest7 = Intrusion(
    'Sooty Mould',  # Title
    """Capnodium mangiferum (mango) Many plants develop sooty moulds when colonised by insects that produce honeydew, e.g., coconut, guava, mango, soursop and ornamentals, e.g., Frangipani.""",  # Brief description
    'images/pests/mango-bacterial-blight-disease-leaves.jpg',  # Location of image
    """Sooty moulds do not attack plants. The fungi that cause sooty moulds grow on the sugary substances that are produced by insects - mostly, aphids, soft scale (not armoured scale), leafhoppers, planthoppers, psyllids and whiteflies - as they suck the sap of plants. The secretions are known as 'honeydew'. The fungi that grow on honeydew reduce the plants ability to photosynthesise and this may stunt growth, cause leaves to yellow and die early, and may reduce the quality of fruit.""",  # Detailed description
    [
        (SEVERITY_WARNING, "Black Velvety Thin Membranous covering on the leaf blade. The entire leaf blade is covered or it may be only as flakes on the leaf."),
        (SEVERITY_DANGER, "In severe cases, the tree completely turns black with mould on the entire surface of twigs and leaves."),
        (SEVERITY_WARNING, "The affected leaves curl and shrivel under dry conditions."),
        (SEVERITY_DANGER, "The fungus multiplies on the ‘honey dew’ secreted by the insects and spreads on the plant surface, making it black and ugly owing to the masses of black spores on the leaf surface. The severity of incidence is dependent upon the sugary secretion by the insects."),
        (SEVERITY_WARNING, "During flowering time, its attack results in reduced fruit set and sometimes causes fruit fall. It is also noticed on fruits of late mango varieties"),
    ],  # Symptoms combined with warning signs
    [
        "Pour Hot Water over Ants Nests that are close to Mango Trees",
        "Prune Branches to prevent access for Ants and other harmful Insects",
        "Use Soap Sprays to kill Sap Sucking Insects",
        "Use Oil and Dishsoap Spray on Infested Leaves",
        "Synthetic pyrethroid insecticides to kill ants; these insecticides may also be tried against scale insects as they are likely to be effective against the crawlers - crawlers are the active nymphs which spread infestations to new plants and/or new gardens."
    ]  # How to treat
)


Pestsdiseases = [Pest1, Pest2, Pest3, Pest4, Pest5, Pest6, Pest7]