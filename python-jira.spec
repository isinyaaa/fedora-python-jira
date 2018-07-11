%global modname jira
%global distname jira
%global eggname jira

Name:               python-%{distname}
Version:            2.0.0
Release:            1%{?dist}
Summary:            A library to ease use of the JIRA 5 REST APIs

Group:              Development/Libraries
License:            BSD
URL:                https://pypi.io/project/%{distname}
Source0:            https://files.pythonhosted.org/packages/source/j/%{distname}/%{distname}-%{version}.tar.gz
Patch0:             python-jira-no-mime-detection.patch

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python2-setuptools
BuildRequires:      python2-sphinx
BuildRequires:      python2-pytest-runner
BuildRequires:      python2-pytest-cov

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-sphinx
BuildRequires:      python3-pytest-runner
BuildRequires:      python3-pytest-cov

%description
A library to ease use of the JIRA 5 REST APIs.


%package -n python2-%{distname}
Summary:            %{summary}
Requires:           python2-requests
Requires:           python2-requests-oauthlib
Requires:           python2-requests-toolbelt
Requires:           python2-magic
Requires:           python2-ipython
Requires:           python2-six
Requires:           python2-pbr
Requires:           python2-defusedxml
%{?python_provide:%python_provide python2-%{distname}}

%description -n python2-%{distname}
A library to ease use of the JIRA 5 REST APIs.


%package -n python3-%{distname}
Summary:            %{summary}
Requires:           python3-requests
Requires:           python3-requests-oauthlib
Requires:           python3-requests-toolbelt
Requires:           python3-magic
Requires:           python3-ipython-console
Requires:           python3-six
Requires:           python3-pbr
Requires:           python3-defusedxml
%{?python_provide:%python_provide python3-%{distname}}

%description -n python3-%{distname}
A library to ease use of the JIRA 5 REST APIs.


%prep
%setup -q -n %{distname}-%{version}
%patch0 -p1

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

# Remove shebang in the non-executable files
sed -i -e '/^#!\//, 1d' %{modname}/{client,config,jirashell}.py


%build
%py2_build
%py3_build


%install
%py2_install
# Package only py3 version of executable.
rm %{buildroot}%{_bindir}/*
%py3_install

# No tests in PYPI package.
# %%check
# python2 -m pytest
# python3 -m pytest

%files -n python2-%{distname}
%doc PKG-INFO
%license LICENSE
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{eggname}-%{version}*


%files -n python3-%{distname}
%doc PKG-INFO
%license LICENSE
%{_bindir}/jirashell
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{eggname}-%{version}*


%changelog
* Tue Jul 17 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.15-3
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Ralph Bean <rbean@redhat.com> - 1.0.15-2
- Add missing deps.  https://bugzilla.redhat.com/show_bug.cgi?id=1589006

* Fri May 25 2018 Ralph Bean <rbean@redhat.com> - 1.0.15-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Nov 21 2016 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.7-1
- Update to 1.0.7 version
- Provide Python 3 subpackage

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 10 2016 Ralph Bean <rbean@redhat.com> - 0.50-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Ralph Bean <rbean@redhat.com> - 0.13-7
- Fix upstream url for https://bugzilla.redhat.com/1285760

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Ralph Bean <rbean@redhat.com> - 0.13-5
- Change dep from the ipython meta package to just python-ipython-console.
- Move the /tools/ module into the jira namespace to avoid potential conflict.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Nov 22 2013 Ralph Bean <rbean@redhat.com> - 0.13-3
- Patch out mime type detection as per review feedback.

* Fri Nov 01 2013 Ralph Bean <rbean@redhat.com> - 0.13-2
- Modernize python2 rpm macros.

* Thu Oct 31 2013 Ralph Bean <rbean@redhat.com> - 0.13-1
- Initial package for Fedora
