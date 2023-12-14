%define flavor lua54%{nil}
%define mod_name posix

%if "%{flavor}" == ""
Name:           lua-posix
ExclusiveArch:  do_not_build
%else
Name:           %{flavor}-%{mod_name}
%endif
Version:        35.0.1
Release:        0
Summary:        A POSIX library for Lua
License:        MIT
URL:            http://luaforge.net/projects/luaposix/
Source0:        %{flavor}-posix-%{version}.tar.gz
Source99:       precheckin.sh
BuildRequires:  gcc
BuildRequires:  %{flavor}-devel
Requires:       %{flavor}
BuildRequires:  lua-macros
BuildRequires:  pkgconfig(libcrypt)


%description
This is a POSIX library for Lua which provides access to many POSIX features
to Lua programs.

%prep
%autosetup -n %{name}-%{version}/upstream


%build
# avoid setting USER tag to not include $USER
export USER=""
build-aux/luke CFLAGS="%build_cflags"


%install
build-aux/luke install \
         PREFIX=%{buildroot}%{_prefix} \
         INST_LIBDIR=%{buildroot}%{lua_archdir} \
         INST_LUADIR=%{buildroot}%{lua_noarchdir}


#check
# Tests require specl which is not yet packaged


%files
%license LICENSE
%doc AUTHORS ChangeLog.old NEWS.md README.md
%{lua_archdir}/posix
%{lua_noarchdir}/posix
