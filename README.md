# Paper Repository: Evaluating Prompt Engineering Strategies for Sentiment Control in AI-Generated Texts

## Overview
This repository contains the code and supplementary materials for the paper "Evaluating Prompt Engineering Strategies for Sentiment Control in AI-Generated Texts" by Kerstin Sahler and Sophie Jentzsch published at HHAI 2025: The 4th International Conference Series on Hybrid Human-Artificial Intelligence.

## Contents
# Improved Text
The prompts for each optimization step are organized and saved based on their respective prompting techniques, accompanied by `util.py` which houses essential utility functions supporting various techniques. For additional reference, `other_prompts.ipynb` contains a comprehensive collection of supplementary prompts, specifically designed for generating few-shot examples and Chain-of-Thought reasoning texts.

.
├── prompts/
│   ├── vanilla_baseline.ipynb
│   ├── zero_shot.ipynb
│   ├── zero_shot_cot.ipynb
│   ├── few_shot.ipynb
│   ├── cot.ipynb
│   ├── other_prompts.ipynb
│   └── util.py
└── Supplementary_Material.pdf

## Setup
```bash
# Instructions to set up the environment
git clone https://github.com/DLR-SC/prompt-sentiment-control.git
cd prompt-sentiment-control
pip install -r requirements.txt
```

## Usage
The experiments were implemented in a Jupyter Notebook, allowing for modular execution. This design allows to run each optimization step independently, facilitating targeted analysis and individual refinement of specific components without requiring a complete rerun.

## Citation

```bibtex
tbd
```

## License
MIT License