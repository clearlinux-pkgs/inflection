#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : inflection
Version  : 0.5.1
Release  : 25
URL      : https://files.pythonhosted.org/packages/e1/7e/691d061b7329bc8d54edbf0ec22fbfb2afe61facb681f9aaa9bff7a27d04/inflection-0.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/e1/7e/691d061b7329bc8d54edbf0ec22fbfb2afe61facb681f9aaa9bff7a27d04/inflection-0.5.1.tar.gz
Summary  : A port of Ruby on Rails inflector to Python
Group    : Development/Tools
License  : MIT
Requires: inflection-license = %{version}-%{release}
Requires: inflection-python = %{version}-%{release}
Requires: inflection-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
==========
        
        |build status|_

%package license
Summary: license components for the inflection package.
Group: Default

%description license
license components for the inflection package.


%package python
Summary: python components for the inflection package.
Group: Default
Requires: inflection-python3 = %{version}-%{release}

%description python
python components for the inflection package.


%package python3
Summary: python3 components for the inflection package.
Group: Default
Requires: python3-core
Provides: pypi(inflection)

%description python3
python3 components for the inflection package.


%prep
%setup -q -n inflection-0.5.1
cd %{_builddir}/inflection-0.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623429824
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/inflection
cp %{_builddir}/inflection-0.5.1/LICENSE %{buildroot}/usr/share/package-licenses/inflection/3528822a9ec44b4f2c14130be19edc108f3b9423
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/inflection/3528822a9ec44b4f2c14130be19edc108f3b9423

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
