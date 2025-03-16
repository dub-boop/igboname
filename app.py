from flask import Flask, render_template

app = Flask(__name__)

# Sample data (can be replaced with a database)
name_of_day = {
    "name": "Ifenkili",
    "pronunciation": "/i-fen-kil-i/",
    "nsidibe_script": "Ṅsịdịbẹ",
    "description": "We feature an Igbo name every day. Visit as often as you can. You might find one for your baby or that favorite person."
}

trending_names = {
    "all_time": ["Chimamanda"],
    "last_week": ["Ikechukwu"],
    "this_week": ["Ali"]
}

proverb_of_day = {
    "text": "Mbe siri ọ bụrụ na e gbuo ya n'ihi na ya jụrụ ajụjụ, ka e lichikwaa ya ụza ka ajụjụ were na-aga n'ihu.",
    "translation": "The tortoise said that if it is killed for asking questions, let it also be given answers so the questions can continue."
}

articles = [
    "What is a Name?",
    "Traditional Titles as Igbo Proper Names",
    "Onwu: Why 'Death' in Igbo Names"
]

games = ["Get Named", "Gwam-Gwam-Gwam", "Igbo Names Puzzle"]

faq = {
    "question": "What is this project about?",
    "answer": "This project aims to explore and share Igbo names and culture through an open-source platform."
}

@app.route('/')
def home():
    return render_template('index.html', 
                          name_of_day=name_of_day,
                          trending_names=trending_names,
                          proverb_of_day=proverb_of_day,
                          articles=articles,
                          games=games,
                          faq=faq)

if __name__ == '_main_':
    app.run(debug=True)