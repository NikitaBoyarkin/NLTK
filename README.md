# NLTK — Natural Language Processing Notes

A set of small, runnable Python scripts written while learning Natural Language
Processing with the **NLTK** library. This is a personal study repo from early NLP
practice — not a maintained library and not a packaged project.

## What's inside

Each file is a self-contained snippet demonstrating one NLTK concept:

| File | Concept |
|---|---|
| `tokenizing.py` | Word / sentence tokenization |
| `stop words.py` | Stop-word filtering |
| `stemming.py` | Porter / Snowball stemming |
| `lemmatizing.py` | WordNet lemmatization |
| `part of speech tagging.py` | Part-of-speech tagging |
| `chunking.py`, `chinking.py` | Chunking and chinking |
| `named entity recognition.py` | Named entity recognition |
| `classification.py`, `naive bayes.py` | Text classification with Naive Bayes |
| `words as features for learning.py` | Feature extraction for learning |
| `combining algos with a vote.py` | Combining classifiers by vote |
| `save classifier with pickle.py` | Persisting a trained classifier |
| `scikit-lean incorporation.py` | Using NLTK together with scikit-learn |
| `corpora.py`, `wordnet.py` | Corpora and WordNet access |
| `ivestigating bias.py` | Exploring bias in corpora |

## Requirements

- Python 3
- `nltk`

```bash
pip install nltk
```

Several scripts download NLTK data (tokenizers, corpora) on first use, for example:

```python
import nltk
nltk.download("punkt")
nltk.download("wordnet")
```

## How to run

Run any script directly:

```bash
python "tokenizing.py"
python "named entity recognition.py"
```

There is no test suite, no packaging and no CI here — these are study notes, run
by hand.

## Topics

`nltk` · `natural-language-processing` · `python` · `text-processing` · `tokenization` · `learning`

## License

Released under the MIT License — see [LICENSE](LICENSE).

## Links

- Portfolio: <https://nikitaboyarkin.github.io/>
