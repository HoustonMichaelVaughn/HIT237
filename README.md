The HIT237 project has been redesigned for comfort and utility

To get started install requirements via requirements.txt (VERY IMPORTANT STEP)
Then from a terminal in mango_pests_project folder run:
python setup/setup.py
Click setup to complete the setup of the HIT237 project
Admin user will be created. User=admin, Pass=admin. 10 survielance records will be generated.
Enjoy!

The HIT237 project strives to meet and excel in all required features.

1. Full CRUD Functionality
   This requirement is demonstrated through the implementation of three models. FarmBlock, Pest and Pest check. They use a foreign key to FarmBlocks to the correct user and PestCheck to the FarmBlock and the relevant Pest being checked for.
   
2. ModelForms with Validation
   FarmBlockForm, PestCheckForm among others are used to obtain user input through validation logic. To demonstrat this, Pest selection is validated contextually dependent upon whether the pest in question is a custom made pest (in which case it will reside in then database) or whether it is a static pest that has been reused from Objective 1.
   
3. Multi-User Support
   User authenticiation is required through the deployment of @login_required. Data is servered dependent on what user is logged in and views only return objects that are owned by the signed in user.
   
4. Histroical Data Tracking
   Any surveillance results are kept within the PestCheck model. These records are accesible through the profile view for review.

The number of plants on the grower’s property:
The "How many trees should I check?" tool helps guide growers in knowning how many trees need to checked to reach a level of confidence.
How many trees the grower has is also used in the calculations of prevalence and confidence.

Location of the surveyed plant:
The FarmBlock creation tool allows growers to create specific FarmBlocks and add notes regarding their location.

The time of surveillance:
The time of surveillance is recorded as a date time in the database.

The tool needs to be flexible enough to be expanded to other types of plants in the future:
The project has been built with an vague "Plant Type" and can easily be extended beyond just simply 'mangos'

The tool will be used by growers who are generally aged between 40 and 60 years old:
The U.I has been desinged to be easy to use and that there is a consistent load out through the webpage. The implementation of HTMX and AJAX was cruical in building a website that is responsive
and does not reload every time a button is hit, minmising navigation paths.

Different pests/diseases may infect different parts of a plant, so the tool should consider surveillance of different parts of the plant:
The different part of plant can be recorded through the PestCheck creation, whether it is on the leaf or any other part of the plant.

Different farms may have different stocking rates:
The stocking rate can be entered in the creation of a FarmBlock and is used in the calculation of the required surveillance.

The surveillance data should be able to record surveillance results by different growers and maintain historical surveillance data:
Surveillance data is actively stored in the database and can be perused from the profile page.
