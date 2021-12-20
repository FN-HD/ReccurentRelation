from readfile import readfile as f
from calmath import recseq as rs
from graphics import sequence_table as table


if __name__ == '__main__'
    # 素数表の生成
    primelist = f.read_integerlist()

    # Fib test
    fibs = rs.get_standard_sequences([-1, -1], primelist[100])

    fib0 = [v%i if i != 0 else v for i, v in enumerate(fibs[0])]
    fib1 = [v%i if i != 0 else v for i, v in enumerate(fibs[1])]
    fib2 = [v%i if i != 0 else v for i, v in enumerate(fibs[0] + fibs[1])]
    
    df = table.get_conditional_table('prime', ['fib 0', 'fib 1', 'fib2'], primelist, [fib0, fib1, fib2])
    df