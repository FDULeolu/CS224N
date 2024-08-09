import numpy as np
import scipy
import tqdm
import docopt
import nltk
import torchvision
import torch
import sentencepiece
import lxml
import sacrebleu
import tensorboard

# 验证 numpy
print("Numpy version:", np.__version__)
print("Numpy array example:", np.array([1, 2, 3]))

# 验证 scipy
print("Scipy version:", scipy.__version__)
print("Scipy stats example:", scipy.stats.norm.pdf(0))

# 验证 tqdm
for i in tqdm.tqdm(range(10)):
    pass

# 验证 docopt
args = docopt.docopt('Usage: prog [options] <file> <file>')
print("Docopt parsed args:", args)

# 验证 nltk
print("NLTK version:", nltk.__version__)
nltk.download('punkt')
print("NLTK tokenize example:", nltk.word_tokenize("This is a test sentence."))

# 验证 torchvision 和 torch
print("Torchvision version:", torchvision.__version__)
print("Torch version:", torch.__version__)
print("Torch tensor example:", torch.tensor([1, 2, 3]))

# 验证 sentencepiece
print("SentencePiece version:", sentencepiece.__version__)

# 验证 lxml
from lxml import etree
print("lxml version:", lxml.__version__)
xml_string = """<root>
    <element key="value">text</element>
</root>"""
root = etree.fromstring(xml_string)
print("XML parsed successfully:")
print(etree.tostring(root, pretty_print=True).decode())

# 验证 sacrebleu
print("SacreBLEU version:", sacrebleu.__version__)

# 验证 tensorboard
print("TensorBoard version:", tensorboard.__version__)