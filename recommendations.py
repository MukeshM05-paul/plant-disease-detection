"""
Plant Disease Detection - Recommendations Knowledge Base
---------------------------------------------------------
This module provides curated, agricultural plant care recommendations
for all 38 plant disease classes supported by the model.

Each entry includes:
- Plant type
- Health status (Healthy vs Disease)
- Disease cause (Fungal, Bacterial, Viral, Pest, or None)
- Symptoms to verify
- Immediate corrective actions
- Long-term prevention strategies
"""

from typing import Dict, Any


RECOMMENDATIONS_DATABASE: Dict[str, Dict[str, Any]] = {
    # ------------------ APPLE ------------------
    "Apple Scab": {
        "plant": "Apple",
        "is_healthy": False,
        "cause": "Fungal (Venturia inaequalis)",
        "severity": "Moderate to High",
        "symptoms": [
            "Olive-green to brown velvety spots on leaf surface.",
            "Leaves may yellow, curl, and drop prematurely.",
            "Deformed, cracked, or corky scabs on fruit."
        ],
        "immediate_actions": [
            "Rake and destroy fallen leaves to remove the overwintering fungal spores.",
            "Prune canopy branches to improve air circulation and sunlight penetration.",
            "Apply a copper-based or sulfur-based organic fungicide during early spring growth."
        ],
        "prevention": [
            "Choose scab-resistant apple cultivars (e.g., Liberty, Freedom, Enterprise).",
            "Avoid overhead sprinkler irrigation; water directly at the root zone.",
            "Space trees properly to allow morning dew to dry rapidly."
        ]
    },
    "Apple with Black Rot": {
        "plant": "Apple",
        "is_healthy": False,
        "cause": "Fungal (Botryosphaeria obtusa)",
        "severity": "High",
        "symptoms": [
            "Frog-eye leaf spots (circular brown lesions with purple borders).",
            "Rotting fruit turning black with concentric rings.",
            "Bark cankers on branches and trunk."
        ],
        "immediate_actions": [
            "Prune out dead wood, twigs, and mummified fruits at least 6-8 inches below visible cankers.",
            "Sanitize pruning shears between cuts with 70% isopropyl alcohol.",
            "Apply an approved fungicide (captan or thiophanate-methyl) according to local extension guidelines."
        ],
        "prevention": [
            "Maintain overall tree vigor with balanced fertilizer; avoid excess nitrogen.",
            "Prevent bark injury from lawn equipment and cold damage.",
            "Inspect trees annually in late winter and prune out diseased shoots."
        ]
    },
    "Cedar Apple Rust": {
        "plant": "Apple",
        "is_healthy": False,
        "cause": "Fungal (Gymnosporangium juniperi-virginianae)",
        "severity": "Moderate",
        "symptoms": [
            "Bright orange-yellow circular spots on upper leaf surfaces.",
            "Small tube-like fruiting structures (aecia) on leaf undersides in summer.",
            "Premature defoliation during severe infections."
        ],
        "immediate_actions": [
            "Remove nearby Eastern red cedar or juniper trees within 1-2 miles if feasible.",
            "Apply preventative fungicides (myclobutanil or sulfur) when cedar galls are blooming in early spring.",
            "Rake and discard heavily infected foliage."
        ],
        "prevention": [
            "Plant rust-resistant apple varieties (e.g., Redfree, Dayton, William's Pride).",
            "Inspect nearby cedar evergreens for brownish-orange gelatinous galls.",
            "Maintain open canopy pruning to promote dry foliage."
        ]
    },
    "Healthy Apple": {
        "plant": "Apple",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Vibrant green leaves with no spotting or discoloration.",
            "Firm foliage with normal leaf expansion.",
            "No signs of wilting, fungal lesions, or pest damage."
        ],
        "immediate_actions": [
            "Maintain the current watering and nutrient schedule.",
            "Ensure the soil remains well-drained and slightly acidic (pH 6.0 - 7.0).",
            "Regularly monitor leaf undersides for early signs of aphids or mites."
        ],
        "prevention": [
            "Apply a 2-3 inch organic mulch layer around the drip line, keeping mulch away from trunk.",
            "Annual dormant pruning in late winter to maintain canopy light penetration.",
            "Soil testing every 2-3 years to calibrate fertilizer needs."
        ]
    },

    # ------------------ BLUEBERRY ------------------
    "Healthy Blueberry Plant": {
        "plant": "Blueberry",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Deep green leaves without yellowing or marginal scorching.",
            "Strong annual cane growth and healthy root system."
        ],
        "immediate_actions": [
            "Continue standard acidic soil maintenance (target pH 4.5 - 5.5).",
            "Keep soil consistently moist with 1-2 inches of water per week.",
            "Apply pine bark or pine needle mulch to preserve soil acidity and moisture."
        ],
        "prevention": [
            "Test soil pH regularly; adjust with elemental sulfur if pH rises above 5.5.",
            "Use drip irrigation rather than overhead sprinklers to prevent fungal leaf spot.",
            "Prune older canes (over 6 years old) to encourage productive new shoots."
        ]
    },

    # ------------------ CHERRY ------------------
    "Cherry with Powdery Mildew": {
        "plant": "Cherry",
        "is_healthy": False,
        "cause": "Fungal (Podosphaera clandestina)",
        "severity": "Moderate",
        "symptoms": [
            "White, powdery fungal patches on young leaves and succulent shoots.",
            "Leaves may curl upward, distort, and develop necrotic patches.",
            "Stunted terminal growth on new branches."
        ],
        "immediate_actions": [
            "Prune and discard infected terminal shoots showing heavy white powdery growth.",
            "Apply horticultural oil, potassium bicarbonate, or neem oil spray in low light conditions.",
            "Improve sunlight penetration by thinning the interior tree canopy."
        ],
        "prevention": [
            "Avoid excessive late-season nitrogen applications which promote vulnerable soft growth.",
            "Water early in the morning so tree foliage dries before sunset.",
            "Apply preventative sulfur sprays in early spring if history of powdery mildew is severe."
        ]
    },
    "Healthy Cherry Plant": {
        "plant": "Cherry",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Glossy, rich green foliage free of spots, holes, or mildew.",
            "Healthy bark without gumming or sunken cankers."
        ],
        "immediate_actions": [
            "Maintain regular deep watering during fruit development.",
            "Monitor for cherry fruit flies and birds as harvest approaches.",
            "Keep the tree base free of competing weeds and grass."
        ],
        "prevention": [
            "Prune during dry summer weather to avoid introducing bacterial canker.",
            "Ensure well-draining loam soil with a pH around 6.5.",
            "Maintain a steady layer of organic mulch around the root perimeter."
        ]
    },

    # ------------------ CORN (MAIZE) ------------------
    "Corn (Maize) with Cercospora and Gray Leaf Spot": {
        "plant": "Corn (Maize)",
        "is_healthy": False,
        "cause": "Fungal (Cercospora zeae-maydis)",
        "severity": "Moderate to High",
        "symptoms": [
            "Rectangular, tan-to-gray lesions restricted between leaf veins.",
            "Lesions expand and coalesce, causing entire leaves to scorch and die.",
            "Premature stalk lodging and reduced grain fill."
        ],
        "immediate_actions": [
            "In commercial fields, consider an approved triazole or strobilurin fungicide if threshold is reached before tasseling.",
            "Avoid working in wet fields to prevent spore dissemination.",
            "Mark heavily infected plots for post-harvest residue burial."
        ],
        "prevention": [
            "Plant resistant or tolerant maize hybrid varieties.",
            "Practice minimum 2-year crop rotation away from corn (e.g., rotate with soybeans).",
            "Till or manage crop residue to accelerate breakdown of overwintered fungal inoculum."
        ]
    },
    "Corn (Maize) with Common Rust": {
        "plant": "Corn (Maize)",
        "is_healthy": False,
        "cause": "Fungal (Puccinia sorghi)",
        "severity": "Low to Moderate",
        "symptoms": [
            "Small, oval to elongate cinnamon-brown pustules on both upper and lower leaf surfaces.",
            "Pustules rupture the epidermis, releasing powdery rust-colored spores.",
            "Leaves turn chlorotic and ragged under heavy infection."
        ],
        "immediate_actions": [
            "Fungicide treatment is rarely needed for field corn, but sweet corn may warrant application if rust appears early.",
            "Ensure plants receive balanced fertility, especially potassium."
        ],
        "prevention": [
            "Select rust-resistant hybrids containing Rp genes.",
            "Plant early in the season to avoid peak spore migration blown from southern regions.",
            "Maintain optimal plant spacing to maximize air movement."
        ]
    },
    "Corn (Maize) with Northern Leaf Blight": {
        "plant": "Corn (Maize)",
        "is_healthy": False,
        "cause": "Fungal (Exserohilum turcicum)",
        "severity": "High",
        "symptoms": [
            "Large, cigar-shaped grayish-green to tan lesions (1-6 inches long).",
            "Dark olive fungal spores visible in lesion centers during humid weather.",
            "Extensive leaf necrosis leading to substantial yield loss."
        ],
        "immediate_actions": [
            "Apply foliar fungicides if lesions appear on the ear leaf or higher before silking.",
            "Ensure adequate soil fertility to minimize plant stress."
        ],
        "prevention": [
            "Plant Northern Corn Leaf Blight (NCLB) resistant hybrids.",
            "Rotate crops annually with non-host crops like legumes.",
            "Shred and incorporate crop residue into the soil after harvest."
        ]
    },
    "Healthy Corn (Maize) Plant": {
        "plant": "Corn (Maize)",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Uniform dark green, broad arching leaves with crisp veins.",
            "Strong, upright central stalk with robust brace roots.",
            "Even tassel development and silk emergence."
        ],
        "immediate_actions": [
            "Maintain adequate soil moisture during the critical tasseling and silking stages.",
            "Apply nitrogen side-dressing according to growth stage and soil test recommendations."
        ],
        "prevention": [
            "Regular scout for early-season insect pests like armyworms or corn borers.",
            "Ensure weed management during the first 4-6 weeks of vegetative growth."
        ]
    },

    # ------------------ GRAPE ------------------
    "Grape with Black Rot": {
        "plant": "Grape",
        "is_healthy": False,
        "cause": "Fungal (Guignardia bidwellii)",
        "severity": "High",
        "symptoms": [
            "Small circular reddish-brown leaf spots with dark margins and tiny black specks.",
            "Infected berries shrivel into hard, black, wrinkled mummies.",
            "Black elongated lesions on shoots and tendrils."
        ],
        "immediate_actions": [
            "Remove and destroy all mummified berries from vines and ground.",
            "Prune infected canes back to healthy wood during dormancy.",
            "Apply protective fungicides (mancozeb, captan, or myclobutanil) starting at budbreak."
        ],
        "prevention": [
            "Adopt open canopy training systems (e.g., Vertical Shoot Positioning) for airflow.",
            "Keep the vineyard floor cleared of tall weeds.",
            "Ensure timely spray coverage during pre-bloom through 4 weeks post-bloom."
        ]
    },
    "Grape with Esca (Black Measles)": {
        "plant": "Grape",
        "is_healthy": False,
        "cause": "Fungal complex (Phaeomoniella, Phaeoacremonium, Fomitiporia)",
        "severity": "High",
        "symptoms": [
            "Tiger-stripe pattern of interveinal chlorosis and necrosis on leaves.",
            "Small dark spots ('measles') on berry skins.",
            "Sudden vine apoplexy (complete vine collapse in hot summer weather)."
        ],
        "immediate_actions": [
            "Mark symptomatic vines for winter rejuvenation or trunk renewal.",
            "Avoid severe stress to the vine; optimize irrigation during heat waves.",
            "Protect pruning wounds with wound sealants or Trichoderma biocontrol agents."
        ],
        "prevention": [
            "Prune late in the dormant season when wound healing is most rapid.",
            "Disinfect pruning shears regularly to prevent fungal transmission.",
            "Replace vines that have died from wood-decay apoplexy with certified clean nursery stock."
        ]
    },
    "Grape with Isariopsis Leaf Spot": {
        "plant": "Grape",
        "is_healthy": False,
        "cause": "Fungal (Phaeoisariopsis vitis)",
        "severity": "Low to Moderate",
        "symptoms": [
            "Irregularly shaped dark brown spots on mature leaves.",
            "Spots may turn grayish on the underside with velvety fungal tufts.",
            "Premature defoliation late in the season."
        ],
        "immediate_actions": [
            "Clean up dropped foliage in autumn to break the spore cycle.",
            "Spray copper or sulfur-based fungicides if defoliation threatens fruit ripening."
        ],
        "prevention": [
            "Canopy management to lower relative humidity within the vine interior.",
            "Avoid overhead irrigation; utilize drip lines under the trellis."
        ]
    },
    "Healthy Grape Plant": {
        "plant": "Grape",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Lush green, well-formed lobed leaves free from spots or curling.",
            "Vigorous shoot growth and clean fruit clusters."
        ],
        "immediate_actions": [
            "Continue shoot tucking and leaf thinning around grape clusters for sunlight.",
            "Regulate water stress strategically (deficit irrigation for quality wine grapes)."
        ],
        "prevention": [
            "Annual dormant pruning to balance shoot count and crop load.",
            "Inspect trellis wires and anchors to support mature fruit weight."
        ]
    },

    # ------------------ ORANGE / CITRUS ------------------
    "Orange with Citrus Greening": {
        "plant": "Orange / Citrus",
        "is_healthy": False,
        "cause": "Bacterial (Candidatus Liberibacter asiaticus, spread by Asian Citrus Psyllid)",
        "severity": "Critical",
        "symptoms": [
            "Asymmetric blotchy yellow mottling on leaves that crosses leaf veins.",
            "Lopsided, bitter, poorly colored fruit with aborted seeds.",
            "Twig dieback, stunted growth, and yellow shoots."
        ],
        "immediate_actions": [
            "Report suspected cases to local agricultural extension office or ministry.",
            "Control the insect vector (Asian Citrus Psyllid) using systemic or foliar insecticides.",
            "Provide enhanced nutritional sprays (zinc, manganese, iron) to support tree resilience."
        ],
        "prevention": [
            "Purchase only certified disease-free nursery stock from quarantine-compliant suppliers.",
            "Install insect mesh barriers in young citrus groves.",
            "Quickly remove and destroy heavily declining infected trees to protect neighboring citrus."
        ]
    },

    # ------------------ PEACH ------------------
    "Peach with Bacterial Spot": {
        "plant": "Peach",
        "is_healthy": False,
        "cause": "Bacterial (Xanthomonas arboricola pv. pruni)",
        "severity": "Moderate to High",
        "symptoms": [
            "Small, angular, water-soaked spots that turn purplish-black and drop out, creating a 'shot-hole' effect.",
            "Cracked, pitted lesions on peach fruit.",
            "Spring and summer twig cankers."
        ],
        "immediate_actions": [
            "Apply dormant copper sprays in late fall and late winter before bud swell.",
            "Prune out dead or cankered twigs during dry weather.",
            "Use oxytetracycline sprays during early fruit development if permitted locally."
        ],
        "prevention": [
            "Plant resistant peach cultivars (e.g., Clayton, Candor, Biscoe).",
            "Avoid planting in extremely sandy, nutrient-poor soils prone to wind erosion.",
            "Avoid overhead irrigation which splashes bacterial cells from leaf to leaf."
        ]
    },
    "Healthy Peach Plant": {
        "plant": "Peach",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Bright, lanceolate green leaves without shot-holes or yellowing.",
            "Smooth bark and clean fruit development."
        ],
        "immediate_actions": [
            "Thin excess fruit early in the season to encourage larger, healthier peaches.",
            "Ensure deep weekly watering during dry summer stretches."
        ],
        "prevention": [
            "Apply dormant copper or horticultural oil spray in winter to prevent peach leaf curl and scale insects.",
            "Maintain an open-center vase pruning architecture for sunlight."
        ]
    },

    # ------------------ BELL PEPPER ------------------
    "Bell Pepper with Bacterial Spot": {
        "plant": "Bell Pepper",
        "is_healthy": False,
        "cause": "Bacterial (Xanthomonas euvesicatoria)",
        "severity": "High",
        "symptoms": [
            "Small, circular, water-soaked lesions that turn brown with yellow halos.",
            "Severe leaf drop exposing fruit to sunscald.",
            "Rough, raised, warty lesions on pepper fruits."
        ],
        "immediate_actions": [
            "Apply fixed copper mixed with mancozeb to slow bacterial spread.",
            "Remove and destroy badly infected pepper plants to preserve the rest of the garden.",
            "Do not handle or prune pepper plants when foliage is wet."
        ],
        "prevention": [
            "Plant certified disease-free, hot-water treated seeds or resistant pepper hybrids.",
            "Rotate with non-solanaceous crops (avoid planting where tomatoes or potatoes grew last year).",
            "Water with drip lines or soaker hoses only at soil level."
        ]
    },
    "Healthy Bell Pepper Plant": {
        "plant": "Bell Pepper",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Lush, glossy, deep green foliage with sturdy branching.",
            "White flowers and developing crisp, firm bell pepper pods."
        ],
        "immediate_actions": [
            "Maintain consistent soil moisture to prevent blossom end rot (calcium deficiency).",
            "Support plants with small stakes or cages to keep heavy fruit off the ground."
        ],
        "prevention": [
            "Mulch around plants with clean straw or wood chips to prevent soil splash.",
            "Provide balanced calcium and magnesium fertilizer during flowering."
        ]
    },

    # ------------------ POTATO ------------------
    "Potato with Early Blight": {
        "plant": "Potato",
        "is_healthy": False,
        "cause": "Fungal (Alternaria solani)",
        "severity": "Moderate to High",
        "symptoms": [
            "Dark brown to black spots with concentric rings ('target-board' appearance) on older lower leaves.",
            "Yellow halo surrounding the lesions.",
            "Leaves turn brown, dry up, and cling to the plant."
        ],
        "immediate_actions": [
            "Remove and discard lower infected foliage showing target spots.",
            "Apply protective fungicides (chlorothalonil, copper, or biofungicides) early.",
            "Ensure proper nitrogen fertility; nitrogen-deficient plants are much more susceptible."
        ],
        "prevention": [
            "Rotate potato crops with corn, beans, or grains for at least 3 years.",
            "Hill potatoes well to protect developing tubers from fungal spores washed off leaves.",
            "Space plants generously to promote rapid drying of foliage."
        ]
    },
    "Potato with Late Blight": {
        "plant": "Potato",
        "is_healthy": False,
        "cause": "Oomycete / Water Mold (Phytophthora infestans)",
        "severity": "Critical",
        "symptoms": [
            "Rapidly spreading water-soaked, dark brown to black irregular lesions on leaves and stems.",
            "Delicate white fungal-like mold on leaf undersides in high humidity.",
            "Rapid collapse of foliage and rotting tubers with foul odor."
        ],
        "immediate_actions": [
            "Immediately destroy and bag infected plants; do NOT compost them.",
            "Apply specialized late blight fungicides (e.g., cymoxanil, mandipropamid) immediately to unaffected plants.",
            "Cut vines 2 weeks before harvest if tubers need to cure without spore contact."
        ],
        "prevention": [
            "Plant only certified disease-free seed potatoes.",
            "Eliminate cull piles and volunteer potato plants where the pathogen overwinters.",
            "Monitor regional late blight tracking maps and forecasts."
        ]
    },
    "Healthy Potato Plant": {
        "plant": "Potato",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Dense, vigorous green bush with healthy compound leaves.",
            "Sturdy stems without dark brown streaks or lesions."
        ],
        "immediate_actions": [
            "Continue hilling soil or mulch around the base to prevent tubers from greening.",
            "Maintain consistent moisture, especially during tuber bulking."
        ],
        "prevention": [
            "Regularly inspect leaf undersides for Colorado potato beetle larvae.",
            "Avoid over-fertilizing with nitrogen which creates excessive foliage at expense of tubers."
        ]
    },

    # ------------------ RASPBERRY & SOYBEAN ------------------
    "Healthy Raspberry Plant": {
        "plant": "Raspberry",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Bright green trifoliate leaves with serrated edges and silvery undersides.",
            "Vigorous canes with upright growth and healthy flower clusters."
        ],
        "immediate_actions": [
            "Maintain moist, well-draining soil with 2-3 inches of organic wood mulch.",
            "Trellis canes to keep berries clean and prevent canes from touching moist soil."
        ],
        "prevention": [
            "Prune out spent floricanes right after summer harvest to promote air circulation.",
            "Water at the base to prevent cane blight and gray mold (Botrytis)."
        ]
    },
    "Healthy Soybean Plant": {
        "plant": "Soybean",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Uniform green trifoliate leaves without mottling, mosaic, or leaf spots.",
            "Abundant healthy nodulation on roots for natural nitrogen fixation."
        ],
        "immediate_actions": [
            "Continue scouting for soybean aphids or bean leaf beetles.",
            "Maintain weed-free canopy closure during early vegetative stages."
        ],
        "prevention": [
            "Practice annual crop rotation with corn or small grains.",
            "Inoculate seeds with Rhizobium bacteria prior to planting in new ground."
        ]
    },

    # ------------------ SQUASH ------------------
    "Squash with Powdery Mildew": {
        "plant": "Squash",
        "is_healthy": False,
        "cause": "Fungal (Podosphaera xanthii)",
        "severity": "Moderate",
        "symptoms": [
            "Powdery white fungal spots on upper and lower surfaces of leaves and stems.",
            "Infected leaves turn yellow, then brown, and dry to a crisp texture.",
            "Premature defoliation resulting in sunscalded squash fruit."
        ],
        "immediate_actions": [
            "Prune out the most severely smothered leaves to improve air flow.",
            "Spray with dilute potassium bicarbonate, neem oil, or sulfur early in the morning.",
            "Do not touch healthy leaves after touching infected foliage."
        ],
        "prevention": [
            "Select powdery mildew resistant squash cultivars (look for 'PMR' on seed packets).",
            "Space squash vines at least 3-4 feet apart in full sun locations.",
            "Use drip irrigation so large squash leaves stay dry overnight."
        ]
    },

    # ------------------ STRAWBERRY ------------------
    "Strawberry with Leaf Scorch": {
        "plant": "Strawberry",
        "is_healthy": False,
        "cause": "Fungal (Diplocarpon earlianum)",
        "severity": "Moderate",
        "symptoms": [
            "Irregular purplish-red spots on leaf upper surfaces.",
            "Spots enlarge and merge until entire leaves look scorched and curled.",
            "Fruit stems and calyxes may also develop dark spots."
        ],
        "immediate_actions": [
            "Remove and dispose of spotted older leaves after the main harvest.",
            "Renovate strawberry beds by mowing above crowns and removing old plant debris.",
            "Apply a copper fungicide in early spring as new green growth begins."
        ],
        "prevention": [
            "Plant on raised beds with straw mulch to prevent soil splashing onto leaves.",
            "Avoid excess nitrogen fertilizer which causes dense, humid leaf canopies.",
            "Replace strawberry beds every 3-4 years with certified clean runner plants."
        ]
    },
    "Healthy Strawberry Plant": {
        "plant": "Strawberry",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Crisp, deep green trifoliate leaves with no purple spots or leaf curl.",
            "Vigorous runner production and plump, sweet berries."
        ],
        "immediate_actions": [
            "Maintain 1-1.5 inches of water per week, especially while berries are sizing up.",
            "Keep fresh straw mulch tucked under berries to elevate them from moist dirt."
        ],
        "prevention": [
            "Inspect regularly for slug and spider mite activity.",
            "Maintain bed spacing to allow morning sun to dry leaves quickly."
        ]
    },

    # ------------------ TOMATO ------------------
    "Tomato with Bacterial Spot": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Bacterial (Xanthomonas species)",
        "severity": "High",
        "symptoms": [
            "Small, dark brown, greasy, water-soaked spots with yellow halos.",
            "Spots may coalesce causing leaf blighting and severe defoliation.",
            "Rough, scabby black spots on green and red tomatoes."
        ],
        "immediate_actions": [
            "Apply a copper fungicide tank-mixed with mancozeb to slow bacterial spread.",
            "Remove lower diseased foliage and keep hands and tools sanitized.",
            "Avoid working in tomato rows when leaves are wet with dew or rain."
        ],
        "prevention": [
            "Use certified clean seed or hot-water treated seed.",
            "Rotate tomato ground for at least 2-3 years away from peppers and eggplants.",
            "Use drip tape irrigation at root level to prevent splashing bacteria."
        ]
    },
    "Tomato with Early Blight": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Fungal (Alternaria solani)",
        "severity": "Moderate to High",
        "symptoms": [
            "Dark brown concentric rings resembling a bullseye or target on older lower leaves.",
            "Surrounding leaf tissue turns yellow and eventually wilts and drops.",
            "Dark, leathery sunken lesions on stems and fruit stem-ends."
        ],
        "immediate_actions": [
            "Prune off all lower branches touching the ground and leaves with target spots.",
            "Apply a broad-spectrum organic copper fungicide or biofungicide (Bacillus subtilis).",
            "Mulch heavily around the plant base to create a physical barrier against soil-borne spores."
        ],
        "prevention": [
            "Stake or cage tomatoes to keep foliage upright and off the wet soil.",
            "Water early in the day directly at the root zone.",
            "Rotate tomato families every 3 years with non-solanaceous crops."
        ]
    },
    "Tomato with Late Blight": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Oomycete / Water Mold (Phytophthora infestans)",
        "severity": "Critical",
        "symptoms": [
            "Large, rapidly expanding dark, greasy-looking water-soaked lesions.",
            "Fuzzy white fungal growth on leaf undersides in humid or cool conditions.",
            "Stems develop dark brown to purple lesions; green fruit turns brown and rots rapidly."
        ],
        "immediate_actions": [
            "Bag and pull out severely blighted plants immediately; do not compost.",
            "Apply systemic or protective late blight fungicides to nearby healthy tomatoes.",
            "Harvest remaining unblemished mature green fruit before spores infect them."
        ],
        "prevention": [
            "Plant late blight-resistant tomato varieties (e.g., Defiant, Mountain Magic, Plum Regal).",
            "Eliminate volunteer tomato and potato sprouts in spring.",
            "Provide maximum spacing between cages for rapid canopy drying."
        ]
    },
    "Tomato with Leaf Mold": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Fungal (Passalora fulva / Cladosporium fulvum)",
        "severity": "Moderate",
        "symptoms": [
            "Pale green to yellowish patches on upper leaf surfaces.",
            "Olive-green to velvety brown mold growth on the corresponding undersides.",
            "Leaves curl, wither, and drop, predominantly in greenhouse or humid settings."
        ],
        "immediate_actions": [
            "Increase greenhouse or garden ventilation immediately to lower humidity below 85%.",
            "Prune lower suckers and crowded leaves to facilitate horizontal air flow.",
            "Apply an approved copper fungicide if conditions remain persistently humid."
        ],
        "prevention": [
            "Utilize circulating fans in greenhouses and high tunnels.",
            "Avoid overhead irrigation; never wet foliage late in the day.",
            "Choose tomato cultivars with known resistance to Passalora races."
        ]
    },
    "Tomato with Septoria Leaf Spot": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Fungal (Septoria lycopersici)",
        "severity": "Moderate to High",
        "symptoms": [
            "Numerous small, circular spots (1/8 inch) with dark borders and tan or gray centers.",
            "Tiny black fruiting bodies (pycnidia) pepper the center of each spot.",
            "Progresses upwards from lower leaves, causing severe leaf drop and exposing fruit to sunscald."
        ],
        "immediate_actions": [
            "Pinch off infected lower leaves as soon as first spots appear.",
            "Apply copper or chlorothalonil fungicide every 7-10 days in wet seasons.",
            "Mulch under the vines with straw or cardboard to stop soil splash."
        ],
        "prevention": [
            "Clean up tomato debris thoroughly at season end.",
            "Rotate planting beds on a 3-year cycle.",
            "Stake plants upright and prune lower foliage up to 12 inches from ground level."
        ]
    },
    "Tomato with Spider Mites or Two-spotted Spider Mite": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Pest / Arachnid (Tetranychus urticae)",
        "severity": "Moderate to High",
        "symptoms": [
            "Fine yellow or white stippling (tiny dots) on upper leaf surfaces.",
            "Silky fine webbing on the undersides of leaves and leaf axils.",
            "Leaves turn bronze, dry, and brittle during hot, dusty summer weather."
        ],
        "immediate_actions": [
            "Spray leaf undersides with a strong jet of water to dislodge mites and webs.",
            "Apply insecticidal soap, neem oil, or horticultural oil, thoroughly coating leaf undersides.",
            "Introduce beneficial predatory mites (e.g., Phytoseiulus persimilis) in enclosed gardens."
        ],
        "prevention": [
            "Keep garden pathways moist or mulched to minimize dust which favors mite outbreaks.",
            "Avoid broad-spectrum synthetic insecticides that kill natural mite predators like lady beetles.",
            "Keep tomato plants well-watered to prevent drought stress that attracts mites."
        ]
    },
    "Tomato with Target Spot": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Fungal (Corynespora cassiicola)",
        "severity": "Moderate",
        "symptoms": [
            "Brown, circular lesions with light brown centers and dark concentric rings.",
            "Lesions expand on both leaves and fruit, causing fruit rot with sunken centers.",
            "Premature defoliation in warm, humid climates."
        ],
        "immediate_actions": [
            "Prune out symptomatic leaves to reduce fungal spore count.",
            "Apply protective fungicides (copper or azoxystrobin) according to local recommendations.",
            "Improve air movement within the plant canopy."
        ],
        "prevention": [
            "Maintain generous 24-36 inch spacing between tomato plants.",
            "Avoid overhead watering; use ground-level drip lines.",
            "Practice continuous weed control around garden borders."
        ]
    },
    "Tomato Yellow Leaf Curl Virus": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Viral (TYLCV, transmitted by Whiteflies / Bemisia tabaci)",
        "severity": "Critical",
        "symptoms": [
            "Severe upward curling and cupping of leaf margins.",
            "Marked interveinal chlorosis (yellowing) on young emerging leaves.",
            "Extreme stunting of plant growth with bushy appearance and flower drop (no fruit set)."
        ],
        "immediate_actions": [
            "Remove and immediately bag infected plants to prevent whiteflies from acquiring the virus.",
            "Control whitefly populations using yellow sticky traps and insecticidal soap sprays.",
            "Install fine insect netting (50-mesh) over nursery beds or greenhouses."
        ],
        "prevention": [
            "Plant certified TYLCV-resistant tomato hybrids.",
            "Eliminate host weeds (e.g., nightshades, mallow) near the garden perimeter.",
            "Use reflective silver mulches which disorient whiteflies and reduce landings."
        ]
    },
    "Tomato Mosaic Virus": {
        "plant": "Tomato",
        "is_healthy": False,
        "cause": "Viral (ToMV, transmitted mechanically by touch, tools, and seeds)",
        "severity": "High",
        "symptoms": [
            "Mottling of light and dark green patches ('mosaic' pattern) on leaves.",
            "Leaf distortion, blistering, or 'shoestring' narrowing of leaflets.",
            "Internal brown browning of tomato fruit wall and stunted plant growth."
        ],
        "immediate_actions": [
            "Immediately remove and burn or bag infected plants; virus persists in soil and plant residue.",
            "Do NOT smoke or handle tobacco products near tomato plants (tobacco can carry related viruses).",
            "Wash hands thoroughly with soap and water and sterilize tools in 20% non-fat dry milk solution or bleach."
        ],
        "prevention": [
            "Purchase virus-resistant tomato varieties (marked with 'T' or 'ToMV').",
            "Use only certified virus-free seed stock.",
            "Disinfect stakes, cages, and pruning shears before every growing season."
        ]
    },
    "Healthy Tomato Plant": {
        "plant": "Tomato",
        "is_healthy": True,
        "cause": "None (Plant is in optimal health)",
        "severity": "None",
        "symptoms": [
            "Deep green, fragrant compound leaves without spots, curling, or yellow halos.",
            "Thick, hairy stems with active flowering trusses and smooth green fruit development."
        ],
        "immediate_actions": [
            "Maintain regular deep watering (1-2 inches per week) to prevent blossom end rot and skin cracking.",
            "Prune non-productive bottom suckers to maintain upright vertical structure and airflow."
        ],
        "prevention": [
            "Apply a 2-3 inch layer of clean straw, untreated grass clippings, or wood chips around base.",
            "Feed every 2-3 weeks with an organic fertilizer high in phosphorus, potassium, and calcium.",
            "Inspect weekly for hornworms, aphids, or early leaf spots."
        ]
    }
}


