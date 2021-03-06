from mdsdata import Data
from mdsscalar import String
from _mdsdtypes import DTYPE_LIST,DTYPE_DICTIONARY

class Apd(Data):
    """The Apd class represents the Array of Pointers to Descriptors structure.
    This structure provides a mechanism for storing an array of non-primitive items.
    """

    def __init__(self,descs,dtype=0):
        """Initializes a Apd instance
        """
        if isinstance(descs,tuple):
            self.descs=descs
            self.dtype=dtype
        else:
            raise TypeError,"must provide tuple of items when creating ApdData"
        return

    def __len__(self):
        """Return the number of descriptors in the apd"""
        return len(self.descs)
    
    def __getitem__(self,idx):
        """Return descriptor(s) x.__getitem__(idx) <==> x[idx]
        @rtype: Data|tuple
        """
        try:
            return self.descs[idx]
        except:
            return None
        return

    def __setitem__(self,idx,value):
        """Set descriptor. x.__setitem__(idx,value) <==> x[idx]=value
        @rtype: None
        """
        l=list(self.descs)
        while len(l) <= idx:
            l.append(None)
        l[idx]=value
        self.descs=tuple(l)
        return None
   
    def getDescs(self):
        """Returns the descs of the Apd.
        @rtype: tuple
        """
        return self.descs

    def getDescAt(self,idx=0):
        """Return the descriptor indexed by idx. (indexes start at 0).
        @rtype: Data
        """
        return self[idx]

    def setDescs(self,descs):
        """Set the descriptors of the Apd.
        @type descs: tuple
        @rtype: None
        """
        if isinstance(descs,tuple):
            self.descs=descs
        else:
            raise TypeError,"must provide tuple"
        return

    def setDescAt(self,idx,value):
        """Set a descriptor in the Apd
        """
        self[idx]=value
        return None

    def append(self,value):
        """Append a value to apd"""
        self[len(self)]=value

    def data(self):
        """Returns native representation of the apd"""
        l=list()
        for d in self.descs:
            l.append(d.data())
        return l

class Dictionary(dict,Data):
    """dictionary class"""
    def __init__(self,value=None):
        if value is not None:
            if isinstance(value,Apd):
                from mdsscalar import Scalar
                import numpy
                for idx in range(0,len(value),2):
                    key=value[idx]
                    if isinstance(key,Scalar):
                        key=key.value
                    if isinstance(key,numpy.string_):
                        key=str(key)
                    elif isinstance(key,numpy.int32):
                        key=int(key)
                    elif isinstance(key,numpy.float32) or isinstance(key,numpy.float64):
                        key=float(key)
                    val=value[idx+1]
                    if isinstance(val,Apd):
                        val=Dictionary(val)
                    self.setdefault(key,val)
            elif isinstance(value,dict):
                for key,val in value.items():
                    self.setdefault(key,val)
            else:
                raise TypeError,'Cannot create Dictionary from type: '+str(type(value))

    def __getattr__(self,name):
        if name in self.keys():
            return self[name]
        else:
            raise AttributeError,'No such attribute: '+name

    def __setattr__(self,name,value):
        if name in self.keys():
            self[name]=value
        elif hasattr(self,name):
            self.__dict__[name]=value
        else:
            self.setdefault(name,value)

    def data(self):
        """Return native representation of data item"""
        d=dict()
        for key,val in self.items():
            d.setdefault(key,val.data())
        return d
        
    def toApd(self):
        apd=Apd(tuple(),DTYPE_DICTIONARY)
        for key,val in self.items():
            apd.append(key)
            apd.append(val)
        return apd

    def __str__(self):
        return dict.__str__(self)
 
class List(list,Data):
    """list class"""
    def __init__(self,value=None):
        if value is not None:
            if isinstance(value,Apd) or isinstance(value,list) or isinstance(value,tuple):
                for idx in range(len(value)):
                    super(List,self).append(value[idx])
            else:
                raise TypeError,'Cannot create List from type: '+str(type(value))

    def toApd(self):
        apd=Apd(tuple(),DTYPE_LIST)
        for idx in range(len(self)):
            apd.append(self[idx])
        return apd

    def __str__(self):
        return list.__str__(self)
 
