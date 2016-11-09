from collections import Counter 

from django.conf import settings
from django.db import models
from django.apps import apps 

from .utils import words_from_html, scaledown, scale_height_width


MODEL = settings.DC_MODEL 
CONTENT = settings.DC_CONTENT_FIELD
TITLE = settings.DC_TITLE_FIELD 
SLUG = settings.DC_SLUG_FIELD 


def aggregate_single_lists(_lists):
    '''
    This function accepts an arbitrary number of lists and
    return a new list with unique words from each list
    e.g. func([1,2], [3], [3, 4, 5]) => [1, 2, 3, 4, 5]
    '''
    _combined = []
    for _lst in _lists:
        for _word in _lst:
            if _word not in _combined:
                _combined.append(_word)
    return _combined


def bag_of_words(big_list, single_list):
    '''
    This function makes bag of words from a list and a super list
    for instance: bag_of_words(['a', 'b', 'c'], ['a', 'c'])
    returns [1, 0, 1]
    '''
    _single_dict = Counter(single_list)
    _total_words = len(big_list)
    _bag_words = [0.0] * _total_words 

    for count, word in enumerate(big_list):
        try:
            _word_frequency = _single_dict[word]
        except KeyError:
            pass 
        _bag_words[count] = _word_frequency

    return _bag_words


def obtain_model_objects():
    '''
    This function imports model fields including content, title,
    and slug fields
    '''
    try:
        _model_object = models.get_model(MODEL)
    except AttributeError:
        _model_object = apps.get_model(MODEL)
    _all_models = _model_object.objects.all()

    return _all_models


def aggregated_word_list_from_models():
    '''
    This function accepts model objects as arguments
    and returns the aggregated word list from content of
    each model object. The output will be fed to bag of words
    '''
    _models = obtain_model_objects()
    _all_words = []
    for _model in _models:
        _single_model_words = words_from_html(
            getattr(_model, CONTENT) )
        _all_words.append( _single_model_words )

    return aggregate_single_lists(_all_words)


def attribute_getter(model, attr):
    try:
        return getattr(model, attr)()
    except AttributeError:
        return ''

def make_matrix_from_models(_models):
    '''
    This function accepts model objects and returns titles array, 
    bag-of-words array, and urls array
    '''
    _titles = []
    _bag_of_words = []
    _urls = []
    _all_words = aggregated_word_list_from_models()

    for _model in _models:
        _titles.append( getattr(_model, TITLE) )
        _bag_of_words_single = getattr(_model, CONTENT)
        _bag_of_words_single = bag_of_words(
            _all_words, 
            words_from_html(_bag_of_words_single)
            )
        _bag_of_words.append( _bag_of_words_single )
        _urls.append( attribute_getter(_model, 'get_absolute_url'))

    return _titles, _bag_of_words, _urls


def scale_models():
    '''
    This is the final function that collects data from database, 
    make bad of words, and scales down the data. 
    '''
    all_models = []
    _models = obtain_model_objects()
    titles, bag_of_words, urls = make_matrix_from_models(_models)
    # 
    scaled_bag_of_words = scaledown(bag_of_words)
    scaled_bag_of_words = scale_height_width(scaled_bag_of_words)
    # iterate through each item and add as a dictionary
    for count, list_ in enumerate(scaled_bag_of_words):
        dict_ = {}
        dict_['title'] = titles[count]
        dict_['url'] = urls[count]
        dict_['coordinates'] = scaled_bag_of_words[count]
        all_models.append(dict_)
    return all_models