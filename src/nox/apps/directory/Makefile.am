include ../../../Make.vars

EXTRA_DIST = \
	meta.xml \
	__init__.py \
	dm_ws_switch.py \
	dm_ws_location.py \
	dm_ws_bindings.py \
	dm_ws_groups.py \
	dm_ws_user.py \
	directorymanagerws.py \
	directorymanager.py \
	dirmanager.i\
	directory.i\
	dir_utils.py \
	netinfo_mod_event.i \
	query.py \
	simple_directory.py \
	discovered_directory.py \
  principal_search.py \
  cidr_group_cache.py \
	static_www

pkglib_LTLIBRARIES =		\
	netinfo_mod_event.la

noinst_HEADERS =		\
	netinfo_mod_event.hh

netinfo_mod_event_la_CPPFLAGS = $(AM_CPPFLAGS) -I $(top_srcdir)/src/nox
netinfo_mod_event_la_SOURCES = netinfo_mod_event.cc
netinfo_mod_event_la_LDFLAGS = -module -export-dynamic

if PY_ENABLED
AM_CPPFLAGS += $(PYTHON_CPPFLAGS)
endif # PY_ENABLED

pkglib_LTLIBRARIES +=		\
	cdirectorymanager.la		


cdirectorymanager_la_CPPFLAGS =							\
	$(AM_CPPFLAGS)								\
	-I$(srcdir)/../								\
	-I$(top_srcdir)/src/nox							\
	-D__COMPONENT_FACTORY_FUNCTION__=cdirectorymanager_get_factory

cdirectorymanager_la_SOURCES = directory.cc directory.hh directorymanager.cc	\
	directorymanager.hh principal_event.hh principal_event.cc 		\
	group_event.hh group_event.cc location_del_event.hh			\
	location_del_event.cc group_change_event.hh group_change_event.cc \
	principal_types.hh principal_types.cc pyprincipal_types.hh \
	pyprincipal_types.cc

cdirectorymanager_la_LDFLAGS = -module -export-dynamic

if PY_ENABLED
pydirmanager_wrap_includes = dirmanager.i directory.i

pydirmanager_wrap.cc pydirmanager.py: $(pydirmanager_wrap_includes)
	$(SWIG) $(SWIG_PYTHON_OPT)  -I$(top_srcdir)/src/nox/lib/ -outdir $(builddir)/. -o pydirmanager_wrap.cc -module pydirmanager $(srcdir)/dirmanager.i

pkglib_LTLIBRARIES += _pydirmanager.la
_pydirmanager_la_CPPFLAGS = $(AM_CPPFLAGS) -I$(top_srcdir)/src/nox/ -I$(srcdir)/../ -I$(top_builddir)/src/nox/
_pydirmanager_la_SOURCES = pydirmanager.cc pydirmanager.hh
nodist__pydirmanager_la_SOURCES = pydirmanager_wrap.cc pydirmanager.py
_pydirmanager_la_LDFLAGS = -module

NOX_PYLIBFILES = _pydirmanager.so

NOX_PYBUILDFILES = \
	pydirmanager_wrap.cc\
	pynetinfo_mod_event_wrap.cc \
	pynetinfo_mod_event.py\
	pydirmanager.py 

netinfo_mod_event_wrap_includes = \
	netinfo_mod_event.i

pynetinfo_mod_event_wrap.cc pynetinfo_mod_event.py: $(netinfo_mod_event_wrap_includes)
	swig -I$(top_srcdir)/src/nox/lib/ -outdir $(builddir)/. -o pynetinfo_mod_event_wrap.cc -c++ -python -module pynetinfo_mod_event $(srcdir)/netinfo_mod_event.i
pkglib_LTLIBRARIES += _pynetinfo_mod_event.la

_pynetinfo_mod_event_la_CPPFLAGS = $(AM_CPPFLAGS) -I$(top_srcdir)/src/nox -I$(srcdir)/../ -I$(top_builddir)/src/nox/
_pynetinfo_mod_event_la_SOURCES = netinfo_mod_event.hh 
nodist__pynetinfo_mod_event_la_SOURCES = pynetinfo_mod_event_wrap.cc pynetinfo_mod_event.py
_pynetinfo_mod_event_la_LDFLAGS = -module


NOX_PYLIBFILES += _pynetinfo_mod_event.so

endif # PY_ENABLED

# Required for static_www build/install
MODULE=directory
MODULE_BASE_PATH=nox/apps
MODULE_BASE_ESCAPE=../..

NOX_RUNTIMEFILES = \
	meta.xml \
	__init__.py \
	dm_ws_bindings.py\
	dm_ws_groups.py \
	dm_ws_user.py \
	dm_ws_switch.py \
	dm_ws_location.py \
	directorymanager.py \
	directorymanagerws.py \
	simple_directory.py \
	discovered_directory.py \
	dir_utils.py \
	principal_search.py \
	cidr_group_cache.py \
	query.py

all-local: nox-all-local nox-runtimefiles-build static-www-build
clean-local: nox-clean-local nox-runtimefiles-clean static-www-clean
install-exec-hook: nox-install-local
