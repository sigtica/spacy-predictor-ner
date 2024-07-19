# Spacy Predictor for Named Entity Recognition

This is a module for spaCy Named Entity Recognition industrial-strength prediction. 

## Getting started

To get started, you will need a pretrained spacy 3 model. Please note that spacy 2 models may or may not be compatible with this module. Please refer to [spaCy's documentation](https://github.com/explosion/spacy-models) on loading models if you have further questions.

Once you have identified your model (which should be a folder), place the folder in the same directory as the `main.py`. Then open `main.py` and make appropriate changes to use the spacy model to predict on your text of choice.

## Sample models 

If you would like to have some models to test out this setup, feel free to work with our content on Hugging Face: https://huggingface.co/sigtica.

### Example 1

For English, a fun one to try out is the following:

```python
!pip install https://huggingface.co/sigtica/data_dev_spacy_en_trf_1/resolve/main/data_dev_spacy_en_trf_1-any-py3-none-any.whl

# Using spacy.load().
import spacy
nlp = spacy.load("data_dev_spacy_en_trf_1")

# Importing as module.
import data_dev_spacy_en_trf_1
nlp = data_dev_spacy_en_trf_1.load()
```

### Example 2

For Chinese, a fun one to try out is the following:

```python
!pip install https://huggingface.co/sigtica/data_dev_spacy_zh_lg_1/resolve/main/data_dev_spacy_zh_lg_1-any-py3-none-any.whl

# Using spacy.load().
import spacy
nlp = spacy.load("data_dev_spacy_zh_lg_1")

# Importing as module.
import data_dev_spacy_zh_lg_1
nlp = data_dev_spacy_zh_lg_1.load()
```

## Support

Please direct any enquiries to info@sigtica.com or check out our [Hugging Face page](https://huggingface.co/sigtica).
