import sys
import core.gen_gensim_model as gen
import core.instruction2vec as inst2vec

def fn_model():
    return model


fd = open("./sample/comb_ben_p1", "r")
asmcode_corpus = fd.read()

vectorsize = 5

model = gen.gen_instruction2vec_model(asmcode_corpus,vectorsize,"test_model")
model.save("m1")
