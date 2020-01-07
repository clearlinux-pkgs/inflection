#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : inflection
Version  : 0.3.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/d5/35/a6eb45b4e2356fe688b21570864d4aa0d0a880ce387defe9c589112077f8/inflection-0.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/35/a6eb45b4e2356fe688b21570864d4aa0d0a880ce387defe9c589112077f8/inflection-0.3.1.tar.gz
Summary  : A port of Ruby on Rails inflector to Python
Group    : Development/Tools
License  : MIT
Requires: inflection-python = %{version}-%{release}
Requires: inflection-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
==========
        
        |build status|_

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

%description python3
python3 components for the inflection package.


%prep
%setup -q -n inflection-0.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541265029
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
