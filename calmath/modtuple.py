from fractions import Fraction
from . import extgcd

class ModTuple:
    ''' An order pair whose i-th element is in Z/iZ
    
    It is a finite ordered pair whose i-th element is in Z/iZ.
    The set of all such element forms a Z-algebra by the following 
    opeartion; for any a = (a_i mod i), b = (b_i mod i), and 
    x in Z,
        a + b = (a_i + b_i mod i)
        a * b = (a_i * b_i mod i)
        z * a = (z * a_i mod i).
    Hence this pair have addition, multiplication, and multiplication
    by scalar. 
            
    Note that if i-th element of iterable_obj is not in Z/iZ, 
    then this index is in the exceptnal list and i-th element 
    of this class is 0. We can get the exceptnal list by 
    __getitem__(key='except').

    Attributes
    ----------
    _list: list
        the list of elements of sequence.
    _except: list
        the list of numbers. If i in except, then iterable[i] is
        not in Z/iZ
       
    '''
    def __init__(self, iterable_obj):
        self._list = []
        self._except = []
        for i, v in enumerate(iterable_obj):
            # 例外処理
            if i == 0:
                self._list.append(v)
                continue
                
            if isinstance(v, int):
                self._list.append(v % i)
            elif isinstance(v, Fraction):
                if v.denominator % i == 0:
                    self._list.append(0)
                    self._except.append(i)
                    continue
                    
                self._list.append(Fraction(v.numerator % i, v.denominator % i))
        
        
    def __add__(self, other):
        if isinstance(other, ModTuple):
            if len(self) != len(other):
                return NotImplemented

            return ModTuple([v + w for v, w in zip(self, other)])
        elif isinstance(other, int) or isinstance(other, Fraction):
            return ModTuple([v + other for v in self])
        else:
            return NotImplemented
   
    def __radd__(self, other):
        if isinstance(other, int):
            return self + other
        else:
            return NotImplemented
        
    def __getitem__(self, key):
        if key == 'except':
            return self._except
        else:
            return self._list[key]
        
    def __sub__(self, other):
        return self + (-1)*other
        
    def __mul__(self, other):
        if isinstance(other, ModTuple):
            if len(self) != len(other):
                return NotImplemented
            
            return ModTuple([v * w for v, w in zip(self, other)])
        elif isinstance(other, int) or isinstance(other, Fraction):
            return other * self
        else:
            return NotImplemented
        
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, Fraction):
            return ModTuple([v * other for v in self])
        else:
            return NotImplemented
        
    def __len__(self):
        return len(self._list)
        
    def __iter__(self):
        return self._list.__iter__()
        