%global modname jira
%global distname jira
%global eggname jira

Name:               python-%{distname}
Version:            1.0.7
Release:            3%{?dist}
Summary:            A library to ease use of the JIRA 5 REST APIs

Group:              Development/Libraries
License:            BSD
URL:                https://pypi.io/project/%{distname}
Source0:            https://files.pythonhosted.org/packages/source/j/%{distname}/%{distname}-%{version}.tar.gz
Patch0:             python-jira-no-mime-detection.patch

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python2-setuptools

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

%description
A library to ease use of the JIRA 5 REST APIs.


%package -n python2-%{distname}
Summary:            %{summary}
Requires:           python2-requests
Requires:           python2-requests-oauthlib
Requires:           python2-requests-toolbelt
Requires:           python2-tlslite
Requires:           python2-magic
Requires:           python2-ipython
Requires:           python2-six
%{?python_provide:%python_provide python2-%{distname}}

%description -n python2-%{distname}
A library to ease use of the JIRA 5 REST APIs.


%package -n python3-%{distname}
Summary:            %{summary}
Requires:           python3-requests
Requires:           python3-requests-oauthlib
Requires:           python3-requests-toolbelt
Requires:           python3-tlslite
Requires:           python3-magic
Requires:           python3-ipython-console
Requires:           python3-six
%{?python_provide:%python_provide python3-%{distname}}

%description -n python3-%{distname}
A library to ease use of the JIRA 5 REST APIs.


%prep
%setup -q -n %{distname}-%{version}
%patch0 -p1

sed -i 's/tools.jirashell/jira.tools.jirashell/g' setup.py
sed -i "s/'ordereddict'//" setup.py

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

# Remove shebang in the non-executable files
sed -i -e '/^#!\//, 1d' %{modname}/{client,config,jirashell}.py


%build
%py2_build
%py3_build


%install
%py3_install
mv %{buildroot}/%{_bindir}/jirashell %{buildroot}/%{_bindir}/jirashell-%{python3_version}
ln -sf %{_bindir}/jirashell-%{python3_version} %{buildroot}/%{_bindir}/jirashell-3

%py2_install
mv %{buildroot}/%{_bindir}/jirashell %{buildroot}/%{_bindir}/jirashell-%{python2_version}
ln -sf %{_bindir}/jirashell-%{python2_version} %{buildroot}/%{_bindir}/jirashell-2
ln -sf %{_bindir}/jirashell-2 %{buildroot}/%{_bindir}/jirashell


%files -n python2-%{distname}
%doc PKG-INFO
%license LICENSE
%{_bindir}/jirashell
%{_bindir}/jirashell-2
%{_bindir}/jirashell-%{python2_version}
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{eggname}-%{version}*


%files -n python3-%{distname}
%doc PKG-INFO
%license LICENSE
%{_bindir}/jirashell-3
%{_bindir}/jirashell-%{python3_version}
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{eggname}-%{version}*


%changelog
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
