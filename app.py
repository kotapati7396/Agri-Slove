# from flask import Flask, render_template, request
# from keras.models import load_model
# from keras.preprocessing import image

# app = Flask(__name__)

# dic = {0 : 'Seedling Blight', 1 : 'Leaf rust', 2 : 'Powdery mildew', 3 : 'Sclerotinia rot', 4 : 'downy mildew', 5 : 'Late blight', 6 : 'Sooty mold', 7 : 'Purple Blotch', 8 : 'Fusarium wilt', 9 : 'Guava wilt', 10 : 'Anthracnose', 11 : 'Common Scab', 12 : 'Black Knot', 13 : 'Cladosporium Leaf Spot', 14 : 'Anthracnose Lichi', 15 : 'Aster Yellows', 16 : 'Charcoal rot', 17 : 'Bud rot', 18 : 'Apple Scab'}

# model = load_model('model.h5')

# model.make_predict_function()

# def predict_label(img_path):
# 	i = image.load_img(img_path, target_size=(100,100))
# 	i = image.img_to_array(i)/255.0
# 	i = i.reshape(1, 100,100,3)
# 	p = model.predict_classe(i)
# 	return 6


# # routes
# @app.route("/", methods=['GET', 'POST'])
# def main():
# 	return render_template("index.html")

# @app.route("/about")
# def about_page():
# 	return "Please subscribe  Artificial Intelligence Hub..!!!"

# @app.route("/submit", methods = ['GET', 'POST'])
# def get_output():
# 	if request.method == 'POST':
# 		img = request.files['my_image']

# 		img_path = "static/" + img.filename
# 		img.save(img_path)

# 		p = predict_label(img_path)

# 	return render_template("index.html", prediction = p, img_path = img_path)


# if __name__ =='__main__':
# 	#app.debug = True
# 	app.run(debug = True)

from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from json import dumps

app = Flask(__name__)

dic = {
    0: "Seedling Blight", 
    1: "Leaf rust",
    2: "Powdery mildew",
    3: "Sclerotinia rot",
    4: "downy mildew",
    5: "Late blight",
    6: "Sooty mold",
    7: "Purple Blotch",
    8: "Fusarium wilt",
    9: "Guava wilt",
    10: "Anthracnose",
    11: "Common Scab",
    12: "Black Knot",
    13: "Cladosporium Leaf Spot",
    14: "Anthracnose Lichi",
    15: "Aster Yellows",
    16: "Charcoal rot",
    17: "Bud rot",
    18: "Apple Scab",
}

model = load_model("testmodel.h5")

model.make_predict_function()


def predict_label(img_path):
    i = image.load_img(img_path, target_size=(100, 100))
    i = image.img_to_array(i) / 255.0
    i = i.reshape(1, 100, 100, 3)
    p = model.predict(i)
    class_indices = np.argmax(p, axis=-1)
    # print(class_indices, "hello")
    return dic[class_indices[0]], class_indices[0]


# routes
@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("index1.html")


# @app.route("/homepage")
# def about_page():
#     return render_template("index.html")


