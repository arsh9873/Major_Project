import sys
import core.gen_gensim_model as gen
import core.instruction2vec as inst2vec


test_asmcode = """
add    %ch,%cl
add    %ebp,%ecx
test   $0x9fd900e6,%eax
or     (%eax),%eax
jmp    0xe940661f
xchg   %eax,%esi
int3
ret
jmp    *0x444950
jmp    *0x444954
jmp    *0x444958
"""

fd = open("./sample/tt", "r")
asmcode_corpus = fd.read()

vectorsize = 5

model = gen.gen_instruction2vec_model(asmcode_corpus,vectorsize,"test_model")

for one_instruction in test_asmcode.split('\n'):
	print(one_instruction)
	vector_of_intruction = inst2vec.instruction2vec(one_instruction,model,vectorsize)
	print (vector_of_intruction)
