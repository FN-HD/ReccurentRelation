from fractions import Fraction


def get_standard_list(size, r):
    ''' get a list with a 1 the r-th element and 0's elsewhere
    
    Parameters
    ----------
    size ; index
        the size of the list
    r : int
        the index of list, whose element is 1

    Raises
    ----------
    ValueError
        If size is less or equal than r
    TypeError
        If size or r are not int

    Examples
    ----------
    >>> e = get_standard_list(3, 2)
    e = [0, 0, 1]
    '''
    if not isinstance(size, int):
        raise TypeError('size is not int')
    if not isinstance(r, int):
        raise TypeError('r is not int')
    
    if size <= r:
        raise ValueError('vec is too large.')
    
    standard_list = [0] * size
    standard_list[r] = 1
    
    return standard_list


def get_standard_sequences(reccurent_relation, max_size):
    '''get the list of sequences defined by the reccurent relation,
    whose initial element is (0, ...,0, 1, 0, ...,0)
    
    Parameters
    ----------
    reccurent_relation : list
        the list of the reccurent relation. Look attribution 
        of ReccurentSequence
    max_size : int
        the maximum number of elements of sequence, which
        you calculate
        
    Raises
    ----------
    TypeError
        If reccurent_relation is not a list or initial_values is not a list.
    ValueError
        If the length of the list of the initial values is less than the 
        length of the list of the reccurent relations.

    Examples
    ----------
    >>> seqs = get_standard_sequnces([-1, -1], 10)
    >>> for seq in seqs:
        >>> for v in seq:
            >>> print(v, end = ' ')
        >>> print()
        1 0 1 1 2 3 5 8 13 21
        0 1 1 2 3 5 8 13 21 34
    '''
    sequences = []
    for r in range(0,len(reccurent_relation)):
        e = get_standard_list(len(reccurent_relation), r)
        reccurent_sequence = ReccurentSequence(reccurent_relation, 
                                               e, 
                                               max_size)
        sequences.append(reccurent_sequence)

    return sequences


