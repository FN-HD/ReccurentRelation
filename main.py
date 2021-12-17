from readfile import readfile as f
from calmath import recseq as rs
from graphics import sequence_table as table

# 素数表の生成
primelist = f.read_integerlist()

# 二次の時
# Fib test
Fibs = rs.get_standard_sequences([-1, -1], primelist[100])

fib1 = [v for i, v in enumerate(Fibs[0])]
df = table.get_conditional_table('prime', 'fib', primelist, fib1)
df