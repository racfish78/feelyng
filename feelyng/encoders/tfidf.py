import feelyng.utils.logging as l
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

logger = l.get_logger(__name__)


def learn_tfidf(sentences, max_features=100):
    """Learns a TFIDF representation based on the words' frequency.

    Args:
        sentences (df): A Panda's dataframe column holding sentences to be fitted.
        max_features (int): Maximum number of features to be fitted.

    Returns:
        A TfidfVectorizer object.

    """

    # Creates a TFIDF vectorizer
    tfidf = TfidfVectorizer(max_features=max_features,
                            preprocessor=lambda p: p, tokenizer=lambda t: t)

    # Fits sentences on it
    logger.info('Learning TFIDF ...')
    tfidf.fit(sentences)
    logger.info('TFIDF learned.')

    return tfidf


def encode_tfidf(tfidf, sentences):
    """Actually encodes the data into a TFIDF representation.

    Args:
        tfidf (TfidfVectorizer): A TfidfVectorizer object.
        sentences (df): A Panda's dataframe column holding sentences to be encoded.

    Returns:
        An encoded TFIDF numpy array.

    """

    logger.info('TFIDF encoding size: (' + str(sentences.size) +
                 ', ' + str(tfidf.idf_.shape[0]) + ')')

    # Transform sentences into TFIDF encoding (only if it has been previously fitted)
    logger.info('Encoding data ...')
    X = tfidf.transform(sentences)

    # Apply encoded TFIDF to numpy array
    encoded_X = X.toarray()
    logger.info('Encoding finished.')

    return encoded_X
