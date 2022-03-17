from enum import Enum

from numpy import loadtxt

from ffast.preprocessor import PreprocessingPipeline

PREPROCESSOR = PreprocessingPipeline()
PATH = "ffast/poincare/poincare.txt"
METAPHONES = "ABCEFHIJKLMNOPRSTUWXY0. "
SIZE_METAPHONES = len(METAPHONES)
raw_vocab = loadtxt(PATH,usecols=0,dtype=str)
VOCABULARY = list(map(PREPROCESSOR.normalise,raw_vocab))
VECTORS = loadtxt(PATH,usecols=range(1,101))

class Poincare(Enum):
    SIZE_VECTOR = 100
    SIZE_VOCABULARY = len(VOCABULARY)
    UNKNOWN = "<Unknown>"
    SKIP = "skip"