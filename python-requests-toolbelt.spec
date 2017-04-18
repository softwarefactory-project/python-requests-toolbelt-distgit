%global with_python3 0
%global module_name requests-toolbelt

Name:           python-%{module_name}
Version:        0.6.0
Release:        1%{?dist}
Summary:        A utility belt for advanced users of python-requests

License:        ASL 2.0
URL:            https://toolbelt.readthedocs.org/
Source0:        https://pypi.python.org/packages/source/r/%{module_name}/%{module_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
This is just a collection of utilities for python-requests, but don’t really
belong in requests proper.

%if 0%{?with_python3}
%package -n python3-%{module_name}
Summary:        A utility belt for advanced users of python-requests
License:        ASL 2.0
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%if 0%{?with_python3}
%description -n python3-%{module_name}
This is just a collection of utilities for python-requests, but don’t really
belong in requests proper.

%endif

%prep
%setup -q -n %{module_name}-%{version}
rm -rf *.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root=%{buildroot}
popd
%endif

%{__python2} setup.py install --skip-build --root=%{buildroot}

%files -n python-%{module_name}
%doc PKG-INFO
%license LICENSE
%{python2_sitelib}/requests_toolbelt
%{python2_sitelib}/requests_toolbelt-%{version}-py2.*.egg-info

%if 0%{?with_python3}
%files -n python3-%{module_name}
%doc PKG-INFO
%license LICENSE
%{python3_sitelib}/requests_toolbelt
%{python3_sitelib}/requests_toolbelt-%{version}-py3.*.egg-info
%endif


%changelog
* Thu Jan 28 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.6.0-1
- update to 0.6.0 release

* Wed Dec 23 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.4.0-1
- Update to 0.4.0

* Fri Feb 13 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.3.1-2
- Add missing LICENSE file

* Mon Feb 02 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.3.1-1
- Initial packaging

