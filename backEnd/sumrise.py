from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import validators
import web2text

text = 'Compatibility of systems of linear constraints over the set of natural \
numbers. Criteria of compatibility of a system of linear Diophantine \
equations, strict inequations, and nonstrict inequations are considered.\
Upper bounds for components of a minimal set of solutions and algorithms\
of construction of minimal generating sets of solutions for all types of\
systems are given. These criteria and the corresponding algorithms for\
constructing a minimal supporting set of solutions can be used in solving\
all the considered types of systems and systems of mixed types.'

def sumrise(text = text, sentences = 5):
    if (validators.url(text)): text = web2text.getwebtxt(text)

    parser = PlaintextParser.from_string(text, Tokenizer('english'))
    summerizer = LsaSummarizer()

    summary = str(summerizer(parser.document, sentences))
    return summary

    # file = 'req.txt'
    # parser = PlaintextParser.from_file(file, Tokenizer('english'))
    # for sentence in summary:
    #     print(sentence)