class ReccurentSequence:
    ''' A sequence with a reccurent relation and a initial values
    
    It is a sequence with given reccurent relation and initial values. 
    This instance does not have all element in sequence, but you 
    can get all value by calling __next__ method. 

    Attributes
    ----------
    _count : int
        the number of times you used __next__ method
    _initial_values : list
        the initial value of the sequnce
    _max_size : int, default=100
        the maximum number of elements of sequence, which
        you calculate
    _reccurent_relation ; list
        the list of the reccurent relation
        If the reccurent relation forms 
            X**d + c_1 X**(d-1) + c_2 X**(d-2) + ... + c_d,
        then this list is defined by
            [c_1, c_2, ..., c_d]
    _values : list 
        the values of sequence which you get in __next__ method. 
    
    Examples
    ----------
    >>> fib0 = ReccurentSequence([-1, -1], [1, 0], 10)
    >>> fib1 = ReccurentSequence([-1, -1], [0, 1], 10)
    >>> for v in fib0:
        >>> print(v, end = ' ')
    1 0 1 1 2 3 5 8 13 21

    >>> newfib = fib0 + fib1
    >>> for v in newfib:
        >>> print(v, end = ' ')
    1 1 2 3 5 8 13 21 34 55
    
    Notes
    ----------
        If two reccrent sequence have a same reccurent
    relation, they have addition, subtraction, and
    scalar multiplication. 
    
    ToDo
    ----------
    * Add lshift and rshift.
    '''

    def __init__(self, 
                 reccurent_relation, 
                 initial_values, 
                 max_size = 100):
        ''' the __init__ method of ReccurentSequence
        
        Parameters
        ----------
        reccurent_relation ; list
            the list of the reccurent relation
            If the reccurent relation forms 
                X**d + c_1 X**(d-1) + c_2 X**(d-2) + ... + c_d,
            then this list is defined by
                [c_1, c_2, ..., c_d]
        initial_value : list
            the initial value of the sequnce
        max_size : int, default=100
            the maximum number of elements of sequence, which
            you calculate
    
        Raises
        ----------
        TypeError
            If reccurent_relation is not a list or initial_values is not a list.
        ValueError
            If the length of the list of the initial values is less than the 
            length of the list of the reccurent relations.
        '''
        if not isinstance(reccurent_relation, list):
            raise TypeError('reccurent_relation should be list.')
        if not isinstance(initial_values, list):
            raise TypeError('initial_values should be list.')

        if len(initial_values) < len(reccurent_relation):
            raise ValueError('initial_value is too short.')

        self._reccurent_relation = reccurent_relation[:]
        self._initial_values = initial_values[0:len(reccurent_relation)]
        self._max_size = max_size
        
        self._values = self._initial_values[:]
        self._count = 0
        
    def __add__(self, other):
        ''' The sum of two numbers. 
        
        Parameters
        ----------
        other : Reccurentsequence
            the other value. 
        
        Returns
        ----------
        ReccurentSequence
            A sequence with the reccurent relation of self, the 
            initial values [v + w for v, w in zip(self._initial_values,
            other._initial_values)], and the max size max(self._max_size,
            other._max_size). 
            If other is not ReccurentSequence or if self and other 
            have not same reccurent relation.
        '''
        if isinstance(other, ReccurentSequence):
            if self._reccurent_relation != other._reccurent_relation:
                return NotImplemented
            
            max_size = max(self._max_size, other._max_size)
            initial_values = [
                v + w for v, w in zip(self._initial_values, 
                                      other._initial_values)
            ]

            return ReccurentSequence(self._reccurent_relation, 
                                     initial_values, 
                                     max_size)
        else:
            return NotImplemented
            
    def __eq__(self, other):
        ''' Is self equal to other.
        
        Returns
        ----------
        bool
            If self and other have a same initial values and a same 
            reccurent relation, then True is returned. 
            If other is not ReccurentSequence, then NotImplemented is 
            returned. 
        '''
        if isinstance(other, ReccurentSequence):
            return NotImplemented
        
        return (self._initial_values==other._initial_values and 
                self._reccurent_relation == other._reccurent_relation)
    
    def __iter__(self):
        self._count = 0
        self._values = self._initial_values[:]
        return self
    
    def __len__(self):
        return self._max_size

    def __ne__(self, other):
        result = self.__eq__(other)
        
        if result is not NotImplemented:
            return result
        
        return NotImplemented
    
    def __neg__(self):
        return (-1)*self
    
    def __next__(self):
        ''' get the next element of the sequence
        
        Returns
        ----------
        int or Fraction or StopIteration
            the next element of the sequence. 
            If _count > _max_size, then 
            StopIteration is returned and 
            this sequence is initialized 
            (It means _values = _initial_values 
            and _count = 0).
        '''
        value = self._values[0]
        
        if self._count > self._max_size:
            self._count = 0
            self._values = self._initial_values[:]
            raise StopIteration
        
        # calculate next values.
        new_value = 0        
        for v, c in zip(self._values, 
                        reversed(self._reccurent_relation)):
            new_value -= v*c

        # delete the value with small index and add next value.
        self._values.pop(0) 
        self._values.append(new_value)
        
        self._count += 1
        
        return value

    def __reversed__(self):
        ''' get new seqeuce which has the reversed reccurent relation. 
                
        Reaises
        ----------
        ZeroDivisionError
            If the constant term of the reccurent relation of self is zero.
        
        Returns
        ----------
        ReccurentSequence
            sequence which has the reversed reccurent relation and 
            same initial value
            
        Examples
        ----------
        >>> fib = ReccurentSequence([-1, -1], [1, 0], 10)
        >>> for v in revesed(fib):
            >>> print(v, end=' ')
            1 0 1 -1 2 -3 5 -8 13 -21
        '''
        constant_term = self._reccurent_relation[len(self._reccurent_relation)-1]

        if constant_term == 0:
            raise ZeroDivisionError(
                'The constant term of the reccurent relation of this sequence ' \
                'is zero.'
                            )
        
        reccurent_relation = []
        for i, c in enumerate(reversed(self._reccurent_relation)):
            if i == 0:
                continue
                
            if isinstance(c, int):
                reccurent_relation.append(
                    Fraction(c, constant_term)
                )
            elif isinstance(c, Fraction):
                reccurent_relation.append(
                    c / constant_term
                )
            else:
                reccurent_relation.append(
                    c / constant_term
                )
        
        # append constant term 
        reccurent_relation.append(Fraction(1, constant_term))
        
        return ReccurentSequence(
            reccurent_relation, 
            self._initial_values, 
            self._max_size
                                )
    
    def __repr__(self):
        return f'recseq.ReccurentSequence(' \
                        + f'{str(self._reccurent_relation)}, ' \
                        + f'{str(self._initial_values)}, ' \
                        + f'{str(self._max_size)})'

    def __rmul__(self, other):
        ''' get scalar multiplication
        
        Returns
        ----------
        ReccurentSequence
            The reccurent sequence defined by multiplicating self by other        
        '''
        # scalar multication
        if isinstance(other, int):
            return ReccurentSequence(self._reccurent_relation,
                                     [other*v for v in self._initial_values],
                                     self._max_size)
        else:
            return NotImplemented
            
    def __str__(self):
        degree = len(self._reccurent_relation)
        self_str = f'Reccurent Relation = X**{degree}'
                        
        for i, c in enumerate(self._reccurent_relation):
            self_str = self_str + f' + ({str(c)})*X**{degree - i - 1}'
        
        self_str = self_str + '\n' + 'initial values = '
                        
        for v in self._initial_values:
            self_str = self_str + f'{v} '
                                                
        self_str = self_str + '\n' + 'values = '
                        
        for v in self._values:
            self_str = self_str + f'{v} '
                                                
        return self_str

    def __sub__(self, other):
        return self + (-1)*other

