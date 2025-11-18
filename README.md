# Paper Repository: Evaluating Prompt Engineering Strategies for Sentiment Control in AI-Generated Texts

## Overview
This repository contains the code and supplementary materials for the paper "Evaluating Prompt Engineering Strategies for Sentiment Control in AI-Generated Texts" by Kerstin Sahler and Sophie Jentzsch published at HHAI 2025: The 4th International Conference Series on Hybrid Human-Artificial Intelligence.

## Contents
The prompts for each optimisation step are organised and saved based on their respective prompting techniques, accompanied by `util.py` which contains essential utility functions supporting various techniques. For additional reference, `other_prompts.ipynb` contains a comprehensive collection of supplementary prompts, specifically designed for generating Few-Shot examples and Chain-of-Thought reasoning texts. However, the Chain-of-Thought reasoning texts used in the original experiments for the Automatic as well as the Manual approach are also provided in the `cot_examples/` folder together with the examples from the Human approach of Few-Shot prompting.


```
prompt-sentiment-control/
├── experiments/
│   ├── cot_examples/
│       ├── automatic_factual_reasoning
│       ├── automatic_subjective_reasoning
│       ├── factual_examples
│       ├── manual_factual_reasoning
│       ├── manual_subjective_reasoning
│       └── subjective_examples
│   ├── queries/
│       ├── factual-queries.txt
│       └── subjective-queries.txt
│   ├── cot.ipynb
│   ├── few_shot.ipynb
│   ├── fine_tuning.ipynb
│   ├── other_prompts.ipynb
│   ├── util.py
│   ├── vanilla_baseline.ipynb
│   ├── zero_shot_cot.ipynb
│   └── zero_shot.ipynb
├── Readme.md
└── Supplementary_Material.pdf
```


## Setup
```bash
git clone https://github.com/DLR-SC/prompt-sentiment-control.git
cd prompt-sentiment-control
# setup environment
pip install -r requirements.txt
```

## Usage
All experiments were implemented in different Jupyter Notebooks, allowing for modular execution. This implementation allows to run each optimisation step independently, facilitating targeted analysis and individual refinement of specific components without requiring a complete rerun.

## Citation

```bibtex
@inproceedings{sahler2025evaluating,
  title={Evaluating Prompt Engineering Strategies for Sentiment Control in AI-Generated Texts},
  author={Sahler, Kerstin and Jentzsch, Sophie},
  booktitle={HHAI 2025: The 4th International Conference Series on Hybrid Human-Artificial Intelligence},
  year={2025},
  series={Frontiers in Artificial Intelligence and Applications},
  volume = {408},
  editors = {Dino Pedreschi, Michela Milano, Ilaria Tiddi, Stuart Russell, Chiara Boldrini, Luca Pappalardo, Andrea Passerini, Shenghui Wang},
  doi = {10.3233/FAIA250659},
  pages = {423 - 438},
  isbn = {9781643686110}
}
```

## License
MIT License