def get_recommendations(disease_name: str) -> Dict[str, Any]:
    """
    Retrieves full agricultural plant care recommendations for a given disease label.
    If the exact name is not found, provides an intelligent general fallback.
    """
    if disease_name in RECOMMENDATIONS_DATABASE:
        data = RECOMMENDATIONS_DATABASE[disease_name]
        return {
            "disease_name": disease_name,
            "plant": data["plant"],
            "is_healthy": data["is_healthy"],
            "cause": data["cause"],
            "severity": data["severity"],
            "symptoms": data["symptoms"],
            "immediate_actions": data["immediate_actions"],
            "prevention": data["prevention"]
        }

    # Fallback for unrecognized classes
    is_healthy_guess = "healthy" in disease_name.lower()
    return {
        "disease_name": disease_name,
        "plant": "Cultivated Plant",
        "is_healthy": is_healthy_guess,
        "cause": "Biological observation" if not is_healthy_guess else "None (Healthy)",
        "severity": "Low" if is_healthy_guess else "Moderate",
        "symptoms": [
            f"Foliage exhibiting characteristics consistent with {disease_name}.",
            "Inspect overall leaf color, texture, and margin uniformity."
        ],
        "immediate_actions": [
            "Isolate the plant if lesions or active discoloration are visible.",
            "Remove dead or decaying plant tissue using clean, sterilized shears.",
            "Consult with your local university extension service or agronomist for targeted treatments."
        ],
        "prevention": [
            "Maintain clean, well-draining soil and avoid overwatering.",
            "Water early in the morning directly at the root zone.",
            "Ensure proper spacing to encourage good air circulation."
        ]
    }
