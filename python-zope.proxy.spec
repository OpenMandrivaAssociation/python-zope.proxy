Name:		python-zope.proxy
Version:	3.5.0
Release:	%mkrel 2
Group:		Development/Python
License:	Zope Public License
Summary:	Generic Transparent Proxies
#md5=ac5fc916b572bc3ff630b49cda52d94a
Source:		http://pypi.python.org/packages/source/z/zope.proxy/zope.proxy-3.5.0.tar.gz
URL:		https://pypi.python.org/pypi/zope.proxy/3.5.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	python-devel
BuildRequires:	python-setuptools

%description
Proxies are special objects which serve as mostly-transparent wrappers
around another object, intervening in the apparent behavior of the wrapped
object only when necessary to apply the policy (e.g., access checking,
location brokering, etc.) for which the proxy is responsible.

%prep
%setup -q -n zope.proxy-%{version}

%build

%install
PYTHONDONTWRITEBYTECODE= \
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
