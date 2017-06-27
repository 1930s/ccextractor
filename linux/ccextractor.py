# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ccextractor')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ccextractor')
    _ccextractor = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ccextractor', [dirname(__file__)])
        except ImportError:
            import _ccextractor
            return _ccextractor
        try:
            _mod = imp.load_module('_ccextractor', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ccextractor = swig_import_helper()
    del swig_import_helper
else:
    import _ccextractor
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

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
        if _newclass:
            object.__setattr__(self, name, value)
        else:
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
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

EXIT_OK = _ccextractor.EXIT_OK
EXIT_NO_INPUT_FILES = _ccextractor.EXIT_NO_INPUT_FILES
EXIT_TOO_MANY_INPUT_FILES = _ccextractor.EXIT_TOO_MANY_INPUT_FILES
EXIT_INCOMPATIBLE_PARAMETERS = _ccextractor.EXIT_INCOMPATIBLE_PARAMETERS
EXIT_UNABLE_TO_DETERMINE_FILE_SIZE = _ccextractor.EXIT_UNABLE_TO_DETERMINE_FILE_SIZE
EXIT_MALFORMED_PARAMETER = _ccextractor.EXIT_MALFORMED_PARAMETER
EXIT_READ_ERROR = _ccextractor.EXIT_READ_ERROR
EXIT_WITH_HELP = _ccextractor.EXIT_WITH_HELP
EXIT_NO_CAPTIONS = _ccextractor.EXIT_NO_CAPTIONS
EXIT_NOT_CLASSIFIED = _ccextractor.EXIT_NOT_CLASSIFIED
EXIT_ERROR_IN_CAPITALIZATION_FILE = _ccextractor.EXIT_ERROR_IN_CAPITALIZATION_FILE
EXIT_BUFFER_FULL = _ccextractor.EXIT_BUFFER_FULL
EXIT_MISSING_ASF_HEADER = _ccextractor.EXIT_MISSING_ASF_HEADER
EXIT_MISSING_RCWT_HEADER = _ccextractor.EXIT_MISSING_RCWT_HEADER
CCX_COMMON_EXIT_FILE_CREATION_FAILED = _ccextractor.CCX_COMMON_EXIT_FILE_CREATION_FAILED
CCX_COMMON_EXIT_UNSUPPORTED = _ccextractor.CCX_COMMON_EXIT_UNSUPPORTED
EXIT_NOT_ENOUGH_MEMORY = _ccextractor.EXIT_NOT_ENOUGH_MEMORY
CCX_COMMON_EXIT_BUG_BUG = _ccextractor.CCX_COMMON_EXIT_BUG_BUG
CCX_OK = _ccextractor.CCX_OK
CCX_FALSE = _ccextractor.CCX_FALSE
CCX_TRUE = _ccextractor.CCX_TRUE
CCX_EAGAIN = _ccextractor.CCX_EAGAIN
CCX_EOF = _ccextractor.CCX_EOF
CCX_EINVAL = _ccextractor.CCX_EINVAL
CCX_ENOSUPP = _ccextractor.CCX_ENOSUPP
CCX_ENOMEM = _ccextractor.CCX_ENOMEM

def fdprintf(fd, fmt):
    return _ccextractor.fdprintf(fd, fmt)
fdprintf = _ccextractor.fdprintf

def millis_to_time(milli, hours, minutes, seconds, ms):
    return _ccextractor.millis_to_time(milli, hours, minutes, seconds, ms)
millis_to_time = _ccextractor.millis_to_time

def freep(arg):
    return _ccextractor.freep(arg)
freep = _ccextractor.freep

def dbg_print(mask, fmt):
    return _ccextractor.dbg_print(mask, fmt)
dbg_print = _ccextractor.dbg_print

def debug_608_to_ASC(ccdata, channel):
    return _ccextractor.debug_608_to_ASC(ccdata, channel)
debug_608_to_ASC = _ccextractor.debug_608_to_ASC

def add_cc_sub_text(sub, str, start_time, end_time, info, mode, arg7):
    return _ccextractor.add_cc_sub_text(sub, str, start_time, end_time, info, mode, arg7)
add_cc_sub_text = _ccextractor.add_cc_sub_text

def api_init_options():
    return _ccextractor.api_init_options()
api_init_options = _ccextractor.api_init_options

def checking_configuration_file(api_options):
    return _ccextractor.checking_configuration_file(api_options)
checking_configuration_file = _ccextractor.checking_configuration_file

def compile_params(api_options, argc):
    return _ccextractor.compile_params(api_options, argc)
compile_params = _ccextractor.compile_params

def api_add_param(api_options, arg):
    return _ccextractor.api_add_param(api_options, arg)
api_add_param = _ccextractor.api_add_param

def api_start(api_options):
    return _ccextractor.api_start(api_options)
api_start = _ccextractor.api_start

def api_param_count(api_options):
    return _ccextractor.api_param_count(api_options)
api_param_count = _ccextractor.api_param_count

def api_param(api_options, count):
    return _ccextractor.api_param(api_options, count)
api_param = _ccextractor.api_param

def sigterm_handler(sig):
    return _ccextractor.sigterm_handler(sig)
sigterm_handler = _ccextractor.sigterm_handler

def sigint_handler(sig):
    return _ccextractor.sigint_handler(sig)
sigint_handler = _ccextractor.sigint_handler

def print_end_msg():
    return _ccextractor.print_end_msg()
print_end_msg = _ccextractor.print_end_msg

def main(argc, argv):
    return _ccextractor.main(argc, argv)
main = _ccextractor.main
# This file is compatible with both classic and new-style classes.

cvar = _ccextractor.cvar