@app.route("/submit", methods=["GET", "POST"])
def get_output():
    if request.method == "POST":
        img = request.files["my_image"]

        img_path = "static/" + img.filename
        img.save(img_path)
        p, index = predict_label(img_path)
    data = [
        [
            "Seedling Blight",
            "As soon as the disease symptoms are observed dusting Sulphur (2.5kg/ha) or spraying Calixin 75 EC (5 ml/10 litres of water) at 15 days interval helps to control the disease.",
        ],
        [
            "Leaf rust",
            "Remove and destroy all leaves and plant parts affected by rust. You might have to destroy badly infected plants completely to prevent them infecting other plants of the same species. Spray with a suitable rust control product containing fungicide, repeating as recommended.",
        ],
        [
            "Powdery mildew",
            "Fungicides containing monopotassium salts, hydrodesulfurized kerosene, aliphatic petroleum solvent, mancozeb and myclobutanil can be used to treat powdery mildew on mangos. For optimal effect, the treatment should start before flowering or at very early flowering stages.",
        ],
        [
            "Sclerotinia rot",
            "Pumpkins can be infected by a wide variety of pathogens and exhibit many diseases. Many of these diseases are prevented by implementing a very basic spray schedule. Pumpkins should receive an application of a fungicide that contains either chlorothalonil or mancozeb every 10 to 14 days.",
        ],
        [
            "downy mildew",
            "Use protectant and systemic fungicides.Protectants such as mancozeb and ziram can provide economical early-season control, especially for Phomopsis and black rot, and sulfur may be used for early powdery mildew control in cultivars that are not sulfur-sensitive, Schilder said.",
        ],
        [
            "Late blight",
            "Apply a tomato fungicide at the first sign of infection or when weather conditions are favorable for disease to develop. Prevent early blight by watering at soil level and mulching. Keep adequate space between plants and rows; use stakes and practice good weed control.",
        ],
        [
            "Sooty mold",
            "Wash hands with soap and water before working in seed beds. Prohibit smoking or chewing of tobacco who are handling brinjal seedlings. Spray insecticides like Dimethoate 2 ml/litre or Metasystox 1 ml/litre of water to control the insect vectors.",
        ],
        [
            "Purple Blotch",
            "For managing the disease effectively, onion bulbs meant for seed crop should be exposed to sun for 12 days to destroy the fungus. Spraying with Zineb (0.2%), Karathane (0.1%) or Tridemorph (0.1%) also gives good control of the disease. disease.",
        ],
        [
            "Fusarium wilt",
            "Management: Because watermelon varieties and hybrids are all susceptible to powdery mildew, fungicide sprays are required to control this disease. Preventive spray programs with fungicides can be effective, but the fungus readily develops fungicide resistance, often within a single season.Like Luna fungicide.",
        ],
        [
            "Guava wilt",
            "Diseases. Red algae, also called algal spot or algal leaf spot, is caused by the fungus Cephaleuros virescens. This condition creates purplish-brown spotting on guava plant leaves and can, if severe, cause defoliation and lowered fruit production. Treat with a copper-based fungicide to prevent diseases.",
        ],
        [
            "Anthracnose",
            "Treating an orange tree disease like this requires controlling the spreaders. Setting up windbreaks (rows of shrubbery) can prevent spider mites from flying onto your trees through the wind. Other ways include removing weeds and pruning dead branches and twigs when needed.",
        ],
        [
            "Common Scab",
            "Always use only disease-free seed tubers for raising the crop.Cultivation of solanaceous crops, being collateral hosts, in nearby potato fields must be avoided.Fungicidal sprays are effective in controlling early blight and other leaf spots. ...Apply recommended dose of fertilizers especially nitrogen.",
        ],
        [
            "Black Knot",
            "From first bloom to harvest and beyond, Luna fungicide protects cherries throughout the growing season, improving plant health for beautiful crops and abundant cherry harvests. Luna provides unparalleled control of Botrytis, powdery mildew and other problematic diseases.",
        ],
        [
            "Cladosporium Leaf Spot",
            "In severe cases, nearly all roots may be girdled or rotted off. Severity is influenced by cultivar, soil texture, irrigation, and pathogen populations. Severe damping- off is associated with clay or poorly draining soils with a history of frequent spinach production.",
        ],
        [
            "Anthracnose Lichi",
            "Maintenance of orchard hygiene, through pruning of dead wood and removal of infected leaves, twigs and fruits help to reduce the incidence of the disease. Pre-harvest applications of fungicides at colour-break stage such as thiophanate methyl (0.14%) or chlorothalonil (0.15%) or difenoconazole (0.025%) or azoxystrobin (0.023%) offer good control. Pre-harvest spray of fungicide helps in extending post-harvest life.",
        ],
        [
            "Aster Yellows",
            "Wet, warm conditions will keep plants away from diseases. Apply organic fungicides when the first symptoms appear. Treat seeds with organic fungicide or hot water before sowing. Application of gibberellic acid will prevent diseases and promote air circulation.",
        ],
        [
            "Charcoal rot",
            "Excessive irrigation should be avoided to reduce humidity around the plants. Seed treatment with antagonist fungal culture of Trichoderma viride (3-4 g/kg of seed) or Thiram (2-3 g /kg of seed) and soil drenching with Dithane M 45 (0.2%) or Bavistin (0.1%) affords protection against the disease.",
        ],
        [
            "Bud rot",
            "Apply Bacillus subtilis (Pf1) @ 200 g/palm + Trichoderma viride @ 200 g/palm/year. Apply 200g phosphobacteria and 200 g Azotobactor mixed with 50 Kg of FYM/palm. Green manure crops must be raised and ploughed in situ.Neem cake 5 kg/tree must be applied along with fertilizers.",
        ],
        [
            "APPLE SCAB",
            "Managing and treating the apple scab fungus is an integrated process that combines sanitation, resistant cultivars, and fungicides. Let’s look at the steps you can take to treat and manage this disease: AD Choose Scab-Resistant Cultivars The best line of defense is to choose resistant varieties when possible. Some great scab-resistant apple cultivars include: Crimson Crisp, Crimson Gold, Enterprise, Freedom, Goldrush, Jonafree, Liberty, Nova Easygro, Novamac, Priscilla, Pristine, Redfree, Scarlet Prima, Sir Prize",
        ],
    ]
    # data = dumps(data[index])
    print(data[index][1])
    return render_template( "index1.html", prediction=p, img_path=img_path,about=data[index][1],name=data[index][0])




if __name__ == "__main__":
    # app.debug = True
    app.run(debug=True)
