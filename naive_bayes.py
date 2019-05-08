import numpy as np
import scipy
from sklearn.naive_bayes import GaussianNB

fake_dense = scipy.sparse.load_npz('fake.npz').todense()
reliable_dense = scipy.sparse.load_npz('reliable.npz').todense()
article_dense = scipy.sparse.load_npz('article.npz').todense()

# assume vocab size for fake and reliable are equal
# if vocab size for article is less, fill with zeros
fake_vocab_size = fake_dense.shape[1]
article_vocab_size = article_dense.shape[1]
if article_vocab_size < fake_vocab_size:
    z = np.zeros((1, fake_vocab_size - article_vocab_size), dtype=fake_dense.dtype)
    article_dense = np.concatenate((article_dense, z), axis=1)

# training_vectors = <concatenation of fake and reliable>
training_vectors = np.concatenate((fake_dense, reliable_dense), axis=0)

# target_values = [<number of fake articles> zeros <number of reliable> ones]
fake_n_articles = fake_dense.shape[0]
reliable_n_articles = reliable_dense.shape[0]
target_values = ([0] * fake_n_articles) + ([1] * reliable_n_articles)

classier = GaussianNB()
classier.fit(training_vectors, target_values)

print('fake = 0, reliable = 1')
print('article =', classier.predict(article_dense))
