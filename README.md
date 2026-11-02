# Intro to NLP

A hands-on introduction to natural language processing. You will start with a classic machine learning spam classifier, then move to modern Transformer models for zero-shot classification, and finish by building word embeddings with a neural network. The exercises use the SMS Spam Collection dataset and pretrained models from the Hugging Face Transformers library.

## Learning Objectives

By the end of this repository, you should be able to:

- Preprocess raw text with tokenisation, stemming, and lemmatisation using NLTK.
- Build a spam classifier with scikit-learn using Bag-of-Words and TF-IDF features.
- Apply pretrained Transformer pipelines to classify text without task-specific training (zero-shot).
- Select the right Transformer pipeline and model for a given NLP task.
- Create word embeddings with a neural network and inspect the learned vectors.

## Learning Path

Work through the notebooks in order. They build on each other, moving from classic machine learning to Transformer-based approaches.

| File / Folder | Description |
|---|---|
| [**1 - Spam Classifier**](1_spam_classifier.ipynb) | Preprocess SMS text and train a logistic regression spam classifier with scikit-learn. |
| [**2 - Spam Zero-Shot**](2_spam_zero_shot.ipynb) | Use a pretrained Transformer pipeline to classify spam with zero-shot learning. |
| [**3 - Transformer Pipeline Models**](3_transformers_zero_shot_pipeline.ipynb) | Explore how different pretrained models and pipelines fit different NLP tasks. |
| [**4 - Create Embeddings**](4_create_embeddings.ipynb) | Build word embeddings with a Keras neural network and inspect the learned vectors. |
| [**5 - Optional**](5_optional.ipynb) | Optional, hands-on exercise: train word embeddings for the spam/ham data with TensorFlow and explore them in the Embedding Projector. |

### Additional Folders and Files

| File / Folder | Description |
|---|---|
| [**Data**](data/) | The SMS Spam Collection dataset and a sample CSV used across the notebooks. |
| [**Extra**](extra/) | Helper functions (`utility.py`) used by the embeddings notebook. |
| [**Solutions**](solutions/) | Reference solutions. |
| [**pyproject.toml**](pyproject.toml) | Project configuration and dependencies. |
| [**uv.lock**](uv.lock) | Dependency lock file. |

## Setup

Use [uv](https://docs.astral.sh/uv/getting-started/installation/) 0.13.5 or newer
and Python 3.13.17 or a newer 3.13 patch release, as defined in
[`.python-version`](.python-version).

> [!NOTE]
> Throughout these steps, text in angle brackets like `<repo-name>` is a **placeholder**. Replace it, including the `< >` brackets, with your own value. For example, `cd <repo-name>` becomes `cd ds-intro-to-NLP`.

### 1. Create the Repository from the Template

Click **Use this template** on GitHub.

When creating the repository:

- Set yourself as the **Owner**
- Choose a repository name
- Disable **Include all branches**
- Click **Create repository**

> [!IMPORTANT]
> If you are working in pairs or groups, only **one person** should complete this step.

---

### 2. Add Collaborators (Pairs/Groups Only)

If working with teammates:

1. Open the repository on GitHub
2. Go to **Settings → Collaborators**
3. Add your teammates as collaborators
4. Share the repository link with your team

Teammates should accept the invitation before continuing.

---

### 3. Clone the Repository

Copy the SSH URL from the **Code** button on GitHub, then run:

```bash
git clone <copied-ssh-url>
```

The copied SSH URL will look like `git@github.com:<your-username>/<repo-name>.git`.

---

### 4. Move into the Project Folder and Install Dependencies

This installs all dependencies and creates a virtual environment in (`.venv/`).

```bash
cd <repo-name>
uv sync
```

> [!NOTE]
> The first run downloads large pretrained models from Hugging Face (notebook 3 fetches a model of around 1.6 GB), so allow time and disk space for it. Models are cached locally after the first download.

---

### 5. Open the Notebooks

> [!NOTE]
> Make sure you open VS Code from the project root so it automatically detects the environment created by `uv sync`.

Launch VS Code in the project root folder:

```bash
code .
```

Then open a notebook and select the Python environment created by `uv sync` as the kernel.

## References & Further Reading

- [**Natural Language Processing with Python (the NLTK book)**](https://www.nltk.org/book/): The standard introduction to text processing with NLTK
- [**scikit-learn: Text feature extraction**](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction): Official guide to CountVectorizer and TF-IDF
- [**Hugging Face: Pipelines**](https://huggingface.co/docs/transformers/main_classes/pipelines): Reference for the Transformer pipeline API used in notebooks 2 and 3
- [**Hugging Face: Zero-Shot Classification**](https://huggingface.co/tasks/zero-shot-classification): What zero-shot classification is and which models to use
- [**The Illustrated Word2vec**](https://jalammar.github.io/illustrated-word2vec/): A visual explanation of how word embeddings are learned and what they represent
