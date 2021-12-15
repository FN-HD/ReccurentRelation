def get_standard_list(size, r):
    '''
    get a list with a 1 the r-th element and 0's elsewhere
    
    Parameters
    ----------
    size ; list
        the size of the list
    r : int
        the index of list, whose element is 1
                
    Examples
    ----------
    >>> e = get_standard_list(3, 2)
    e = [0, 0, 1]
    
    Notes
    ----------
    If size is less or equal than r, then TypeError is raised.   
    '''
    if size <= r:
        raise TypeError('vec is too large.')
    
    standard_list = [0] * size
    standard_list[r] = 1
    
    return standard_list


def get_standard_sequences(reccurent_relation, max_size):
    '''
    get the list of sequences defined by the reccurent relation,
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
            >>> print(v)
        >>> print()
        1 0 1 1 2 3 5 8 13 21
        0 1 1 2 3 5 8 13 21 34
    '''
    sequences = []
    for r in range(0,len(reccurent_relation)):
        e = get_standard_list(len(reccurent_relation), r)
        reccurent_sequence = ReccurentSequence(reccurent_relation, e, max_size)
        sequences.append(reccurent_sequence)

    return sequences


class ReccurentSequence:
    '''
    A class to represent a sequence with a reccurent relation

    Attributes
    ----------
    reccurent_relation ; list
        the list of the reccurent relation
        If the reccurent relation forms 
            X**d + c_1 X**(d-1) + c_2 X**(d-2) + ... + c_d,
        then this list is defined by
            [c_1, c_2, ..., c_d]
    initial_value : list
        the initial value of the sequnce
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
    >>> for v in ReccurentSequence([-1, -1], [1, 0], 10)
        >>> print(v)
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    
    ToDo
    ----------
    * Actualize +, -, and scalar. 
    '''
    def __init__(self, 
                 reccurent_relation, 
                 initial_values, 
                 max_size = 100):
        if not isinstance(reccurent_relation, list):
            raise TypeError('reccurent_relation should be list.')
        if not isinstance(initial_values, list):
            raise TypeError('initial_values should be list.')

        if len(initial_values) < len(reccurent_relation):
            raise ValueError('init_value is too short.')
            
        self._reccurent_relation = reccurent_relation
        self._initial_values = initial_values[0:len(reccurent_relation)]
        self._max_size = max_size
        
        self._values = self._initial_values
        self._count = 0
        
    def initialize(self):
        '''
        initialize this instance.
        
        
        Examples
        ----------
        >>> Fib = RecSeq([-1, -1], [1, 0], 10)
        >>> for v in Fib:
            >>> print(v)
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34
        >>> Fib.initialize()
        >>> for v in Fib:
            >>> print(v)
        0, 1, 1, 2, 3, 5, 8, 13, 21, 34
        

        Note
        ----------
            If you initialize, then you lose the data, that 
        you calculated. 
        '''
        self._values = self._initial_values
        self._count = 0
        
    def __eq__(self, other):
        if isinstance(other, recseq):
            return False
        
        return (self._initial_values==other._initial_values and 
                self._reccurent_relation == other._reccurent_relation)
    
    def __iter__(self):
        self._count = 0
        self._values = self._initial_values
        return self
    
    def __len__(self):
        '''
        get the maximal number of elements of sequence, which
        you calculate.
        '''
        return self._max_size
    
    def __next__(self):
        value = self._values[0]
        
        if self._count > self._max_size:
            raise StopIteration
        
        # calculate new values
        new_value = 0        
        for v, c in zip(self._values, 
                        reversed(self._reccurent_relation)):
            new_value -= v*c
                        
        self._values.pop(0) 
        self._values.append(new_value)
        
        self._count += 1
        
        return value
                        
    def __repr__(self):
        return f'recseq.RecSeq(' \
                        + f'{str(self._rec_rel)}, ' \
                        + f'{str(self._init_values)}, ' \
                        + f'{str(self._max_size)})'

    def __str__(self):
        degree = len(self._reccurent_relation)
        self_str = f'Reccurent Relation = X**{degree}'
                        
        for i, c in enumerate(self._reccurent_relation):
            self_str = self_str + f' + ({str(c)})*X**{degree - i}'
        
        self_str = self_str + '\n' + 'initial values = '
                        
        for i, v in enumerate(self._initial_values):
            self_str = self_str + f'{v} '
                                                
        self_str = self_str + '\n' + 'values = '
                        
        for v in self._values:
            self_str = self_str + f'{v} '
                                                
        return self_str

                        