# Richel Makes Tech Easy

**The code, notebooks and data behind every lesson on my YouTube channel.** Watch the video, then open the matching notebook here to read along, run the code and practise.

[![YouTube](https://img.shields.io/badge/YouTube-@richelattafuah23-red?logo=youtube)](https://www.youtube.com/@richelattafuah23)
[![Website](https://img.shields.io/badge/Website-richelcode.github.io-0C2A4A)](https://richelcode.github.io/)
[![Code: MIT](https://img.shields.io/badge/code-MIT-blue)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey)](LICENSE-CONTENT.md)

## Series

| Series | What it covers | Level | Start here |
|---|---|---|---|
| **[Forecasting Made Easy](forecasting-made-easy/)** | Predicting what happens next with Python: time series, classic models, AI foundation models, and how to know when to trust a forecast | Beginner to intermediate | [Episode 1: Can AI Predict Tomorrow?](forecasting-made-easy/01-can-ai-predict-tomorrow/) |
| **[Python for Beginners](python-for-beginners/)** | Python from zero: variables, strings, loops, functions, files, data structures and more | Beginner | [Lesson 01: Variables and data types](python-for-beginners/01-variables-and-data-types.ipynb) |

## Latest episode

### [Can AI Predict Tomorrow?](forecasting-made-easy/01-can-ai-predict-tomorrow/)

We race Amazon's Chronos-2 AI model against "same as yesterday" and a classic statistics model on 56 days of Accra temperature. The AI wins with about 26% less error, but its ranges turn out to be overconfident.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RichelCode/Youtube/blob/main/forecasting-made-easy/01-can-ai-predict-tomorrow/can_ai_predict_tomorrow.ipynb)

## How to use this repository

| I want to… | Do this |
|---|---|
| **Read along** | Click any notebook. GitHub shows the code, explanations and saved results |
| **Run the code online, free** | Click an **Open in Colab** button. Nothing to install |
| **Run it on my computer** | Clone the repo, then `pip install -r requirements.txt` (only needed for the forecasting series) |
| **Find a specific lesson** | Each series folder has a README with every lesson in order |

```bash
git clone https://github.com/RichelCode/Youtube.git
cd Youtube
pip install -r requirements.txt
```

## Repository layout

```
Youtube/
├── forecasting-made-easy/        # Forecasting Made Easy series
│   └── 01-can-ai-predict-tomorrow/
│       ├── can_ai_predict_tomorrow.ipynb   # slides + code, in video order
│       ├── data/                            # the dataset and its source
│       └── figures/                         # diagrams used in the video
├── python-for-beginners/         # Python for Beginners series (lessons 01–10)
├── requirements.txt              # packages for the forecasting series
├── LICENSE                       # MIT, for the code
└── LICENSE-CONTENT.md            # CC BY 4.0, for lessons and figures
```

## About me

I'm **Richel Ohenewaa Attafuah, GStat**, a machine learning engineer and statistician. I work on forecasting (demand, traffic and energy load) and I love making tech easy to understand. I hold an MS in Statistics from Miami University and a BSc in Statistics and Mathematics from the University of Ghana.

- **YouTube:** [@richelattafuah23](https://www.youtube.com/@richelattafuah23). New lessons regularly
- **Website and consulting:** [richelcode.github.io](https://richelcode.github.io/)
- **Found a mistake or have a question?** Open an [issue](https://github.com/RichelCode/Youtube/issues), or ask in the video's comments

## Licence

The code is under the [MIT licence](LICENSE). The lessons, explanations and figures are under [CC BY 4.0](LICENSE-CONTENT.md): you can share and adapt them, including for teaching, as long as you give credit. Datasets keep their own licences, listed in each `data/` folder.
