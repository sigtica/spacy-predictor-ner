# Spacy Predictor for Named Entity Recognition

This is a module for spaCy Named Entity Recognition industrial-strength prediction. 

## Getting started

### Your trained model 
To get started, you will need a pretrained spacy 3 model. Please note that spacy 2 models may or may not be compatible with this module. Please refer to [spaCy's documentation](https://github.com/explosion/spacy-models) on loading models if you have further questions.

### Dependencies

Please ensure that your environment has spacy installed (please see `requirements.txt` for specific versions) and that you are running Python 3.8 or higher.

### `main.py`

Once you have identified your model (which should be a folder), place the folder in the same directory as the `main.py`. Then open `main.py` and make appropriate changes to use the spacy model to predict on your text of choice.

## Sample models 

If you would like to have some models to test out this setup, feel free to work with our content on Hugging Face: https://huggingface.co/sigtica.

### Example 1

For English, a fun one to try out is the following:

First in shell, run:
```shell
pip install https://huggingface.co/sigtica/en_data_dev_spacy_trf_1/resolve/main/en_data_dev_spacy_trf_1-any-py3-none-any.whl
```

Then in a python runtime, run:
```python
# Using spacy.load().
import spacy
nlp = spacy.load("en_data_dev_spacy_trf_1")
doc = nlp('I live in London.')

# print out the tokens
for token in doc:
    print(token)

# print out the entities
for ent in doc.ents:
    print(ent, ent.label_)


# Importing as module.
import en_data_dev_spacy_trf_1
nlp2 = en_data_dev_spacy_trf_1.load()
doc = nlp2('I live in London.')

# print out the tokens
for token in doc:
    print(token)

# print out the entities
for ent in doc.ents:
    print(ent, ent.label_)
```

### Example 2

For Chinese, a fun one to try out is the following:

First in shell, run:
```shell
pip install https://huggingface.co/sigtica/zh_data_dev_spacy_trf_1/resolve/main/zh_data_dev_spacy_trf_1-any-py3-none-any.whl
```

Then in a python runtime, run:
```python
# Using spacy.load().
import spacy
nlp = spacy.load("zh_data_dev_spacy_trf_1")
doc = nlp('北京大兴国际机场是位于中国北京市大兴区榆垡镇、礼贤镇和河北省廊坊市广阳区之间的一座大型民用机场，于2019年9月25日正式运营。其飞行区等级为4F，是北京市的第二座国际机场，具有“新国门”之稱。
')

# print out the tokens
for token in doc:
    print(token)

# print out the entities
for ent in doc.ents:
    print(ent, ent.label_)


# Importing as module.
import zh_data_dev_spacy_trf_1
nlp2 = zh_data_dev_spacy_trf_1.load()
doc = nlp2('北京大兴国际机场是位于中国北京市大兴区榆垡镇、礼贤镇和河北省廊坊市广阳区之间的一座大型民用机场，于2019年9月25日正式运营。其飞行区等级为4F，是北京市的第二座国际机场，具有“新国门”之稱。
')

# print out the tokens
for token in doc:
    print(token)

# print out the entities
for ent in doc.ents:
    print(ent, ent.label_)
```










## Support

Please direct any enquiries to info@sigtica.com or check out our [Hugging Face page](https://huggingface.co/sigtica).
