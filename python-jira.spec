%global modname jira
%global distname jira
%global eggname jira

Name:               python-jira
Version:            0.13
Release:            7%{?dist}
Summary:            A library to ease use of the JIRA 5 REST APIs.

Group:              Development/Libraries
License:            BSD
URL:                http://pypi.python.org/pypi/%{distname}
Source0:            http://pypi.python.org/packages/source/j/%{distname}/%{distname}-%{version}.tar.gz
Patch0:             python-jira-no-mime-detection.patch

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python-setuptools

BuildRequires:      python-requests
BuildRequires:      python-requests-oauthlib
BuildRequires:      python-tlslite
BuildRequires:      python-magic
BuildRequires:      python-ipython-console

Requires:           python-requests
Requires:           python-requests-oauthlib
Requires:           python-tlslite
Requires:           python-magic
Requires:           python-ipython-console

%description
A library to ease use of the JIRA 5 REST APIs.

%prep
%setup -q -n %{distname}-%{version}
%patch0 -p1

sed -i 's/tools.jirashell/jira.tools.jirashell/g' setup.py

# Remove bundled egg-info in case it exists
rm -rf %{distname}.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

# Move this into the jira namespace.  It gets fixed in a more modern version.
mv %{buildroot}%{python2_sitelib}/tools/ %{buildroot}%{python2_sitelib}/jira/tools/

# Why does it even install these?  A mistake.
rm -rf %{buildroot}%{python2_sitelib}/tests/


# The tests could be run with nosetests, but they require hardcoded
# certificates found on the author's computer.
#%%check
#nosetests

%files
# Filed an issue asking for license full text
# https://bitbucket.org/bspeakmon/jira-python/issue/70
%doc PKG-INFO
%{python2_sitelib}/%{modname}/
%{python2_sitelib}/%{eggname}-%{version}*
%{_bindir}/jirashell


%changelog
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
