# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module(
                '_htmc', [dirname(__file__)])
            print "====================== HERE ======================="
        except ImportError, e:
            print str(e)
            import _htmc
            return _htmc
        if fp is not None:
            try:
                _mod = imp.load_module('_htmc', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _htmc = swig_import_helper()
    del swig_import_helper
else:
    import _htmc
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError(name)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class HTMC(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, HTMC, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HTMC, name)
    __repr__ = _swig_repr

    def __init__(self, depth=10):
        this = _htmc.new_HTMC(depth)
        try:
            self.this.append(this)
        except:
            self.this = this

    def init(self, depth=10):
        return _htmc.HTMC_init(self, depth)
    __swig_destroy__ = _htmc.delete_HTMC
    __del__ = lambda self: None

    def lookup_id(self, *args):
        return _htmc.HTMC_lookup_id(self, *args)

    def intersect(self, *args):
        return _htmc.HTMC_intersect(self, *args)

    def cmatch(self, *args):
        return _htmc.HTMC_cmatch(self, *args)

    def cbincount(self, *args):
        return _htmc.HTMC_cbincount(self, *args)

    def depth(self):
        return _htmc.HTMC_depth(self)

HTMC_swigregister = _htmc.HTMC_swigregister
HTMC_swigregister(HTMC)


class Matcher(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(
        self, Matcher, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Matcher, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _htmc.new_Matcher(*args)
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _htmc.delete_Matcher
    __del__ = lambda self: None

    def get_depth(self):
        return _htmc.Matcher_get_depth(self)

    def match(self, *args):
        return _htmc.Matcher_match(self, *args)
Matcher_swigregister = _htmc.Matcher_swigregister
Matcher_swigregister(Matcher)

# This file is compatible with both classic and new-style classes.
